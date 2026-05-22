# Artifact Analysis Skill

## Purpose
Read raw discovery artifacts, validate their completeness, and extract operational findings.

## Operational Knowledge
- Discovery artifacts are JSON or CSV files stored in `artifacts/`.
- The `artifact_read` and `artifact_list` tools are used to access them.
- Artifacts may contain anomalies, missing fields, or large datasets requiring summarization.

## Reasoning Guidelines
1. **Validate Structure:** Check if the expected fields are present in the artifact.
2. **Extract Findings:** Identify key metrics (e.g., total sites, total storage, number of users).
3. **Identify Outliers:** Surface anomalies (e.g., sites with 0 quota, users without email addresses).
4. **Synthesize Insights:** Transform raw data rows into operational intelligence.

## Execution Rules
- Do NOT fabricate data. If a field is empty, report it as empty.
- Do NOT generate the final executive report. Focus on analyzing the evidence.
- Produce a structured summary of findings that the reporting agent can use to draft the final deliverable.
