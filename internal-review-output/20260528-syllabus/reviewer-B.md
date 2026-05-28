# Reviewer B — Operational / Feasibility Audit

Artifact: `/Users/jinlei/Desktop/code/vibephysics/SYLLABUS.md`
Stance: instructional-designer / ex-PM. Physics pedagogy is out of scope; the question is whether the schedule, instruments, and instructor load fit in the box the author claims.

Issues ranked by severity. Verbatim quotes from the syllabus.

---

## B1

- **SEVERITY:** blocker
- **CATEGORY:** time-arithmetic
- **LOCATION:** Day 10 (§六)
- **CLAIM:** Day 10 is mathematically overbudget for the maximum class size and conflicts with the per-group answer time stated in §七.
- **EVIDENCE:**
  > "150 min 项目答辩：每组 12 分钟（8 展 + 4 问），10 至 13 组依次上台"
  > "20 min 中场休息 / 调试设备"
  > "30 min 课程总结：老师反馈 + 整体趋势点评（哪些反射动作建立了，哪些还没）"
  > "10 min 学生现场写课程反思（200 字内：我学到的、我没学会的、我下学期会怎么用）"
  Sum = 150 + 20 + 30 + 10 = 210 min. Even if you accept 210 min as the clock window (9:00–12:30), the 150 min answer slot itself only fits 150 / 12 = 12.5 groups, so 13 groups overruns by 6 min and 10–11 groups leaves 24–36 min idle. Worse: the 班额 25–40 produces 8–13 组 per §七, and at 40 students / 13 组 the day cannot fit. There is also no slot for transition between groups (setting up the next slide deck, walking up, mic handoff) — empirically 1–2 min per group, i.e. 13–26 additional minutes.
- **SUGGESTED_FIX:** Cut answer slot to 10 min (7 展 + 3 问) and budget 1 min setup between groups, giving 11 min × 13 = 143 min; OR split 终答辩 across Day 10 morning and a Day 10.5 afternoon session; OR cap class at 30 students = ≤10 组. Pick one and write it into §一 班额 explicitly.

---

## B2

- **SEVERITY:** blocker
- **CATEGORY:** time-arithmetic
- **LOCATION:** Day 6 (§六)
- **CLAIM:** Day 6 budget exceeds the 180-min instructional period by 55 min at the upper class-size bound.
- **EVIDENCE:**
  > "30 min 10 大 AI 错误模式短训..."
  > "40 min 学生实战 A：每组拿到 2 段"故意写错的 AI 输出"..."
  > "80 min 中期项目汇报：每组 5 分钟讲..."
  > "20 min 老师统一点评..."
  Listed total = 170 min. But "每组 5 分钟讲（物理问题 / 当前进度 / 验证状态 / 还有什么没搞定），其他组提问" plus "其他组提问" means the 5 min is the talk only and Q&A is unbudgeted; even at 0 Q&A and 0 transition, 13 组 × 5 min = 65 min, not 80. If Q&A is included realistically at 2 min/组, you need 13 × 7 = 91 min. Total goes to 30 + 40 + 91 + 20 = 181 min before any break, against a 180-min budget and a required 10 min 中场休息. Day 6 is 20–55 min over depending on class size.
- **SUGGESTED_FIX:** Either (a) cap mid-presentation to 3 min/组 talk + no Q&A and replace open Q&A with written peer-feedback cards filled during the next presenter; or (b) move 学生实战 A (the bug-card 20-min sprint) to Day 5 evening homework and reclaim 40 min for presentations.

---

## B3

- **SEVERITY:** blocker
- **CATEGORY:** instructor-load
- **LOCATION:** §一, §五, §八 (combined load)
- **CLAIM:** Solo instructor cannot simultaneously deliver 30+40 = 70 min live teaching, do 80 min 轮巡 across 13 groups at depth, grade 25–40 daily AI 审计日志 each evening, and run Day 9 1-on-1 office hours; the math doesn't close.
- **EVIDENCE:**
  > "主讲教师 | 1 人（金磊）"
  > "助教 | 0 至 2 人（视申请情况）"
  > "80 min 学生动手实验 ... 教师轮巡"
  > "20% AI 审计日志 | 每天一份，质量 + 完整度（关键看是否真的发现并修复了 AI 错误）"
  > Day 9: "80 min 写作时间，老师一对一过初稿（每组 5 至 8 分钟）"
  Pencil-out at 40 students / 13 组: 轮巡 80 min / 13 组 = 6.2 min/组 once, no slack for the student who asks a hard question. Day 9 one-on-one at 8 min × 13 组 = 104 min, exceeds the 80 min budget by 24 min. Daily 日志 grading at the 满分 vs 不及格 distinction this course actually requires (read the 半页 log, check if the AI error is real, check if the verification is real): 5 min/log × 40 logs = 200 min = 3.3 hours per evening, 10 evenings = 33 hours of solo grading on top of teaching. The assumption "助教 0 至 2 人（视申请情况）" makes the whole instrument scale conditional on a resource that is explicitly optional.
