# Assessment Skill

## Description
This skill enables migration readiness assessment and evaluation based on discovery data.

## Capabilities

### Migration Readiness Calculation
Calculates overall migration readiness score based on discovery data.

**Parameters:**
- discovery_data: Complete discovery data from execution phase

**Output:**
- Readiness score (0-100)
- Category scores (infrastructure, data, security, users)
- Readiness level (Ready, Mostly Ready, Partially Ready, Not Ready)

### Risk Identification
Identifies potential migration risks from discovery data.

**Parameters:**
- discovery_data: Complete discovery data from execution phase

**Output:**
- List of identified risks with severity levels
- Risk categories (high, medium, low)
- Mitigation recommendations

### Migration Timeline Estimation
Generates migration timeline estimate based on data volume.

**Parameters:**
- discovery_data: Complete discovery data from execution phase

**Output:**
- Estimated duration in days
- Phase breakdown
- Milestones

## Tool Dependencies
- file_read: For reading JSON discovery outputs
- file_write: For writing assessment reports

## Examples
```python
# Calculate readiness
readiness_score = await skills.calculate_readiness_score(discovery_data)
```

## Notes
- Assessment is performed on JSON outputs from execution phase
- Part of Reporting subagent workflow
- Generates Dell-approved assessment formats
