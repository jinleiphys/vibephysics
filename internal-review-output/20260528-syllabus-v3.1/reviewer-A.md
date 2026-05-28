# Reviewer A — Course Identity Coherence Audit

Artifact: `/Users/jinlei/Desktop/code/vibephysics/SYLLABUS.md` v3.1 (692 lines).
Stance: hunt for cross-section contradictions, concept-stack overload, numbered-list inflation, template-stance leakage, hidden dependencies, redundant new injections, timing math, and aspiration vs. reality calibration.

---

## ID: A1
**SEVERITY:** blocker
**CATEGORY:** template-stance-inconsistency
**LOCATION:** §二 line 61 + §四 line 124 + Day 8 lines 414, 430, 435 vs §五.2 lines 170–183
**CLAIM:** §五.2 declares "不发任何 fill-in-the-blank 模板", yet the SKILL.md description in §二/§四/Day 8 hard-mandates a YAML frontmatter with the exact three-field set `name / description / triggers`. Mandating a fixed YAML frontmatter schema IS a template, just renamed "三件套必有". For a 大一 student who has never seen YAML, "frontmatter 三件套必有" is operationally indistinguishable from "fill in these three fields".
**EVIDENCE:**
- Line 61: `必须含: YAML frontmatter (定义 name / description / 触发条件) + 正文 (定义触发时 AI 应执行的工作流).`
- Line 172: `不发 PRD 模板, 不发 AGENTS.md 模板, 不发 SKILL.md 模板, 不发 6-D prompt 模板。这不是疏忽, 是设计。`
- Line 414: `**写出第一个 \`SKILL.md\`**——一页 Markdown，YAML frontmatter（name / description / triggers）+ 正文（AI 在该场景下应做什么）`
- Line 430: `选其中一个**自己长出一份 SKILL.md 草稿** (frontmatter 必有 name / description / triggers 三件套, 其余内容由你决定)`
**SUGGESTED_FIX:** Either (a) acknowledge the YAML frontmatter is a hard schema requirement (because Claude Skill loader parses those three keys — that is the technology contract, not pedagogy) and drop the SKILL.md item from the §五.2 "no-template" list, or (b) keep SKILL.md in the no-template list but rewrite as "学生自己决定 SKILL.md 该怎样让另一个 AI 自动激活" without pre-naming the three fields. Pick one. Same applies to AGENTS.md line 58's "至少回答: 单位制 / 允许的库 / 数值方法限制 / 物理结果的标注要求 / 引用规范" — that is a 5-row schema in everything but the word "模板".

---

## ID: A2
**SEVERITY:** major
**CATEGORY:** template-stance-inconsistency
**LOCATION:** §十二 line 659 + line 663 vs §五.2 line 172 and line 185
**CLAIM:** §五.2 line 185 promises §十二 has been revised to call the instructor-internal materials "范例库 + 评分细则, 不是发给学生填的表格". The revision did happen for items 10, 12, 13, 16. But items 3 and 7 still use the bare word "模板" without the renaming pass, and item 7 explicitly states it IS given to students. This contradicts the post-revision claim that §十二 has been cleaned up.
**EVIDENCE:**
- Line 185: `**老师的 §十二 备课资产里那些被称为"模板"的东西, 实际上是老师自己的范例库和评分细则 ... §十二 已经按这个方向修订。**`
- Line 659: `- [ ] **3. 五项验证清单模板 \`checklist.md\`**（≈ 2 小时）`
- Line 663: `- [ ] **7. 课程仓库模板**（≈ 5 小时, 每组从这个模板 fork 一份做自己的项目仓库, 含目录结构 + README 占位 + .gitignore + LICENSE）`
**SUGGESTED_FIX:** Rename item 3 to "五项验证清单评分细则 + 一份老师示范填写" and rename item 7 to "课程仓库骨架 (目录 + .gitignore + README 占位, 不预填内容)". The repo skeleton is unavoidably template-shaped — call out that this single exception is structural, not pedagogical, so the inconsistency is visible rather than hidden.

---

