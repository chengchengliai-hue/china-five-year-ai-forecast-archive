---
name: china-five-year-forecast-team
description: Run a repeatable four-expert, five-year structural forecasting study about how China’s economy, industries, occupations, technology, demographics, regions, housing, family burdens, and external environment may affect ordinary residents. Use when Codex must freeze a China forecast at a dated information cutoff, commission four independent full-length expert reports, preserve disagreements, produce a detailed synthesis report, or repeat the same five-year experiment in later years without drifting the questionnaire or prompts.
---

# China five-year forecast team

Produce a forecast bundle, not a short answer. Treat probabilities as a compact registry field; make evidence, causal mechanisms, resident impact, counterarguments, and verifiability the main output.

Before starting, read all of:

- [fixed-questionnaire.md](references/fixed-questionnaire.md)
- [structural-expert.md](references/structural-expert.md)
- [industry-career-expert.md](references/industry-career-expert.md)
- [resident-life-expert.md](references/resident-life-expert.md)
- [skeptic-external-expert.md](references/skeptic-external-expert.md)
- [report-contract.md](references/report-contract.md)

## Workflow

### 1. Register the experiment

Record:

- actual execution time;
- information cutoff, including timezone;
- five-year target date;
- model name and the most specific exposed version;
- tool and search access;
- ordinary-resident definition;
- any deviations from the fixed protocol.

Never claim the report was executed on the cutoff date when it was executed later.

### 2. Freeze the shared source pack

Build one compact source pack before launching specialists. Give the identical pack to all four.

- Exclude every source published after the cutoff.
- Prefer Chinese government originals, official statistics, regulator documents, company filings, identified research papers, and primary international-organization reports.
- Include both domestic and external evidence when it materially affects residents.
- Label each item `Fact`, `Policy target`, `Interpretation`, or `Unknown`.
- Do not treat a plan, slogan, target, announcement, or pilot as a measured outcome.
- Include publication date and direct link for every source.
- Keep short-term observations only as baseline evidence; do not forecast their yearly continuation.

### 3. Run four independent specialists

Use four specialist runs. Give every specialist the fixed questionnaire, shared source pack, cutoff, target date, resident definition, and its role contract.

- Do not let specialists read one another’s drafts.
- Do not ask one specialist to summarize another.
- Require a full report, not a probability table or memo.
- Require 2,500–5,000 Chinese characters per specialist report unless the user requests another length.
- Require inline links beside key factual claims.
- Permit at most four additional role-specific sources, all published by the cutoff.
- Preserve the first draft. Do not overwrite it after discussion.
- If only three subagents can run while the team lead remains active, start three together and launch the fourth after a slot opens with the unchanged source pack. Do not reveal prior reports.

### 4. Synthesize without erasing the reports

Read all four completed reports only after independence is preserved. Produce the synthesis required by [report-contract.md](references/report-contract.md).

- Lead with a detailed causal account, not a leaderboard.
- Explain supporting evidence and transmission to ordinary residents.
- Preserve meaningful disagreements and state what evidence would resolve them.
- Do not manufacture consensus.
- Keep numeric probabilities in one compact table or the CSV registry; do not repeat them throughout the prose.
- Distinguish the final integrated interpretation from each specialist’s original view.

### 5. Deliver and validate the bundle

Create every required file in the report contract. Never deliver only `05-synthesis-report.md`.

Run:

```bash
python3 scripts/validate_forecast_bundle.py <bundle-directory>
```

Fix every reported error before delivery. Compute SHA-256 hashes after final validation. Provide clickable links to all four specialist reports and the synthesis.

## Non-negotiable quality rules

- Do not reduce a specialist report to bullet conclusions.
- Do not use event probabilities as the main content.
- Do not name a few fashionable industries in the permanent questionnaire; let each annual run identify relevant sectors from that year’s evidence.
- Do not predict annual fluctuations unless the user explicitly expands the protocol.
- Do not hide uncertainty behind vague language. Give a concrete target-date end state and a way to verify it.
- Do not present private chain-of-thought. Present concise reasons, evidence, mechanisms, counterarguments, and assumptions.
- Do not provide personalized investment, property-purchase, or career instructions unless separately requested.
