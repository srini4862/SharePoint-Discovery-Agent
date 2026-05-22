---
name: reporting
description: Operational knowledge for SharePoint discovery report generation, audience-aware synthesis, and Dell-standard assessment delivery.
license: Proprietary

metadata:
  author: wfx-org
  version: "2.0"

intent:
  - report generation
  - executive summary synthesis
  - technical findings presentation
  - risk communication
  - migration readiness assessment

tags:
  - sharepoint
  - reporting
  - assessment
  - executive-summary
  - dell-standards
  - migration
---

# SharePoint Discovery Reporting Knowledge

## Purpose

This skill provides operational knowledge for reasoning about SharePoint
discovery report generation — what to include, how to structure it for
different audiences, what quality looks like, and how to handle data gaps.

The reporting agent uses this knowledge to apply professional judgment
to report synthesis, not to mechanically format data into a fixed template.

---

# Audience-Aware Reasoning

A complete assessment package addresses two distinct audiences with
different information needs. The reporting agent should reason about
what each audience needs to make decisions:

**Executive Audience**
Executives need to understand the strategic picture: what was discovered,
what it means for the migration, what the key risks are, and what
decisions or approvals are needed. They do not need granular technical detail.

An effective executive summary:
- Communicates the discovery scope and methodology briefly
- States the migration readiness conclusion clearly upfront
- Highlights the 2-4 most significant risks or considerations
- Articulates recommended next steps without requiring technical context
- Uses business language, not technical jargon

**Technical Audience**
IT teams need actionable detail: specific findings, environment characteristics,
data volumes, permission structures, and risk specifics they can act on.

Effective technical findings:
- Document environment characteristics systematically
- Provide specific data (site counts, storage volumes, user counts)
- Identify specific risks with technical root cause and impact
- Surface actionable remediation recommendations
- Use precise technical language

The reporting agent should calibrate the depth and language of each section
to its intended audience.

---

# Report Composition Reasoning

A complete assessment report typically includes the following sections.
The reporting agent should reason about the appropriate depth for each
section based on what the discovery data actually reveals:

**Executive Summary**
What was the scope of discovery? What is the overall migration readiness
conclusion? What are the most important things leadership needs to know?
Keep this concise — 1-2 paragraphs maximum.

**Technical Findings**
What did the discovery data reveal about the environment? Include site
inventory characteristics, storage consumption analysis, user landscape,
and any notable environment characteristics that affect migration planning.
Support findings with specific numbers from the discovery outputs.

**Risk Summary**
What risks were identified, and how severe are they? Categorize risks
(High / Medium / Low) and explain the operational impact of each.
Risks should be grounded in the discovery data, not generic migration risks.

**Migration Readiness Assessment**
Based on the findings, what is the overall migration readiness level?
What specific factors support this assessment? What gaps or remediation
items exist before migration can proceed safely?

**Recommendations**
What specific, actionable steps should be taken before and during migration?
Recommendations should follow logically from the findings and risk summary.
Prioritize recommendations by impact and urgency.

---

# Data Quality and Gap Handling

The reporting agent should reason about the quality and completeness of
the discovery data before synthesizing findings:

- Are all expected discovery outputs present and valid?
- Are there gaps in the data (missing scripts, empty outputs, partial data)?
- Do the data volumes and characteristics appear consistent with the
  described environment scope?

When data gaps exist, the reporting agent should surface them explicitly
in the report rather than working around them with assumptions. A finding
that says "storage data was unavailable due to X" is more valuable than
a fabricated estimate.

Never fabricate statistics, findings, or risk ratings. Report what the
data shows, and clearly note where data is absent or inconclusive.

---

# Dell Reporting Standards

Reports are delivered using Dell Technologies enterprise standards:
- Professional, authoritative tone consistent with client-facing delivery
- Structured Markdown with clear hierarchical headings
- Factual, precise language — avoid hedging or ambiguity where clarity is possible
- Clear distinction between findings (what was observed) and recommendations
  (what should be done about it)
- Reports must be saved to disk using `file_write` as part of delivery —
  this is a delivery responsibility, not optional

The report should be suitable for direct client presentation without
requiring further editing by the delivery team.

