# Internal Review — SYLLABUS.md v3.1

| Field | Value |
| --- | --- |
| Artifact | `/Users/jinlei/Desktop/code/vibephysics/SYLLABUS.md` (v3.1, 692 lines) |
| Venue | 内部立项 + 课程实施前再审 |
| Date | 2026-05-28 |
| Reviewer A | Claude (general-purpose Agent), 课程身份连贯性审计 stance |
| Reviewer B | Claude (general-purpose Agent), 大一可行性 + 单师工作量审计 stance |
| Cross-checker | Host Claude (codex 仍被 Bash 权限门挡); 已 grep 验证两份报告所有 evidence 在 SYLLABUS 中逐字命中, 无幻觉 |

**Summary**: 2 consensus blockers, 4 consensus majors, 13 single-reviewer majors, 6 minors. **Zero disagreement** — 两份报告完全互补 (A 走概念维度, B 走可行性维度, 不撞车不矛盾)。

**Effort estimate**:
- 框架收束 (Kong 4×8 demotion + 4 阶段 = 5 反射 isomorphic 处理 + 13 名 framework 压到 1 中心): ~3 小时
- Day 2 / Day 8 / Day 9 工作量重排 (PRD/AGENTS/SKILL deliverable 重新分布): ~3 小时
- §一附注 instructor load 数学重算 + Streamlit local-zip 改默认 + B10 风险加: ~2 小时
- SKILL.md 国内栈平替 reframe (A8+B6): ~1.5 小时
- 反模板立场杂项 (A1 frontmatter / A2 §十二 items 3+7 / A11 5类 vs 5栏): ~1 小时
- Day 1 不适合谁段重写 (A10+B5): ~30 min
- Day 5 reverse-tagging fix (B3) + 4 战术 fold-in (A12) + No-AI 负担收束 (B7): ~1 小时
- §九 phase-handoff list 内部矛盾修复 (A7): ~15 min

总计 ~12 小时 v3.2 修订。

---

## Consensus issues — A 与 B 从两个维度撞到同一个洞

### C1. **框架饱和: §二 装载 8+ 个独立命名框架, 全文 13 个, 大一记不住** (consensus: A3 + A9 + B8)

- **Severity**: major | **Category**: concept-stack-overload + framework-saturation
- **Location**: §二 (lines 36-84) + 全文计数
- **A 角度**: §二 现在用 8 个独立编号的框架定义课程身份（5 反射 + 5 工件 + 4 阶段 + 4-phase×8-stage + Karpathy + cognitive ownership）, 全文累计 13 个 named numbered frameworks. §二 line 84 自己列出"5 个动作、5 个工件、4 个阶段、cognitive ownership 原则"——课程身份段在承认自己是 4 套并列分类堆叠。
- **B 角度**: 5 反射 + 5 工件 + 4 阶段 + 6 维 + 4 原则 + 三类→十类审计 + 5 项验证 + 三条红线 + 4 栏 AI 使用说明 + 4×8 lifecycle = ≥ 10 个独立框架, 大一在 2 周里能 track 2-3 个, 其余被默默放弃, 沦为老师评分用的 jargon 而不是学生内化的脚手架。
- **Suggested fix**: 选 **5 反射动作** 作为 the central framework, 其余降为"教师讲解时引用的脚手架"。删 §二 4 阶段 Setup→Code→Test→Deploy 表（与 5 反射近同构, 见 C2）, 把 Kong 4×8 lifecycle map 移到 §十二 教师阅读清单（见 C3）。明确告诉学生"你只需要记住 5 反射 + 5 工件; 其他出现在评分细则里, 不要求你背"。

### C2. **Day 2 课后要求 PRD + AGENTS.md 双交付, 但 Day 1-2 in-class 从未教过 PRD / AGENTS.md** (consensus: A6 + B1 + B9)

