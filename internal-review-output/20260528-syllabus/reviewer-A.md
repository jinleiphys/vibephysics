# Reviewer A — Internal Review of SYLLABUS.md

**Role:** Senior physics pedagogy referee (15+ yr freshman physics, top-tier 中国 physics department).
**Artifact:** `/Users/jinlei/Desktop/code/vibephysics/SYLLABUS.md`
**Date:** 2026-05-28
**Stance:** Skeptical of AI-titled freshman courses; care about audience calibration, hidden assumptions, claim plausibility under classroom friction, and whether AI is load-bearing vs decorative.

Issues are ranked by severity. No positives included by design — this is a work list.

---

## A1
- **SEVERITY:** blocker
- **CATEGORY:** audience-mismatch
- **LOCATION:** Day 2, "课堂内容" block
- **CLAIM:** Day 2 budgets only 40 minutes to teach 大一 students (with at most a C/C++ syntax course) the full set Python variables + loops + functions + numpy arrays + matplotlib, which is wildly insufficient for genuine literacy and will collapse the rest of Day 2.
- **EVIDENCE:** "40 min Python 速成：变量、循环、函数、numpy 数组、matplotlib 画图（不教 OOP，不教异常处理）" and immediately after, "80 min 学生实战：先用计算器手算前 10 步 Euler，再让 AI 写完整脚本，跑出 100 步，对比手算和数值结果差在哪、为什么"
- **SUGGESTED_FIX:** Either (a) push a 2-hour pre-course Python primer as a non-graded but required pre-arrival module (with a one-page checklist students must self-certify before Day 1), or (b) move RC + Euler to Day 3 and let Day 2 be a full 180 minutes of Python-on-physics scaffolding (read-modify-rerun, not 从零写). The current Day 2 plan assumes students arrive numpy-literate.

## A2
- **SEVERITY:** blocker
- **CATEGORY:** hidden-assumption
- **LOCATION:** Day 3, learning objectives
- **CLAIM:** "化二阶 ODE 为两个一阶" is treated as something students just do — but 大一 students who have only seen 基础 ODE in 高数 have almost never encountered state-vector reduction; this is the central step and gets one bullet with no scaffolding.
- **EVIDENCE:** "用 Python 解二阶 ODE（化为两个一阶）" and the day's classroom slots contain 30 min 物理 + 40 min AI demo + 80 min student实战 + 20 min复盘, with no slot devoted to teaching the reduction itself.
- **SUGGESTED_FIX:** Allocate an explicit 20–30 minute mini-lecture (carve from the 80-min student实战 or from the AI demo) that walks through y'' = -ω²y → y'=v, v'=-ω²y on the board, with a paper exercise students do before touching code. Otherwise Day 3 is the first hard wall of the course.

## A3
- **SEVERITY:** major
- **CATEGORY:** hidden-assumption
- **LOCATION:** Day 3, "学生实战" sub-bullet
- **CLAIM:** "尝试半隐式（leapfrog）作为对比" is dropped on freshmen with no explanation of staggered grids, symplectic integrators, or even why a half-step works; this is a 数值分析 / 理论力学 topic being squeezed in as a "magic trick".
- **EVIDENCE:** "80 min 学生实战：各组写自己的阻尼振子，验证能量行为；尝试半隐式（leapfrog）作为对比，看到能量不漂的奇迹"
- **SUGGESTED_FIX:** Either drop leapfrog (the Euler-drift demonstration alone makes the pedagogical point) or replace with semi-implicit Euler stated as one literal line change (`v_{n+1} = v_n + a(x_n)*dt; x_{n+1} = x_n + v_{n+1}*dt`) and label it explicitly as a black-box upgrade students should not be tested on. The current phrasing reads as "trust me, leapfrog is magic", which contradicts the course's own anti-authority spine.

## A4
- **SEVERITY:** major
- **CATEGORY:** hidden-assumption
- **LOCATION:** Day 4, classroom content block
- **CLAIM:** Day 4 simultaneously introduces 2D vectorization, numpy broadcasting, AND nondimensionalization in one 30-min concept slot + 40-min demo; for 大一 students one day after first seeing numpy, this is three new abstractions stacked.
- **EVIDENCE:** "30 min 二维向量化思路、numpy 数组与广播" and "40 min 教师演示：抛体 + 线性阻力的全过程；让 AI 给出代码…" and the learning objective "让 AI 帮你做无量纲化，并自己检查无量纲化对不对"
- **SUGGESTED_FIX:** Cut nondimensionalization out of Day 4 entirely and move it to Day 5 (where it pairs naturally with fitting). Day 4 should be: 2D = pair of 1D ODEs (no broadcasting magic required), and the limit-case validation move. Broadcasting can be introduced only when the physics actually demands it (e.g., the spring chain in P6).