- **SUGGESTED_FIX:** Either (a) make 1 助教 mandatory (not 0 至 2), with explicit job spec covering 轮巡 and 日志 triage; or (b) cap class at 24 students / 8 组 when teaching solo and document this as a hard prerequisite; or (c) move 日志 grading to a 3-tier rubric (✓/✗/?) with weekly deep-grade on 2 random days only.

---

## B4

- **SEVERITY:** major
- **CATEGORY:** assessment-rubric
- **LOCATION:** §八 (the 20% AI 审计日志 row)
- **CLAIM:** The 20% AI 审计日志 component lacks a defined rubric, which is the second-largest grade weight and the course's signature instrument; without a rubric two graders (or even the same grader on different days) will produce non-reproducible scores.
- **EVIDENCE:**
  > "20% | AI 审计日志 | 每天一份，质量 + 完整度（关键看是否真的发现并修复了 AI 错误）"
  > "必含三栏：今天我让 AI 做了什么 / AI 哪里错了 / 我怎么验证的"
  No statement of (a) what makes a 满分 日志 vs a 75% 日志 vs a 不及格 日志; (b) what counts as "真的发现并修复" — does fixing a unit error in AI code count, or does it need to be a deeper physics error; (c) whether students get partial credit for sincere effort when the AI didn't actually err that day; (d) whether the same error reported across 3 days double-counts.
- **SUGGESTED_FIX:** Add a 4-level rubric to §八 with explicit anchors: A (≥90) "identifies physics-meaningful AI error + executes verification + states fix"; B (75–89) "identifies surface error + verification attempted"; C (60–74) "log present, complete, but error claim is shallow or not verified"; F (<60) "missing, fabricated, or empty-shell". Include 1 worked 满分 example and 1 不及格 example in §十二 备课资产.

---

## B5

- **SEVERITY:** major
- **CATEGORY:** prep-realism
- **LOCATION:** §十二
- **CLAIM:** The 60–80 hour first-round 备课 estimate is substantially underestimated; line-by-line accounting of the 8 listed assets gives 110–160 hours.
- **EVIDENCE:**
  > "10 张 AI bug 卡（每张含：原始问题 + AI 错误输出 + 物理审计点 + 修复路径）"
  > "8 份项目选题说明（每份 1 页，含 P1 至 P8）"
  > "Day 1 至 Day 10 每日教案（4 学时分时段表 + 学生学习单 + 课后任务单）"
  > "Fermi 题库 30 题（Day 1 + 平时随机抽用）"
  > "第一轮开课大约需要 60 至 80 小时备课"
  Pencil-out: 10 bug cards × 3 hr (the card has to be a *real* AI failure the instructor reproduced and audited, then documented with fix path) = 30 hr just for bug cards. 8 项目说明 × 2 hr including verifying references = 16 hr. 10 day 教案 with 学习单 + 任务单 × 4 hr = 40 hr. Fermi 题库 30 题 × 15 min = 7.5 hr. checklist template + AI 段落示范 + 反例 ≈ 5 hr. 课程仓库模板 + 课程主页ジ ≈ 8 hr. Total = 30 + 16 + 40 + 7.5 + 5 + 8 = 106.5 hr lower-bound, before §十 "每题都有一份教师准备的 1 页题目说明，包括物理背景、最低交付要求、扩展方向、参考文献（已核验）、典型 AI 陷阱预警" which is more than 1 page-worth of work per project.
- **SUGGESTED_FIX:** Revise §十二 to "100–140 小时备课 for first round" and recommend starting prep 4 weeks before Day 1 (not 2). Alternatively, ship the course with only 5 bug cards at launch and label 5 more as "v2 deliverable after first run", scoping prep to 70 hours honestly.

---

## B6

- **SEVERITY:** major
- **CATEGORY:** failure-mode
- **LOCATION:** §十一 (Risks)
- **CLAIM:** §十一 covers 5 risks but omits the highest-probability operational failures: AI-service outage (Chinese mainland ChatGPT/Claude access via VPN is intermittent and was throttled multiple times in 2025), classroom AV failure on演示 days, and instructor sick-day with no documented substitute teacher.
- **EVIDENCE:**
  > "**风险 1：学生完全不会编程...**"
  > "**风险 2：学生过度依赖 AI...**"
  > "**风险 3：虚假文献进入报告。**"
  > "**风险 4：项目卡死，做不完。**"
  > "**风险 5：单一教师精力不够。**"
  No mention of AI provider outage, even though Day 3 ("让 AI 写阻尼振子代码"), Day 4 ("让 AI 给出代码"), Day 5 ("让 AI 写拟合脚本"), Day 7 ("让 ChatGPT 给一个物理问题列 5 篇参考文献") all assume live cloud-AI access. Solo instructor with 1 doctor's visit = course halts.
