# Idea PK — Designing "AI 辅助数理建模与应用实践" for 大一 students who haven't studied 专业物理

| Field | Value |
| --- | --- |
| Stuck-point | Design a 40-学时 / 10-教学日 / 2-周 summer intensive for incoming-大二 Tongji physics students whose only prior physics is 大一 普物 (力学 + maybe basic E&M) and whose only math is 微积分 + 线代; two prior drafts (research-method shell + high-octane numerics 大纲) were both rejected without pilot. |
| Solver A | Claude (general-purpose Agent), contrarian / diagonal-mover |
| Solver B | Claude fallback (general-purpose Agent), methodologist / cheapest-test designer (originally codex:codex-rescue, blocked by Bash permission on `codex-companion.mjs`; stance preserved) |
| Cross-checker | Claude fallback (general-purpose Agent), independent context (originally codex:codex-rescue, same gate) |
| Date | 2026-05-28 |
| Budget | 40 学时 fixed, 25–40 students, 2 instructors, summer 2-week window |
| Tried list | T1 = 32 学时 / 16-session research-method shell (commit-superseded). T2 = 40 学时 / 4-phase numerics 大纲 with RK4 + SymPy + FFT + MC + Bootstrap as core (rejected: too advanced for 大一). Raw + normalized lists at `./stuck-card.md`. |
| Output mode | file |

**Solver A's anchored assumption**: you are silently treating this as a numerical-methods course "watered down for 大一" — keeping the topic spine (RK4 / SymPy / FFT / MC / Bootstrap) intact and only tuning depth. The shape of the course itself is never on the table. A proposes to keep the calendar (40 学时, 10 日, 2 教师) and tear up the topic-list-as-spine.

**Solver B's disambiguation question**: we do not know whether the binding bottleneck for these students is H3 MODELING (cannot translate a physical scene into variables/equations), H2 CODING (env+syntax burn the block before physics lands), or H4 AI-LITERACY (over-trust AI outputs). T1 and T2 silently picked one of these without testing. B proposes to measure before committing.

**Convergence**: A and B diverged structurally (A re-shapes the course; B postpones shaping until a diagnostic runs). No groupthink flag. 9 candidates total, all 9 survived cross-check, 2 had first-step refinements applied.

---

## The diagonal — most orthogonal to your tried list

### A3. Inverted-instructor model: drop the topical A-track / B-track split, reassign the two instructors as **Prompter** (queries AI live) + **Adversary** (challenges AI output live), so the course teaches an AI-collaboration *stance* through 20 sessions of two-person sparring instead of 20 sessions of lecture.

- **Why it's the diagonal**: every other surviving candidate (and both tried items) treats either the syllabus or its diagnostic as the unit. A3 treats the in-class human–AI interaction itself as the deliverable, and explicitly forbids the topical split that anchored T2's "主线 A / 主线 B".
- **First concrete step (today)**: schedule a 90-minute mock session with the second instructor on one shared 大一 problem (e.g. "estimate the terminal velocity of a coffee filter"). One of you plays Prompter and queries Claude/GPT live on a projected screen; the other plays Adversary and forces dimensional checks, limit cases, sign checks. Record. Watch back.
- **Cost**: design ~15 h (role-card protocol + ~20 problem corpus). Per-cycle teach cost: high in instructor time (both must be live), low in prep after year 1.
- **Info gain — works**: students absorb AI-collaboration skills better by watching skilled adults negotiate with AI than by being told algorithm names — a hypothesis no Chinese physics department has tested. **Fails**: you learn the cognitive ceiling of pure-observation learning for 大一 (probably ~half a day before they need to do something themselves), calibrating sparring-vs-hands-on ratio.
- **Risk**: the second instructor cannot or will not sustain live adversarial sparring; format collapses to single-lecture. The 90-min mock today is also the hiring filter — you find out today, not week 2.
- **Orthogonality to tried**: T1 has instructors lecturing on research method; A3 has instructors performing AI collaboration in front of students, with method visible by demonstration. T2 splits instructors by topic (物理 / 数据); A3 forbids topical split and splits them by role (Prompter / Adversary) on the same problem.
- **Source**: Solver A only.

---

## The cheapest disambiguator — best info-gain per hour

### B5. Define the course-end deliverable **rubric FIRST** as a published artifact spec (what every group's Day-10 output must demonstrate); then fabricate one "good" and one "bad" student artifact yourself and have the second instructor blind-grade them — confirm the rubric discriminates before any teaching is designed.

