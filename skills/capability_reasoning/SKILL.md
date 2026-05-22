# Capability Reasoning Skill

## Purpose
Map user intent to discrete discovery capabilities, infer execution requirements, and determine operational dependencies.

## Operational Knowledge
- SharePoint discovery operations are defined as **Capabilities**.
- Capabilities are declared in YAML files located in `src/capabilities/`.
- Each capability defines its required inputs, authentication methods, scripts, and expected artifacts.

## Reasoning Guidelines
1. **Analyze Intent:** Determine what the user wants to know (e.g., "who owns my sites?" -> `permissions_inventory`).
2. **Read Declarations:** Parse the YAML definitions to understand what the capability requires.
3. **Map Requirements:** Check if the required inputs (tenant_id, scope) have been gathered by the intake agent.
4. **Identify Artifacts:** Note what JSON/CSV artifacts the execution agent will produce for this capability.
5. **Surface Gaps:** If a required capability needs inputs not currently in context, state the missing inputs clearly.

## Execution Rules
- Do NOT plan migration batches or sequences.
- Do NOT execute scripts.
- ONLY output the mapping of intent -> capability -> requirements.
