"""PowerShell tool for DeepAgents framework with persistent session management."""

from langchain_core.tools import tool
from pathlib import Path
import subprocess
import json
import uuid
import threading
import queue


class PowerShellSession:
    """PowerShell session manager for maintaining persistent authenticated session."""

    def __init__(self):
        """Initialize PowerShell session."""
        self.process = None
        self.authenticated = False
        self.tenant_name = None
        self.tenant_id = None
        self.client_id = None
        self._lock = threading.Lock()

    def _start(self):
        if self.process is None or self.process.poll() is not None:
            # Start pwsh in NoExit mode
            self.process = subprocess.Popen(
                ["pwsh", "-NoProfile", "-NoExit", "-Command", "-"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(
                    subprocess, 'CREATE_NO_WINDOW') else 0
            )

    def execute_command(self, command: str, timeout: int = 300) -> dict:
        """Executes a command in the persistent session and returns the output."""
        with self._lock:
            self._start()
            proc = self.process
            if proc is None:
                return {"success": False, "error": "PowerShell process failed to initialize."}

            marker = str(uuid.uuid4())
            # Wrap command in try/catch to capture output and exit code correctly
            full_command = f"""
$ErrorActionPreference = 'Stop'
try {{
    {command}
    $__exitCode = $LASTEXITCODE
    if ($null -eq $__exitCode) {{ $__exitCode = 0 }}
}} catch {{
    Write-Error $_
    $__exitCode = 1
}} finally {{
    Write-Output '{marker}_END_OUT'
    [Console]::Error.WriteLine('{marker}_END_ERR')
    Write-Output "{marker}_EXITCODE:$__exitCode"
}}
"""
            # Write to process
            proc.stdin.write(full_command + "\n")
            proc.stdin.flush()

            stdout_lines = []
            stderr_lines = []
            exit_code = 1

            # We need to read until we hit the markers
            def reader(pipe, q, marker_str):
                for line in iter(pipe.readline, ''):
                    if marker_str in line:
                        break
                    q.put(line)

            stdout_q = queue.Queue()
            stderr_q = queue.Queue()

            t_out = threading.Thread(target=reader, args=(
                proc.stdout, stdout_q, f"{marker}_END_OUT"))
            t_err = threading.Thread(target=reader, args=(
                proc.stderr, stderr_q, f"{marker}_END_ERR"))

            t_out.start()
            t_err.start()

            t_out.join(timeout=timeout)
            t_err.join(timeout=timeout)

            if t_out.is_alive() or t_err.is_alive():
                # Timeout occurred, restart process to recover state
                proc.kill()
                self.process = None
                return {"success": False, "error": "Command execution timed out."}

            while not stdout_q.empty():
                stdout_lines.append(stdout_q.get().strip('\n'))

            while not stderr_q.empty():
                stderr_lines.append(stderr_q.get().strip('\n'))

            # Read the exit code line
            exit_code_line = proc.stdout.readline().strip()
            if exit_code_line.startswith(f"{marker}_EXITCODE:"):
                try:
                    exit_code = int(exit_code_line.split(":")[1])
                except ValueError:
                    pass

            has_error = exit_code != 0 or len(stderr_lines) > 0
            return {
                "success": not has_error,
                "output": "\n".join(stdout_lines),
                "error": "\n".join(stderr_lines),
                "exit_code": exit_code
            }

    def authenticate(self, tenant_name: str, tenant_id: str, client_id: str):
        """Authenticate PowerShell session with credentials."""
        self.tenant_name = tenant_name
        self.tenant_id = tenant_id
        self.client_id = client_id

        admin_url = f"https://{tenant_name}-admin.sharepoint.com"
        command = f"Connect-PnPOnline -Url '{admin_url}' -Tenant '{tenant_id}' -ClientId '{client_id}' -Interactive"

        res = self.execute_command(command, timeout=300)
        if res["success"]:
            self.authenticated = True
            return res
        else:
            raise Exception(f"Authentication failed: {res['error']}")


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
        script_path_obj = Path(script_path)
        if not script_path_obj.is_absolute():
            # Resolve relative to project root
            project_root = Path(__file__).parent.parent.parent
            script_path_obj = project_root / script_path

        script_path_str = str(script_path_obj.resolve())
        if not script_path_obj.exists():
            return json.dumps({"error": f"Script not found at path: {script_path_str}", "success": False})

        # Build PowerShell command to invoke script with parameters
        ps_command = f"& '{script_path_str}'"
        for key, value in parameters.items():
            ps_command += f" -{key} '{value}'"

        # Execute inside persistent session
        result = _powershell_session.execute_command(ps_command)

        if not result["success"]:
            return json.dumps({"error": result["error"], "success": False})

        return json.dumps({"output": result["output"], "success": True})

    except Exception as e:
        return json.dumps({"error": str(e), "success": False})


@tool
def powershell_authenticate(tenant_name: str, tenant_id: str, client_id: str) -> str:
    """
    Authenticate PowerShell session with credentials.

    Args:
        tenant_name: SharePoint Tenant Name (e.g. contoso)
        tenant_id: Azure AD tenant ID
        client_id: Azure AD client ID

    Returns:
        Authentication result
    """
    try:
        _powershell_session.authenticate(tenant_name, tenant_id, client_id)
        return json.dumps({"success": True, "message": "PowerShell session authenticated"})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})