## ID: A3
**SEVERITY:** major
**CATEGORY:** concept-stack-overload
**LOCATION:** §二 lines 36–84 (whole section)
**CLAIM:** §二 now declares the course identity through eight independently-named numbered frameworks that students must internalize: 5 reflex actions, 5 工件, 4-phase Setup→Code→Test→Deploy, 4-phase × 8-stage Kong et al. research lifecycle map, Karpathy philosophy, cognitive ownership principle. The closing sentence on line 84 itself enumerates "5 个动作、5 个工件、4 个阶段、cognitive ownership 原则" — the syllabus is admitting that its own identity section is four parallel taxonomies stacked. For 大一 in a 2-week intensive this is too many independent name-counted frameworks to track; the Kong et al. 4×8 map in particular is presented in 抱负级 (lines 67–78) and then never operationally used in any of Day 1–10.
**EVIDENCE:**
- Line 84: `这五个动作、五个工件、四个阶段、cognitive ownership 原则, 物理学院后面四年的专业课基本不会专门教。`
- Lines 71–76: the 4-phase × 8-stage table (Phase 1 Creation S1–S4, Phase 2 Writing S5, Phase 3 Validation S6–S7, Phase 4 Dissemination S8) — never referenced again outside §二.
**SUGGESTED_FIX:** Demote the Kong et al. 4×8 map to a one-line footnote ("这门课覆盖学术生命周期的 S2/S3/S4/S8; 详见 Kong et al."). The 8-stage taxonomy is not operationalized anywhere in Day 1–10 and only inflates the "must remember" stack. Keep 5 reflex actions + 5 工件 + 4 phases as the spine.

---

## ID: A4
**SEVERITY:** major
**CATEGORY:** numbered-list-inflation
**LOCATION:** §二 line 36 (5 reflex actions) vs §二 line 44 (4-phase Setup→Code→Test→Deploy)
**CLAIM:** The 4-phase Setup→Code→Test→Deploy table (lines 44–51) and the 5 reflex actions (lines 36–42) are not independent dimensions; they are mostly the same content sliced two different ways. Setup phase IS reflex actions 1+2 (PRD + architecture); Code phase IS reflex action 5 (and partly 3); Test phase IS reflex action 3 (Trust but Verify); Deploy phase IS reflex action 4 (Ship). The 5th reflex action (Skill-building) does not map cleanly onto any phase. Students will be forced to memorize two near-isomorphic 4-vs-5 lists, which doubles cognitive load without adding information.
**EVIDENCE:**
- Line 41: `4. **Ship something real**：交付件不是 PDF 报告，是一个**别人能点开 URL 就能玩、或者一键启动的物理交互工件**`
- Line 51: `| **Deploy（Ship）** | Day 9 - Day 10 | 可访问 URL + 报告 + Demo Day 答辩 |`
**SUGGESTED_FIX:** Pick one as the spine and present the other as an annotation. Recommend: keep the 5 reflex actions as the identity-level statement, present Setup→Code→Test→Deploy only as a Day-range header annotation in §六. Drop the §二 phase table entirely; or conversely keep the phase table and reframe reflex actions as the verbs each phase requires.

---

## ID: A5
**SEVERITY:** major
**CATEGORY:** new-injection-redundancy
**LOCATION:** §五.1 (6-D framework, lines 147–166) + Day 5 lines 333–348 vs Day 6 line 366 (10 大 AI 错误模式) vs §九 lines 591–596 (Kong 4 principles)
**CLAIM:** Three independently-introduced frameworks all claim to be the lens through which students should evaluate AI output. They partially overlap and have no cross-mapping. Concrete: D2 "Tone and Confidence + 不确定时显式说不确定" overlaps with 10 大错误模式 categories "虚假引用 / 混淆模型 / 过拟合掩盖". D3 "Background Details (AGENTS.md 引用)" overlaps with Kong principle (d) "Make AI involvement transparent". D6 "Final Reminder" overlaps with the 五项验证清单 "量纲检查 + 守恒律". None of the three is cross-referenced to the other two. Students will encounter three differently-numbered taxonomies (6 / 10 / 4 / 5) for nearly the same concern (catch AI mistakes), each in a different section.
**EVIDENCE:**
- Line 154: `D2 ... | 设定输出风格（事实性 / 高信心 / 不确定时显式标注）`
- Line 366: `30 min 10 大 AI 错误模式短训：Day 1 三类（单位/符号/数量级）+ 新增 7 类（求解器误用、收敛假象、虚假引用、混淆模型、过拟合掩盖、误用近似、丢边界条件 / 能量不守恒）`
- Line 594: `**(b) Use execution and retrieval grounding wherever possible** — 优先用执行结果 + 检索证据来取代纯文本自判断`
**SUGGESTED_FIX:** Add an explicit cross-walk table somewhere in §二 or §五: "6-D 是 prompt 写法的脚手架 (输入端); 10 大错误模式是审计 AI 输出的检查表 (输出端); 5 项验证清单是物理对账 (结果端); Kong 4 原则是规范契约 (元层)。" Then cut at least one — the 10 大错误模式is arguably already covered by the 5 reflex actions × 5 项验证清单; consider folding it back to "Day 1 三类 + 课程其余 7 类按需引入" without naming it as a 10-item canon.

