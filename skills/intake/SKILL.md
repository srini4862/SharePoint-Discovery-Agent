---
name: intake
description: Operational guidance for SharePoint discovery intake, execution readiness validation, authentication assessment, and discovery scope collection.
license: Proprietary

metadata:
  author: wfx-org
  version: "2.0"

intent:
  - sharepoint discovery intake
  - discovery readiness assessment
  - authentication readiness validation
  - execution readiness validation
  - discovery scope collection

tags:
  - sharepoint
  - discovery
  - intake
  - authentication
  - readiness
  - execution
  - enterprise
---

# SharePoint Discovery Intake Guidance

## Purpose

This skill provides operational guidance for collecting discovery readiness information required to safely and successfully execute SharePoint discovery operations.

The intake agent uses this knowledge to reason about what is operationally
required to enable successful discovery execution — not to complete a
static questionnaire. Intake behavior should be adaptive, execution-oriented,
and driven by what is actually needed to proceed safely and successfully.

---

# Operational Objective Reasoning

The intake agent should reason backward from the user's operational objective to determine what information is required for successful execution.

The intake process should:
- understand the intended discovery outcome
- determine what execution requirements exist
- collect only information relevant to execution readiness
- avoid unnecessary onboarding or overcollection

Example:

If the user requests:
- SharePoint site count

The likely required intake areas may include:
- authentication method
- tenant access readiness
- permission validation
- execution environment

Additional intake questions should only be asked when operationally necessary.

---

# Discovery Intake Areas

Depending on the user's objective and discovery scope, intake information may include:

- tenant name
- tenant ID
- SharePoint Online or On-Premises scope
- discovery objectives
- discovery boundaries and scope
- authentication approach
- permission availability
- operational constraints
- compliance requirements
- reporting expectations

The intake agent should collect only information relevant to the intended discovery scenario.

---

# Discovery Scope Examples

## Tenant-Wide Discovery

Typically requires:
- tenant-level access
- broader permission validation
- storage and permissions analysis readiness
- tenant scope clarification

## Site-Level Discovery

Typically requires:
- targeted site scope
- site-level access validation
- reduced discovery scope clarification

## OneDrive Discovery

May require:
- OneDrive administrative permissions
- user inventory scope clarification
- storage analysis readiness

## Permission and Access Discovery

May require:
- administrative permission validation
- delegated access verification
- access scope clarification

---

# Authentication Guidance

## Supported Authentication Approaches

Supported delegated authentication approaches may include:
- interactive delegated authentication
- delegated app registration authentication
- PnP.PowerShell delegated authentication flows

The intake agent should first understand the user's preferred authentication approach before requesting authentication-related information.

Authentication-related questioning should dynamically adapt based on:
- selected authentication approach
- discovery scope
- environment restrictions
- operational readiness requirements

---

## Authentication Rules

- Use only approved delegated authentication approaches
- Do not use Graph-based authentication for discovery operations
- Do not request unnecessary authentication details
- Request Client ID only when required for the selected authentication approach
- Validate authentication readiness before intake completion

---

# Permission Readiness Validation

The intake agent should validate whether sufficient permissions likely exist for the requested discovery scope.

Examples may include:
- SharePoint Administrator access
- Site Collection Administrator access
- delegated discovery permissions
- approved app registration access

Where permissions appear insufficient or uncertain, the intake agent should identify the issue as a potential execution blocker.

---

# Environment Considerations

The intake agent should determine whether discovery is operating within:
- Dell-managed environments
- customer-managed environments
- restricted enterprise environments
- compliance-controlled environments

Environment conditions may influence:
- authentication requirements
- execution methods
- operational constraints
- approval requirements

---

# Execution Readiness Principles

Execution readiness may be considered sufficient when:
- discovery objectives are understood
- authentication readiness exists
- required permissions likely exist
- critical blockers are identified
- sufficient operational context exists
- downstream execution can proceed safely

The intake agent should optimize for:
- minimal required questioning
- operational efficiency
- execution enablement
- reduced user friction

---

# Blocker Identification Guidance

Potential blockers may include:
- insufficient permissions
- unsupported authentication approaches
- incomplete discovery scope
- restricted customer environments
- missing tenant access
- missing delegated consent
- unavailable authentication configuration
- compliance restrictions
- incomplete operational context

The intake agent should clearly identify blockers requiring clarification or escalation before intake completion.

---

# Intake Completion Criteria

Intake may be considered complete when:
- sufficient execution readiness context exists
- authentication readiness is validated
- critical blockers are identified
- required operational context exists
- user confirmation has been received

---

# Intake Best Practices

- minimize unnecessary questioning
- prefer adaptive questioning over static forms
- reuse existing context whenever possible
- avoid duplicate information collection
- prioritize execution readiness
- maintain concise and professional interactions
- validate information before progression
- identify blockers early
- optimize for downstream execution success