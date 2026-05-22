<#
.SYNOPSIS
    External Sharing and Security Inventory Discovery Script

.DESCRIPTION
    Collects inventory of SharePoint external sharing settings across the tenant using PnP.PowerShell.
    Identifies sites that allow external sharing, guest user presence, and anonymous link policies.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\external_sharing_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
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

    foreach ($site in $sites) {
        $inventory.sites += @{
            url = $site.Url
            title = $site.Title
            sharing_capability = $site.SharingCapability.ToString()
            sharing_allowed_domain_list = $site.SharingAllowedDomainList
            sharing_blocked_domain_list = $site.SharingBlockedDomainList
            sharing_domain_restriction_mode = $site.SharingDomainRestrictionMode.ToString()
            is_teams_connected = $site.IsTeamsConnected
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
