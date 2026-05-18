# Execution Skill

## Description
This skill enables script execution and autonomous discovery with self-healing capabilities.

## Capabilities

### Script Execution
Executes PowerShell discovery scripts.

**Parameters:**
- script_path: Path to PowerShell script
- parameters: Script parameters
- auth_context: Authentication context

**Output:**
- Script execution result
- Output file path
- Execution details

### Output Validation
Validates discovery script outputs.

**Parameters:**
- output_path: Path to output file

**Output:**
- Validation result (valid/invalid)
- Validation message

### Self-Healing
Analyzes script errors and attempts to fix them automatically.

**Parameters:**
- script_path: Path to PowerShell script
- error_message: Error from script execution

**Output:**
- Healing actions taken
- Fixed script content
- Retry recommendation

### Non-Destructive Validation
Validates that scripts are non-destructive.

**Parameters:**
- script_path: Path to PowerShell script

**Output:**
- Validation result (safe/unsafe)
- Validation message

## Tool Dependencies
- powershell_execute: For running PowerShell scripts
- powershell_authenticate: For authenticating PowerShell session
- file_write: For writing outputs to JSON files
- file_read: For reading outputs
- retry_handler: For retry logic
- self_heal_script: For automatic error fixing

## Examples
```python
# Execute script with self-healing
result = await skills.execute_script(script_path, parameters, auth_context)
if not result["success"]:
    healed = await skills.self_heal_script(script_path, result["error"])
```

## Notes
- Maintains single authenticated PowerShell session
- Self-heals failed scripts by analyzing errors
- Outputs are stored in JSON format
- All scripts are validated as non-destructive before execution
- Retry logic with exponential backoff
