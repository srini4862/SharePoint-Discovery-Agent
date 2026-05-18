"""File tool for DeepAgents framework."""

from langchain_core.tools import tool
import json
from pathlib import Path


@tool
def file_write(content: str, file_path: str) -> str:
    """
    Write content to a file.

    Args:
        content: Content to write
        file_path: Path to the file

    Returns:
        Success message or error
    """
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return json.dumps({"success": True, "message": f"Successfully wrote to {file_path}"})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})


@tool
def file_read(file_path: str) -> str:
    """
    Read content from a file.

    Args:
        file_path: Path to the file

    Returns:
        File content or error message
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return json.dumps({"success": False, "error": "File does not exist"})
        content = path.read_text()
        return json.dumps({"success": True, "content": content})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})