- **Why it's the cheapest**: 7 instructor-hours today, **zero student involvement**, no scheduling chain, binary outcome (rubric discriminates or it does not) that conditions every downstream design choice in B1 / B3 / B4 and A1 / A2.
- **First concrete step (today)**: write a 5-binary-item rubric on one page, e.g. (1) the artifact states the physical scene in 3 sentences using only 大一-普物 vocabulary; (2) equations of motion derived on paper and photographed in; (3) ≥1 numerical plot with AI-assisted code AND the student annotates one prompt they had to reject; (4) one cross-check (analytical limit, dimensional check, textbook value); (5) a 60-second video explanation a 大一 classmate can follow. Then fabricate two artifacts in 3 h (one pass / one fail on items 3 and 4). Co-grade blind with second instructor.
- **Cost**: 7 instructor-hours, today.
- **Disambiguates**: "is the intended course outcome operationally defined yet?" (assumed yes by T1's 50/20/15/10/5 weights) vs. "is the rubric still instructor-aspirational rather than student-achievable?" (B's hypothesis).
- **What you learn either way — passes**: defensible, examinable assessment instrument exists; the 10-day syllabus design becomes a backward induction from the rubric. **Fails**: the course's intended outcome is not yet defined; B1 / B3 / B4 and A1–A4 are all grading against an undefined target — caught now, not at the end.
- **Risk**: rubric ends up instructor-aspirational. Mitigation: cross-reference each item to 大一-普物 vocabulary only.
- **Source**: Solver B only.

---

## Divergent paths — your call

These are A-vs-B pairs where both candidates survived cross-check but the two impose incompatible course choices. Pick the side whose underlying hypothesis you find more probable now.

### Pair 1 — No-code Day 1: **A4** (Fermi-paper) vs **B4** (Excel-only spreadsheet)

Both want Day 1 to forbid Python and AI code-generation. They disagree on what replaces them.

- **A4 (Solver A, contrarian)**: Days 1–4 use *only* paper estimation + Desmos + GeoGebra to build dimensional analysis, idealization, model comparison, order-of-magnitude reflexes. Python and AI enter on Day 5. *First step today*: solve 3 Fermi questions ("how high on the Moon?", "coffee cool to drinkable?", "Eiffel sway in wind?") in 90 min using only paper + Desmos; if you cannot, Day 1 is too thin. *Teaches*: whether 大一 普物 reflexes carry dimensional intuition or not.
- **B4 (Solver B, methodologist)**: pilot Day 1 as Excel-only damped-oscillator modeling with a pass/fail criterion (median student finds critical-damping boundary by 17:00). *First step today*: write the Excel template + worksheet + answer key (3 h). *Teaches*: cleanly separates H2 (coding floor) from H3 (modeling floor) — pass means modeling capacity exists and AI/Python is only about scale; fail means adding AI on top of a broken modeling habit will produce confident-looking-but-wrong outputs all course long.

**Author note (host editor)**: A4 commits Days 1–4 of the real course to no-code; B4 uses no-code only as a **diagnostic** for one Saturday and decides what the real Day 1 should be afterward. If you currently believe the bottleneck is *modeling* (H3), B4 produces the strongest single experiment in the entire panel and you should run it first. If you already believe modeling reflexes exist but coding doesn't, A4's 4-day modeling phase is overkill and a different no-code allocation (1–2 days) would suffice — re-pose the question.

### Pair 2 — Course geometry: **A2** (one continuous flagship) vs **B3** (Day-1-as-atomic-unit)

These impose opposite course geometries. They cannot both define Days 2–10.

- **A2 (Solver A)**: build the entire 10-day course around ONE flagship narrative — e.g. "reproduce Galileo's inclined-plane discovery from raw phone-video frames with an AI partner". Daily milestones (Day 1 raw video → Day 3 first ugly fit → Day 6 model comparison → Day 9 report). The 大纲 is scaffolding around a single story; topic list emerges from what the problem demands. *First step today*: 30-sec phone video of a ball on an inclined board, hand to Claude/ChatGPT with vision, see where the AI helps, where it fakes, where 大一 普物 is enough to check — 2 h tells you whether monolithic-flagship has enough texture for 40 学时.
- **B3 (Solver B)**: make 1 day the smallest replicable unit. Design Day 1 as a self-contained 4-学时 workshop with a pass/fail end-of-day milestone; teach it once to 8 volunteers; only proceed to Days 2–10 (templated as "1 scene per day, escalating complexity") if median student hits the criterion. *First step today*: write the single-page Day-1 plan with explicit success criterion ("by 17:00, every student has (a) a defended projectile-motion plot, (b) a plot with air drag added via AI assistance, (c) caught one injected error") + the 4 lesson blocks (45 min each).

**Author note**: A2 optimizes for narrative coherence and research-attention span. B3 optimizes for pacing calibration and reproducibility-by-TA. If your second instructor and TA pipeline are weak, B3's 1-day-as-atom is the only structure that survives staff turnover. If you can carry the narrative yourself and want the highest engagement ceiling, A2 is the bolder bet.

---

## Single-source paths — only one solver, cross-check confirmed not generic / not reinvention

