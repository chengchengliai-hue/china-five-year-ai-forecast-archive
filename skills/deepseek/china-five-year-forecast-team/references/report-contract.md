# Forecast bundle and report contract

## Required files

Create one directory containing:

1. `00-experiment-and-sources.md`
2. `01-structural-report.md`
3. `02-industry-career-report.md`
4. `03-resident-life-report.md`
5. `04-skeptic-external-report.md`
6. `05-synthesis-report.md`
7. `forecast-registry.csv`

Do not hide the four reports inside the synthesis. Deliver clickable links to all five reports.

## Experiment and source file

Record execution time, cutoff, target, timezone, model/version, tools, resident definition, prompt version, deviations, source links, publication dates, source type, and cutoff audit. Separate:

- facts;
- policy targets;
- third-party interpretations;
- unknowns.

## Specialist reports

Each report must:

- contain 2,500–5,000 Chinese characters unless overridden;
- use its role-specific exact headings;
- answer every item `P01`–`P12` in developed prose;
- include at least six direct source links;
- connect evidence to a causal mechanism and then to resident outcomes;
- identify winners, pressured groups, counterarguments, and failure conditions;
- provide target-date verification methods;
- keep its probability judgments in the CSV rather than repeatedly displaying percentages.

A concise opening thesis is allowed. A conclusion list or probability table is not a replacement for the detailed body.

## Synthesis report

Target 4,000–7,000 Chinese characters unless overridden. Use:

1. `## 一、综合判断`
2. `## 二、四位专家的共同结论`
3. `## 三、四位专家的关键分歧`
4. `## 四、P01—P12综合预测`
5. `## 五、支持这些判断的主要因果链`
6. `## 六、外部因素如何传导到普通人`
7. `## 七、最可能推翻报告的变化`
8. `## 八、2031年验证与评分`

For each `P01`–`P12`, explain:

- the integrated end state;
- the strongest supporting evidence;
- the causal path to ordinary residents;
- which specialist disagreed and why, if material;
- the validation rule.

The synthesis must not merely restate twelve conclusions. It must explain why the conclusions fit together as one view of the future.

## Probability registry

Use one row per question:

```csv
id,structural,industry_career,resident_life,skeptic_external,ensemble,direction,disagreement,target_date
```

Use probability only here and, if helpful, in one compact appendix table in the synthesis. Do not make probabilities the visual center of the reports.

Aggregate with the median. Mark a question `high` disagreement when expert directions split or the probability range is at least 25 percentage points. Never replace a split direction with a false consensus.

## Final delivery

Report:

- the bundle directory;
- links to all four specialist reports;
- link to the synthesis;
- link to the CSV;
- cutoff audit result;
- validation result;
- SHA-256 hashes.
