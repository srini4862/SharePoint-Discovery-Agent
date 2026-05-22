<#
.SYNOPSIS
    Customizations and SPFx Inventory Discovery Script

.DESCRIPTION
    Collects inventory of SharePoint Framework (SPFx) solutions and legacy add-ins across the tenant using PnP.PowerShell.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\customizations_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$TenantId,
    
    [Parameter(Mandatory=$true)]
    [string]$ClientId
)

$ErrorActionPreference = "Stop"

try {
    # Import PnP.PowerShell module
    Import-Module PnP.PowerShell -ErrorAction Stop

    # Connect to SharePoint Online App Catalog (Tenant level)
    # The App Catalog URL typically follows the pattern https://tenant-admin.sharepoint.com (or specifically the app catalog site)
    # Connect-PnPOnline -Url "https://$TenantId.sharepoint.com/sites/appcatalog" -ClientId $ClientId -Interactive -ErrorAction Stop
    # We will connect to Admin first, then try to get the App Catalog URL
    Connect-PnPOnline -Url "https://$TenantId-admin.sharepoint.com" -ClientId $ClientId -Interactive -ErrorAction Stop
    
    $inventory = @{
        apps = @()
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        tenant_id = $TenantId
    }

    try {
        # Note: Get-PnPTenantApp requires connecting to the admin center or app catalog.
        $apps = Get-PnPTenantApp -ErrorAction Stop

        foreach ($app in $apps) {
            $inventory.apps += @{
                id = $app.Id
                title = $app.Title
                deployed = $app.Deployed
                app_catalog_version = $app.AppCatalogVersion
                installed_version = $app.InstalledVersion
                is_client_side_solution = $app.IsClientSideSolution
            }
        }
    } catch {
        $inventory.error = "Failed to access App Catalog or Apps: $_"
    }

    # Output as JSON
    $inventory | ConvertTo-Json -Depth 10

} catch {
    $errorResult = @{
        error = $_.Exception.Message
        success = $false
    }
    $errorResult | ConvertTo-Json -Depth 10
    exit 1
}
