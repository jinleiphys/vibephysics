# Reviewer B — 大一 Student Reality Check + Instructor Feasibility Audit

Artifact: `/Users/jinlei/Desktop/code/vibephysics/SYLLABUS.md` (v3.1, 692 lines)
Stance: 大一 finished 普物 + 微积分 + 线代 + maybe a C++ intro. Solo instructor, 1 助教 if class > 24. 10 教学日 × 4 学时.

---

## ID: B1
SEVERITY: blocker
CATEGORY: self-generate-overreach
LOCATION: §五.2 (lines 168-188) + Day 2 课后任务 (lines 258-259) + §七 时间节点 (line 500)
CLAIM: Requiring 大一 students who have never seen a PRD or AGENTS.md to **simultaneously** self-generate BOTH artifacts on Day 2 evening — within hours of their first day of actual Python — is a cognitive overload that the "原则 + case study" scaffolding does not adequately support, and the timing collides with the Python-script-comprehension homework also due that night.
EVIDENCE:
- §五.2: "这门课**不发任何 fill-in-the-blank 模板给学生**。不发 PRD 模板, 不发 AGENTS.md 模板, 不发 SKILL.md 模板, 不发 6-D prompt 模板。"
- Day 2 课后任务: "为主选题自己写一页 `PRD.md`. 课堂上你听过原则 (5 类必答问题... ) + 看过老师投影上的 good/bad/ugly 范例 case study. 现在用你自己决定的格式 (表格 / 散文 / 图表均可) 把 5 类问题答了."
- Day 2 课后任务: "为主选题自己写一页 `AGENTS.md`. 课堂上你听过原则 ... + 看过范例 case study. 现在用你决定的方式把这些约束写下来."
- Day 2 课后任务 also includes: "用 Euler 解一个自选小问题 ... 交一张图"
- Day 1 only contains 5 min PRD pre-announcement: "今天你只需要知道它存在" — no actual PRD instruction time on Day 1.
- Day 2 课堂内容 has zero minutes allocated explicitly for AGENTS.md teaching (60 min reading script + 60 min student script work + 25 min Euler debrief).
SUGGESTED_FIX: Stagger the two artifacts — PRD due Day 2 night (a v0 sketch only, 5 questions answered crudely), AGENTS.md due Day 3 night after Day 3 has at least 15-20 min explicit AGENTS.md case-study slot. Tell students explicitly "Day 2 PRD is intentionally bad and will be torn apart Day 3 morning, do not over-polish." Add a Day 3 morning explicit AGENTS.md case-study segment before assigning it.

---

## ID: B2
SEVERITY: blocker
CATEGORY: cognitive-overload
LOCATION: Day 8 (lines 407-438), specifically lines 425-431
CLAIM: Day 8's 180-min teaching block is asked to deliver (i) 5-item verification checklist explained with 3 examples, (ii) live instructor demo of running the checklist on a student project, (iii) Skill-building 速通 lecture with a Skill case study, (iv) 40 min students run checklist on their own project, (v) 30 min students draft their first-ever SKILL.md, (vi) class point-evaluation of one Skill draft. This is six different cognitive tasks in 200 minutes, and the SKILL.md drafting at the end (30 min, after 70 min of unrelated checklist work) is where most students will be cognitively bankrupt.
EVIDENCE:
- Day 8 schedule: "25 min 五项验证清单详解，配 3 个例子" + "30 min 教师演示" + "10 min 中场" + "25 min Skill-building 速通" + "70 min 学生实战分两段: 前 40 min 各组对自己工件跑五项清单 ... 后 30 min 每组讨论 ... 选其中一个**自己长出一份 SKILL.md 草稿**" + "20 min 答疑 + 抽 1 组展示 Skill 草稿全班点评"
- "**今天是这门课最具复利价值的一天**——五项清单 + 自己的 Skill 是你下学期解新物理问题时能直接用的两套工具" — but the schedule treats two complex artifacts as if they could share one day.
SUGGESTED_FIX: Split Day 8 into "verify-only" and move first-attempt SKILL.md drafting to **Day 9 morning** (currently Day 9 has 25 min 报告写作 + 25 min AI使用说明 + 50 min architecture review + 50 min unstructured writing — easy to carve a 60-min Skill block out of). SKILL.md is a Day 9 deliverable, not a Day 8 课后 deliverable.

