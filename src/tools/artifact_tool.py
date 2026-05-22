"""Artifact management tool for DeepAgents framework."""

from langchain_core.tools import tool
import json
import os
from datetime import datetime

# Determine project root based on package structure
_project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_artifacts_dir = os.path.join(_project_root, "artifacts")

# Ensure artifacts directory exists
os.makedirs(_artifacts_dir, exist_ok=True)

@tool
def artifact_save(name: str, content: str, artifact_type: str = "json") -> str:
    """
    Saves an operational artifact (JSON, CSV, or text) to the artifacts directory.
    
    Args:
        name: Name of the artifact file (e.g., 'site_inventory.json')
        content: The string content to save
        artifact_type: Type of artifact ('json', 'csv', 'log', 'analysis')
        
    Returns:
        Result message including the path where it was saved.
    """
    try:
        # Sanitize filename
        safe_name = os.path.basename(name)
        file_path = os.path.join(_artifacts_dir, safe_name)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return json.dumps({
            "success": True, 
            "message": f"Artifact saved successfully to {file_path}",
            "path": file_path,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})

@tool
def artifact_read(name: str) -> str:
    """
    Reads an artifact from the artifacts directory.
    
    Args:
        name: Name of the artifact file
        
    Returns:
        The content of the artifact or an error message.
    """
    try:
        safe_name = os.path.basename(name)
        file_path = os.path.join(_artifacts_dir, safe_name)
        
        if not os.path.exists(file_path):
            return json.dumps({"success": False, "error": f"Artifact {safe_name} not found"})
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        return json.dumps({"success": True, "content": content})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})

@tool
def artifact_list() -> str:
    """
    Lists all artifacts available in the artifacts directory.
    
    Returns:
        JSON list of artifact files and their sizes.
    """
    try:
        artifacts = []
        for filename in os.listdir(_artifacts_dir):
            file_path = os.path.join(_artifacts_dir, filename)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                artifacts.append({"name": filename, "size_bytes": size})
                
        return json.dumps({"success": True, "artifacts": artifacts})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})
