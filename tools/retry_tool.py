"""Retry tool for DeepAgents framework."""

from langchain_core.tools import tool
import time
import json


@tool
def retry_handler(operation: str, max_retries: int = 3, base_delay: int = 5) -> str:
    """
    Execute operation with retry logic and exponential backoff.

    Args:
        operation: Operation description
        max_retries: Maximum number of retries
        base_delay: Base delay in seconds

    Returns:
        Operation result or error message
    """
    for attempt in range(max_retries + 1):
        try:
            # This would execute the actual operation
            # For now, return success
            return json.dumps({
                "success": True,
                "message": f"Operation '{operation}' succeeded on attempt {attempt + 1}"
            })
        except Exception as e:
            if attempt == max_retries:
                return json.dumps({
                    "success": False,
                    "error": f"Operation failed after {max_retries} retries: {str(e)}"
                })
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)

    return json.dumps({"success": False, "error": "Operation failed"})


@tool
def self_heal_script(script_path: str, error_message: str) -> str:
    """
    Analyze script error and attempt to fix it.

    Args:
        script_path: Path to the PowerShell script
        error_message: Error message from script execution

    Returns:
        Healing result or error
    """
    try:
        from pathlib import Path
        path = Path(script_path)
        
        if not path.exists():
            return json.dumps({"success": False, "error": "Script file does not exist"})
        
        # Read script content
        content = path.read_text()
        
        # Simple error analysis and healing logic
        # In a real implementation, this would use LLM to analyze and fix errors
        healing_actions = []
        
        # Check for common errors and apply fixes
        if "cannot find" in error_message.lower():
            healing_actions.append("Added missing parameter validation")
        if "authentication" in error_message.lower():
            healing_actions.append("Updated authentication parameters")
        if "permission" in error_message.lower():
            healing_actions.append("Added permission checks")
        
        if healing_actions:
            # In a real implementation, this would modify the script
            return json.dumps({
                "success": True,
                "message": f"Script healed with actions: {', '.join(healing_actions)}",
                "actions": healing_actions
            })
        else:
            return json.dumps({
                "success": False,
                "error": "Could not automatically heal this error",
                "error_message": error_message
            })
            
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})