## A5
- **SEVERITY:** major
- **CATEGORY:** pedagogy-claim
- **LOCATION:** §二 "课程定位", item 3
- **CLAIM:** The 60-second AI audit reflex is presented as the course's unique value-add, but the syllabus never specifies what taxonomy of "可疑" the student should be checking against until Day 6 (mid-course). For 8 days students are told to "find at least one suspicious thing" without a prior framework — they will either pattern-match noise or freeze.
- **EVIDENCE:** "看到 AI 给出的代码 / 推导 / 图，能在 60 秒内指出至少一个值得怀疑的地方" stated on Day 1, while the 10-mode taxonomy ("10 大 AI 错误模式短训：单位错、符号错、求解器误用…") is not introduced until Day 6.
- **SUGGESTED_FIX:** Front-load a minimal taxonomy on Day 1 itself — even 3 categories (unit/sign/order-of-magnitude) is enough. Then expand to 10 on Day 6 as deepening, not as first exposure. Otherwise the Day 1 AI audit log assignment is asking students to use a reflex they have no vocabulary for.

## A6
- **SEVERITY:** major
- **CATEGORY:** risk-realism
- **LOCATION:** §十一 风险 5
- **CLAIM:** The mitigation for "solo instructor for 8–13 groups" is "轮巡 + 1-2 名助教（视申请情况）", but the syllabus also commits to 5-8 min one-on-one report review on Day 9 for every group (= 40–104 min just for that one slot) plus daily 轮巡 (each group at least once = ~7 min/group/day = 60–90 min/day pure rounds). With 0 TAs in the worst case, the math does not close.
- **EVIDENCE:** "助教 0 至 2 人（视申请情况）" in §一; "80 min 写作时间，老师一对一过初稿（每组 5 至 8 分钟）" in Day 9; "教师轮巡" appears in every day's实战 block; "应对：班额控制在 25 至 40 人，分 8 至 13 组；申请 1 至 2 名研究生助教协助轮巡和批改日志"
- **SUGGESTED_FIX:** Make at least 1 TA a hard precondition for opening the course (not "if申请通过"); above 8 groups, require 2 TAs. Alternatively cap enrollment at 6 groups (≤18 students) for the first offering and explicitly mark this as a pilot constraint. The current "视申请情况" defers the operational risk onto Day 1.

## A7
- **SEVERITY:** major
- **CATEGORY:** ai-use-honesty
- **LOCATION:** Day 5 + Day 7
- **CLAIM:** AI's role on Day 5 (fitting) and Day 7 (literature) is essentially "AI generates, student verifies", but the syllabus never asks the student to do the fitting or DOI lookup once without AI as a calibration baseline. Without that, students cannot tell whether their auditing skill is real or whether they are just rubber-stamping AI output that happens to be correct.
- **EVIDENCE:** Day 5: "让 AI 写拟合脚本，看残差图发现…" and Day 7: "30 min 真实演示：让 ChatGPT 给一个物理问题列 5 篇参考文献，逐条用 Google Scholar 和 DOI 验证"
- **SUGGESTED_FIX:** Add a "no-AI baseline" exercise to at least Day 5 (do `curve_fit` by hand once, get the same answer) and Day 7 (find 1 of your 3 papers entirely without AI, just Google Scholar). The course should be able to demonstrate that students could function in an AI outage; right now it cannot.

## A8
- **SEVERITY:** major
- **CATEGORY:** motivation-gap
- **LOCATION:** Day 5
- **CLAIM:** The leap from Day 4 (forward simulation of ODEs) to Day 5 (curve fitting from data with scipy.curve_fit + covariance matrix) is not motivated — the syllabus treats "now we add data" as obvious, but conceptually this is a backwards-inference problem with completely different machinery (least squares, parameter uncertainty, residual reading) that the student has not been primed for.
- **EVIDENCE:** "30 min 拟合的物理意义：从模型到数据 vs 从数据到模型" is the only motivational move, then jumps straight to "理解参数有不确定性（用协方差矩阵的对角，不上 Bootstrap）"
- **SUGGESTED_FIX:** Insert one explicit pedagogical bridge: "Day 1–4 你建模并预测，Day 5 你反过来从数据估参数 — 这是科学闭环的另一半". Also flag that the协方差对角 ≈ parameter σ² requires assumptions students cannot yet check (normal residuals, correct model) — better to teach σ as "fit-replicate scatter" via 参数±10% scan than via curve_fit's `pcov` whose meaning is opaque without statistics background.

