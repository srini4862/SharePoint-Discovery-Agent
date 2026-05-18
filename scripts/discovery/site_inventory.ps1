<#
.SYNOPSIS
    SharePoint Site Inventory Discovery Script

.DESCRIPTION
    Collects comprehensive inventory of all SharePoint sites in the tenant using PnP.PowerShell.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\site_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
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

    # Connect to SharePoint Online
    Connect-PnPOnline -Url "https://$TenantId.sharepoint.com" -ClientId $ClientId -Interactive -ErrorAction Stop

    # Get all sites
    $sites = Get-PnPTenantSite -ErrorAction Stop

    # Build inventory result
    $inventory = @{
        sites = @()
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        tenant_id = $TenantId
    }

    foreach ($site in $sites) {
        $inventory.sites += @{
            url = $site.Url
            title = $site.Title
            template = $site.Template
            owner = $site.Owner
            storage_usage_mb = $site.StorageUsage
            storage_quota_mb = $site.StorageMaximumLevel
            last_content_modified = $site.LastContentModifiedDate
        }
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
