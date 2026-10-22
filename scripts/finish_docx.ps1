# Second step of the Word version (after scripts/make_docx.py): Word builds up the linear UnicodeMath equations into native
# equations, saves the .docx, exports a PDF next to it and prints the number of pages.
# Usage (Windows, Microsoft Word installed):  powershell -ExecutionPolicy Bypass -File scripts/finish_docx.ps1 PPFedData.docx
param([Parameter(Mandatory = $true)][string]$Docx, [string]$Pdf = "")
$full = (Resolve-Path $Docx).Path
if (-not $Pdf) { $Pdf = [IO.Path]::ChangeExtension($full, ".pdf") }
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    $doc = $word.Documents.Open($full)
    $n = $doc.OMaths.Count
    for ($k = 1; $k -le $n; $k++) { $doc.OMaths.Item($k).BuildUp() }
    # every table but the author block: fit the columns to their content, then to the column width
    for ($k = 2; $k -le $doc.Tables.Count; $k++) {
        $t = $doc.Tables.Item($k)
        $t.AllowAutoFit = $true
        $t.AutoFitBehavior(1)
        $t.AutoFitBehavior(2)
    }
    $doc.AutoHyphenation = $true
    $doc.Repaginate()
    $pages = $doc.ComputeStatistics(2)
    $doc.Save()
    $doc.ExportAsFixedFormat($Pdf, 17)
    "equations built: $n; pages: $pages; pdf: $Pdf"
    $doc.Close($false)
}
finally {
    $word.Quit()
}
