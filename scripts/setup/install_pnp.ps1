<#
.SYNOPSIS
    Install PnP.PowerShell Module

.DESCRIPTION
    Installs the PnP.PowerShell module for SharePoint discovery operations.

.PARAMETER Force
    Force reinstall the module

.EXAMPLE
    .\install_pnp.ps1
.EXAMPLE
    .\install_pnp.ps1 -Force
#>

param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

try {
    Write-Host "Checking PnP.PowerShell module installation..." -ForegroundColor Cyan

    # Check if module is already installed
    $module = Get-Module -ListAvailable -Name PnP.PowerShell

    if ($module -and -not $Force) {
        Write-Host "PnP.PowerShell is already installed (version: $($module.Version))" -ForegroundColor Green
        $result = @{
            success = $true
            message = "PnP.PowerShell already installed"
            version = $module.Version.ToString()
        }
        $result | ConvertTo-Json -Depth 10
        exit 0
    }

    # Install or reinstall module
    Write-Host "Installing PnP.PowerShell module..." -ForegroundColor Yellow

    if ($Force) {
        Uninstall-Module -Name PnP.PowerShell -Force -ErrorAction SilentlyContinue
    }

    Install-Module -Name PnP.PowerShell -Force -AllowClobber -Scope CurrentUser -ErrorAction Stop

    # Verify installation
    $installedModule = Get-Module -ListAvailable -Name PnP.PowerShell

    if ($installedModule) {
        Write-Host "PnP.PowerShell installed successfully (version: $($installedModule.Version))" -ForegroundColor Green
        $result = @{
            success = $true
            message = "PnP.PowerShell installed successfully"
            version = $installedModule.Version.ToString()
        }
        $result | ConvertTo-Json -Depth 10
        exit 0
    } else {
        throw "Module installation verification failed"
    }

} catch {
    $errorResult = @{
        error = $_.Exception.Message
        success = $false
    }
    $errorResult | ConvertTo-Json -Depth 10
    exit 1
}
