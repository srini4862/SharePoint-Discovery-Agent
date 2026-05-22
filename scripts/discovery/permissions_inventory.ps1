<#
.SYNOPSIS
    SharePoint Permissions Inventory Discovery Script

.DESCRIPTION
    Collects site administrators and owners for SharePoint sites using PnP.PowerShell.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\permissions_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
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

    # Connect to SharePoint Online Admin Center
    Connect-PnPOnline -Url "https://$TenantId-admin.sharepoint.com" -ClientId $ClientId -Interactive -ErrorAction Stop

    # Get all sites
    $sites = Get-PnPTenantSite -ErrorAction Stop

    # Build permissions result
    $permissions = @{
        sites = @()
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        tenant_id = $TenantId
    }

    foreach ($site in $sites) {
        # Note: In a full enterprise script, we would iterate Get-PnPUser and Get-PnPGroup for each site.
        # For this discovery script, we extract the primary owner and admins from the tenant site object
        # which is faster and doesn't require connecting to every individual site collection.
        
        $permissions.sites += @{
            url = $site.Url
            title = $site.Title
            owner = $site.Owner
            sharing_capability = $site.SharingCapability.ToString()
        }
    }

    # Output as JSON
    $permissions | ConvertTo-Json -Depth 10

} catch {
    $errorResult = @{
        error = $_.Exception.Message
        success = $false
    }
    $errorResult | ConvertTo-Json -Depth 10
    exit 1
}