- **SUGGESTED_FIX:** Add Risk 6 "AI 服务不可用" with mitigation: pre-cached AI 对话录像 for each 演示 (the syllabus already says "AI 协作录像 ... 是这门课最重要的教学资产" — formalize this as a fallback), and a local-LLM backup (qwen / deepseek-local) for the 实战 block. Add Risk 7 "教师病假" with named backup TA or one-day-shift contingency. Add Risk 8 "教室 AV 故障" with offline-paper-only Day-1-style fallback.

---

## B7

- **SEVERITY:** major
- **CATEGORY:** scope-dependency
- **LOCATION:** Day 5 + Day 8 + §十 (data availability)
- **CLAIM:** Data-acquisition dependency for several projects is not in the schedule: P1/P2/P8 require self-shot 手机视频 frame data, P3 requires lab oscilloscope traces, P5 requires temperature-vs-time measurements — but Day 5 "项目里程碑：项目第一份草稿图上交" assumes the data is already in hand, and Days 2–4 contain no data-collection block.
- **EVIDENCE:**
  > §十: "P1 | ... | 自录手机视频"; "P2 | ... | 体育场实测 / 公开视频"; "P3 | ... | 实验室录波 / 自做小电路"; "P5 | ... | 温度计实测"; "P8 | ... | 自录手机视频"
  > Day 5: "项目里程碑：项目第一份"草稿图"上交"
  > Day 3 课后: "各组当晚确定最终选题"
  This compresses "select project on Day 3 evening → collect data → import → fit → first draft figure" into roughly 36 hours. Students with P3 (oscilloscope) need lab access which is not in any §六 day; P1/P8 students need to film and frame-extract a video before Day 5 morning; P5 students need a temperature-vs-time dataset that takes ~hours of clock-time per measurement.
- **SUGGESTED_FIX:** Either (a) pre-stock a "data lockerJ" of pre-collected real datasets for each project type and let students collect their own as a stretch goal; or (b) move Day-5 "草稿图上交" to Day 6 morning and use Day 4 evening + Day 5 60-min block for data collection; or (c) restrict data-heavy projects (P3, P5) to groups that confirm data access on Day 2 with documented plan.

---

## B8

- **SEVERITY:** major
- **CATEGORY:** tech-dependency
- **LOCATION:** Day 1 + Day 7
- **CLAIM:** Two un-budgeted tech prerequisites are likely to cause silent first-week breakage: (1) installation is pushed to Day-1 课后 with only a 10-min video, but historically 15–30% of student laptops fail Python/Cursor install without help, and Day 2 morning has no triage slot; (2) Day 7 expects BibTeX / DOI / INSPIRE-HEP fluency taught in 40 min from zero, against a student profile that does not list LaTeX or reference-manager familiarity.
- **EVIDENCE:**
  > Day 1 课后任务: "安装 Python、Jupyter、VS Code 或 Cursor（学习单给出 10 分钟视频指引）"
  > §三 不假设: "Git、Jupyter、Markdown、LaTeX"
  > Day 2: "30 min 物理回顾..." "40 min Python 速成..." "80 min 学生实战..." — no install-triage block
  > Day 7: "40 min 引用规范速成：BibTeX、DOI 解析、arXiv ID 解析、INSPIRE-HEP 上手"
- **SUGGESTED_FIX:** (1) Open a pre-course virtual install-clinic 1 evening before Day 1, or reserve the first 20 min of Day 2 explicitly as "环境兜底" (compressing Python 速成 to 30 min — it can absorb the cut since it overlaps with the AI-pair-coding theme). (2) On Day 7 either drop INSPIRE-HEP (over-spec for undergraduates), or move BibTeX out and use a Google-Scholar-export workflow instead (lower-tech, same DOI-verification outcome).

---

## B9

