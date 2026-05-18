# Intake Skill

## Description
This skill enables question-based intake for gathering comprehensive discovery requirements and authentication context.

## Capabilities

### 1. Interactive Requirement Gathering
Collects all necessary information from the user required before discovery planning can begin.

**Inputs:**
- None (Interactive chat flow)

**Outputs:**
- Tenant information (Tenant Name, Azure AD Tenant ID)
- Authentication details (PnP.PowerShell Client ID; specify ONLY user delegated authentication, NO Graph-based authentication)
- Environment details & Discovery scope
- Permission availability
- Compliance requirements & Reporting expectations

### 2. State Management
**Outputs:**
- Returns all gathered information as structured Markdown to the Supervisor Agent. This ensures the data is persisted in the workflow state for reuse by the Planning and Execution agents.

## Notes
- Ask clear, concise, step-by-step questions.
- Validate responses before proceeding to the next question.
- Avoid repeatedly asking for credentials once they have been provided.