- **Severity**: blocker → demoted to major after cross-check (real but solvable by repositioning)
- **Category**: hidden-dependency + self-generate-overreach
- **A 角度**: Day 1 只有 5-min PRD 预告 (line 221) 明确说"今天你只需要知道它存在"; Day 2 in-class (lines 246-253) 是物理回顾 + 读 Python 脚本 + 手算 Euler——零 PRD/AGENTS.md 教学时段。Day 2 课后任务 (line 258) 却说"课堂上你听过原则 + 看过 case study", 这是 counterfactual 的。
- **B 角度**: Day 2 evening 要求 3 件交付 (PRD ~30-60 min + AGENTS.md ~30-60 min + Euler 图 ~30-60 min) = 2-3 小时聚焦作业, 紧跟在刚学过 Python 的一天后。完成率会远低于 syllabus 假设。
- **Suggested fix**: 二选一:
  - (a) Day 2 in-class 砍 25-30 min Python 阅读时段, 改成 PRD/AGENTS.md case-study 讲解 + 25 min student PRD draft; Day 2 课后只补完 PRD; AGENTS.md 推到 Day 3 课后;
  - (b) Day 2 课后只留 PRD, 明确告诉学生"今晚 PRD 写得粗糙没关系, Day 3 morning 会被全班撕开看"; Day 3 morning 新增 15-20 min AGENTS.md case study, AGENTS.md 改成 Day 3 课后交。**推荐 (b)**: 更尊重 cognitive ownership, 让学生交一份 grateful-to-improve 的草稿而不是充满恐慌的精修品。

### C3. **Kong 4 阶段 × 8 stages lifecycle map 在 §二 占位但 Days 1-10 从未运用** (consensus: A3 + B11)

- **Severity**: major
- **Category**: numbered-list-inflation + framework-difficulty
- **A 角度**: lines 71-76 列了 4-phase × 8-stage 表, 之后从未在任何 Day 引用; 占了课程身份段的认知预算。
- **B 角度**: 这是"抱负级地图", 但 S6 Peer Review 等阶段对大一无操作意义 (几年外的事), 占 §二 是浪费 cognitive real estate, 应让位给 5 反射 reps。
- **Suggested fix**: 把 4×8 表完整移到 §十二 教师参考阅读列表。§二 保留一句话: "这门课覆盖了未来研究生涯的 idea→experiment→figure→share 那一段; 后面 4-5 年还会学到 paper writing / peer review / rebuttal——但你今天练的 5 反射弧在那些阶段一字不变, 详见 §十二 推荐阅读 Kong et al. 2026"。这句话保留了"抱负级地图"的鼓励价值, 删掉了 8-stage table 的认知负担。

### C4. **SKILL.md "在另一个 AI 上激活" 的承诺与 §九 国内栈平替声明矛盾** (consensus: A8 + B6)

- **Severity**: major
- **Category**: aspiration-vs-reality + cross-section-contradiction
- **A 角度**: §四 line 124 / Day 8 line 431 / Day 10 line 479 都要求 SKILL.md 能"在 Claude / Cursor 里激活" + "下学期 fork 时另一个 AI 准确激活". 但 §九 (lines 558-563) 主推境内栈 (DeepSeek / Qwen / Trae / Kimi), 这些没有 Claude/Cursor 那种 skill-loader 解析 frontmatter 自动激活的机制 (Trae 有 rule files, Kimi/Qwen 几乎没有)。
- **B 角度**: AGENTS.md 和 Claude Skill 都是 2026 年还在演化的 emerging community formats, 不是 stable 标准。学生毕业带走一份 SKILL.md 半年后可能 illegible to AI 社区。"最值钱的可携带产出" 的 framing 过强。
- **Suggested fix**: §四 line 124 + §八 评分细则 + Day 10 演示要求 全部 reframe: **"Skill 是抽象, 不是文件语法"**。可分享产出 = "一份描述触发场景和工作流的 Markdown 文档, 在你今天用的 AI 工具的 instruction-file 机制 (任意: Claude Skill / Cursor rule / Trae rule / 系统 prompt 复制粘贴) 上能激活"。Day 10 演示从"在 Claude/Cursor 激活"改为"在你自选的 AI 上激活, 没有自动激活机制的口头解释你怎么手动 invoke"。删 "最值钱的可携带产出" 那句, 改为"反射弧 + Skill 抽象习惯 = 真正的可携带产出"。

### C5. **Day 1 "不适合谁" 段命名了学生还没见过的工件, 而且退课 admin 现实未验证** (consensus: A10 + B5)

