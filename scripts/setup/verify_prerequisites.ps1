<#
.SYNOPSIS
    Verify Prerequisites for SharePoint Discovery Agent

.DESCRIPTION
    Verifies all prerequisites before proceeding with installation.

.EXAMPLE
    .\verify_prerequisites.ps1
#>

$ErrorActionPreference = "Stop"

try {
    $checks = @()
    $allPassed = $true

    # Check 1: PowerShell Core version
    Write-Host "Checking PowerShell Core version..." -ForegroundColor Cyan
    $psVersion = $PSVersionTable.PSVersion
    if ($psVersion.Major -ge 7) {
        Write-Host "PowerShell Core version: $psVersion (OK)" -ForegroundColor Green
        $checks += @{
            check = "PowerShell Core Version"
            status = "passed"
            value = $psVersion.ToString()
        }
    } else {
        Write-Host "PowerShell Core version: $psVersion (FAILED - requires 7.0 or higher)" -ForegroundColor Red
        $checks += @{
            check = "PowerShell Core Version"
            status = "failed"
            value = $psVersion.ToString()
        }
        $allPassed = $false
    }

    # Check 2: PnP.PowerShell module
    Write-Host "Checking PnP.PowerShell module..." -ForegroundColor Cyan
    $pnpModule = Get-Module -ListAvailable -Name PnP.PowerShell
    if ($pnpModule) {
        Write-Host "PnP.PowerShell version: $($pnpModule.Version) (OK)" -ForegroundColor Green
        $checks += @{
            check = "PnP.PowerShell Module"
            status = "passed"
            value = $pnpModule.Version.ToString()
        }
    } else {
        Write-Host "PnP.PowerShell module not found (FAILED)" -ForegroundColor Red
        $checks += @{
            check = "PnP.PowerShell Module"
            status = "failed"
            value = "not installed"
        }
        $allPassed = $false
    }

    # Check 3: Network connectivity to Microsoft 365
    Write-Host "Checking network connectivity..." -ForegroundColor Cyan
    try {
        $response = Test-NetConnection -ComputerName "microsoft.com" -Port 443 -WarningAction SilentlyContinue -ErrorAction Stop
        if ($response.TcpTestSucceeded) {
            Write-Host "Network connectivity to Microsoft 365 (OK)" -ForegroundColor Green
            $checks += @{
                check = "Network Connectivity"
                status = "passed"
                value = "connected"
            }
        } else {
            Write-Host "Network connectivity to Microsoft 365 (FAILED)" -ForegroundColor Red
            $checks += @{
                check = "Network Connectivity"
                status = "failed"
                value = "not connected"
            }
            $allPassed = $false
        }
    } catch {
        Write-Host "Network connectivity check failed (FAILED)" -ForegroundColor Red
        $checks += @{
            check = "Network Connectivity"
            status = "failed"
            value = "check failed"
        }
        $allPassed = $false
    }

    # Output result
    $result = @{
        success = $allPassed
        checks = $checks
        message = if ($allPassed) { "All prerequisites verified" } else { "Some prerequisites failed" }
    }

    $result | ConvertTo-Json -Depth 10

    if (-not $allPassed) {
        exit 1
    }

} catch {
    $errorResult = @{
        error = $_.Exception.Message
        success = $false
    }
    $errorResult | ConvertTo-Json -Depth 10
    exit 1
}
