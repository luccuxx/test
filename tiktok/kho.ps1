# Kho anh nhieu goc de tu chon: tao spec_kho.txt (tao_kho.py), render 9:16 day du (fov mo rong nhu render_tiktok)
# cho 2 skin vao _kho/, roi xuat_kho.py -> kho/<ma>_<skin>.jpg (san sang dang TikTok). Unity Editor phai dong.
param([string]$Spec = "D:/model_aov/GiaLa/tiktok/spec_kho.txt")
$G = "D:/model_aov/GiaLa"
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.24f1\Editor\Unity.exe"
if (-not (Test-Path $Spec)) { py -3.14 "$PSScriptRoot/tao_kho.py" }
New-Item -ItemType Directory -Force "$G/tiktok/_kho" | Out-Null
$sp = "$G/tiktok/_kho/spec_916.txt"
py -3.14 "$PSScriptRoot/mo_fov.py" $Spec $sp
foreach ($sk in "001", "002") {
    $out = "$G/tiktok/_kho/$sk"
    New-Item -ItemType Directory -Force $out | Out-Null
    & $unity -batchmode -quit -projectPath "$G/unity_$sk" -executeMethod GameKit.GameSceneBuilder.RenderAnglesCli `
        -angles $sp -out $out -width 1440 -height 2560 -metal 0.8 -metalrim 1.8 `
        -logFile "$G/unity_$sk/Logs/tiktok_kho.log" | Out-Null
    "$sk exit=$LASTEXITCODE anh=$((Get-ChildItem $out -Filter *.png).Count)"
    Select-String -Path "$G/unity_$sk/Logs/tiktok_kho.log" -Pattern "error CS|\[GameKit\] thieu|Exception|OutOfMemory" | ForEach-Object { $_.Line }
}
py -3.14 "$PSScriptRoot/xuat_kho.py" $Spec
