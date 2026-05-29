#!/usr/bin/env python3
"""Batch-generate 16 session decks for Vibe Physics course.

Each session deck has 6 slides:
  1. Cover (IKB hero)
  2. 学习目标 + 课节坐标 (KPI grid)
  3. 核心知识 / 方法论 (sub-cards)
  4. 课堂实验 (90 min timeline)
  5. 验证清单 + 常见坑
  6. 作业 + 下节预告 (split closing)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "session-01.html"  # fresh template-swiss.html copy
OUT_DIR = ROOT

# ---------- 16 节课内容数据 ----------
SESSIONS = [
    # ============ 阶段一 · 问题定义与使用规范 ============
    {
        "n": 1, "stage": "01", "stage_zh": "问题定义",
        "title_zh": "课程方法<br/>与基本规范",
        "title_en": "Course Methodology",
        "tagline": "为什么开这门课;Vibe Physics 是什么;课堂结构、交付物、评分标准、学术诚信底线。",
        "kpi": [
            ("能用一句话讲清", "Vibe Physics 是什么、不是什么", "STMT"),
            ("理解课堂 4 段式", "15-20-45-10 分钟节奏", "RHYTHM"),
            ("看懂评分鲁布里克", "50/20/15/10/5 的依据", "RUBRIC"),
            ("写下 AI 使用边界", "工具 / 用途 / 责任", "ETHICS"),
        ],
        "concepts": [
            ("Vibe Physics 不是什么", "不是软件教学,不是 AI 取代物理课。"),
            ("Vibe Physics 是什么", "在 AI 工具参与下完成问题定义、模型实现、结果审查、可复现表达的训练。"),
            ("课堂 4 段式", "15 概念 → 20 示范 → 45 实验 → 10 复盘。每节课都按这个走。"),
            ("交付即评分", "代码仓库 + 报告 + 交互日志 + 验证清单 + 工具使用说明。"),
        ],
        "lab": [
            ("15min", "概念", "课程目标 + 4 原则 + 评分鲁布里克"),
            ("20min", "示范", "教师现场打开一个示例任务,演示模板填写"),
            ("45min", "实验", "学生用任务模板写下你想做的项目方向(草稿)"),
            ("10min", "复盘", "同桌互看任务草稿,圈出最弱的一条"),
        ],
        "checks": [
            ("任务有清晰物理动机吗", "如果讲不出为什么要做,先停一步"),
            ("假设、方程、边界写下来了吗", "至少一行,不要「等想清楚再写」"),
            ("验证标准提到了吗", "解析极限 / 基准 / 误差 / 收敛 / 守恒,至少一条"),
            ("AI 使用边界写了吗", "我会让 AI 做 X,我自己核 Y"),
        ],
        "hw": [
            "用任务模板填写两个候选项目方向,400 字 / 个",
            "在 Git 上建立个人仓库 vibephysics-<姓名>,推一个 README",
            "读完《课程白皮书》(链接发到群里),记 3 条问题",
        ],
        "next_zh": "下节课 · 物理任务描述模板",
        "next_desc": "把任务模板逐字段过一遍,练习「把模糊想法写清楚」。",
    },
    {
        "n": 2, "stage": "01", "stage_zh": "问题定义",
        "title_zh": "物理任务<br/>描述模板",
        "title_en": "Task Description Template",
        "tagline": "用统一模板把物理任务写下:背景、假设、方程、输入输出、验证标准。这是后续 14 节课能站得住的地基。",
        "kpi": [
            ("能填完 6 字段模板", "背景/假设/方程/IO/验证/责任", "TASK"),
            ("能写出 3 个具体边界", "上下界、定义域、单位", "BNDR"),
            ("能列出 ≥ 1 个验证标准", "解析极限 或 基准", "VALD"),
            ("能拒绝模糊任务", "讲不清就退回去", "REJECT"),
        ],
        "concepts": [
            ("背景与动机", "为什么这个问题值得做。1 段。"),
            ("假设与方程", "你做了什么近似、写出主方程、说明边界条件。"),
            ("输入与输出", "输入参数列表、量纲、范围;输出量纲、目标精度。"),
            ("验证标准", "至少一项可比对的解析极限 / 基准算例 / 实验数据。"),
        ],
        "lab": [
            ("15min", "讲解", "6 字段模板逐项展开 + 范例"),
            ("20min", "示范", "教师把「散射截面随能量变化」这个题填进模板"),
            ("45min", "实验", "学生 2 人一组,把上周草稿填成完整模板"),
            ("10min", "复盘", "同组互改,圈出「假设」和「验证」两栏的疏漏"),
        ],
        "checks": [
            ("背景写清楚了吗", "1 段说明该问题在物理里的位置"),
            ("假设可被推翻吗", "如果假设「无穷远」,写明何时失效"),
            ("方程符号都有定义吗", "每个变量都列出量纲和典型范围"),
            ("验证标准能 30 行代码验证吗", "如果不能,标准还不够具体"),
        ],
        "hw": [
            "把候选项目模板写完,提交 PR 到课程公共仓库",
            "回看上节课「假引用识别」预备材料(链接群里)",
            "在自己仓库下建 task.md,这就是项目的合同书",
        ],
        "next_zh": "下节课 · 文献阅读与假引用识别",
        "next_desc": "教 AI 找的文献怎么核 DOI,怎么识别 LLM 编造的引用。",
    },
    {
        "n": 3, "stage": "01", "stage_zh": "问题定义",
        "title_zh": "文献阅读与<br/>假引用识别",
        "title_en": "Literature & Fake Citations",
        "tagline": "AI 编造引用是真实风险。教学生怎么核 DOI、怎么读摘要、怎么记笔记。第 3 课确定本学期项目方向。",
        "kpi": [
            ("能用 AI 找 3 篇相关文献", "并核验每篇的真实 DOI", "FIND"),
            ("能识别 LLM 编造的引用", "至少 2 类典型作弊模式", "FAKE"),
            ("能写 1 页文献综述", "结构化 200 字 / 篇", "SUM"),
            ("能确定项目方向", "本学期跟到底的那一个", "PICK"),
        ],
        "concepts": [
            ("AI 找文献的三种坑", "编 DOI / 张冠李戴 / 拼接作者。每个都见过。"),
            ("DOI 核验流程", "doi.org/<doi> 是不是真打得开;crossref 上能否查到。"),
            ("摘要 → 结构化笔记", "目标 / 方法 / 结论 / 与我项目的关系,各一句。"),
            ("项目方向选择标准", "可做 + 可验证 + 你愿意做 8 周。"),
        ],
        "lab": [
            ("15min", "讲解", "LLM 假引用真实案例 3 则"),
            ("20min", "示范", "教师让 AI 找文献,逐条核 DOI"),
            ("45min", "实验", "小组找本项目相关的 3-5 篇文献,做核验表"),
            ("10min", "复盘", "选出本学期项目方向,在共享文档上登记"),
        ],
        "checks": [
            ("每条引用都有真 DOI 吗", "doi.org 能打开的才算"),
            ("摘要是自己看过吗", "不是,标记「未核验」,不算有效文献"),
            ("项目方向有可比对的数据 / 极限吗", "没有就再换"),
            ("能在 8 周里做完吗", "时间不够就缩小范围"),
        ],
        "hw": [
            "本项目文献综述 1 页 + 文献清单 BibTeX",
            "在 task.md 里更新项目方向(确认版)",
            "组队完成,2-3 人一组,提交组员名单",
        ],
        "next_zh": "下节课 · 从想法到原型",
        "next_desc": "把任务和文献揉成第一个能跑的代码原型。",
    },
    {
        "n": 4, "stage": "01", "stage_zh": "问题定义",
        "title_zh": "从想法<br/>到原型",
        "title_en": "From Idea to Prototype",
        "tagline": "把任务和文献揉成第一个能跑的代码原型。本课结束时,每个项目都应该有一个 100 行内的最小版本。",
        "kpi": [
            ("跑通最小原型", "main.py + 一张图 + 一个数", "MVP"),
            ("理解模块化结构", "data / model / viz 三件套", "MOD"),
            ("写一个单元测试", "至少 1 个可断言函数", "TEST"),
            ("交第一版报告框架", "6 段结构 + 占位图", "DRAFT"),
        ],
        "concepts": [
            ("最小可行原型 MVP", "100 行内,跑通端到端,不求精度求闭环。"),
            ("模块化目录结构", "src/ + notebooks/ + tests/ + figures/ + data/。"),
            ("单元测试的最低要求", "至少一个 assert 验证已知极限或基准值。"),
            ("报告框架先于结果", "用 LaTeX 占位先把骨架搭起,边做边填。"),
        ],
        "lab": [
            ("15min", "讲解", "MVP 三原则 + 目录模板"),
            ("20min", "示范", "教师从 task.md 出发,15 分钟搭一个 MVP"),
            ("45min", "实验", "小组合作,搭出本项目第一个能 run 的 main.py"),
            ("10min", "复盘", "组间快速演示,圈最不像 MVP 的地方"),
        ],
        "checks": [
            ("一条命令能跑吗", "python main.py 或 jupyter 跑通"),
            ("结果有一个数能比较吗", "没有数就不算原型"),
            ("代码超过 200 行了吗", "超了就拆 — 第一版只要核心"),
            ("有 README 说明怎么跑吗", "没有,别人就复现不了"),
        ],
        "hw": [
            "把 MVP 推到自己仓库,带 README",
            "写一个单元测试,验证至少一个极限",
            "在报告框架里填好「动机」和「方法」两段",
        ],
        "next_zh": "下节课 · 量纲、极限、守恒律",
        "next_desc": "进入阶段二。学三种最廉价的物理审查方法。",
    },
    # ============ 阶段二 · 数值计算与可信验证 ============
    {
        "n": 5, "stage": "02", "stage_zh": "数值计算",
        "title_zh": "量纲、极限<br/>与守恒律",
        "title_en": "Dimensions · Limits · Conservation",
        "tagline": "三类最廉价的物理审查。能挡掉 80% 的「代码能跑但物理是错的」问题。每个项目结果都要过这一关。",
        "kpi": [
            ("能查清所有量纲", "包括 const 和拟合参数", "DIM"),
            ("能取 2 个极限", "如 ℏ→0, m→∞, T→0", "LIMIT"),
            ("能验证 1 条守恒律", "能量 / 动量 / 概率 / 电荷", "CONS"),
            ("能挑出代码里的物理错", "至少 1 个", "BUG"),
        ],
        "concepts": [
            ("量纲分析 · Buckingham π", "把所有量化成无量纲组合;参数空间瞬间瘦下来。"),
            ("解析极限作为 sanity check", "经典极限、零阶近似、自由极限,各取一个。"),
            ("守恒律 · 数值中的 drift", "能量 / 概率 / 流量;数值 drift 应小于 1e-6 / 1e-4。"),
            ("Astropy units / pint", "Python 量纲库;让单位错误在编译期暴露。"),
        ],
        "lab": [
            ("15min", "讲解", "Buckingham π + 守恒 drift 经典案例"),
            ("20min", "示范", "教师把上节课的 MVP 加上 pint,加守恒律检查"),
            ("45min", "实验", "小组改写 MVP,加上 2 个极限 + 1 个守恒律 assert"),
            ("10min", "复盘", "看谁的代码先报错 — 报错最多的最受益"),
        ],
        "checks": [
            ("所有 magic number 都有量纲注释吗", "光速 c = 2.998e8 m/s"),
            ("ℏ→0 极限会回到经典吗", "如果不会,说明 ℏ 出现在不该出现的地方"),
            ("能量守恒 drift < 误差容限吗", "drift 大于容限,说明算法有问题"),
            ("AI 写的代码有量纲错误吗", "经常有 — 必须人工审一遍"),
        ],
        "hw": [
            "MVP 加上量纲检查,推 PR",
            "写 1 张极限对比图(经典 vs 数值)",
            "在报告「验证」段填上极限 + 守恒律两条",
        ],
        "next_zh": "下节课 · 拟合与误差条",
        "next_desc": "χ²、似然、bootstrap;给每个数标上不确定度。",
    },
    {
        "n": 6, "stage": "02", "stage_zh": "数值计算",
        "title_zh": "拟合与<br/>误差条",
        "title_en": "Fitting · Uncertainty",
        "tagline": "无误差条的数 = 谣言。这节课学 χ²、似然、参数置信区间、bootstrap 重采样。",
        "kpi": [
            ("能做最小二乘拟合", "scipy.curve_fit + Jacobian", "FIT"),
            ("能算 1σ 误差条", "from Hessian or bootstrap", "ERR"),
            ("能画带阴影的拟合曲线", "数据点 + 拟合 + 1σ band", "PLOT"),
            ("能解释为什么不能信", "拟合优度 / 残差结构", "DOUBT"),
        ],
        "concepts": [
            ("最小二乘 vs 加权拟合", "数据各点误差不同时,必须加权。"),
            ("协方差矩阵 → 参数误差", "Hessian 的逆 = 协方差;对角是方差。"),
            ("bootstrap 重采样", "原始数据采样 N 次,每次拟合,看参数分布。"),
            ("拟合优度", "reduced χ² ~ 1 才合理;偏大说明模型差。"),
        ],
        "lab": [
            ("15min", "讲解", "χ² 推导 + 误差传播公式"),
            ("20min", "示范", "教师用 curve_fit 拟合一组真实数据,画 1σ 带"),
            ("45min", "实验", "小组在自己 MVP 里加入拟合 + 误差条"),
            ("10min", "复盘", "看谁的误差带最窄 — 检查是否过拟合"),
        ],
        "checks": [
            ("拟合参数有误差条吗", "没有不算结果"),
            ("拟合曲线有 1σ band 吗", "没有就再画"),
            ("reduced χ² 在 0.5-2 吗", "不在,说明模型或误差估计有问题"),
            ("残差有结构吗", "残差呈现系统性 → 模型缺一项"),
        ],
        "hw": [
            "把 MVP 的所有数加上误差条",
            "画一张带 1σ band 的拟合图",
            "写 1 段：为什么我相信这个误差估计",
        ],
        "next_zh": "下节课 · SymPy 与 LaTeX 推导",
        "next_desc": "用 CAS 检查手算,让 AI 推导可审查、可重现。",
    },
    {
        "n": 7, "stage": "02", "stage_zh": "数值计算",
        "title_zh": "SymPy 与<br/>LaTeX 推导",
        "title_en": "Symbolic Computation",
        "tagline": "AI 推导经常错。用 SymPy 检查每一步,让推导可审查。报告里的每个公式都要走过这一关。",
        "kpi": [
            ("能用 SymPy 求导积分", "diff / integrate / simplify", "SYM"),
            ("能验证手算结果", "数值 + 符号双校", "VERIFY"),
            ("能输出 LaTeX 源码", "sympy.latex()", "TEX"),
            ("能识别 AI 错推", "至少 2 类常见错误", "CATCH"),
        ],
        "concepts": [
            ("SymPy 基础", "symbols, diff, integrate, solve, simplify。"),
            ("数值 + 符号双校", "符号推一遍,数值代一遍,两边对上再信。"),
            ("LaTeX 自动生成", "sympy.latex() 让推导可粘进报告。"),
            ("AI 推导常见错", "符号搞反 / 边界条件丢 / 因子 2 / 缺归一化。"),
        ],
        "lab": [
            ("15min", "讲解", "SymPy 常用 API + AI 推导坑展示"),
            ("20min", "示范", "教师用 SymPy 验证一个 Green's function 推导"),
            ("45min", "实验", "学生选一段 AI 给的推导,用 SymPy 完整验证"),
            ("10min", "复盘", "找出 AI 错的至少 1 处,讨论错在哪"),
        ],
        "checks": [
            ("推导每步都有 SymPy 校验吗", "至少关键步要校"),
            ("数值代入对得上吗", "数值不对,符号一定错"),
            ("LaTeX 源码可重新生成吗", "不能 → 报告无法复现"),
            ("AI 编的「显然可证」句子有验吗", "经常是错的"),
        ],
        "hw": [
            "把项目核心推导用 SymPy 验一遍,提交 notebook",
            "在报告里把推导段补上",
            "记下 AI 至少一处推导错误,写「我是怎么发现的」",
        ],
        "next_zh": "下节课 · ODE / PDE 求解",
        "next_desc": "进入数值积分核心,振动 / 传热 / 散射全用得上。",
    },
    {
        "n": 8, "stage": "02", "stage_zh": "数值计算",
        "title_zh": "ODE / PDE<br/>求解",
        "title_en": "Numerical Integration",
        "tagline": "物理建模的核心算法。这节课覆盖 ODE 初值问题、PDE 显式差分、收敛性测试。第 8 课中期检查。",
        "kpi": [
            ("能用 solve_ivp 求 ODE", "RK45 / BDF / 选 stiffness", "ODE"),
            ("能写一个 1D PDE 显式差分", "热方程 / 波方程", "PDE"),
            ("能做收敛性测试", "误差随 Δt, Δx 下降的阶", "CONV"),
            ("交中期项目成果", "第 8 课硬节点", "MIDTERM"),
        ],
        "concepts": [
            ("solve_ivp + 算法选择", "非 stiff 用 RK45,stiff 用 BDF;别全用默认。"),
            ("CFL 条件", "显式差分稳定性 Δt < CFL × Δx²/(2D);破了就发散。"),
            ("收敛阶检查", "Δx 减半,误差按 Δx^p 下降。p 不对 → 实现有 bug。"),
            ("隐式法 vs 显式法", "刚性问题必须隐式;Crank-Nicolson 是经典选择。"),
        ],
        "lab": [
            ("15min", "讲解", "ODE / PDE 算法选择决策树"),
            ("20min", "示范", "教师把 1D 热方程从写公式到收敛测试做一遍"),
            ("45min", "实验", "小组实现项目中需要的 ODE / PDE 数值求解"),
            ("10min", "复盘", "组间互看 CFL 设置,找隐藏的发散点"),
        ],
        "checks": [
            ("CFL 条件满足吗", "Δt 太大会发散"),
            ("收敛阶对吗", "二阶差分应有 p=2"),
            ("能量 / 概率守恒住吗", "drift 大说明算法有问题"),
            ("与解析极限对得上吗", "如平衡态、长时间渐近"),
        ],
        "hw": [
            "项目核心 ODE/PDE 求解器实现 + 收敛性测试",
            "提交中期报告 v1(3 页),含验证两条",
            "为下节 Monte Carlo 课预习抽样基本概念",
        ],
        "next_zh": "下节课 · Monte Carlo 方法",
        "next_desc": "用抽样 + 误差估计处理高维积分、随机过程、贝叶斯。",
    },
    {
        "n": 9, "stage": "02", "stage_zh": "数值计算",
        "title_zh": "Monte Carlo<br/>方法",
        "title_en": "Monte Carlo",
        "tagline": "高维 + 随机 + 难积分,用抽样。统计意义上的「对」。这节课覆盖 importance sampling、MCMC、误差估计。",
        "kpi": [
            ("能写一个 MC 积分", "估计 π 的经典例子", "MC"),
            ("能用 importance sampling", "提升收敛速度 10×", "IS"),
            ("能跑一个 MCMC", "Metropolis-Hastings", "MCMC"),
            ("能估计 MC 误差", "标准误 σ/√N", "SE"),
        ],
        "concepts": [
            ("基本 MC 积分", "⟨f⟩ ± σ/√N;收敛速度独立于维度。"),
            ("重要性抽样 IS", "从更聪明的分布抽,可降低方差几个量级。"),
            ("MCMC · Metropolis-Hastings", "平稳分布 = 目标分布;接受率 0.2-0.5。"),
            ("自相关时间 τ", "有效样本数 = N/(2τ);误差要按 √(2τ/N) 算。"),
        ],
        "lab": [
            ("15min", "讲解", "MC 抽样基本套路 + MCMC 思想"),
            ("20min", "示范", "教师用 MCMC 拟合一组数据 + 后验图"),
            ("45min", "实验", "小组在项目中加入 MC 或 MCMC 模块"),
            ("10min", "复盘", "看自相关图,确认有效样本数"),
        ],
        "checks": [
            ("MC 误差按 1/√N 收敛吗", "不是的话,可能有偏"),
            ("MCMC 接受率合理吗", "0.2-0.5 是经验最佳"),
            ("自相关时间算了吗", "没算就别看后验"),
            ("总样本数 ≥ 10× 自相关时间吗", "不够,后验不可信"),
        ],
        "hw": [
            "项目加入 MC 或 MCMC 模块,提交结果图",
            "更新报告:把验证清单中「误差估计」段补完",
            "进入阶段三准备:复习反问题与 UQ 的概念",
        ],
        "next_zh": "下节课 · 反问题与 UQ",
        "next_desc": "进入阶段三。从数据反推参数 — 贝叶斯框架下的不确定性量化。",
    },
    # ============ 阶段三 · 项目流程与项目表达 ============
    {
        "n": 10, "stage": "03", "stage_zh": "项目流程",
        "title_zh": "反问题<br/>与 UQ",
        "title_en": "Inverse Problems · UQ",
        "tagline": "从数据反推参数。前向问题人人会算,反问题靠贝叶斯。这节课覆盖后验、置信区间、敏感性分析。",
        "kpi": [
            ("能写出贝叶斯三件套", "似然 + 先验 + 后验", "BAYES"),
            ("能跑一个 MCMC 反推", "参数 → 后验分布", "POST"),
            ("能画 corner plot", "参数 pair 后验图", "CORNER"),
            ("能做敏感性分析", "Sobol or Morris", "SENS"),
        ],
        "concepts": [
            ("贝叶斯反推", "p(θ|D) ∝ p(D|θ) p(θ);先验决定结论的边界。"),
            ("emcee / cobaya / dynesty", "Python 反问题三剑客;前两个 MCMC,后者 nested sampling。"),
            ("后验图解读", "1D 边缘 + 2D corner;主对角是单参数,off 是相关性。"),
            ("敏感性分析", "哪个参数最影响输出;指导未来加数据点。"),
        ],
        "lab": [
            ("15min", "讲解", "贝叶斯框架 + 反问题示例"),
            ("20min", "示范", "教师用 emcee 反推一个项目相关的参数"),
            ("45min", "实验", "小组对项目的核心参数做贝叶斯反推"),
            ("10min", "复盘", "看 corner plot,讨论参数相关性"),
        ],
        "checks": [
            ("先验合理吗", "uniform 太宽 / 太窄都会扭曲后验"),
            ("MCMC 收敛了吗", "用 Gelman-Rubin R̂ < 1.05"),
            ("后验里有 banana / 多峰吗", "可能是真实结构,也可能是退化"),
            ("敏感性分析做了吗", "没做就不知道下一步加什么数据"),
        ],
        "hw": [
            "项目核心参数做一次贝叶斯反推",
            "提交 corner plot + 1σ 区间表",
            "在报告里加一段：参数不确定性",
        ],
        "next_zh": "下节课 · 计划、实现、审查、写作分工",
        "next_desc": "把小组工作拆成 4 个角色,轮换练习。",
    },
    {
        "n": 11, "stage": "03", "stage_zh": "项目流程",
        "title_zh": "计划、实现<br/>审查、写作",
        "title_en": "Project Roles",
        "tagline": "小组协作的 4 个角色:Plan / Do / Review / Write。每个学生都至少轮换两次,期末报告靠四力合一。",
        "kpi": [
            ("理解 4 角色边界", "PDRW 各做什么", "ROLE"),
            ("已经轮换过 ≥ 2 角色", "亲身体验差异", "ROTATE"),
            ("能做一次同行评阅", "用清单不用情绪", "PEER"),
            ("中期报告四角色署名", "谁写了哪段都清楚", "AUTHOR"),
        ],
        "concepts": [
            ("Plan 角色", "确定本周目标、分配任务、写 issue;最容易被忽视。"),
            ("Do 角色", "实现代码;不是英雄主义,要可被 Review。"),
            ("Review 角色", "看代码、看结果、看物理;不舒服就提 issue。"),
            ("Write 角色", "把所有人的工作翻译成报告;最后一步,但贯穿全程。"),
        ],
        "lab": [
            ("15min", "讲解", "4 角色清单 + 常见冲突"),
            ("20min", "示范", "教师演示一次 PR Review 流程"),
            ("45min", "实验", "小组按角色重做一遍上周任务,记录差异"),
            ("10min", "复盘", "讨论「哪个角色最不舒服」 — 那是你最需要练的"),
        ],
        "checks": [
            ("Plan 写下来了吗", "口头不算,issue / TODO 才算"),
            ("Review 用清单了吗", "凭感觉评不算 Review"),
            ("Write 提前开始了吗", "最后一周写出来的报告必然差"),
            ("每个人都轮换过吗", "没有 → 期末必有人掉链子"),
        ],
        "hw": [
            "小组在 issue / Project board 上记录 4 角色分工",
            "至少做一次跨成员 Code Review,带评论",
            "更新中期报告,标注每段的写作责任人",
        ],
        "next_zh": "下节课 · Git、环境与交互日志",
        "next_desc": "把工程基础设施搭对 — 不然组协作就是空话。",
    },
    {
        "n": 12, "stage": "03", "stage_zh": "项目流程",
        "title_zh": "Git、环境<br/>与交互日志",
        "title_en": "Engineering Basics",
        "tagline": "代码可复现的底盘。git 分支模型、conda 环境、AI 交互日志,这三件不到位,项目就停在「我电脑能跑」。",
        "kpi": [
            ("能用 PR 流程协作", "branch + PR + review", "GIT"),
            ("能写 environment.yml", "conda 锁版本", "ENV"),
            ("能记 AI 交互日志", "提示词 + 输出 + 人工修改", "LOG"),
            ("能 git clone 在新机器跑通", "30 min 内复现", "REPRO"),
        ],
        "concepts": [
            ("Git branch 模型", "main 受保护 / dev / feature/<name>;PR 合并才入 main。"),
            ("conda + pip 混合管理", "conda 装系统库,pip 装纯 Python;锁 environment.yml。"),
            ("AI 交互日志格式", "时间 / 任务 / 提示词 / 输出摘要 / 人工修改;Markdown 表。"),
            ("README + Makefile", "make data / make figs / make report 三个目标,标准操作。"),
        ],
        "lab": [
            ("15min", "讲解", "PR 流程 + conda 锁版本 + 日志模板"),
            ("20min", "示范", "教师从空目录开始 30 分钟搭一个可复现项目"),
            ("45min", "实验", "小组把现有项目改造成「换电脑能跑」的状态"),
            ("10min", "复盘", "组间交换电脑 git clone,看能不能跑通"),
        ],
        "checks": [
            ("environment.yml 在仓库里吗", "没有就没法在别的机器跑"),
            ("README 写了如何跑吗", "make / python main.py 一行命令"),
            ("AI 交互日志至少写了 5 条吗", "记得 prompt + 改了什么"),
            ("换台电脑能 30 分钟内复现吗", "做不到就还不是工程产物"),
        ],
        "hw": [
            "项目仓库整理成可复现结构,推 PR",
            "AI 交互日志补到 ≥ 10 条",
            "用另一台电脑或同学的电脑测试 git clone 跑通",
        ],
        "next_zh": "下节课 · 项目报告写作",
        "next_desc": "把所有结果翻译成 4-6 页报告 — 期末交付的核心。",
    },
    {
        "n": 13, "stage": "03", "stage_zh": "项目流程",
        "title_zh": "项目报告<br/>写作",
        "title_en": "Report Writing",
        "tagline": "4-6 页 LaTeX 报告:动机、模型、方法、验证、结果、局限性。这节课教结构、教图表规范、教局限性怎么写。",
        "kpi": [
            ("理解 6 段结构", "每段写什么 / 不写什么", "STRUCT"),
            ("能做 1 张出版级图", "Morandi 色系 + 字号 ≥ 9pt", "FIG"),
            ("能写「局限性」段", "诚实地说哪不靠谱", "LIMIT"),
            ("交报告 draft v2", "完整 6 段 + 3 张图", "DRAFT"),
        ],
        "concepts": [
            ("报告 6 段结构", "Intro / Model / Method / Validation / Results / Limitations。"),
            ("图表规范", "Morandi 色系、字号、量纲、误差条、图例位置;一张图讲一件事。"),
            ("局限性的诚实写法", "我们没做 X,因为 Y;在 Z 条件下结论可能不成立。"),
            ("LaTeX + BibTeX", "用 overleaf 或本地 latexmk;参考文献从 task.md 来。"),
        ],
        "lab": [
            ("15min", "讲解", "6 段结构 + 写作禁忌(假谦虚 / 模糊语言)"),
            ("20min", "示范", "教师改一份学生 draft,展示怎么砍废话"),
            ("45min", "实验", "小组写完报告 draft v2,准备互评"),
            ("10min", "复盘", "跨组互评,圈每段最强 / 最弱句"),
        ],
        "checks": [
            ("摘要写完了吗", "200 字内,讲清问题 + 方法 + 关键结果"),
            ("图都能独立看懂吗", "caption 写清楚,不靠正文"),
            ("局限性段诚实吗", "不是「未来可以改进」这种废话"),
            ("参考文献都有 DOI 吗", "没有就不算有效引用"),
        ],
        "hw": [
            "提交报告 draft v2(4-6 页)",
            "至少完成 1 张出版级图 + caption",
            "跨组评阅另一组的报告,写 200 字 review",
        ],
        "next_zh": "下节课 · AI 工具使用说明 + 学术诚信",
        "next_desc": "进入阶段四。把 AI 使用的边界、责任、声明写清楚。",
    },
    # ============ 阶段四 · 伦理规范与项目展示 ============
    {
        "n": 14, "stage": "04", "stage_zh": "伦理规范",
        "title_zh": "AI 工具使用说明<br/>+ 学术诚信",
        "title_en": "AI Disclosure · Ethics",
        "tagline": "学术诚信底线高于工程效率。最终报告必须包含 AI 使用说明:工具、用途、人工核查、最终责任。",
        "kpi": [
            ("能写 AI 使用说明", "4 字段:工具 / 用途 / 核查 / 责任", "DISC"),
            ("理解学术诚信红线", "什么算抄,什么算用工具", "RED"),
            ("能区分数据边界", "公开 / 实验室 / 个人隐私", "DATA"),
            ("签署诚信承诺", "本组所有人", "SIGN"),
        ],
        "concepts": [
            ("AI 使用说明 4 字段", "工具(Claude/GPT/...) / 用途(代码/写作/...) / 人工核查(谁审了什么) / 最终责任(本人)。"),
            ("AI 使用 vs 学术不端", "用 AI 写代码 ≠ 抄;不声明 + 不核查 = 不端。"),
            ("数据边界与隐私", "公开数据集可发 → 实验室内部数据要授权 → 个人识别数据绝不发 AI。"),
            ("诚信承诺书", "本课要求每个学生签;承诺核验、声明、承担最终责任。"),
        ],
        "lab": [
            ("15min", "讲解", "学术诚信红线 + 4 个真实失败案例"),
            ("20min", "示范", "教师把项目报告的 AI 使用说明从头写一遍"),
            ("45min", "实验", "小组为自己项目写 AI 使用说明草稿"),
            ("10min", "复盘", "跨组互看,圈「还不够具体」的地方"),
        ],
        "checks": [
            ("声明里写了具体用途吗", "写「用 AI 写代码」不算具体"),
            ("声明里写了人工核查动作吗", "我核了 X,运行了 Y,改了 Z"),
            ("数据上传 AI 前征得授权了吗", "实验室数据要老师签字"),
            ("责任栏写了「本人承担」吗", "不能写「AI 负责」"),
        ],
        "hw": [
            "完成本组 AI 使用说明终稿,合入报告附录",
            "签署诚信承诺书,扫描发课程平台",
            "为下节工作坊准备 5 分钟内部进度展示",
        ],
        "next_zh": "下节课 · 项目工作坊",
        "next_desc": "课堂冲刺;同组 + 跨组互审;教师现场答疑。",
    },
    {
        "n": 15, "stage": "04", "stage_zh": "伦理规范",
        "title_zh": "项目<br/>工作坊",
        "title_en": "Project Workshop",
        "tagline": "最后一次教师答疑机会。同组冲刺 + 跨组互审 + 现场答疑。下次课就是 8 分钟展示。",
        "kpi": [
            ("完成最后 1 处验证", "把最后那条还差的补上", "FILL"),
            ("通过 1 次跨组评阅", "至少 1 条 actionable 反馈", "PEER"),
            ("演讲幻灯片 v1", "≤ 10 页,8 分钟", "SLIDES"),
            ("演练 1 次", "8 分钟讲完不超时", "DRILL"),
        ],
        "concepts": [
            ("8 分钟讲什么", "1 动机 + 3 核心 + 1 验证 + 1 局限 + 1 致谢。"),
            ("跨组互审清单", "数据可信? 验证齐? 局限诚实? 展示有「啊哈」时刻?"),
            ("常见演讲毛病", "字太多 / 念稿 / 时间超 / 图太挤;每条都有对策。"),
            ("最后冲刺优先级", "故事 > 验证 > 美观 > 完整。"),
        ],
        "lab": [
            ("15min", "讲解", "8 分钟演讲模板 + 跨组评阅清单"),
            ("20min", "示范", "教师演 1 次 8 分钟「反面教材」"),
            ("45min", "实验", "组内冲刺 + 跨组互审,迭代幻灯片"),
            ("10min", "复盘", "每组演 1 张最自豪的图,30 秒讲"),
        ],
        "checks": [
            ("8 分钟刚好讲完吗", "超 30 秒会被扣分"),
            ("最关键结论 1 张图能讲完吗", "讲不完,图就要重做"),
            ("局限性诚实吗", "没有 → 评委一定追问"),
            ("AI 使用说明放进 backup 了吗", "答辩时被问要能秒掉"),
        ],
        "hw": [
            "幻灯片 v2 + 演练 2 次,每次录像自审",
            "提交项目终稿 PDF + 仓库链接",
            "为答辩准备 backup 图(被问到时调出)",
        ],
        "next_zh": "下节课 · 8 分钟展示与答辩",
        "next_desc": "32 学时的终点。每组 8 分钟 + 5 分钟教师答辩。",
    },
    {
        "n": 16, "stage": "04", "stage_zh": "伦理规范",
        "title_zh": "8 分钟展示<br/>与答辩",
        "title_en": "Final Defense",
        "tagline": "32 学时终点。每组 8 分钟讲 + 5 分钟答辩。教师 + 同学一起评。课程结束,你带走的是一套可复用的方法。",
        "kpi": [
            ("8 分钟讲完", "不超时 不超字", "TIME"),
            ("回答 ≥ 3 个问题", "用数据回答,不靠感觉", "QA"),
            ("交付项目档案", "代码 + 报告 + 日志 + 验证清单 + 声明", "DELIV"),
            ("写下 1 条带走的方法", "你这门课最大收获", "TAKEAWAY"),
        ],
        "concepts": [
            ("8 分钟节奏", "0-1 动机 / 1-4 核心 / 4-6 验证 / 6-7 局限 / 7-8 收束。"),
            ("答辩 5 分钟", "教师 3 问,同学 1-2 问;用数据回,不要「我感觉」。"),
            ("教师评分维度", "物理 + 方法 + 验证 + 表达 + 诚信。"),
            ("课程结束 ≠ 学完", "带走的方法可以用在后面所有的研究里。"),
        ],
        "lab": [
            ("15min", "开场", "课程总结 + 评分说明"),
            ("20min", "展示", "前 2-3 组 · 8 分钟 + 5 分钟答辩"),
            ("45min", "展示", "剩余组 · 8 分钟 + 5 分钟答辩"),
            ("10min", "收束", "颁奖 + 每个学生写下 1 条最大收获"),
        ],
        "checks": [
            ("时间控制到位吗", "8:00 自动停,后面被砍"),
            ("回答用了数据吗", "用图 / 数 / 公式回,不靠「感觉」"),
            ("项目档案全交了吗", "5 件 deliverable 一件不落"),
            ("写下「我带走什么」了吗", "没写就只完成了课程,没完成自己"),
        ],
        "hw": [
            "提交项目终稿 + 5 件 deliverable",
            "填写课程反馈问卷",
            "选一项今天没做完的方法,放进下学期某门课的工具箱",
        ],
        "next_zh": "课程结束 · End of Course",
        "next_desc": "32 学时只是起点。Vibe Physics 的方法,跟你一辈子。",
    },
]

# ---------- HTML 片段模板 ----------

def sec_cover(s):
    return f'''
<section class="slide accent" data-animate="hero">
  <div class="canvas-card">
    <canvas class="ascii-bg" aria-hidden="true"></canvas>
    <div class="chrome-min">
      <div class="l">Vibe Physics · Stage {s["stage"]} · {s["stage_zh"]}</div>
      <div class="r">L{s["n"]:02d} · 01 / 06</div>
    </div>
    <div style="flex:1;padding:0;display:grid;grid-template-rows:auto 1fr auto;gap:2.6vh">
      <div data-anim="kicker" class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em">Session {s["n"]:02d} · {s["title_en"]}</div>
      <h1 data-anim="title" style="align-self:center;font-family:var(--sans),var(--sans-zh);font-weight:200;font-size:min(8.4vw,15vh);line-height:.96;letter-spacing:-.025em;color:#fff">第 {s["n"]:02d} 课<br/>{s["title_zh"]}</h1>
      <div data-anim="bottom" style="display:grid;grid-template-rows:auto auto;gap:1.6vh;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh">
        <div data-anim="lead" class="lead" style="max-width:62ch;color:rgba(255,255,255,.86);font-weight:300">{s["tagline"]}</div>
        <div style="display:flex;justify-content:space-between;align-items:end">
          <div class="t-meta" style="color:rgba(255,255,255,.6)">2 学时 · 90 分钟 · 阶段 {s["stage"]}</div>
          <div class="t-meta" style="color:rgba(255,255,255,.6)">→ swipe / arrow keys</div>
        </div>
      </div>
    </div>
  </div>
</section>'''

def sec_objectives(s):
    cells = ""
    for i, (title, desc, label) in enumerate(s["kpi"]):
        cells += f'''
        <div class="kpi-cell">
          <div class="lbl">Goal · {label}</div>
          <div class="nb" style="font-size:min(3vw,5.2vh);font-weight:300;line-height:1.1;letter-spacing:-.02em">{title}</div>
          <div class="note">{desc}</div>
        </div>'''
    return f'''
<section class="slide" data-animate="grid-reveal">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">第 {s["n"]:02d} 课 · 学习目标</div>
      <div class="r">02 / 06</div>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:5vh">
      <div data-anim="title">
        <span class="t-cat accent">Learning Objectives</span>
        <h2 class="h-xl-zh" style="margin-top:1.4vh;max-width:24ch">本节课结束时,<br/>你应该能做到这<span style="color:var(--accent)">四件事</span>。</h2>
      </div>
      <div data-anim="kpi" class="kpi-row-4">{cells}
      </div>
    </div>
  </div>
</section>'''

def sec_concepts(s):
    cards = ""
    n = len(s["concepts"])
    cols = "1fr 1fr" if n <= 2 else ("repeat(2,1fr)" if n == 4 else "repeat(3,1fr)" if n == 3 else "repeat(4,1fr)")
    for i, (title, desc) in enumerate(s["concepts"]):
        cls = "card-accent" if i == n - 1 else "card-fill"
        title_color = "#fff" if i == n - 1 else "var(--text-primary)"
        desc_color = "rgba(255,255,255,.86)" if i == n - 1 else "var(--text-secondary)"
        meta_color = "rgba(255,255,255,.78)" if i == n - 1 else "var(--accent)"
        cards += f'''
      <article class="{cls}" style="padding:3vh 2vw;display:flex;flex-direction:column;gap:1.2vh;min-height:0">
        <div class="t-meta" style="color:{meta_color}">CONCEPT · {i+1:02d}</div>
        <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:500;font-size:max(17px,1.55vw);letter-spacing:-.015em;color:{title_color}">{title}</h3>
        <p style="font-family:var(--sans),var(--sans-zh);font-size:max(12px,.95vw);line-height:1.6;color:{desc_color};font-weight:300;margin-top:auto">{desc}</p>
      </article>'''
    return f'''
<section class="slide grey" data-animate="grid-reveal">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">第 {s["n"]:02d} 课 · 核心概念</div>
      <div class="r">03 / 06</div>
    </div>
    <div data-anim="title" style="display:grid;grid-template-columns:5fr 7fr;gap:4vw;align-items:end;margin-bottom:4vh">
      <div>
        <span class="t-cat accent">Core Concepts</span>
        <h2 class="h-xl-zh" style="margin-top:1.4vh">这一节课<br/>的几个支点。</h2>
      </div>
      <p class="body" style="font-size:max(13px,1.1vw);line-height:1.65;padding-bottom:1vh">先把这几个概念立起来,后面 90 分钟才有共同语言。讲不动的概念,课后立刻提问。</p>
    </div>
    <div data-anim="cards" style="flex:1;display:grid;grid-template-columns:{cols};gap:1.8vh 1.8vw;align-content:start">{cards}
    </div>
  </div>
</section>'''

def sec_lab(s):
    cells = ""
    for i, (mins, phase, desc) in enumerate(s["lab"]):
        is_core = (i == 2)
        bg = "var(--accent)" if is_core else "var(--paper)"
        fg = "#fff" if is_core else "var(--text-primary)"
        sub_fg = "rgba(255,255,255,.86)" if is_core else "var(--text-secondary)"
        meta = "rgba(255,255,255,.78)" if is_core else "var(--accent)"
        cells += f'''
      <div style="background:{bg};color:{fg};padding:3vh 1.6vw;display:flex;flex-direction:column;gap:1.2vh;justify-content:space-between">
        <div>
          <div class="t-meta" style="color:{meta}">PHASE {i+1:02d} · {phase}</div>
          <div style="font-family:var(--sans);font-weight:200;font-size:min(6vw,10.2vh);line-height:.9;letter-spacing:-.03em;margin-top:1vh;color:{fg}">{mins}</div>
        </div>
        <p style="font-family:var(--sans),var(--sans-zh);font-size:max(11px,.94vw);line-height:1.55;color:{sub_fg};font-weight:300">{desc}</p>
      </div>'''
    return f'''
<section class="slide" data-animate="timeline-walk">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">第 {s["n"]:02d} 课 · 课堂实验 90 分钟</div>
      <div class="r">04 / 06</div>
    </div>
    <div data-anim="title" style="margin-bottom:5vh">
      <span class="t-cat accent">In-Class Lab · 90 min</span>
      <h2 class="h-xl-zh" style="margin-top:1.4vh;max-width:24ch">这节课<span style="color:var(--accent)">怎么过</span>。</h2>
    </div>
    <div data-anim="timeline" style="flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--grey-2);border:1px solid var(--grey-2);min-height:0">{cells}
    </div>
  </div>
</section>'''

def sec_checks(s):
    cards = ""
    for i, (q, ans) in enumerate(s["checks"]):
        cards += f'''
      <div class="card-fill" style="padding:2.6vh 1.8vw;display:flex;flex-direction:column;gap:.8vh;border-left:3px solid var(--accent)">
        <div class="t-meta accent" style="color:var(--accent)">CHECK {i+1:02d}</div>
        <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:500;font-size:max(14px,1.25vw);line-height:1.25;letter-spacing:-.01em">{q}</h3>
        <p style="font-family:var(--sans),var(--sans-zh);font-size:max(11px,.9vw);line-height:1.55;color:var(--text-secondary);font-weight:300;margin-top:.4vh">→ {ans}</p>
      </div>'''
    return f'''
<section class="slide" data-animate="grid-reveal">
  <div class="canvas-card">
    <div class="chrome-min">
      <div class="l">第 {s["n"]:02d} 课 · 验证清单 / 常见坑</div>
      <div class="r">05 / 06</div>
    </div>
    <div data-anim="title" style="margin-bottom:4.4vh">
      <span class="t-cat accent">Validation Checklist</span>
      <h2 class="h-xl-zh" style="margin-top:1.4vh;max-width:24ch">提交前,先过这<span style="color:var(--accent)">四问</span>。</h2>
    </div>
    <div data-anim="checks" class="grid-4" style="flex:1;align-content:stretch;gap:2.6vh 2.4vw;grid-template-rows:1fr 1fr">{cards}
    </div>
  </div>
</section>'''

def sec_closing(s):
    hws = ""
    for i, hw in enumerate(s["hw"]):
        is_last = (i == len(s["hw"]) - 1)
        color = "var(--accent)" if is_last else "var(--text-primary)"
        border = "border-bottom:2px solid var(--accent)" if is_last else ""
        hws += f'''
          <div style="display:grid;grid-template-columns:auto 1fr;gap:2vw;align-items:start;padding:2.4vh 0;border-top:1px solid var(--border-subtle);{border}">
            <div style="font-family:var(--sans);font-weight:200;font-size:min(4.2vw,7.4vh);line-height:.9;color:{color}">{i+1:02d}</div>
            <div>
              <h3 style="font-family:var(--sans),var(--sans-zh);font-weight:400;font-size:max(15px,1.45vw);line-height:1.3;letter-spacing:-.015em;color:{color};margin-bottom:.6vh">{hw}</h3>
            </div>
          </div>'''
    return f'''
<section class="slide split" data-animate="split-statement">
  <div class="canvas-card">
    <div class="split-half">
      <div class="half b-accent" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between;position:relative;overflow:hidden">
        <canvas class="ascii-bg" aria-hidden="true"></canvas>
        <div class="chrome-min" style="margin-bottom:0;position:relative;z-index:1">
          <div class="l">06 / 06</div>
          <div class="r">NEXT · L{s["n"]+1:02d}</div>
        </div>
        <div data-anim="manifesto" style="display:flex;flex-direction:column;gap:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.78);letter-spacing:.22em;margin-bottom:1.6vh">UP NEXT</div>
          <h2 style="font-family:var(--sans),var(--sans-zh);font-size:min(6.4vw,11.4vh);line-height:.98;letter-spacing:-.025em;font-weight:200;color:#fff">{s["next_zh"]}</h2>
          <div style="font-family:var(--sans),var(--sans-zh);font-size:max(13px,1vw);line-height:1.6;color:rgba(255,255,255,.84);font-weight:300;max-width:38ch;margin-top:1.4vh">{s["next_desc"]}</div>
        </div>
        <div data-anim="signature" style="display:flex;justify-content:space-between;align-items:end;border-top:1px solid rgba(255,255,255,.22);padding-top:2vh;position:relative;z-index:1">
          <div class="t-meta" style="color:rgba(255,255,255,.62)">L{s["n"]:02d} 结课 · Session ends</div>
          <div class="t-meta" style="color:rgba(255,255,255,.62)">Vibe Physics</div>
        </div>
      </div>
      <div class="half" style="padding:5.6vh 3.6vw 4.4vh;justify-content:space-between">
        <div class="chrome-min">
          <div class="l">课后作业 · HOMEWORK</div>
          <div class="r">{len(s["hw"]):02d} TASKS</div>
        </div>
        <div data-anim="rules" style="display:flex;flex-direction:column;gap:0">{hws}
        </div>
        <div data-anim="foot" class="t-meta" style="color:var(--text-helper);text-align:right">→ 下周见 · See you next session</div>
      </div>
    </div>
  </div>
</section>'''

# ---------- 主流程 ----------

def main():
    raw_template = (ROOT / "session-01.html").read_text(encoding="utf-8")

    for s in SESSIONS:
        slides_html = (
            sec_cover(s)
            + sec_objectives(s)
            + sec_concepts(s)
            + sec_lab(s)
            + sec_checks(s)
            + sec_closing(s)
        )

        # Replace title
        title = f'<title>第 {s["n"]:02d} 课 · {s["title_en"]} · Vibe Physics</title>'
        out = re.sub(
            r'<title>.*?</title>',
            title,
            raw_template,
            count=1,
        )

        # Replace everything from the SLIDES_HERE comment to just before <div id="nav">
        start_marker = "<!-- SLIDES_HERE"
        end_marker = '<div id="nav">'

        start_idx = out.find(start_marker)
        end_idx = out.find(end_marker)
        if start_idx < 0 or end_idx < 0:
            print(f"ERROR: SLIDES markers not found for session {s['n']:02d}", file=sys.stderr)
            sys.exit(1)

        # Find the closing </div> of #deck just before <div id="nav">
        deck_close = out.rfind("</div>", start_idx, end_idx)
        if deck_close < 0:
            print(f"ERROR: deck </div> not found for session {s['n']:02d}", file=sys.stderr)
            sys.exit(1)

        new_block = (
            "<!-- SLIDES · auto-generated by build_sessions.py · 6 pages -->\n"
            + slides_html.strip()
            + "\n\n</div>\n\n"
        )
        out = out[:start_idx] + new_block + out[end_idx:]

        out_path = OUT_DIR / f"session-{s['n']:02d}.html"
        out_path.write_text(out, encoding="utf-8")
        print(f"✓ wrote {out_path.relative_to(ROOT.parent)}")

    print(f"\n✓ Generated {len(SESSIONS)} session decks")

if __name__ == "__main__":
    main()
