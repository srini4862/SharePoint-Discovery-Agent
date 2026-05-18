# Reporting Skill

## Description
This skill enables report generation using Dell-approved formats for client showcasing.

## Capabilities

### Executive Summary Generation
Generates executive summary for leadership.

**Parameters:**
- discovery_data: Complete discovery data (JSON outputs from execution)
- workflow_id: Workflow identifier

**Output:**
- Executive summary markdown
- Key findings
- Recommendations

### Technical Findings Generation
Generates technical findings report for IT teams.

**Parameters:**
- discovery_data: Complete discovery data (JSON outputs from execution)
- workflow_id: Workflow identifier

**Output:**
- Technical findings markdown
- Environment overview
- Detailed analysis

### Migration Readiness Assessment
Generates migration readiness assessment.

**Parameters:**
- discovery_data: Complete discovery data (JSON outputs from execution)
- workflow_id: Workflow identifier

**Output:**
- Readiness assessment markdown
- Readiness score
- Gap analysis

### Recommendations Generation
Generates actionable recommendations.

**Parameters:**
- discovery_data: Complete discovery data (JSON outputs from execution)
- workflow_id: Workflow identifier

**Output:**
- Recommendations markdown
- Pre-migration recommendations
- Migration strategy recommendations

## Tool Dependencies
- file_read: For reading JSON discovery outputs from execution
- file_write: For writing Dell-approved report formats

## Examples
```python
# Generate executive summary
executive_summary = await skills.generate_executive_summary(discovery_data, workflow_id)
```

## Notes
- Reads JSON outputs from execution phase
- Generates Dell-approved report formats
- Reports are formatted for client showcasing
- Includes executive summaries and technical findings
- Part of Reporting subagent workflow
