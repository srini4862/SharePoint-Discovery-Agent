# Readiness Skill

## Purpose
Validate environment dependencies, establish authentication, and determine execution feasibility.

## Operational Knowledge
- Readiness must be validated before execution begins.
- Two primary setup scripts exist: `verify_prerequisites.ps1` and `install_pnp.ps1`.
- Authentication uses `powershell_authenticate`.

## Reasoning Guidelines
1. **Dependency Check:** Determine if PnP.PowerShell is installed and available.
2. **Authentication Check:** Determine if an active, authenticated session exists.
3. **Feasibility Check:** Verify if the selected execution mode (platform-managed vs customer-managed) is viable.
4. **Autonomous Recovery:** If prerequisites fail, attempt installation. If authentication fails, report the error.

## Execution Rules
- ONLY use the validated intake context for credentials. Do NOT ask the user for them.
- Do NOT execute discovery scripts. That is the execution agent's job.
- Only declare readiness when all dependencies and authentication requirements for the planned capabilities are met.
