# Discovery Skill

## Description
This skill enables SharePoint and OneDrive discovery operations for migration assessment.

## Capabilities

### Site Inventory Discovery
Collects comprehensive inventory of all SharePoint sites in the tenant.

**Parameters:**
- tenant_id: Azure AD tenant ID
- client_id: Azure AD client ID

**Output:**
- JSON file with site inventory including URL, title, template, owner, storage usage

### User Inventory Discovery
Collects inventory of all Microsoft 365 users.

**Parameters:**
- tenant_id: Azure AD tenant ID

**Output:**
- JSON file with user inventory including user principal name, email, account status

### Storage Analysis
Analyzes storage usage across SharePoint sites and OneDrive.

**Parameters:**
- tenant_id: Azure AD tenant ID

**Output:**
- JSON file with storage usage statistics and projections

## Tool Dependencies
- powershell_execute: For running PnP.PowerShell commands
- file_write: For writing discovery outputs to JSON files
- file_read: For reading discovery outputs

## Examples
```python
# Execute site inventory
result = await tools.powershell_execute(
    script_path="scripts/discovery/site_inventory.ps1",
    parameters={"tenant_id": "xxx", "client_id": "yyy"}
)
```

## Notes
- All discovery scripts use PnP.PowerShell
- Outputs are stored in JSON format in the outputs directory
- Scripts are read-only and non-destructive
