# Kho anh nhieu goc de tu chon: tao spec_kho.txt (tao_kho.py), render cho 2 skin vao _kho/:
#   _kho/<skin>/     9:16 day du (fov mo rong nhu render_tiktok) -> xuat_kho.py -> kho/<ma>_<skin>.jpg (anh rieng)
#   _kho/<skin>_98/  o 9:8 -> ghep_ss.py -> kho_ss/<so>_<ma>.jpg (slide so sanh MAC DINH / TUYET SAC)
# -Chi98: chi render o 9:8 (chi can slide so sanh). Unity Editor phai dong.
param([string]$Spec = "D:/model_aov/GiaLa/tiktok/spec_kho.txt", [switch]$Chi98)
$G = "D:/model_aov/GiaLa"
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.24f1\Editor\Unity.exe"
if (-not (Test-Path $Spec)) { py -3.14 "$PSScriptRoot/tao_kho.py" }
New-Item -ItemType Directory -Force "$G/tiktok/_kho" | Out-Null
$sp = "$G/tiktok/_kho/spec_916.txt"
py -3.14 "$PSScriptRoot/mo_fov.py" $Spec $sp
$khung = @(, @("98", 1280, $Spec))
if (-not $Chi98) { $khung += , @("916", 2560, $sp) }
foreach ($sk in "001", "002") {
    foreach ($kh in $khung) {
        $out = if ($kh[0] -eq "98") { "$G/tiktok/_kho/${sk}_98" } else { "$G/tiktok/_kho/$sk" }
        New-Item -ItemType Directory -Force $out | Out-Null
        & $unity -batchmode -quit -projectPath "$G/unity_$sk" -executeMethod GameKit.GameSceneBuilder.RenderAnglesCli `
            -angles $kh[2] -out $out -width 1440 -height $kh[1] -metal 0.8 -metalrim 1.8 `
            -logFile "$G/unity_$sk/Logs/tiktok_kho.log" | Out-Null
        "$sk $($kh[0]) exit=$LASTEXITCODE anh=$((Get-ChildItem $out -Filter *.png).Count)"
        Select-String -Path "$G/unity_$sk/Logs/tiktok_kho.log" -Pattern "error CS|\[GameKit\] thieu|Exception|OutOfMemory" | ForEach-Object { $_.Line }
    }
}
py -3.14 "$PSScriptRoot/ghep_ss.py" $Spec _kho kho_ss
if (-not $Chi98) { py -3.14 "$PSScriptRoot/xuat_kho.py" $Spec }
