# Internal Review — AI 辅助数理建模与应用实践 SYLLABUS.md

| Field | Value |
| --- | --- |
| Artifact | `/Users/jinlei/Desktop/code/vibephysics/SYLLABUS.md` |
| Venue | 内部立项 / 院系教学委员会评审 |
| Date | 2026-05-28 |
| Reviewer A | Claude (general-purpose Agent), 资深物理教学评审 stance |
| Reviewer B | Claude (general-purpose Agent), 教学设计 / 运营可行性 stance |
| Cross-checker | Host Claude (codex:codex-rescue 因 Bash 权限被门挡，由 host 直接对 SYLLABUS 验证 evidence) |

**Summary**: 5 blockers (2 凑齐为 1 consensus pair), 14 majors (1 consensus pair, 其余 single-source 但 cross-check 全部确认), 4 minors. **零 disagreement**, A 与 B 完全正交（A 走 pedagogy 维度，B 走 operations 维度，没有撞车也没有矛盾）。所有 22 个 issue 的 evidence 都在 SYLLABUS 里逐字可查，无幻觉。

**Effort estimate**:
- 必须修正的硬数学错误（Day 6 + Day 10 时间溢出 + 实例兑现）: ~3 小时
- 必须补的缺失资产（AI 审计日志 rubric + 备课资产里的演示录屏要求 + 数据采集时间块）: ~4 小时
- 必须做的结构调整（Python 速成扩容 + ODE 状态化简补丁 + 师资硬约束）: ~6 小时
- 可选优化（菜单多样化 + no-AI baseline + 失败模式 6/7/8）: ~4 小时

总计 ~13-17 小时修订工时，全部在大纲层面，未触及备课资产。

---

## Consensus issues — A 与 B 从不同角度撞到同一个洞

### C1. **单一教师负载在 25–40 人 / 8–13 组班额下数学上不闭合**
- **Severity**: blocker | **Category**: instructor-load / risk-realism
- **Location**: §一（助教 0 至 2 人视申请情况）+ §五（每日轮巡）+ §八（20% AI 审计日志）+ Day 9（一对一 5–8 min/组）+ §十一 风险 5
- **Evidence**: §一 "助教 0 至 2 人（视申请情况）"; Day 9 "80 min 写作时间，老师一对一过初稿（每组 5 至 8 分钟）"; §八 AI 审计日志权重 20%
- **A's angle (A6)**: Day 9 一对一 8 min × 13 组 = 104 min, 已经爆掉 80 min 预算；每日轮巡 80 min / 13 组 = 6.2 min / 组只能照看一遍，碰到一个难问题就崩。
- **B's angle (B3)**: 还要加上每晚批改 25–40 份 AI 审计日志，按 "真的发现并修复" 这种深度评分大约 5 min/份 × 40 份 = 200 min / 晚 = 33 小时 10 天，纯加班量。
- **Suggested fix**: 把 "助教 0 至 2 人" 改成硬约束：≤ 8 组（≤ 24 人）才能单师，> 8 组必须配 1 名助教。或者把日志评分降级为三档勾选制（✓ / ✗ / ?）+ 每周 2 天深批，把 200 min/晚 砍到 60 min/晚。**这条不解决，第一轮开课会直接翻车。**

### C2. **AI 演示的可复制性资产缺失，但课程把它定为 "最重要的教学资产"**
- **Severity**: major | **Category**: reproducibility + ai-use-honesty
- **Location**: §五 "教学方法" 的关键原则 + §十二 备课清单 + 每个 Day 的 "教师演示" 块
- **Evidence**: §五 "这门课最重要的教学资产是真实的 AI 协作录像，不是 PPT"; §十二 列出 8 项备课资产但**不含演示录屏**
- **A's angle (A11)**: 课程承诺 "演示真实 AI 对话, 包括 AI 出错的瞬间", 但到 Day 4 AI 可能就不出错了, 直播变 theater, 课程自己批评的"伪装"反过来打在自己脸上。
- **B's angle (B10)**: 没有 master tape, 下一年别的老师 (或 PhD 助教) 接班这门课时无法复现, 课程隐式绑死单一教师。
- **Suggested fix**: §十二 备课清单增加第 9 项: "10 段教师 AI 演示录屏 (每天 1 段, 30–40 min/段, 含 fallback prompt list when AI 当天不自然出错)"。把录屏从 "副产品" 升格为 "首要交付件"。

---

## Single-reviewer blockers — cross-check 确认, 但只有一位 reviewer 触及