### A1 (Solver A). 10-day **AI-output-audit bootcamp**: students do not write much code themselves; they spend the 40 学时 catching planted bugs in AI-generated physics solutions, building a "distrust then verify" reflex no later physics course will teach.
- **First step**: pick one 大一-accessible problem (projectile with drag, simple pendulum large-angle, RC charging); ask Claude/GPT-4 to solve it three ways; hand-annotate every wrong / lazy / unverifiable claim on a single A4 sheet. That sheet seeds the "famous bugs" catalog and tells you in an afternoon whether audit-mode has enough material for 10 days.
- **Cost**: ~30 h design (20-card bug library) | **Info gain**: works → 大一 + 普物 + 高数 is enough to catch dimensional / limit / sign errors. Fails → you learn the floor where audit breaks (probably anything requiring 数理方法 or 理论力学).
- **Risk**: bugs too easy (caught Day 2) or too hard (not caught without 专业物理). The afternoon pilot detects this before any syllabus is written.
- **Incompatibility note**: A1 makes audit the spine from Day 1; **A4 forbids code (and thus AI code-audit) until Day 5** — you must pick one starting epistemic posture.

### B1 (Solver B, first-step refined by cross-check). **3-station diagnostic clinic** with 6–8 大一-末 volunteers on one fixed physics scene (damped pendulum, 30° release, with drag), measuring where they break: modeling / coding / AI-trust.
- **First step [cross-check refined]**: today, write the 1-page 3-station protocol (Station 1 pencil-ODE / Station 2 AI+laptop x(t) plot / Station 3 sign-flip-trap critique) AND author the wrong-sign reference code (~1 h). The Saturday session itself is week-1 work, scheduled separately.
- **Cost**: 12 instructor-hours end-to-end + pizza ~300 RMB. **Info gain**: stalling at Station 1 → H3 modeling; Station 2 → H2 coding; Station 3 → H4 AI-trust. No clear pattern → heterogeneous cohort, Day 1 must fork into a placement track. Every branch decisive.
- **Risk**: n=8 not statistically representative. Mitigation: actively recruit self-reported strugglers, not just top of the class.

### B2 (Solver B, first-step refined by cross-check). Port **MIT 8.S50 / Rice "Vibe Coding for Research"** as a known-solved subproblem skeleton: take the shortest self-contained module from those public materials and walk one 大二-incoming student through it; only modules that land cleanly earn slots in the 10-day syllabus.
- **First step [cross-check refined]**: today, pull MIT 8.S50 + Rice Vibe Coding public materials; identify the shortest freshman-accessible module (~3 h student-time, scene → plot end-to-end); run it yourself in a 2-h block while noting where 大一-普物 vocabulary breaks. Student walk-through is next-day, not today.
- **Cost**: 8 instructor-hours over 2 days. **Info gain**: module lands → Tongji 大一 is within range of established freshman computational-physics curricula, syllabus can be 4–5 such modules stitched together. Module fails → positive evidence the audience is *below* MIT-freshman calibration, rules out N existing curricula, forces ground-up design. Either way the design space shrinks.
- **Risk**: n=1 student; chosen module unrepresentative. Mitigation: pick the importing curriculum's advertised-easiest first-week module so failure is informative.

---

## Filtered out (audit)

No candidates were filtered. Cross-check applied two first-step refinements (B1, B2 — both bundled today-tasks with multi-day chains; reduced to today-deliverable only). All 9 candidates survived `reinvention`, `infeasible`, `generic`, `redundant`, `orthogonality_underspecified` tests.

---

## Your options (you pick — I am not picking for you)

Before any 课程大纲 .md gets written, three structurally different next moves:

1. **Run the cheapest disambiguator (B5, today, 7 instructor-hours, no students)** — fix the rubric and verify it discriminates fabricated-good from fabricated-bad. Every other candidate on this panel implicitly grades against the rubric you would build here. This is the highest-leverage 7 hours you can spend before the course exists.
2. **Run the most informative student-facing experiment (B4 spreadsheet null OR B1 3-station clinic)** — both isolate H2 (coding) vs H3 (modeling). B4 is cheaper (8 h, one Saturday, Excel-only); B1 is sharper (3 stations cleanly separate H2/H3/H4 but costs 12 h). If you can spend 1 weekend you can run B4 + B5 in the same week and have both the rubric AND the modeling-floor measurement before Day 1.
3. **Commit to a course-shape bet without piloting (A1 audit-spine, A2 single-flagship, or A3 Prompter/Adversary)** — bolder, no diagnostic, locks in the epistemic posture by instructor judgment. A3 (the diagonal) gives the highest ceiling but requires the second instructor's live commitment; the 90-min mock session today *is* the feasibility test.

Which one do you want to drill into? I can:
- write up the chosen path as a concrete syllabus draft (the `SYLLABUS.md` you originally asked for, now conditioned on a real bet rather than a guess);
- spawn `debug-physics-first` to think through the H2/H3/H4 hypothesis space if you want a deeper read on which floor binds;
- spawn `literature-search` on the MIT 8.S50 + Rice Vibe Coding materials so we know what is publicly available before B2's walkthrough.

Or "none of the above" — that is a valid answer; we can re-spawn with new constraints (e.g. "I commit the no-AI bet, design A4 in full" or "rule out A3 because instructor 2 won't co-perform").
