<#
.SYNOPSIS
    Pages and Branding Inventory Discovery Script

.DESCRIPTION
    Collects inventory of SharePoint pages across the tenant to distinguish between Classic and Modern pages using PnP.PowerShell.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\pages_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
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

    # For performance, we sample the site level data. Iterating every page in every site takes too long for standard discovery.
    foreach ($site in $sites) {
        $siteData = @{
            url = $site.Url
            title = $site.Title
            pages = @()
        }

        try {
            # Connect to specific site
            Connect-PnPOnline -Url $site.Url -ClientId $ClientId -Interactive -ErrorAction Stop
            
            # Get pages from the Site Pages library
            # Get-PnPListItem -List "Site Pages" can be used, but Get-PnPClientSidePage gives modern pages specifically
            # We will grab all items from "Site Pages" to check the template
            $pages = Get-PnPListItem -List "Site Pages" -Includes FileLeafRef, ClientSideApplicationId

            foreach ($page in $pages) {
                # ClientSideApplicationId distinguishes modern pages
                $isModern = ($null -ne $page["ClientSideApplicationId"] -and $page["ClientSideApplicationId"] -ne "00000000-0000-0000-0000-000000000000")
                
                $siteData.pages += @{
                    name = $page["FileLeafRef"]
                    is_modern = $isModern
                }
            }
        } catch {
            $siteData.error = "Failed to access pages: $_"
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