---

## ID: B3
SEVERITY: major
CATEGORY: framework-difficulty
LOCATION: §五.1 (lines 147-167) + Day 5 (lines 320-353)
CLAIM: Day 5 expects 大一 with no prior prompt engineering exposure to: (a) absorb 6 abstract dimensions in 25 min lecture, (b) watch one 35-min v1-vs-v2 comparison demo, (c) write their own 6-dimension-covering prompt in 25 min while **reverse-tagging which sentences are D1..D6 in their own prose**, (d) run a prompt-iteration round documenting which dimension they edited, (e) do a no-AI Excel baseline, (f) draw a 3-panel data figure, all in 70 min student work. The reverse-tagging step in particular is meta-cognition about prose they just wrote — this is graduate-level reflection asked of week-2 大一.
EVIDENCE:
- Day 5: "前 25 min: 各组把自己项目的'接数据 + 做拟合'任务写成一份 prompt, **6 个维度都要覆盖到**" + "在日志里**显式标出'我这份 prompt 的 D1 是哪几句, D2 是哪几句...'** 这个反向标注动作本身就是 6-D 内化的训练."
- Day 5: "后 45 min: 用这份 prompt 让 AI 出代码, 接入数据, 画三联图; **显式做一次 prompt 迭代轮**; **显式做一次 No-AI 基线对账**"
- 学习目标 expects: "**掌握 Anthropic 6-D 框架** (D1-D6), 能在 5 分钟内为一个物理任务写出符合 6-D 的完整 prompt"
SUGGESTED_FIX: Drop the reverse-tagging requirement for Day 5; replace with "your prompt must have a section labelled '我覆盖了哪些维度' listing 6 checkboxes" — that is checkbox-discipline, not reflexive tagging of one's own prose. Push reverse-tagging to Day 6 or Day 8 as part of the audit habit, when students have prose they did NOT just write under time pressure. Also cut the no-AI Excel baseline on Day 5 (see B7).

---

## ID: B4
SEVERITY: blocker
CATEGORY: instructor-load
LOCATION: §一附注 (lines 23-26) + §五.2 (line 187) + §八 (lines 524-545) + multiple grading touchpoints across Days 2/3/6/7/8/9/10
CLAIM: Solo instructor with 1 TA for 9-11 组 cannot sustain the cumulative evening grading load. Pencil it out for an 11-组 class:
- Every night × 10: 11 AI 审计日志 (11 × 1 min checkbox + 5 × 5 min deep-审 on Tue/Thu = ~11 + 25 = 36 min on deep-审 nights, ~11 min other nights)
- Day 2 night: 11 PRD + 11 AGENTS.md, each format-free, instructor must judge by 原则 not format-match → realistically 10-15 min per pair = 110-165 min one night
- Day 3 morning: 抽 3 组 PRD/AGENTS 投影 — requires Day 2 night reading **all** to pick the 3
- Day 6 night: post mid-term critique cards distribution + per-group 1-条 improvement = additional 30-45 min
- Day 7 night: 抽 3 组 streamlit URL 启动验证(=15-30 min) + DOI 反查 all submitted citations (3 refs × 11 组 = 33 DOIs to verify = ~60 min)
- Day 8 night: 11 checklist.md + 11 first-version SKILL.md (the latter format-free, judged by "是否能在另一个 AI 上激活") = ~120 min
- Day 9 night: 11 final reports (2-4 pp each) + 11 slide decks + 11 AI 使用说明 finals = ~150 min minimum
- Day 10: 121 min 答辩 + on-the-spot grading of all 5 工件
This sums to **~12-15 hours of evening grading over 10 days, on top of 9:00-12:30 teaching and 80-min daily 轮巡**. With 1 TA who is a graduate student not the instructor, the format-free 原则-based grading (PRD / AGENTS / SKILL) cannot be delegated — only DOI checks and checklist.md formal items can.
EVIDENCE:
- §五.2: "**这条立场对教师有更高要求**: 你要能即兴评价 8-13 份格式完全不同的学生 PRD, 不能简单按'格式对不对'打分."
- §一附注: "单师每晚批改 AI 审计日志按'勾选 + 抽审'制：勾选每份 1 分钟，抽审 ≤ 5 份每份 5 分钟（详见 §八）。24 人班额下单师总评分时长 ~50 分钟 / 晚" — this estimate only counts AI 审计日志, ignoring PRD, AGENTS, streamlit, SKILL, report grading on their respective deadline nights.
- §一附注 班额数学 only addresses 答辩 slot + 轮巡 + 日志, **not the cumulative non-日志 grading**.
SUGGESTED_FIX: Hard-cap class at 8 组 (24 人) **regardless of TA presence** for v1 offering — the format-free grading is the real bottleneck, not the 答辩 slot. Re-do §一附注 math to include PRD-night (~150 min), Day 8 night (~120 min), Day 9 night (~150 min) — these are the actual budget breakers, not the 50 min/晚 日志 figure. Alternatively, soften "format-free" rule for v1: provide a 30-second-fill rubric checkbox even if students choose free format, so TA can do first-pass triage.