## A9
- **SEVERITY:** major
- **CATEGORY:** scope-equity
- **LOCATION:** §十 项目选题菜单
- **CLAIM:** 6 of 8 menu items (P1, P2, P3, P4, P5, P6) are oscillator/ODE family problems; only P7 (Monte Carlo) and P8 (video extraction) are off the振子 spine. Students whose physics taste leans statistical, computational, or experimental have only 2 of 8 options.
- **EVIDENCE:** P1 单摆, P2 抛体阻力, P3 RC/RL/RLC, P4 行星轨道, P5 牛顿冷却, P6 弹簧振子链 — all ODE evolution problems. P7 + P8 are the only outliers. "学生可以自选题，但自选题需经老师审批可行性"
- **SUGGESTED_FIX:** Add 2 more genuinely different-flavor projects: e.g., (a) 一维 random walk / 扩散模拟 with comparison to analytic mean-square displacement (continues P7's MC spine but adds a physics narrative), (b) Light interference / diffraction pattern from photo extraction (光学, completely outside the ODE family). This also pairs with A10 below.

## A10
- **SEVERITY:** major
- **CATEGORY:** physics-accuracy
- **LOCATION:** §三 "这意味着课程内容的硬约束"
- **CLAIM:** "数值方法只用 Euler 和向前差分" is then directly contradicted by Day 3's leapfrog appearance and Day 5's `scipy.curve_fit` (a Levenberg-Marquardt nonlinear least squares solver — not Euler, not forward difference). The syllabus's stated method floor and its actual use do not match.
- **EVIDENCE:** §三: "数值方法只用 Euler 和向前差分（足够说清"逐步演化"）" vs Day 3: "尝试半隐式（leapfrog）作为对比" vs Day 5: "用 scipy.curve_fit 做最小二乘拟合"
- **SUGGESTED_FIX:** Rewrite §三 honestly: "explicitly taught: Euler. Used as black-box library tools with disclosure: semi-implicit Euler, scipy.curve_fit, scipy.optimize." Black-box use is fine but should be flagged as such in the same place the floor is stated, so the rest of the document is internally consistent.

## A11
- **SEVERITY:** major
- **CATEGORY:** ai-use-honesty
- **LOCATION:** §五 + §六 (every Day)
- **CLAIM:** The promise of "演示真实 AI 对话" (including failed prompts, on-screen AI errors caught live) is operationally fragile — by Day 3/4 the instructor will have prepared the demo, AI may not produce the same error in class, and the "live audit" becomes theater. The syllabus does not specify a fallback when AI behaves correctly on demo day.
- **EVIDENCE:** "演示真实 AI 对话。老师把和 AI 的对话过程投出来，包括失败的 prompt、AI 出错的瞬间、自己怎么发现错的，全程透明。这门课最重要的教学资产是真实的 AI 协作录像，不是 PPT"
- **SUGGESTED_FIX:** Require the instructor to prerecord 10 AI-failure-and-catch sessions (one per day) as the canonical demo, with one live attempt per day for spontaneity. Otherwise the "real AI conversation" claim becomes either staged (a credibility loss the course explicitly criticizes) or genuinely random (a pedagogical risk on tight 30-40 min slots). The AI bug 卡 asset mentioned for Day 6 should be extended to all 10 days.

## A12
- **SEVERITY:** minor
- **CATEGORY:** risk-realism
- **LOCATION:** §十一 风险 4 + Day 8 timing
- **CLAIM:** "应急方案" allowing Day 8 switch to a backup project is unrealistic — by Day 8 the group has 8 working days invested; switching projects with 2 days left (Day 9 writeup, Day 10 defense) is functionally project abandonment, not a rescue.
- **EVIDENCE:** "老师保留'应急方案'，对实在卡死的组允许 Day 8 切到 backup 题"
- **SUGGESTED_FIX:** Move the backup-switch deadline to Day 5 or Day 6 (mid-defense), not Day 8. Or restate Day 8's emergency option as "scope reduction within current project" (cut a planned validation, drop a parameter dimension), not project swap. Day 8 swap is a face-saving fiction.

---

**Total issues:** 12 (3 blocker, 7 major, 2 minor).
**Pattern:** the highest-severity issues cluster on Days 2–5, where the syllabus silently assumes Python/ODE/numpy fluency it never builds. Secondary cluster: AI-audit reflex is sold as the course identity but operationalized late and without a no-AI baseline.
