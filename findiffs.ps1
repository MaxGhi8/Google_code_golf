<#
findiffs.ps1
PowerShell rewrite of findiffs.sh (removes dependency on pup, curl, awk) using Invoke-WebRequest DOM parsing.

Run using:
powershell -ExecutionPolicy Bypass -File .\findiffs.ps1 | Select-Object -First 10

Behavior:
1. Downloads the public Google Sheets published HTML (the waffle table).
2. Extracts the 5th column numeric cells (two columns right of original script; CSS: table.waffle tbody tr td:nth-child(5)).
3. Keeps only the last 400 numeric entries (tail -n 400 equivalent).
4. For each row (numbered starting at 1) builds task ID (zero-padded to 3 digits) and checks for finals/taskNNN.py.
   - If file exists, measure its size in bytes.
   - Else assume 2500 (mirrors original script's default upper bound logic).
5. Computes potential size saving: local_size - remote_size.
6. Sorts descending by potential saving (same as sort -nr on first field) and prints human-readable lines:
   - If local < 2500:  "task NNN could be X B smaller, they did in REMOTE B, we took LOCAL B"
   - Else:            "task NNN could be done in just REMOTE B, we should try it"

Optional switches:
 -RawObjects : Output objects instead of formatted strings (useful for further scripting).

#>
[CmdletBinding()]
param(
    [switch]$RawObjects,
    [string]$Link = "https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml/sheet?headers=false&gid=1427788625",
    [int]$TailCount = 400,
    [string]$FinalsDir = "finals",
    [int]$MissingSize = 2500
)

$ErrorActionPreference = 'Stop'

function Get-WaffleThirdColumnValues {
    param(
        [Parameter(Mandatory)]$Response
    )
    # Try DOM parse first (without -UseBasicParsing so ParsedHtml is populated in Windows PowerShell)
    try {
        $parsed = $Response.ParsedHtml
        if ($null -eq $parsed) { throw "ParsedHtml not available" }
        $tables = @($parsed.getElementsByTagName('table'))
        $waffle = $tables | Where-Object { $_.className -match 'waffle' } | Select-Object -First 1
        if (-not $waffle) { throw "Waffle table not found" }
        $vals = New-Object System.Collections.Generic.List[int]
        foreach ($row in @($waffle.rows)) {
            if ($row.cells.length -ge 2) {
                $text = ($row.cells.item(1).innerText).Trim()
                if ($text -match '^[0-9]+$') { [void]$vals.Add([int]$text) }
            }
        }
        return ,$vals.ToArray()
    } catch {
        Write-Warning "DOM parse failed ($($_.Exception.Message)); using regex fallback."
        $html = $Response.Content
        $tables = [regex]::Matches($html,'<table[^>]*class="[^"]*waffle[^"]*"[\s\S]*?</table>',"IgnoreCase")
        if ($tables.Count -eq 0) { throw "No waffle table in HTML (regex fallback)" }
        $table = $tables[0].Value
        $rows = [regex]::Matches($table,'<tr[\s\S]*?</tr>',"IgnoreCase")
        $vals = @()
        foreach ($r in $rows) {
            $cells = [regex]::Matches($r.Value,'<td[\s\S]*?</td>',"IgnoreCase")
            if ($cells.Count -ge 2) {
                $cell = $cells[1].Value -replace '<[^>]+>','' -replace '&nbsp;',' ' -replace '&amp;','&'
                $cell = $cell.Trim()
                if ($cell -match '^[0-9]+$') { $vals += [int]$cell }
            }
        }
        return ,$vals
    }
}

Write-Verbose "Fetching spreadsheet..."
$response = Invoke-WebRequest -Uri $Link
$values = Get-WaffleThirdColumnValues -Response $response

if ($values.Count -gt $TailCount) {
    # Proper tail equivalent
    $values = $values | Select-Object -Last $TailCount
}

$results = @()
for ($i=0; $i -lt $values.Count; $i++) {
    $remote = $values[$i]
    $task = '{0:000}' -f ($i + 1)
    $path = Join-Path $FinalsDir ("task{0}.py" -f $task)
    if (Test-Path $path) {
        $local = (Get-Item $path).Length
    } else {
        $local = $MissingSize
    }
    $diff = $local - $remote
    $results += [pscustomobject]@{
        Task = $task
        Remote = $remote
        Local = $local
        Diff = $diff
    }
}

$results = $results | Sort-Object Diff -Descending

if ($RawObjects) { return $results }

foreach ($r in $results) {
    if ($r.Diff -gt 0) {
        # We are larger than reference
        if ($r.Local -lt $MissingSize) {
            "task {0} could be {1}B smaller, they did in {2}B, we took {3}B" -f $r.Task,$r.Diff,$r.Remote,$r.Local
        } else {
            "task {0} could be done in just {1}B, we should try it" -f $r.Task,$r.Remote
        }
    } elseif ($r.Diff -lt 0) {
        # We are already smaller
        $gain = -1 * $r.Diff
        "task {0} is already {1}B smaller (we: {2}B vs them: {3}B)" -f $r.Task,$gain,$r.Local,$r.Remote
    } else {
        "task {0} matches exactly ({1}B)" -f $r.Task,$r.Local
    }
}

exit 0