- **Severity**: major
- **Category**: timing + dropout-mechanism
- **A 角度**: Day 1 line 216 blockquote 提到 "PRD、AGENTS.md、SKILL.md、6-D prompt" 这四个工件作为退课判断标准, 但这四个术语都在 Day 1 第 25 分钟还没引入过——学生听到"你交上来的 SKILL.md 由你自己长出来"却不知 SKILL.md 为何物, 无法做出有意义的自我选择。
- **B 角度**: 中国高校暑期实践课的 admin 现实是退课截止日通常在开课前几天/周; Day 1 morning 看到"教务系统选课退课截止日之前请退"基本不可执行——这段读起来像 instructor 抱怨/威胁但没有 escape valve。
- **Suggested fix**: 二选一:
  - (a) 把 "不适合谁" 段移到 Day 1 末尾 15 min 复盘后 (改成"做完 80 min 实战后, 如果你觉得这种节奏不适合你, 来跟我谈, 我帮你走教务流程"), 把退课从抽象 admin 路径改为人工协商路径;
  - (b) 课前 1 周发一份课程预期单给所有选课学生 ("这门课不发模板, 你要自己长出 5 件工件 ..."), 把退课决定推到 Day 0 之前; Day 1 段保留但缩短到"如果你还在这里说明你接受了, 我们开始", 不再点名退课。
  - **推荐 (b)**: 早期 self-selection 比 Day 1 当场决定更人道, 也避免 admin 路径风险。

---

## Single-reviewer blockers — cross-check 确认

### S1. **Day 8 cognitive overload: 6 个独立认知任务塞进 200 min** (Reviewer B only, B2)

- **Severity**: blocker
- **Category**: cognitive-overload
- **Location**: Day 8 (lines 407-438)
- **Issue**: Day 8 要在 200 min 内交付: (i) 五项验证清单详解 (25 min) + (ii) 老师跑清单演示 (30 min) + (iii) Skill-building 速通 (25 min) + (iv) 学生跑清单 (40 min) + (v) 学生写人生第一份 SKILL.md 草稿 (30 min) + (vi) 全班点评 1 组 (20 min)。第 (v) 块发生在第 (iv) 块之后, 70 min 的无关 checklist 工作已经把学生认知预算烧干, 学生在认知破产状态下写 SKILL.md 草稿——质量必然差到老师 Day 10 评分时为难。
- **Suggested fix**: Day 8 改为"验证清单专题"单一主题, 完成 checklist 即终止; SKILL.md 草稿移到 **Day 9 morning** (Day 9 现在有 25 min 报告写作 + 25 min AI 使用说明 + 50 min 架构互查 + 50 min 写作时间, 易于切出 60 min Skill 块)。Day 9 课后交 SKILL.md 第一版, Day 10 demo 展示终版。

### S2. **单师晚间批改累计 12-15 小时 / 10 天, §一附注数学只算了日志没算 PRD/AGENTS/SKILL/报告之夜** (Reviewer B only, B4)

- **Severity**: blocker
- **Category**: instructor-load
- **Location**: §一附注 (lines 23-26) + §五.2 line 187 + §八 4 档 rubric + 多个 Day 截止夜
- **Issue**: 单师 + 1 助教 in 9-11 组 班额, 实际晚间批改账目（B 给出的 pencil-out）:
  - 每晚 × 10: 日志 ~11-36 min
  - Day 2 night: 11 PRD + 11 AGENTS.md, format-free 必须按原则审, ~110-165 min
  - Day 6 night: 同伴反馈卡分发 + per-group 1-条 ~30-45 min
  - Day 7 night: streamlit 抽 3 组 + DOI 反查 33 篇 ~75-90 min
  - Day 8 night: 11 checklist + 11 SKILL.md ~120 min
  - Day 9 night: 11 报告 + 11 slides + 11 AI 使用说明 ~150 min
  - **总计 ~12-15 小时晚间, 加上每天 9:00-12:30 教学 + 80 min 轮巡**。1 助教 (研究生) 无法分担 format-free 原则审, 只能分担 DOI 检查和 checklist formal items。