### S1. **Day 2 仅 40 min Python 速成不足以承接当天 80 min 实战** [Reviewer A only]
- **Severity**: blocker | **Category**: audience-mismatch
- **Location**: Day 2
- **Evidence**: "40 min Python 速成：变量、循环、函数、numpy 数组、matplotlib 画图（不教 OOP，不教异常处理）" + 紧接 "80 min 学生实战：先用计算器手算前 10 步 Euler，再让 AI 写完整脚本"
- **Issue**: 大一只学过 C/C++ 入门的学生在 40 min 里达到 numpy 字面理解几乎不可能。Day 2 后半段的 "对比手算和 AI 数值结果" 假设学生已经能读懂 AI 给的 numpy 代码。
- **Suggested fix**: 两条路二选一: (a) 在 Day 1 之前发一个 2 小时的预修 Python 速成视频 + 自测清单 (强制非评分); (b) 把 RC + Euler 推到 Day 3, Day 2 整 180 分钟全部给 "读改 AI 给的脚本", 不要求学生从零写。**当前 Day 2 默认学生 numpy-literate, 这是没说出口的硬假设。**

### S2. **Day 3 引入 "二阶 ODE 化为两个一阶" 但没分配任何讲解时间** [Reviewer A only]
- **Severity**: blocker | **Category**: hidden-assumption
- **Location**: Day 3 学习目标
- **Evidence**: 学习目标 "用 Python 解二阶 ODE（化为两个一阶）"; 当天分时段 30 min 物理 + 40 min AI demo + 80 min 实战 + 20 min 复盘, **没有一格留给 state-vector reduction 的讲解**
- **Issue**: 这是大一学生在数理方法之前从未接触过的概念, 是 Day 3 物理建模的中枢动作, 但被当成 obvious 一句话带过。
- **Suggested fix**: 从 80 min 实战块切 20–30 min 出来, 板书 y'' = -ω²y → y' = v, v' = -ω²y, 学生用纸笔做一次再碰代码。

### S3. **Day 6 时间预算在 13 组班额下溢出 20–55 min** [Reviewer B only]
- **Severity**: blocker | **Category**: time-arithmetic
- **Location**: Day 6
- **Evidence**: 列表预算 30+40+80+20 = 170 min, 80 min 中期答辩在 "每组 5 分钟讲" + "其他组提问" 的设置下: 13 组 × 5 min talk = 65 min + 1 min/组 Q&A = 78 min, 已经吃满 80 min 没有切换间隙; 若 Q&A 2 min/组则 91 min 直接爆 80 min slot
- **Issue**: 班额上界 (40 人 / 13 组) 时 Day 6 跑不下来。
- **Suggested fix**: 取消 Day 6 中期 Q&A 改为同伴书面反馈卡, 同时把 "学生实战 A (bug 卡 20-min sprint)" 移到 Day 5 课后作业, 腾出 40 min 给答辩。

### S4. **Day 10 时间预算在 13 组班额下数学上跑不下来** [Reviewer B only]
- **Severity**: blocker | **Category**: time-arithmetic
- **Location**: Day 10
- **Evidence**: "150 min 项目答辩 + 20 min 中场 + 30 min 总结 + 10 min 反思" = 210 min, 已超出 180 min 教学日预算 30 min; 13 组 × 12 min = 156 min 本身就 > 150 min slot, 还不算切换、设备调试、超时
- **Issue**: 列表加和直接看就溢出。
- **Suggested fix**: 三条任选: (a) 把单组答辩压到 10 min (7 展 + 3 问) + 1 min 切换 → 11 min × 13 = 143 min; (b) 终答辩拆成 Day 10 上午 + 下午两段; (c) §一 班额硬卡到 ≤30 人 ≤10 组。**写哪条进 §一**, 别留在脑子里。

---

## Single-reviewer majors — cross-check 全部确认

### Pedagogy 维度 (Reviewer A)

| ID | 一句话 | Location | Fix |
| --- | --- | --- | --- |
| A3 | leapfrog 在 Day 3 当 "magic trick" 出现, 但学生没数理基础解释它 | Day 3 实战块 | 要么删除, 要么显式声明是黑箱升级且不考 |
| A4 | Day 4 一格 30 min 同时塞二维向量化 + numpy 广播 + 无量纲化, 三个新抽象叠加 | Day 4 课堂内容 | 把 nondimensionalization 推到 Day 5 (天然搭配拟合), Day 4 只保留 2D = 两个 1D |
| A5 | 60 秒 AI 审计反射弧从 Day 1 卖, 但 10 模式分类法到 Day 6 才教 | §二 + Day 1 vs Day 6 | Day 1 先给 3 类简版分类 (单位 / 符号 / 数量级), Day 6 扩到 10 类 |
| A7 | Day 5 拟合 + Day 7 文献核验都没有 "无 AI 基线" 校准 | Day 5, Day 7 | Day 5 让学生手动跑一次 curve_fit, Day 7 用 Google Scholar 自己找 1 篇 |
| A8 | Day 4 (forward sim) → Day 5 (backwards inference) 概念跳跃没桥 | Day 5 概念开场 | 加一句 "Day 1-4 模型预测, Day 5 数据反推, 这是科学闭环另一半"; 用参数 ±10% 扫代替不可解释的 pcov |
| A9 | 8 个项目里 6 个是振子家族, 偏 ODE 单一 | §十 项目菜单 | 加 P9 一维 random walk / 扩散 (含解析对比) + P10 光学衍射图案提取 |
| A10 | §三 声明 "数值方法只用 Euler", Day 3 leapfrog + Day 5 curve_fit 直接打脸 | §三 vs Days 3,5 | 改写为 "显式教 Euler; 黑箱用 (leapfrog, curve_fit, optimize) 且明确披露" |