---

## ID: B5
SEVERITY: major
CATEGORY: dropout-mechanism
LOCATION: Day 1 (lines 215-220)
CLAIM: The "退课" mechanism reads as a real escape hatch on Day 1 morning, but 中国高校 admin reality for a 暑期实践 intensive course is that drop deadlines are typically set days/weeks before the course starts — students who show up Day 1 morning have already committed and likely cannot drop without academic-affairs friction (or at all). Without an actual drop window verified against 教务处 policy, this paragraph reads as instructor venting / threat with no escape valve, which contradicts the cognitive-ownership ethic the course preaches.
EVIDENCE:
- Day 1: "**如果你想要的是 '老师给标准答案我照着填' 这种课, 这门课不适合你**, 教务系统选课退课截止日之前请退. 退课不影响你后续课程, 这门课也不缺人."
- The phrase "教务系统选课退课截止日之前" presupposes the deadline is after Day 1 morning — but the syllabus nowhere documents this is true.
- Course is "10 个连续工作日，每日 4 学时" 暑期实践 (line 17), the most common admin pattern for which is "drop deadline = day before T-day".
SUGGESTED_FIX: Either (a) verify with 教务处 that drop is permitted through Day 1 EOD and write the explicit deadline into the syllabus ("退课截止 Day 1 17:00"), or (b) reframe as "如果你听完今天 30 分钟介绍想退, 我尊重 — 来跟我谈, 我帮你走流程" putting the human-mediated path on record rather than pointing at an admin deadline that may not exist. Otherwise delete the段 entirely; the threat without escape is worse than no threat.

---

## ID: B6
SEVERITY: major
CATEGORY: concept-realism
LOCATION: §二 "五件工件" 第 2/5 项 (lines 58, 61) + §四 学习目标 9 (line 124) + §十二 第 12-13 项 (lines 668-669) + §教师参考阅读 (line 690)
CLAIM: AGENTS.md and the Claude Skill format are both very-recent emerging community conventions, not stable shared-community standards. Betting a 2-week 大一 course's headline transferable artifact on formats that may shift, get superseded, or simply fail to gain critical mass means students may graduate carrying a skill that is illegible to the AI community by next summer. This is a concept-realism risk distinct from "is it teachable" — it is "is this thing still going to exist".
EVIDENCE:
- §二 (line 58): "**`AGENTS.md`**（或 `.cursorrules`）: 项目级 AI 约束文件" — the slash with `.cursorrules` itself signals the format is in flux.
- §二 (line 61): "**`SKILL.md`（你自己造的物理 Skill）**: 一份 Claude Skill / Cursor rule / 通用 AI 工作流定义文件" — three different community conventions are being conflated.
- §四 (line 124): "课程结束时每个学生至少带走一个能在自己电脑 Claude / Cursor 上激活的物理 Skill, 下学期解新问题时能复用. **这是这门课最值钱的可携带产出**"
- 教师参考 (line 690): "AGENTS.md spec (Linux Foundation 管理) + .cursorrules 集合 + llms.txt 规范" — three not-yet-converged specs listed.
- 教师参考 (line 691): "Claude Skill 文档 (Anthropic) + Claude Code Skills 实际例子" — vendor-specific format, not a community standard.
SUGGESTED_FIX: Reframe the artifact as "you build a project-instruction-file in whatever AI-instruction format your tools support today; the **skill is the abstraction, not the file syntax**". Make explicit in §二 that "this format may evolve; what carries forward is your habit of compressing reusable workflows into a single file." Drop "最值钱的可携带产出" framing — the verification-reflex and PRD-writing reflex are far more durable than the file syntax. Also avoid claiming AGENTS.md is a standard the wider research community has adopted; in 2026 it is not, and 大一 saying "I wrote an AGENTS.md" outside this course will mostly get blank looks.

