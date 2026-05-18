<#
.SYNOPSIS
    Microsoft 365 User Inventory Discovery Script

.DESCRIPTION
    Collects inventory of all Microsoft 365 users using PnP.PowerShell.
    Outputs results in JSON format.

.PARAMETER TenantId
    Azure AD tenant ID for authentication

.PARAMETER ClientId
    Azure AD client ID for authentication

.EXAMPLE
    .\user_inventory.ps1 -TenantId "xxx" -ClientId "yyy"
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

    # Get all users
    $users = Get-PnPUser -ErrorAction Stop

    # Build inventory result
    $inventory = @{
        users = @()
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        tenant_id = $TenantId
    }

    foreach ($user in $users) {
        $inventory.users += @{
            user_principal_name = $user.UserPrincipalName
            email = $user.Email
            display_name = $user.Title
            account_enabled = $user.IsSiteAdmin
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
