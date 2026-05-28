# Goal

User's verbatim words (zh-CN, from this conversation):

- "这个项目要重新定位， 课程名称为AI辅助数理建模与应用实践 ， 然后 这个是给大一的学生开的， 在大一结束的暑假， 2周的密集课程"
- "你要重新设计课程大纲"
- "你写个md文档， 详细写课程大纲"
- "用这个， 你要记住， 这个是大一的学生， 基本上没怎么学过专业的物理"

Restated in one sentence (organization, not summarization): design a complete 课程大纲 (10-day, 40-academic-hour, 2-week summer intensive) for a Tongji Physics-Department course titled "AI 辅助数理建模与应用实践", offered between the freshman year and sophomore year of physics-majoring undergraduates, where the students have basically not yet studied 专业物理 (professional / upper-level physics) of any kind beyond freshman 普物.

# Current state

- Project workspace: `/Users/jinlei/Desktop/code/vibephysics/`. Git branch `main`. Recent commits:
  - `7227a25` Refocus course copy from research-method to undergraduate practice
  - `7335909` Rename course to "AI 辅助数理建模与应用实践"
  - `c874fe0` Create Vibe Physics course proposal page
- HTML one-pager at `index.html` already partially refactored: hero now displays "2 周密集课程 / 40 总学时 / 10 教学日 / 2 教师合开", brief card updated to "大一暑期密集实践训练".
- Course structural shell still in HTML but unsettled in content:
  - 4 phases (问题定义→数值与验证→项目流程→展示) — content too advanced
  - 2 教师合开 双主线 (主线 A 物理建模与数值计算 / 主线 B 数据驱动建模与应用)
  - 课堂结构 90 min (assumed pre-redesign), 项目里程碑 第3/第8/第16 课 (still pre-2-week)
  - 考核 50/20/15/10/5 (期末项目 / 验证 / 交互日志 / 作业 / 讨论)
  - 4 risk cards (依赖、假文献、错误代码、伦理边界)
- Pending product: a markdown `SYLLABUS.md` (or equivalent) with the FULL 10-day breakdown — this is what the user explicitly asked for right before invoking idea-pk.
- 2 instructors confirmed. Tongji Physics Department. Summer practice course track. Intended for a small-class pilot (25–40 人).

# Tried

## raw

Two design drafts have been considered and rejected in this conversation thread; neither was physically run as a class.

- Earlier (pre-conversation) shell: "Vibe Physics 32 学时 16-session 2学时/次 research-method course" for general undergraduates. Per commit 7227a25, the research-method framing was already refocused away toward undergraduate practice, but the 32 学时 / 16 sessions shape persisted in the HTML.
- Just before this idea-pk invocation, Claude proposed a 40 学时 / 10 教学日 / 4 学时 per day, 4-phase 大纲: Day 1–2 入门与规范 → Day 3–5 物理建模与数值计算 (含 RK4 ODE 数值积分 + SymPy 符号推导 + 数据拟合误差棒) → Day 6–8 数据应用与不确定性入门 (含 FFT 频谱分析 + 蒙特卡洛 + Bootstrap 重采样) → Day 9–10 项目冲刺与展示. The user rejected it with two messages, "你要重新设计课程大纲" and "用这个， 你要记住， 这个是大一的学生， 基本上没怎么学过专业的物理".

## normalized

- T1. Course shell modeled as 32 学时 / 16 sessions × 2 学时, framed as undergraduate research-method training for general physics undergraduates. [status: succeeded-but-insufficient; structural shell partially preserved in HTML but content already moved off research-method per commit 7227a25, and per the new mandate the time allocation is wrong for 2-week intensive]
- T2. 40 学时 / 10 教学日 / 4-phase 大纲 with core content drawn from upper-undergraduate / early-graduate numerical methods: explicit RK4 for ODE, SymPy symbolic derivations cross-checked against numerics, FFT-based signal processing, Monte Carlo integration with Bootstrap error bars, plus 反问题 / UQ as a topic. Tracks A and B kept 数学物理方法-flavored case library (振动 / 传热 / 散射 / 信号与图像). [status: failed; user's explicit reason: students "基本上没怎么学过专业的物理" — content level mismatched the audience]

(No `[needs-clarification]` items: both tried items have unambiguous status.)

# Budget / constraints

- Total academic hours: **40 学时**, fixed.
- Schedule: **10 教学日** (2 weeks, Mon–Fri × 2), **每日 4 学时** (each 学时 = 45 min, so daily teaching block ≈ 3 h).
- Class size: **25–40 students** (small-class pilot), single section.
- Instructors: **2 教师合开**. Double-track design preserved: 主线 A 偏物理建模与数值, 主线 B 偏数据与可视化分析. Identities not specified; assume one theoretical-computational and one experimental/data-analysis colleague.
- Audience math/physics floor: **freshman year complete only**.
  - Has done: 高等数学 (微积分 single + multi variable, basic ODE), 线性代数, 大学物理 (普物力学 with possibly some electromagnetism).
  - Has likely done: ONE introductory programming course (likely C++ in Chinese physics curricula), so basic loops/functions but not scientific Python yet.
  - **Has NOT done**: 数学物理方法, 理论力学, 电动力学, 量子力学, 热力学统计物理, 数值分析, 概率论与数理统计, 机器学习. The user emphasized this with "基本上没怎么学过专业的物理".
- Course name fixed: **"AI 辅助数理建模与应用实践"**. Cannot be relabeled. Must visibly use AI tools.
- Project deliverable required. Format: small-group (2–3 人), per-group artifact at the end.
- Resource baseline: machine room or BYOD with unified Python environment, Git, vetted AI tool accounts. No expectation of GPU clusters or external collaborators.
- Soft constraints (inferred from user's profile preferences, must be respected by candidate paths):
  - No em-dashes (Chinese —— / English —) in any deliverable.
  - Physics correctness > engineering polish. Course must teach a thinking habit, not a software stack.
  - Run-then-think over plan-then-think: students should see numerical/visual results within the first session, not after a week of setup.
  - Anti-overengineering: course content must not be padded to fill hours; 40 学时 should be filled by depth on a small surface, not breadth.
- Hard editor stance: the course must be teachable, examinable, and reproducible by a TA in the next summer cycle. Avoid candidates that depend on a single instructor's personal magic.
