# 中国五年 AI 预测记录

这是一个长期、可复核的AI前瞻预测档案。项目在固定信息截止时间后，让不同AI系统对五年后的中国普通居民生活进行结构性预测，并完整保存问题、来源、专家原文、综合报告、概率注册表和文件哈希。

研究对象是主要依靠本人或家庭劳动收入、没有大量资本、特殊权力、内部信息或稳定被动收入的中国普通居民。预测重点包括经济与购买力、就业与职业、产业与技术、住房、地区机会、家庭负担、人口结构和外部环境。

## 当前记录

### Codex：2026—2031年预测

- 信息截止：2026年7月20日23:59，Asia/Shanghai
- 实际执行：2026年7月24日
- 预测终点：2031年7月20日
- 执行系统：Codex
- 完整报告：[reports/codex/2026-07-20](reports/codex/2026-07-20)
- 综合报告：[05-synthesis-report.md](reports/codex/2026-07-20/05-synthesis-report.md)

本轮包含四份相互独立的专家报告：

1. 长期结构与基础趋势；
2. 产业、技术与职业传导；
3. 普通居民生活与家庭决策；
4. 反方、外部环境与模型风险。

概率只作为辅助注册字段，完整理由、因果机制、普通居民影响、反例和2031年验证方法保留在报告正文中。

## 目录

```text
.
├── reports/
│   └── codex/
│       └── 2026-07-20/
│           ├── 00-experiment-and-sources.md
│           ├── 01-structural-report.md
│           ├── 02-industry-career-report.md
│           ├── 03-resident-life-report.md
│           ├── 04-skeptic-external-report.md
│           ├── 05-synthesis-report.md
│           ├── forecast-registry.csv
│           └── SHA256SUMS.txt
└── skills/
    ├── codex/china-five-year-forecast-team/
    └── claude/china-five-year-forecast-team/
```

`skills/codex` 保存Codex使用的原始Skill；`skills/claude` 保存适配Claude Code的版本。Claude版要求四位专家在相互隔离的子代理上下文中运行；如果环境无法提供独立子代理，不得在一个上下文里模拟独立实验。

## 实验原则

- 固定并记录信息截止时间，排除截止时间后的资料；
- 四位专家获得同一份冻结来源包，但不能看到彼此报告；
- 保存四份专家初稿，不用综合报告覆盖原始意见；
- 区分事实、政策目标、解释和未知事项；
- 不把短期增速机械外推为五年趋势；
- 预先固定P01—P12、报告结构和评分方式；
- 综合报告保留分歧，不制造共识；
- 验证后计算SHA-256，防止后续无痕修改。

## 使用Skill

Codex个人Skill目录：

```text
~/.codex/skills/china-five-year-forecast-team/
```

Claude Code个人Skill目录：

```text
~/.claude/skills/china-five-year-forecast-team/
```

在相应环境中复制对应版本后，可以明确要求：

```text
使用 china-five-year-forecast-team skill，
以指定日期为信息截止时间，
完成中国普通居民五年结构预测。
```

## 完整性验证

进入报告目录后运行：

```bash
shasum -a 256 -c SHA256SUMS.txt
python3 ../../../skills/codex/china-five-year-forecast-team/scripts/validate_forecast_bundle.py .
```

本项目是预测实验与研究档案，不构成个人投资、购房或职业建议。