---

## ID: A6
**SEVERITY:** major
**CATEGORY:** hidden-dependency
**LOCATION:** Day 2 课后任务 lines 258–259 vs Day 2 课堂内容 lines 246–253
**CLAIM:** Day 2 in-class content teaches Python reading + Euler手算 (60+60 min on RC discharge script). Day 2 课后 then requires students to deliver a PRD + AGENTS.md by morning Day 3. But Day 2 in-class never teaches PRD writing or AGENTS.md writing — it teaches Python. The only PRD exposure students received was the 5-min "PRD 预告" on Day 1 (line 221) which explicitly said "今天你只需要知道它存在". So between 09:00 Day 1 (existence-level) and 12:30 Day 2 (assignment due that evening), students received zero structured instruction on PRD/AGENTS.md and are nonetheless expected to deliver both that night.
**EVIDENCE:**
- Line 221: `5 min **PRD 预告**："...今天你只需要知道它存在。"`
- Line 258: `**为主选题自己写一页 \`PRD.md\`**. 课堂上你听过原则 (5 类必答问题: ...) + 看过老师投影上的 good/bad/ugly 范例 case study.`
- Day 2 in-class block (lines 246–253) contains: 物理回顾, 读脚本学 Python, 中场, 手算 Euler 实战, Euler 截断误差复盘. No PRD instruction block.
**SUGGESTED_FIX:** Either (a) move the PRD/AGENTS.md case-study lecture (with the good/bad/ugly 范例 投影) into Day 2 morning (would require cutting 25–30 min from the Python reading block), or (b) push the PRD/AGENTS.md deliverable from Day 2-evening to Day 3-evening and use a Day 3 morning sub-block (currently 二阶 ODE 化简 owns Day 3 morning) for the case-study lecture. The current line 258 phrasing "课堂上你听过原则 + 看过 case study" is counterfactual.

---

## ID: A7
**SEVERITY:** major
**CATEGORY:** cross-section-contradiction
**LOCATION:** §九 (c) line 595 vs §九 phase-boundary warning line 598
**CLAIM:** Two adjacent paragraphs in §九 give two different lists of phase-handoff checkpoints. The (c) row of the Kong-principle table lists four checkpoints (Day 3→4, Day 5→7, Day 6 中期答辩, Day 9 架构互查). The very next paragraph lists three (Day 4, Day 7, Day 10). Day 6 and Day 9 appear in the first list but not the second; Day 10 appears in the second but not the first. Day 4 explicitly has a phase-handoff block (line 312) and Day 7 has one (line 399) and Day 10 has one (line 479) — so the second list (three) matches the actual Day-by-Day insertions, and the first list (four) is the one that doesn't match what was inserted into the days.
**EVIDENCE:**
- Line 595: `| **(c) Include human checkpoints at phase boundaries** ... | Day 3→Day 4 架构到代码的忠实度检查 + Day 5→Day 7 数据流到工件的忠实度检查 + Day 6 中期答辩 + Day 9 架构互查 |`
- Line 598: `**Day 4 / Day 7 / Day 10 各设一次显式 phase-handoff verification**：30 秒回到上一阶段交付件, 确认这一阶段的工件没有偷偷修改前一阶段的事实。`
**SUGGESTED_FIX:** Reconcile to a single canonical list. The actual injected verification blocks live on Days 4, 7, 10 (lines 312, 399, 479). Update line 595 to read "Day 4 + Day 7 + Day 10 三次 phase-handoff verification + Day 6 中期答辩 + Day 9 架构互查" and explicitly distinguish "3 次硬性 30-秒 handoff check (Day 4/7/10)" from "2 次软性 cross-team peer-check (Day 6, Day 9)" so the categories don't blur.

---

