<#
.SYNOPSIS
    Storage Usage Inventory Discovery Script

.DESCRIPTION
    Analyzes storage usage across SharePoint sites using PnP.PowerShell.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\storage_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
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

    # Build storage result
    $storage = @{
        sites = @()
        summary = @{
            total_storage_used_mb = 0
            total_storage_quota_mb = 0
            site_count = 0
        }
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        tenant_id = $TenantId
    }

    foreach ($site in $sites) {
        $storage.summary.total_storage_used_mb += $site.StorageUsage
        $storage.summary.total_storage_quota_mb += $site.StorageMaximumLevel
        $storage.summary.site_count += 1

        $storage.sites += @{
            url = $site.Url
            title = $site.Title
            storage_used_mb = $site.StorageUsage
            storage_quota_mb = $site.StorageMaximumLevel
            usage_percent = if ($site.StorageMaximumLevel -gt 0) { 
                [math]::Round(($site.StorageUsage / $site.StorageMaximumLevel) * 100, 2) 
            } else { 0 }
        }
    }

    # Output as JSON
    $storage | ConvertTo-Json -Depth 10

} catch {
    $errorResult = @{
        error = $_.Exception.Message
        success = $false
    }
    $errorResult | ConvertTo-Json -Depth 10
    exit 1
}
