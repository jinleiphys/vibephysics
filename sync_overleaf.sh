#!/bin/bash
# Sync 讲义 (lecture notes) to Overleaf — clone to tmp, copy, push, cleanup
# Usage: ./sync_overleaf.sh
# Modeled on DREAM_project/sync_overleaf.sh

set -euo pipefail

# Config — 讲义 Overleaf project (same URL as 讲义/.git origin)
OVERLEAF_URL=${OVERLEAF_URL:-"https://git@git.overleaf.com/6a18e1212522e318f9f1aaba"}

# Resolve repo root
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
TEX_SRC="$REPO_ROOT/讲义"
FIG_SRC="$REPO_ROOT/讲义/Pictures"

# Create tmp dir, auto-cleanup on exit
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

echo "Syncing 讲义 to Overleaf..."

# Clone into tmp
echo "Cloning Overleaf repo to tmp..."
git clone "$OVERLEAF_URL" "$TMPDIR/overleaf"
cd "$TMPDIR/overleaf"
BRANCH=$(git symbolic-ref --short HEAD 2>/dev/null || echo "master")

# ── Clean: remove everything except .git ──
echo "Cleaning Overleaf directory..."
find "$TMPDIR/overleaf" -maxdepth 1 -mindepth 1 -not -name '.git' -exec rm -rf {} +

# ── Copy: only what main.tex needs ──

# 1. Top-level LaTeX, bib, style, index-style, and latexmkrc build config
echo "Copying top-level LaTeX source files..."
shopt -s nullglob
for f in "$TEX_SRC"/*.tex "$TEX_SRC"/*.bib "$TEX_SRC"/*.bst "$TEX_SRC"/*.sty "$TEX_SRC"/*.cls "$TEX_SRC"/*.ist; do
    [ -f "$f" ] && cp "$f" "$TMPDIR/overleaf/"
done
[ -f "$TEX_SRC/latexmkrc" ] && cp "$TEX_SRC/latexmkrc" "$TMPDIR/overleaf/"

# 2. Modular chapter sources in subdirectories (\input{chapters/...}, \input{frontmatter/...})
echo "Copying chapter subdirectories..."
tex_count=0
for sub in chapters frontmatter; do
    if [ -d "$TEX_SRC/$sub" ]; then
        mkdir -p "$TMPDIR/overleaf/$sub"
        for f in "$TEX_SRC/$sub"/*.tex; do
            [ -f "$f" ] && cp "$f" "$TMPDIR/overleaf/$sub/" && tex_count=$((tex_count+1))
        done
    fi
done
echo "  Copied $tex_count chapter/frontmatter files"

# 3. Pictures — into Pictures/ subdir (matches \graphicspath{{Pictures/}})
echo "Copying Pictures..."
mkdir -p "$TMPDIR/overleaf/Pictures"
fig_count=0
for ext in pdf png eps jpg jpeg; do
    for f in "$FIG_SRC"/*.$ext; do
        [ -f "$f" ] && cp "$f" "$TMPDIR/overleaf/Pictures/" && fig_count=$((fig_count+1))
    done
done
echo "  Copied $fig_count pictures"
shopt -u nullglob

# ── Commit and push ──
cd "$TMPDIR/overleaf"
if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git commit -m "Sync from local: $(date '+%Y-%m-%d %H:%M')"
    git push origin "$BRANCH"
    echo "Done! All files synced."
else
    echo "No changes to sync."
fi

echo "Overleaf project: $OVERLEAF_URL"
# tmp dir auto-removed by trap
