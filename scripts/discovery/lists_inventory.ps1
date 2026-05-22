<#
.SYNOPSIS
    Lists and Libraries Inventory Discovery Script

.DESCRIPTION
    Collects inventory of SharePoint lists and libraries across the tenant using PnP.PowerShell.
    Identifies large lists (over 5,000 items), document libraries, list templates, and versioning limits.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\lists_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
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

    # Build inventory result
    $inventory = @{
        sites = @()
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        tenant_id = $TenantId
    }

    # For performance across a tenant, we sample the top lists or just rely on site-level aggregate properties if possible.
    # To truly get list items, we have to iterate each site. We will do a safe extraction.
    foreach ($site in $sites) {
        $siteData = @{
            url = $site.Url
            title = $site.Title
            lists = @()
        }

        try {
            # Connect to specific site
            Connect-PnPOnline -Url $site.Url -ClientId $ClientId -Interactive -ErrorAction Stop
            
            # Retrieve lists (excluding hidden/system lists to reduce noise)
            $lists = Get-PnPList -Includes ItemCount, BaseTemplate, EnableVersioning, MajorVersionLimit | Where-Object { $_.Hidden -eq $false }

            foreach ($list in $lists) {
                $siteData.lists += @{
                    title = $list.Title
                    item_count = $list.ItemCount
                    template = $list.BaseTemplate.ToString()
                    is_large_list = ($list.ItemCount -gt 5000)
                    versioning_enabled = $list.EnableVersioning
                    version_limit = $list.MajorVersionLimit
                }
            }
        } catch {
            $siteData.error = "Failed to access lists: $_"
        }

        $inventory.sites += $siteData
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
