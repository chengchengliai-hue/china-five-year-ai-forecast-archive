---
name: china-five-year-forecast-team
description: Run a repeatable four-expert DeepSeek five-year China forecast for ordinary residents, with a dated cutoff, independent reports, preserved disagreements, validation, and hashes.
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

## DeepSeek execution rules

- Use DeepSeek models for the lead and all four specialist runs. A compatible agent host such as Claude Code may provide orchestration, but the host name does not determine the model identity.
- Before analysis, verify and record the actual DeepSeek model identifier exposed by the API or host. When available, also record the backend fingerprint. Do not label a run as DeepSeek if the host silently falls back to an Anthropic Claude or OpenAI model.
- Prefer the most capable DeepSeek model available at execution time for the lead and all specialists. If different DeepSeek models are used for cost or capacity reasons, record the assignment as a protocol deviation.
- Use an agent host with isolated subagent contexts to run the four specialists. A role played sequentially in the lead agent's context is not an independent specialist.
- Build and freeze the shared source pack before launching any specialist. Pass the identical frozen pack to every subagent.
- Give each subagent only the fixed questionnaire, frozen source pack, cutoff, target date, resident definition, report contract, and its own role contract. Do not expose other specialists' drafts or conclusions.
- Have subagents return their complete first-draft reports to the lead agent. The lead agent must write the four final report files sequentially; do not let subagents concurrently edit the same output bundle.
- Launch as many specialists concurrently as the environment safely supports and queue the rest without changing their prompts or source pack.
- If isolated subagent contexts are unavailable, stop before specialist analysis and require four separate DeepSeek API requests or chat sessions followed by a fifth synthesis session. Do not simulate independence in one context.
- Do not claim fixed weights or model-version continuity. Each annual run must record the exact model identifier and configuration available at that time.

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

Use four isolated DeepSeek specialist runs. Give every specialist the fixed questionnaire, shared source pack, cutoff, target date, resident definition, report contract, and its role contract.

- Do not let specialists read one another’s drafts.
- Do not ask one specialist to summarize another.
- Require a full report, not a probability table or memo.
- Require 2,500–5,000 Chinese characters per specialist report unless the user requests another length.
- Require inline links beside key factual claims.
- Permit at most four additional role-specific sources, all published by the cutoff.
- Preserve the first draft. Do not overwrite it after discussion.
- If concurrency is limited, start the available specialists and launch the remaining specialists after a slot opens with the unchanged source pack. Do not reveal prior reports.

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
python3 <skill-directory>/scripts/validate_forecast_bundle.py <bundle-directory>
```

Resolve `<skill-directory>` to this installed skill's absolute path before running the command. Fix every reported error before delivery. Compute SHA-256 hashes after final validation. Verify the hashes once, then provide links or absolute paths to all four specialist reports and the synthesis.

## Non-negotiable quality rules

- Do not reduce a specialist report to bullet conclusions.
- Do not use event probabilities as the main content.
- Do not name a few fashionable industries in the permanent questionnaire; let each annual run identify relevant sectors from that year’s evidence.
- Do not predict annual fluctuations unless the user explicitly expands the protocol.
- Do not hide uncertainty behind vague language. Give a concrete target-date end state and a way to verify it.
- Do not present private chain-of-thought. Present concise reasons, evidence, mechanisms, counterarguments, and assumptions.
- Do not provide personalized investment, property-purchase, or career instructions unless separately requested.
