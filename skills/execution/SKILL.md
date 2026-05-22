# Execution Skill

## Purpose
Execute discovery operations, coordinate runtime execution, handle failures, and collect artifacts.

## Operational Knowledge
- Execution relies on the established, authenticated session from the Readiness Agent.
- Discovery scripts are located in `scripts/discovery/`.
- Execution can fail due to throttling, permissions, or network drops.

## Reasoning Guidelines
1. **Pre-Flight Check:** Verify that readiness has been declared and required context is available.
2. **Execution:** Run the specific scripts identified by the Capability Reasoning Agent using `powershell_execute`.
3. **Failure Handling:** Differentiate between transient errors (use `retry_handler`) and structural errors (use `self_heal_script` or escalate).
4. **Artifact Collection:** Capture the JSON output from the scripts. Use `artifact_save` to persist the data to the `artifacts/` directory.

## Execution Rules
- Do NOT authenticate the session. Assume it is ready.
- Do NOT analyze the data. Save it as an artifact and let the Artifact Analysis Agent handle it.
- Never fabricate execution results.
