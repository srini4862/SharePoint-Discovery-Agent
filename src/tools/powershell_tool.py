"""PowerShell tool for DeepAgents framework with session management."""

from langchain_core.tools import tool
import subprocess
import json


class PowerShellSession:
    """PowerShell session manager for maintaining authenticated session."""

    def __init__(self):
        """Initialize PowerShell session."""
        self.session = None
        self.authenticated = False

    def authenticate(self, tenant_id: str, client_id: str):
        """Authenticate PowerShell session with credentials."""
        # Authentication will be handled by scripts directly
        self.authenticated = True
        self.tenant_id = tenant_id
        self.client_id = client_id


# Global PowerShell session
_powershell_session = PowerShellSession()


@tool
def powershell_execute(script_path: str, parameters: dict) -> str:
    """
    Execute PowerShell script with optional parameters.

    Maintains a single authenticated session for all script executions.

    Args:
        script_path: Path to PowerShell script
        parameters: Optional script parameters

    Returns:
        Script output as JSON string
    """
    if parameters is None:
        parameters = {}

    try:
        from pathlib import Path
        script_path_obj = Path(script_path)
        if not script_path_obj.is_absolute():
            # Resolve relative to project root (powershell_tool.py is in src/tools)
            project_root = Path(__file__).parent.parent.parent
            script_path_obj = project_root / script_path
            
        script_path_str = str(script_path_obj.resolve())
        if not script_path_obj.exists():
            return json.dumps({"error": f"Script not found at path: {script_path_str}", "success": False})

        # Build PowerShell command with authentication context
        ps_command = f"& '{script_path_str}'"
        for key, value in parameters.items():
            ps_command += f" -{key} '{value}'"

        # Add authentication parameters if session is authenticated
        if _powershell_session.authenticated:
            if _powershell_session.tenant_id:
                ps_command += f" -TenantId '{_powershell_session.tenant_id}'"
            if _powershell_session.client_id:
                ps_command += f" -ClientId '{_powershell_session.client_id}'"

        # Execute PowerShell command (using pwsh - PowerShell Core)
        result = subprocess.run(
            ["pwsh", "-Command", ps_command],
            capture_output=True,
            text=True,
            timeout=300,
        )

        if result.returncode != 0:
            return json.dumps({"error": result.stderr, "success": False})

        return json.dumps({"output": result.stdout, "success": True})

    except Exception as e:
        return json.dumps({"error": str(e), "success": False})


@tool
def powershell_authenticate(tenant_id: str, client_id: str) -> str:
    """
    Authenticate PowerShell session with credentials.

    Args:
        tenant_id: Azure AD tenant ID
        client_id: Azure AD client ID

    Returns:
        Authentication result
    """
    try:
        _powershell_session.authenticate(tenant_id, client_id)
        return json.dumps({"success": True, "message": "PowerShell session authenticated"})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})