---

## ID: B7
SEVERITY: major
CATEGORY: no-ai-burden
LOCATION: Day 5 (line 328) + Day 7 (line 393) + Day 8 五项清单 (line 422)
CLAIM: A course explicitly titled "AI 辅助" and built on "let students direct AI" then imposes **cumulative** no-AI overhead in Days 5-8 that contradicts the headline. The no-AI Excel/纸笔 least-squares baseline on Day 5 (a topic 大一 has never seen formally — they likely cannot do mean(x)mean(y) least squares by hand without a 25-min teaching segment first), the no-AI literature search on Day 7, and the largely-no-AI 5-item verification checklist on Day 8 stack on top of each other in a way that turns Days 5-8 into a no-AI审计 marathon, exactly the phase when students should be in flow shipping their工件.
EVIDENCE:
- Day 5: "**No-AI 基线**：自己用 Excel 或纸笔做一次同数据的简单最小二乘（比如线性拟合的 mean(x)mean(y) 公式），与 AI 给的数字对账"
- Day 7: "**No-AI 基线**：手动用 Google Scholar 自己找 1 条文献（不让 AI 推荐）"
- Day 7 task: "至少有 1 条文献你完全不用 AI、只用 Google Scholar 自己找到"
- Day 8 五项清单 — items 1 (量纲), 3 (守恒律), 4 (参数扫描), 5 (与文献对比) are mostly no-AI activities; only item 2 (解析极限) cleanly uses AI.
- §四 学习目标 6 (line 121): "对自己（或 AI）的数值结果跑完五项检查" — all five are no-AI-able.
SUGGESTED_FIX: Pick ONE no-AI baseline as the canonical "you must prove you can do it by hand" demonstration — recommend Day 5 's least-squares-by-hand because it dovetails with linear-algebra they have just finished. Drop the Day 7 "1 文献不靠 AI" rule (a 大一 finding a real physics paper without AI guidance is just frustrating, not pedagogically valuable) — replace with "you must read at least 1 paper end-to-end". Reframe Day 8 checklist as "AI does the math, you decide which math to ask for" rather than "you do the math".

---

## ID: B8
SEVERITY: major
CATEGORY: framework-saturation
LOCATION: throughout — §二 (5 反射 + 5 工件 + 4 阶段), §五.1 (6 维), §九 (4 原则 + 三条红线 + 4 栏 AI 说明), Day 6 (10 大错误), Day 8 (5 项验证)
CLAIM: The course as written exposes 大一 to: 5 反射动作 + 5 件工件 + 4 阶段工作流 + Anthropic 6 维 + Kong 4 原则 + 三类→十类审计 + 5 项验证 + 三条红线 + 4 栏 AI 使用说明 + 4 phase × 8 stage lifecycle map. Counting distinct named frameworks the student is expected to track simultaneously: ≥ 10. Cognitive science strongly suggests 大一 will track 2-3 and quietly abandon the rest. The frameworks then become opaque jargon used by the instructor to grade, not internalized scaffolds the student uses.
EVIDENCE:
- §二 (lines 36-42): "**五条反射动作**"
- §二 (line 53): "**项目必须同时产出的'五件工件'**"
- §二 (lines 46-51): "Setup → Code → Test → Deploy 四阶段工作流"
- §五.1: "Anthropic 6-D prompt engineering 框架"
- §九 (lines 591-596): Kong et al. 4 design principles a-d
- Day 6 (line 366): "10 大 AI 错误模式"
- Day 8 (lines 417-423): 五项验证清单
- §九 三条红线 + 4 栏 AI 使用说明
- §二 (lines 68-78): "4 个阶段 × 8 个 stages" Kong life-cycle map
- §二 (line 84): "这五个动作、五个工件、四个阶段、cognitive ownership 原则" — already 4 nested frameworks just in this sentence.
SUGGESTED_FIX: Designate ONE central framework — the 5 反射动作 — as the **only** thing every student must internalize and be assessable on. Demote the others to instructor-side teaching scaffolds that the syllabus describes but does not require the student to actively reference. Specifically: drop the "4 phase × 8 stage Kong lifecycle map" from student-facing material (keep in §十二 instructor reading), do not test on 4 design principles a-d, do not require 反向标注 to D1-D6 (see B3). One central framework + scaffold rest = students actually remember 5 things; ten central frameworks = students remember zero and fake the others on exam.

