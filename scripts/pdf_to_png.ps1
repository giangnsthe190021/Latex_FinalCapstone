# Render a PDF page to PNG with the Windows PDF renderer (Windows.Data.Pdf), no extra software. Used by the Word version of the
# paper to turn the ConceptDraw figures (Fig. 1-2) into images, and to look at the pages of the exported PDF.
# Usage (Windows PowerShell 5.1): powershell -File scripts/pdf_to_png.ps1 <in.pdf> <out.png> [dpi] [page]
#   page: 0-based index (default 0); -1 renders every page to <out>-<n>.png
param([string]$In, [string]$Out, [int]$Dpi = 600, [int]$Page = 0)
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Data.Pdf.PdfDocument, Windows.Data.Pdf, ContentType = WindowsRuntime]
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Storage.Streams.InMemoryRandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime]

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
function Await($op, [Type]$type) {
    $t = $asTaskGeneric.MakeGenericMethod($type).Invoke($null, @($op)); $t.Wait(-1) | Out-Null; $t.Result
}
function AwaitAction($op) {
    $m = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction' }
    $t = $m[0].Invoke($null, @($op)); $t.Wait(-1) | Out-Null
}

$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync((Resolve-Path $In).Path)) ([Windows.Storage.StorageFile])
$pdf = Await ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
$which = if ($Page -lt 0) { 0..($pdf.PageCount - 1) } else { @($Page) }
foreach ($k in $which) {
    $pg = $pdf.GetPage($k)
    $opt = New-Object Windows.Data.Pdf.PdfPageRenderOptions
    $opt.DestinationWidth = [uint32]([math]::Round($pg.Size.Width / 96.0 * $Dpi))
    $opt.DestinationHeight = [uint32]([math]::Round($pg.Size.Height / 96.0 * $Dpi))
    $opt.BitmapEncoderId = [Windows.Graphics.Imaging.BitmapEncoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime]::PngEncoderId
    $opt.BackgroundColor = [Windows.UI.Color]::FromArgb(255, 255, 255, 255)
    $stream = New-Object Windows.Storage.Streams.InMemoryRandomAccessStream
    AwaitAction ($pg.RenderToStreamAsync($stream, $opt))
    $net = [System.IO.WindowsRuntimeStreamExtensions]::AsStreamForRead($stream.GetInputStreamAt(0))
    $target = if ($Page -lt 0) { [IO.Path]::ChangeExtension($Out, $null).TrimEnd('.') + "-$($k + 1).png" } else { $Out }
    $fs = [System.IO.File]::Create($target); $net.CopyTo($fs); $fs.Close()
    "{0}: {1} x {2} px" -f $target, $opt.DestinationWidth, $opt.DestinationHeight
}
