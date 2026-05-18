# Intake Skill

## Description
This skill enables question-based intake for gathering discovery requirements and authentication credentials.

## Capabilities

### Requirement Gathering
Collects comprehensive discovery requirements from the user.

**Parameters:**
- None (interactive)

**Output:**
- Intake data including tenant name, tenant ID, client ID
- Discovery scope

**Parameters:**
- tenant_name: Tenant name
- tenant_id: Azure AD tenant ID
- client_id: Azure AD client ID

**Output:**
- Saved credentials in memory for use in later phases

## Notes
- Asks one question at a time
- Validates responses before proceeding
- Saves credentials in memory for reuse in later phases
- Avoids repeatedly asking for credentials