## ID: A8
**SEVERITY:** major
**CATEGORY:** aspiration-vs-reality
**LOCATION:** §二 line 42 + §四 line 124 + Day 8 lines 414, 429, 431 + Day 10 line 479
**CLAIM:** The course promises that every 大一 student walks away with a `SKILL.md` "another AI can activate in your next physics course" (line 124 + line 431 "在另一个 AI 上能否激活"). This requires: (i) the student's home machine has Claude Code or Cursor installed and configured to read `~/.claude/skills/`; (ii) the student knows how the skill-loader resolves YAML frontmatter; (iii) the student returns next semester and remembers to activate it. None of (i)/(ii) is taught — the only in-class instruction on Skill mechanics is 25 min on Day 8 (line 429) which is "讲原则 + case study, 不发模板". The Day 10 demo requirement "演示自己造的 Skill 至少一次 (在 Claude 或 Cursor 里激活, 让它对一段陌生输入跑一遍, 大约 90 秒)" (line 479) presupposes that every student has a working Claude or Cursor with skills enabled on the demo-day machine, which §九 工具栏 (lines 558–563) does not guarantee — DeepSeek / Trae / Qwen are accepted, none of which has a directly comparable skill-activation mechanism.
**EVIDENCE:**
- Line 124: `课程结束时每个学生至少带走一个能在自己电脑 Claude / Cursor 上激活的物理 Skill, 下学期解新问题时能复用。`
- Line 431: `**点评不按格式打分, 按"这个 Skill 在下学期 fork 出来时, 能不能让另一个 AI 准确激活并执行"打分.**`
- Line 559: `**境内工具（国内学生首选, 避免网络问题）**: 通义千问 (Tongyi) / DeepSeek / 智谱 GLM / Kimi / 字节跳动 Trae（国内对标 Cursor 的 IDE）/ 文心一言 / 月之暗面`
**SUGGESTED_FIX:** Either (a) restrict Skill demo on Day 10 to Claude / Cursor only and add "Day 8 课后必须装好 Claude Code 或 Cursor + 验证 skills 目录被读到" as a hard prerequisite in Day 8 课后任务, or (b) reframe the Skill deliverable as a portable Markdown specification with documented triggers, runnable by any AI that supports a system-prompt + instruction file (DeepSeek + Trae have rule files; Kimi/Qwen do not), and downgrade Day 10's "在 Claude 或 Cursor 里激活" to "在你选的工具里激活, 没有激活机制的口头解释 Skill 在你工具上怎么手动 invoke". The current ask asymmetrically privileges students using foreign tools while §九 actively encourages 国内工具.

---

## ID: A9
**SEVERITY:** minor
**CATEGORY:** numbered-list-inflation
**LOCATION:** Whole document
**CLAIM:** Counting the named numbered frameworks the student is expected to recall: 3 条红线 (line 573), 5 条反射动作 (line 36), 5 件工件 (line 53), 4 阶段 Setup→Code→Test→Deploy (line 44), 4 phases × 8 stages Kong map (line 69), 6 维 prompt (line 147), 4 条 Kong design principles (line 589), 3 类 then 10 类 AI 错误模式 (Day 1 + Day 6), 5 项验证清单 (line 417), 4 栏 AI 使用说明 (line 567), 3 件 frontmatter (line 124), 3 phase-handoff checkpoints (line 598), 4 档 AI 审计日志 rubric (line 538). Thirteen named numbered groupings. Even with the merges suggested in A3/A4/A5, this is on the edge of what a 2-week course can land.
**EVIDENCE:**
- Line 84: `这五个动作、五个工件、四个阶段、cognitive ownership 原则, 物理学院后面四年的专业课基本不会专门教。`
- Line 173 (sentence right after the no-template declaration immediately introduces another numbered list): `理由（Kong et al. 2026 §7.4.7 cognitive ownership 原则的直接应用）: 如果学生拿到一份 5 栏 PRD 模板照着填...`
**SUGGESTED_FIX:** Add a §二.尾 "本课程的可携带框架收束" subsection that explicitly lists the 3 you want students to memorize (recommend: 5 reflex actions + 5 项验证清单 + 4 栏 AI 使用说明) and demotes the rest to instructor-facing or as-needed references. Without an explicit收束 list, all 13 are equally weighted in the student's mind, and none will actually be remembered.

---