- **Suggested fix**: 三选一(可叠加):
  - (a) **班额硬卡到 ≤ 8 组 (≤ 24 人) 即便有助教**——format-free 原则审是真正瓶颈, 不是答辩 slot;
  - (b) §一附注重做工作量数学, 把 PRD-night / Day 8-night / Day 9-night 显式纳入 (这才是 budget 杀手);
  - (c) 软化 "完全 format-free" 立场: 提供一份"30 秒 fill 的 rubric checkbox" (5 个二元问题), 学生选自由格式但必须自查 5 个 checkbox, 助教 first-pass 用 checkbox triage, 老师只看 checkbox 高的或低的极端样本。第 (c) 项是 v3.2 最实用妥协。

---

## Single-reviewer majors — cross-check 全部确认

### Reviewer A 视角

| ID | 一句话 | Location | Fix |
| --- | --- | --- | --- |
| A1 | SKILL.md frontmatter "三件套必有" 实质是 3 字段 schema, 与 §五.2 反模板立场矛盾 | §二 line 61 / §四 line 124 / Day 8 lines 414, 430, 435 | 承认 frontmatter 是技术契约 (Claude Skill loader 必须解析这 3 键) 而非教学模板; §五.2 立场只适用于内容结构, 不适用于工具协议 |
| A2 | §十二 items 3 (验证清单模板) + 7 (课程仓库模板) 仍用"模板"措辞, 与 §五.2 反模板立场不一致 | §十二 lines 659, 663 | 第 3 项改"五项验证清单评分细则 + 老师示范填写"; 第 7 项改"课程仓库骨架 (目录 + .gitignore + README 占位)", 显式说明这是基础设施 template, 不是内容 template |
| A4 | 5 反射 vs 4 阶段 Setup→Code→Test→Deploy 内容近同构, 双倍认知负担 | §二 lines 36-51 | 留 5 反射作课程身份层声明, 4 阶段降为 §六 Day-range header annotation, 不在 §二 设独立表 |
| A5 | 6-D / 10 错误 / Kong 4 原则 / 5 验证清单四套都说"怎么对待 AI 输出"且无 cross-walk | §五.1 + Day 6 + §九 + Day 8 | §二 加 cross-walk 一句话: "6-D 是输入端脚手架 / 10 类错误是输出端检查表 / 5 项清单是结果端物理对账 / Kong 4 原则是元层规范契约"; "10 类错误" 不再 named 为 10-item canon, 用 "Day 1 三类 + 课程其余按需引入" |
| A7 | §九 (c) 列 4 个 phase-handoff checkpoints (Day 3-4/5-7/6/9), 下段又列 3 个 (Day 4/7/10), 内部矛盾 | §九 lines 595 vs 598 | 统一为"3 次硬性 30-秒 handoff check (Day 4/7/10) + 2 次软性 cross-team peer-check (Day 6 中期, Day 9 架构互查)", 删掉合并写法 |
| A11 | §五.2 自诩 "5 类不是 5 栏", 但 §二 line 57 的 "5 类问题" 与 5 栏操作上等价 | §二 line 57 + §五.2 line 178 | 二选一: (i) 把 5 类减到 3 类 (Spec / Verification / Stack), 让 5-栏 hash 不成立; (ii) 拥抱矛盾, 删掉 §五.2 line 178 "5 类不是 5 栏" 那句 |
| A12 | Day 5 4 战术补充 (be-specific / examples / think-hard / new-chat) 全是 6-D 子情形 | Day 5 line 342 | 把战术 1/2/3 折进 §五.1 的 D4/D5/D2 解释里; 只保留战术 4 (开新 chat) 作为 standalone failure-mode advisory |

### Reviewer B 视角

