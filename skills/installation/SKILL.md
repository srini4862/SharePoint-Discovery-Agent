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
- powershell_execute: For running PowerShell commands
- powershell_authenticate: For authenticating PowerShell session
- file_write: For writing installation logs
- file_read: For reading configuration

## Examples
```python
# Verify prerequisites
verification = await skills.verify_prerequisites()

# Install PnP.PowerShell
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
