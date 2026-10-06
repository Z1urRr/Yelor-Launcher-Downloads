param(
    [Parameter(Mandatory = $true)]
    [string]$File,
    [Parameter(Mandatory = $true)]
    [string]$ExpectedSha256
)

$resolved = (Resolve-Path -LiteralPath $File -ErrorAction Stop).Path
$actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $resolved).Hash.ToUpperInvariant()
$expected = $ExpectedSha256.Trim().ToUpperInvariant()

if ($actual -ne $expected) {
    Write-Error "SHA-256 mismatch. Expected $expected, got $actual."
    exit 1
}

Write-Output "Verified: $resolved"
Write-Output "SHA-256: $actual"