### Operations 维度 (Reviewer B)

| ID | 一句话 | Location | Fix |
| --- | --- | --- | --- |
| B4 | 20% AI 审计日志没有评分细则, 教学组无法可复现地打分 | §八 | 加 4 档 anchor 描述 (A 90+, B 75-89, C 60-74, F <60) + §十二 备课清单加 1 满分 1 不及格示范 |
| B5 | 第一轮 60-80 小时备课低估, 逐项算下来 100-140 小时 | §十二 | 改为 "100-140 小时, 提前 4 周开始"; 或开课时只交付 5 张 bug 卡, 另 5 张第 1 轮课后补 |
| B6 | 风险段缺 3 项高概率运营故障: AI 服务断、教师病假、教室 AV 故障 | §十一 | 增 Risk 6 (本地 LLM + 预录演示兜底), Risk 7 (指定备份助教), Risk 8 (Day-1-style 离线纸笔兜底) |
| B7 | 数据采集型项目 (P1/P2/P3/P5/P8) 没排数据采集时段, Day 5 草稿图截止时数据未必在手 | Day 2-5 + §十 | 三选一: (a) 预备 "数据 locker" 给每个题型; (b) Day 5 草稿图推到 Day 6 上午, 给 Day 4 晚 + Day 5 60 min 做采集; (c) 数据重项目要 Day 2 提交采集计划 |
| B8 | Day 1 课后 10-min 视频指引装 Python 历来 15-30% 失败, Day 2 早晨没兜底; Day 7 BibTeX/DOI/INSPIRE-HEP 40 min 速成对没用过 LaTeX 的大一太满 | Day 1 课后 + Day 7 | Day 1 前夜开 1 个虚拟装机 clinic 或 Day 2 前 20 min 留 "环境兜底"; Day 7 删 INSPIRE-HEP, 改 Google Scholar 导出 |
| B9 | 三条红线 enforcement 几乎全是 honor system, 但语气是 "按学术不端处理" | §九 | 加一段把契约说透: "(1)(2) 是 honor + 抽查 + 答辩问答交叉检验, (3) 做 DOI 反查; 失报本身即违规" |

---

## Single-reviewer minors

| ID | 一句话 | Location | Fix |
| --- | --- | --- | --- |
| A12 | Day 8 切换备选项目实质上是项目放弃, 不是救援 | §十一 风险 4 | 把备选切换 deadline 提到 Day 5 或 Day 6; Day 8 的紧急选项改为 "缩减当前项目范围" |
| B11 | 9:00–12:30 = 210 clock min vs 4 学时 = 180 min, 多出 20 min 没标明 | §一 + §五 | 把 20 min 标为 "缓冲 / 切换 / 溢出" 写进 §五, 或缩到 9:00-12:10 |
| B12 | "自由组队" + 无项目数量上限 → 4+ 组撞 P3 RC 电路是常见模式, 答辩多样性崩 | §七 + §十 | 每个菜单题最多 ⌈n_组/4⌉ 组, Day 2 晚先到先选 |

---

## Disputed / withdrawn items (audit footnote)

无。两位 reviewer 没有相互矛盾或被 cross-check 撤回的 issue。Reviewer B 的 B2 严重性在班额下界 (8 组) 时为 major, 上界 (13 组) 时为 blocker; host 按 SYLLABUS 上界保留为 blocker 与 B 一致。

---

## Recommended next steps (你拍板)

按修复影响 × 工时排序:

1. **先把硬数学错误关掉 (~3 小时)**: 修 Day 6 + Day 10 时间预算 (S3, S4) + §一 班额硬卡上限。这两条不修就不能进立项书。
2. **再补两个 0 成本资产 (~4 小时)**: AI 审计日志 rubric (B4) + §十二 加 10 段演示录屏要求 (C2)。这是 review 里"无需思考、必须做"的两件事。
3. **结构性大改 (~6 小时)**: 接受单师班额上限 (C1, 改 §一 为 "≤ 8 组单师 / 8 组以上必须 1 助教"); Day 2 Python 扩容 (S1); Day 3 ODE 化简补讲 (S2); §三 数值方法声明改诚实 (A10)。
4. **可选优化 (~4 小时, 投硬币决定做不做)**: 项目菜单多样化 (A9), 增加 no-AI 基线 (A7), 风险段补 6/7/8 (B6), 装机兜底 (B8)。

要我现在直接对 SYLLABUS.md 做哪一档的修订? 或者你自己看完想动手, 我可以给你一份按 ID 排序的逐条修订 diff (不修改原文件, 只输出 patch) 供你逐个 accept/reject。