---

## ID: B9
SEVERITY: major
CATEGORY: day-load
LOCATION: Day 2 morning (lines 246-253) + Day 2 课后任务 (lines 256-261)
CLAIM: Day 2 morning is the first day students touch Python in class (the "通过读一段完整脚本学 Python" segment is 60 min). The course assumes that by Day 2 evening, those same students who just learned Python an-hour-ago can produce: (i) PRD page (~30-60 min of cognitive work for a first attempt), (ii) AGENTS.md page (~30-60 min), (iii) Euler scratch problem with a figure (~30-60 min). That is 2-3 hours of focused homework on top of a full teaching morning, with two of the deliverables being formats they have never seen before. Realistic completion rate on Day 3 morning will be much lower than the syllabus assumes.
EVIDENCE:
- Day 2 课堂内容 line 249: "60 min **通过读一段完整脚本学 Python**：老师投影一份 RC 放电完整脚本... 逐行讲。涉及的语言要素只是：变量、`for` 循环、函数定义、`numpy.zeros`+`numpy.linspace` 两个数组操作、`matplotlib.pyplot.plot` 一个绘图调用."
- Day 2 课后任务 lines 256-261: 主选题 + PRD + AGENTS.md + Euler 自选小问题图.
- Day 3 morning lines 280-282: "板书 y'' = -ω²y → y' = v..." + "PRD → 架构图 → AI 实现 vibe-coding flow 演示" — Day 3 morning **assumes** Day 2 night homework is done well enough to be peer-comparable on the projector by line 262 抽 3 组 投影.
SUGGESTED_FIX: Either (a) push AGENTS.md to Day 3 evening (after Day 3 morning has dedicated case-study time) — see B1, or (b) reduce Day 2 evening to PRD-only and drop the Euler 自选小问题 (the Day 2 in-class Euler-by-hand-5-steps already provides the Euler practice). Add an explicit line in Day 2: "tonight's PRD is intentionally crude — 30 min not 3 hours".

---

## ID: B10
SEVERITY: major
CATEGORY: deployment-realism
LOCATION: Day 7 (lines 380-403) + §七 时间节点 (line 505) + §十一 风险 (lines 627-650 — no risk addresses Streamlit deploy failure)
CLAIM: Streamlit Community Cloud deployment requires (i) a GitHub account, (ii) a public GitHub repo with `requirements.txt` correctly pinned, (iii) Streamlit Cloud OAuth-linked to GitHub, (iv) successful build under network conditions that may not exist in CN classrooms. §三 explicitly does not assume Git background. Day 7 课后 requires "项目仓库里有可跑的 `streamlit_app.py`" and the instructor "当晚抽 3 组验证启动" — but this is **local** validation, while §七 line 511 lists "Streamlit Community Cloud URL（推荐）" as the main deliverable. The gap between "I have a streamlit_app.py file" and "I have a working public URL" is the entire Git+CI+OAuth+deploy stack, none of which is taught.
EVIDENCE:
- §三 line 100: "**不假设：** ... Git、Jupyter、Markdown、LaTeX"
- Day 7 line 391: "40 min 学生实战 A：各组让 AI 把自己项目的核心脚本包装成 Streamlit 应用..."
- Day 7 line 397: "Day 7 课后每组项目仓库里必须有一个可跑的 `streamlit_app.py`"
- §七 line 511: "**可访问可分享工件**：Streamlit Community Cloud URL（推荐）/ Hugging Face Spaces URL / 本地一键启动 zip 任选其一"
- Day 9 line 462: "Streamlit 工件 URL 提交（如部署在 Streamlit Community Cloud / Hugging Face Spaces；不部署的话提交本地一键启动脚本 + zip）"
- §十一 has no risk entry for "Streamlit Cloud deploy fails for 30% of groups on Day 9 night."
- Day 10 line 483: "14 min 缓冲: 设备切换 / **Streamlit 起不来兜底** / 答辩超时收尾" — the syllabus itself anticipates startup failure on Demo Day.
SUGGESTED_FIX: Demote Streamlit Community Cloud from "推荐" to "可选 stretch goal". Make the **default** deliverable a local one-click zip (a `run.sh` or `run.bat` that creates a venv, pip-installs, and launches streamlit on localhost). Add explicit risk 9 to §十一 covering "deploy fails" with the local-zip fallback as canonical. If Cloud deploy is to be taught, add a 30-min Git-+-deploy mini-session somewhere in Day 7 (currently zero minutes on Git).

