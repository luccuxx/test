# Do goc nhanh: render spec do cho 2 skin vao _do/ (khong dung _render/ va anh/), roi to_do.py ghep _do/to_do_N.jpg
# (khong chu) de chon goc; moi o cat giong anh cuoi. Unity Editor phai dong 2 project GiaLa/unity_00X.
# -Khung 916: khung 9:16 (fov mo rong nhu render_tiktok, giong anh rieng); -Khung 98: o 9:8 (giong o trong anh ghep/viral).
# -Cot 5: moi hang 5 o (dung cho spec tu tao_do.py: a..e cua 1 goc); -Nhanh: render nua do phan giai.
param([string]$Spec = "D:/model_aov/GiaLa/tiktok/spec_do.txt", [int]$Cot = 3, [string]$Khung = "916", [switch]$Nhanh)
$G = "D:/model_aov/GiaLa"
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.24f1\Editor\Unity.exe"
New-Item -ItemType Directory -Force "$G/tiktok/_do" | Out-Null
if ($Khung -eq "98") { $sp = $Spec; $w = 1440; $h = 1280 }
else { $sp = "$G/tiktok/_do/spec_916.txt"; py -3.14 "$PSScriptRoot/mo_fov.py" $Spec $sp; $w = 1440; $h = 2560 }
if ($Nhanh) { $w = $w / 2; $h = $h / 2 }
foreach ($sk in "001", "002") {
    $out = "$G/tiktok/_do/$sk"
    if (Test-Path $out) { Remove-Item "$out/*.png" }
    New-Item -ItemType Directory -Force $out | Out-Null
    & $unity -batchmode -quit -projectPath "$G/unity_$sk" -executeMethod GameKit.GameSceneBuilder.RenderAnglesCli `
        -angles $sp -out $out -width $w -height $h -metal 0.8 -metalrim 1.8 `
        -logFile "$G/unity_$sk/Logs/tiktok_do.log" | Out-Null
    "$sk exit=$LASTEXITCODE anh=$((Get-ChildItem $out -Filter *.png).Count)"
    Select-String -Path "$G/unity_$sk/Logs/tiktok_do.log" -Pattern "error CS|\[GameKit\] thieu|Exception|OutOfMemory" | ForEach-Object { $_.Line }
}
py -3.14 "$PSScriptRoot/to_do.py" $Spec $Cot 5 $Khung