## ID: A10
**SEVERITY:** minor
**CATEGORY:** timing
**LOCATION:** Day 1 lines 213–225 (sub-block timing)
**CLAIM:** Day 1 timing math actually checks (20+5+5+30+80+15 = 155 min teaching + 20 min buffer = 175 min, within 210 clock-min). However, the ordering is questionable: the 5-min 不适合谁 expectation-management block (line 215) is placed BEFORE the 5-min PRD 预告 (line 221) and BEFORE students have actually done any AI work or seen what a SKILL.md looks like. The blockquote on line 216 refers to PRD/AGENTS.md/SKILL.md/6-D prompt by name as artifacts the student must "长出来 by yourself" — but none of those four artifacts has been introduced yet at minute 25 of Day 1. A 大一 hearing "你交上来的 SKILL.md 全部由你自己长出来" before knowing what a SKILL.md is can't actually self-select on it.
**EVIDENCE:**
- Line 214: `20 min 课程总览 (vibe coding director 身份介绍 + ... 三条红线、必交日志、报告 AI 段落要求)`
- Line 216: `"这门课不发模板。你交上来的 PRD、AGENTS.md、SKILL.md、6-D prompt 全部由你自己长出来 ..."`
- Line 221: `5 min **PRD 预告**："明天晚上你们要为自己组的项目自己长出一页 PRD ..."`
**SUGGESTED_FIX:** Move the 不适合谁 block to the very end of Day 1 (e.g., as the final 5 min of the 15-min 复盘 on line 224), AFTER students have actually run the 80-min single-pendulum AI exercise and felt what "find 2 suspicious things in AI output" feels like. Concrete experience first, expectation management second. Or, keep at Day 1 morning but cut the artifact-name list ("PRD、AGENTS.md、SKILL.md、6-D prompt") since students haven't met those terms — phrase as "你交上来的所有交付件全部由你自己长出来".

---

## ID: A11
**SEVERITY:** minor
**CATEGORY:** cross-section-contradiction
**LOCATION:** §五.2 line 173 vs §二 line 57 + §四 line 117
**CLAIM:** §五.2 makes a point of distinguishing "5 类必答问题" from "5 栏 PRD 模板": "这 5 个不是固定 5 栏, 而是 5 类必须自己回答的问题" (line 178). But §二 line 57 introduces the PRD as "必须回答 5 类问题: 做什么 / 输入是什么 / 输出是什么 / 怎么算成功 / 选什么技术栈以及为什么" — that is the same 5-tuple, comma-delimited, as the "5 栏" it warns against. The slash-delimited list is operationally a row schema; a 大一 will hash to "PRD = 5 boxes" whether you call them 栏 or 类. Same for AGENTS.md (line 58: "至少回答: 单位制 / 允许的库 / 数值方法限制 / 物理结果的标注要求 / 引用规范" — five slots).
**EVIDENCE:**
- Line 57: `必须回答 5 类问题: 做什么 / 输入是什么 / 输出是什么 / 怎么算成功 / 选什么技术栈以及为什么.`
- Line 174: `如果学生拿到一份 5 栏 PRD 模板照着填, 他们学到的不是"如何思考问题边界", 而是"如何把模糊想法塞进 5 个格子"。`
**SUGGESTED_FIX:** Either (i) reduce the 5-question canonical list to 3 (e.g. "Spec / Verification / Stack") so students cannot trivially re-format it as 5 boxes, or (ii) acknowledge that 5 questions naturally collapse to 5 sections and own the contradiction — drop the "5 类不是 5 栏" sentence on line 178 since the only thing distinguishing them is the absence of literal table borders. Right now the rhetorical distinction is not actually load-bearing.

---

## ID: A12
**SEVERITY:** minor
**CATEGORY:** new-injection-redundancy
**LOCATION:** Day 5 line 342 (4 战术补充) vs §五.1 (6-D framework)
**CLAIM:** Day 5 introduces the Anthropic 6-D framework (D1–D6) as the spine for 25 min, then 35 min v1-vs-v2 demo, then in the closing 20-min 复盘 (line 342) adds 4 战术补充 ("Be specific / Provide examples / Think harder / Open new chat"). These four are sub-cases of D4 (specificity), D5 (examples), and D3 (context), labeled as "战术补丁". Adding 4 战术补充 to a 6 维 framework on the same day, in the same session, before students have used the 6 维 even once in a real prompt, is yet another numbered-list addition where the natural cognitive move is "subsume战术 1–3 under D4/D5/D3 and only keep '开新 chat' as a separate failure-mode advisory".
**EVIDENCE:**
- Line 342: `20 min **复盘 + 4 条战术补充**（采自 analyticalrohit/awesome-vibe-coding-guide, 作为 6-D 框架的战术补丁）`
- Line 343: `1. **Be specific over vague**（D4 的具体战术）`
- Line 344: `2. **Provide examples + edge cases**（D5 的具体战术）`
- Line 345: `3. **"Think hard / Think deep / Think longer"**（D2/D4 之间的战术）`
**SUGGESTED_FIX:** Fold战术 1, 2, 3 directly into the D4/D5/D2 explanation in the morning 25-min framework lecture (line 333). Keep only战术 4 (开新 chat) as the standalone "failure-mode advisory" in the 20-min 复盘, retitled as "When 6-D doesn't save you: open a new chat". This drops a 4-item sub-list while strengthening the 6-D 维度 explanations with concrete tactical handles.

---