---

## ID: B11
SEVERITY: minor
CATEGORY: framework-difficulty
LOCATION: §二 lines 68-78 (Kong 4 phase × 8 stage lifecycle map)
CLAIM: The "where this course sits in the broader research lifecycle" map drops a 4-phase × 8-stage taxonomy onto 大一 students who do not yet know what peer review, rebuttal, or paper2X mean. Presenting it as an "抱负级地图" (aspirational map) is honest framing, but it still occupies cognitive real estate in §二 — the course's identity-setting section — that would be better spent reinforcing the 5 反射 reps. 大一 cannot use information about Stage S6 Peer Review until they actually do peer review, which is years out.
EVIDENCE:
- §二 line 68: "**这门课在更大研究生命周期里的位置（抱负级地图）：**"
- Lines 71-76: full 4-phase × 8-stage table.
- Line 78: "**今天学到的 5 条反射动作在那些后续阶段一字不变**——只是工件从'Streamlit 物理交互页'换成'PRC 投稿稿件' / 'rebuttal letter' / '组会 slides'." — this is the actual takeaway and could replace the table.
SUGGESTED_FIX: Compress the lifecycle map to a single sentence: "这门课覆盖了未来研究生涯的 idea→experiment→figure→share 那一段; 后面 4-5 年还会学到 paper writing, peer review, rebuttal — 但你今天练的 5 条反射弧在那些阶段一字不变." Move the full table to §十二 教师参考阅读 as instructor-side reference.

---

## ID: B12
SEVERITY: minor
CATEGORY: instructor-load
LOCATION: §十二 备课清单 (lines 656-680)
CLAIM: The 100-140 hour first-round prep budget is plausible **only if** the instructor already owns deep familiarity with all source material (Kong et al., Anthropic 6-D, Karpathy vibe coding, AGENTS.md spec, Claude Skill format, Streamlit). For an instructor encountering 6-D framework or Claude Skill format for the first time, add another 30-50 hours of background reading before item 16 can be authored. The estimate also undercounts item 9 (10 recording sessions × 30-40 min each, but recording-then-editing-then-fallback-prompt-prep is closer to 4-5 hr per session than the 2.5 hr implied).
EVIDENCE:
- §十二 line 656: "开课前需要准备的资产（按 internal-review B5 重新校准时间预算 100-140 小时）"
- Item 9 line 666: "10 段教师 AI 演示录屏（每天 1 段, 30-40 min/段; 解决 internal-review C2 issue + 风险 8 的 master tape 要求）...≈ 25 小时" → 2.5 hr per finished 30-40-min recording with fallback-prompt prep is unrealistic; professional edu video is typically 5-10× final length.
- Item 16 line 672: "Anthropic 6-D Prompt Engineering 教学包 ... ≈ 5 小时" — only feasible if instructor already fluent in 6-D; otherwise add reading time.
SUGGESTED_FIX: Re-estimate item 9 at ≈ 40-50 hours (4-5 hr × 10 segments) and add an explicit "background reading prerequisite" line in §十二 listing the source materials and the assumption that the instructor has read them before counting starts. Note that 第二轮 30 hr estimate is fine because by then the background is amortized.

---