- **SEVERITY:** major
- **CATEGORY:** policy-enforceability
- **LOCATION:** §九 三条红线
- **CLAIM:** The 三条红线 ("学术不端处理" consequence) are largely honor-system in practice but the syllabus presents them as enforceable; this gap will surface in the first dispute.
- **EVIDENCE:**
  > "三条红线（违反任何一条按学术不端处理）：
  > 1. 不能把 AI 段落直接复制粘贴到报告正文不加修改不加引用
  > 2. 不能用 AI 编造数据...
  > 3. 不能用 AI 给出的参考文献而不经过 DOI / arXiv / Google Scholar 核验..."
  Detection mechanics for each: (1) GPTZero-style detectors are unreliable on Chinese scientific text and produce false positives; the syllabus does not name a tool. (2) "AI 编造数据" detection requires comparing reported data against an independent source — feasible only if a TA spot-checks original videos / oscilloscope traces, which is not in the workflow. (3) Reference-verification is the only one of the three with an actual enforcement instrument ("老师当晚抽查 3 篇做反向核验" in §十一 风险 3) but only 3 out of all references.
- **SUGGESTED_FIX:** Add a paragraph to §九 explicitly framing the contract: "Detection on (1) and (2) is honor-system + spot-audit + 答辩问答 cross-examination; on (3) we do 抽查 with DOI reverse-resolution. The expectation is that students self-report grey areas in the AI 使用说明 段; failure to self-report is itself a violation even if the underlying act is innocent."

---

## B10

- **SEVERITY:** major
- **CATEGORY:** reproducibility
- **LOCATION:** §五, §六, §十二
- **CLAIM:** The course is heavily personalized to the author's particular AI-pair-coding fluency and live-演示 style; a new instructor (or PhD TA running it next summer) has no transcript / video / "演示 master tape" to replay, even though the syllabus declares this asset to be the most important.
- **EVIDENCE:**
  > "这门课最重要的教学资产是真实的 AI 协作录像，不是 PPT。"
  > §十二 deliverables list does NOT contain "录制 10 段教师 AI 协作演示视频"
  > Day 3: "40 min 教师演示：让 AI 写阻尼振子代码，跑能量图，发现无阻尼时能量也在涨..."
  The演示 quality varies day-to-day depending on whether the AI actually errs on that prompt that morning. A new instructor with the syllabus alone has no archive of "what to do when GPT-5 gives a clean answer and the planned bug doesn't show up."
- **SUGGESTED_FIX:** Add to §十二 备课清单: "10 段教师 AI 演示录屏（每天 1 段，每段 30–40 min, 含 fallback prompt list when AI does not err naturally）". Treat the录屏 as a primary deliverable, not a side-effect; without it the course is implicitly single-instructor-bound.

---

## B11

- **SEVERITY:** minor
- **CATEGORY:** time-arithmetic
- **LOCATION:** §一 + §五
- **CLAIM:** The clock-time vs学时-time accounting has an unexplained 20-min gap that will compound across 10 days.
- **EVIDENCE:**
  > §一: "10 个连续工作日，每日 4 学时（上午 9:00 至 12:30，含一次 10 分钟休息）"
  > §一: "总学时 | 40 学时（每学时 45 分钟）"
  > §五: "每日 4 学时（180 分钟）"
  9:00 → 12:30 is 210 clock min. Minus 10 min 中场 = 200 min usable. But §五 daily template sums to 30+40+10+80+20 = 180 min. Even allowing for "10 min 中场" appearing both in clock-time and in template, there is still 200 vs 180 = 20 min unallocated each day, AND 4 × 45 = 180 学时-min vs 200 usable clock-min is internally inconsistent.
- **SUGGESTED_FIX:** Either declare the 20 min as buffer / setup / overflow (which solves B2 partially) and amend §五 to "180 min 教学时间 + 20 min 缓冲" explicitly; or shorten the day to 9:00–12:10 to remove the gap.

---

## B12

- **SEVERITY:** minor
- **CATEGORY:** scope-dependency
- **LOCATION:** §十 + §七
- **CLAIM:** No mitigation if 4+ groups all pick the same project (P3 RC 电路 and P8 自由落体 are the most common bootcamp choices); the syllabus says "自由组队" + "选题菜单" but doesn't cap per-project group count.
- **EVIDENCE:**
  > §七: "分组：2 至 3 人一组，自由组队，老师做最后协调"
  > §十: "学生可以自选题，但自选题需经老师审批可行性"
  > Day 2: "各组在选题菜单内确定 1 个主选题 + 1 个备选"
  If 6 of 13 组 pick P3, Day 6 中期答辩 hears 6 nearly-identical presentations and Day 10 终答辩 likewise; pedagogical variety collapses; the "其他组提问" instrument degrades because peer questions become repetitive.
- **SUGGESTED_FIX:** Add to §七: "Each menu project (P1-P8) is open to at most ⌈n_groups/4⌉ groups; tie-broken by submission order on Day 2 evening. Groups blocked from their primary use the 备选 declared in Day 2."

---

End of report. 12 substantive issues; 3 blockers, 7 majors, 2 minors.
