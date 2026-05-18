# Installation Skill

## Description
This skill enables prerequisite installation and authentication configuration with verification steps.

## Capabilities

### Prerequisite Verification
Verifies all prerequisites before installation.

**Parameters:**
- None

**Output:**
- Verification results for PowerShell version
- Network connectivity status
- Permission validation
- Module availability

### Module Installation
Installs required PowerShell modules.

**Parameters:**
- module_name: Name of module to install (e.g., PnP.PowerShell)
- force: Force reinstall flag

**Output:**
- Installation result
- Module version
- Installation status

### Authentication Configuration
Configures authentication for Microsoft 365.

**Parameters:**
- tenant_id: Azure AD tenant ID
- client_id: Azure AD client ID
- auth_model: Authentication model (certificate, secret, interactive)

**Output:**
- Authentication configuration result
- Connection status

## Tool Dependencies
- powershell_execute: For running existing PowerShell scripts
- powershell_authenticate: For authenticating PowerShell session
- file_read: For reading configuration
- retry_handler: For retrying transient errors
- self_heal_script: For analyzing and fixing script failures
- file_write: For saving healed scripts

## Examples
To verify prerequisites using the existing script:
```python
result = await tools.powershell_execute(
    script_path="scripts/setup/verify_prerequisites.ps1"
)
```

To install PnP.PowerShell using the existing script:
```python
result = await tools.powershell_execute(
    script_path="scripts/setup/install_pnp.ps1",
    parameters={"force": true}
)
```

## Notes
- Performs verification before installation
- Reuses authentication context from intake phase
- Validates installation success
- Uses PnP.PowerShell only (no Microsoft Graph)
- MUST use existing scripts first. If they fail due to outdated documentation or environment issues, use `self_heal_script` to analyze and apply fixes.