| ID | 一句话 | Location | Fix |
| --- | --- | --- | --- |
| B3 | Day 5 反向标注 D1-D6 自己刚写的 prose 是研究生级 meta-cognition, 对 week-2 大一过难 | Day 5 lines 335, 337 | 把"反向标注"换成"在 prompt 文件末尾附 6 个 checkbox 自查清单"; reverse-tagging 推到 Day 6 或 Day 8 当 audit 习惯, 用别人的 prose 练 |
| B7 | Days 5-8 累计 no-AI 负担 (Day 5 Excel 手算最小二乘 + Day 7 自找 1 篇文献 + Day 8 五项清单大部分 no-AI) 与 "AI 辅助" 课程名矛盾 | Day 5 line 328 + Day 7 line 393 + Day 8 lines 417-423 | 选 ONE 作为 canonical no-AI baseline (推荐 Day 5 最小二乘, 因为衔接刚学完的线代); 删 Day 7 "1 篇不靠 AI", 改为 "至少读完 1 篇"; Day 8 五项清单 reframe 为 "AI 做数学, 你决定问什么数学" |
| B10 | Streamlit Cloud 部署需 Git+OAuth+CI, §三 不假设 Git 背景; Day 7 课后从 streamlit_app.py 到 public URL 中间整个栈未教 | Day 7 + §七 + §十一 | Streamlit Cloud 降为"可选 stretch goal"; 默认交付改 **本地一键启动 zip** (含 `run.sh` 或 `run.bat`); §十一 加 Risk 9 "Streamlit Cloud 部署失败, 本地 zip 兜底"; 如保留 Cloud 选项, Day 7 需补 30 min Git + 部署 mini-session |
| B12 | §十二 第 9 项录屏 25 hr 估计不足, 实际 4-5 hr/段 × 10 段 = 40-50 hr | §十二 line 666 | item 9 重估为 40-50 hr; 备课总预算从 100-140 hr 上调到 115-160 hr; 加"背景阅读前置": Kong / Karpathy / Anthropic 6-D / awesome-vibe-coding 至少花 20-30 hr 读完才能开始备课 |

---

## Single-reviewer minors

| ID | 一句话 | Fix |
| --- | --- | --- |
| A9 | 13 个 named numbered groupings, 即便 C1/C3 收束后仍 borderline | §二 加 "本课程的可携带框架收束" 子段, 明确学生只需记住 3 个 (推荐: 5 反射 + 5 项验证 + 4 栏 AI 使用说明); 其余声明为 instructor-facing |
| A10 | Day 1 不适合谁 段时机过早 (line 25 时点) | C5 已含 fix; 或把段移到 Day 1 末尾 15-min 复盘后 |

---

## Disputed / withdrawn items (audit footnote)

无 disputed。两份报告所有 evidence 在 SYLLABUS 中 verbatim 命中, 无幻觉; A 与 B 也无相互矛盾 (互补无重叠冲突)。**A1 严重度从 blocker 经 cross-check 降到 major**: frontmatter 三件套是 Claude Skill loader 的技术契约 (loader 必须解析 name/description/triggers 这三个 YAML key), 不是教学模板; §五.2 反模板立场只适用于内容结构, 应明确豁免工具协议层。**C2 严重度从 blocker 降到 major**: 通过重新分布 Day 2/Day 3 deliverable 即可解决, 不需要整体重构。

---

## 我建议接下来怎么动 (你拍板)

按修复影响 × 工时排序:

1. **【blocker 必修, ~5 小时】** B4 instructor load 数学 + B2 Day 8 cognitive overload + C2 Day 2 课后重排 + C4 SKILL.md 国内栈 reframe. 这 4 条不修就不能开课。
2. **【consensus major, ~3 小时】** C1 框架收束 (定 5 反射为 the central, Kong map 移 §十二, 4 阶段降为 Day-range header) + C3 Kong 4×8 移到 §十二 + C5 不适合谁段重写
3. **【single major 选择性修, ~3 小时】** A1 + A2 反模板措辞清理; A4 5反射 vs 4阶段 isomorphic 处理; A5 cross-walk 一句话; A7 phase-handoff 列表内部矛盾修复; B3 reverse-tagging 改 checkbox; B7 no-AI 负担收束到 1 项; B10 Streamlit local-zip 改默认
4. **【minor 可不修, ~1 小时】** A9 加收束段 / A11 5 类 vs 5 栏 / A12 4 战术 fold-in / B12 录屏工时上调

要我现在动手做哪一档?
- **(a)** 全部 18 issue 一次性修完 (v3.2), ~12 小时, 出完整 SYLLABUS v3.2 文件
- **(b)** 只修 2 blocker + 4 consensus major (S1 S2 + C1-C5), ~8 小时, 留 single-source major 给你下次决定
- **(c)** 只修 2 blocker (B2 + B4), ~5 小时, 把课程能开起来的最低门槛先达到
- **(d)** 输出按 issue ID 排序的 patch 文件 (不修原文件), 你自己逐条 accept/reject
- **(e)** 停手, 你自己读完 panel 再说
