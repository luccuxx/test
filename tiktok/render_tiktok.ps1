# Render 25 goc (spec25.txt) cho 2 skin, 9:8 va 9:16, anh kim; roi ghep vao anh/ (watermark howtocheckmap, tranh vung TikTok che).
# Khung 9:16 dung spec mo rong fov (mo_fov.py) de ghep.py doi tam nhan vat vao vung an toan ma khong mat bo cuc.
# Unity Editor phai dong 2 project GiaLa/unity_00X. -Spec <file> de render lai vai dong (ghi de anh cung ten).
# -Ghep <script> doi buoc ghep (vd ghep_viral.py); -Chi98 bo khung 9:16 (bai viral chi dung o 9:8).
param([string]$Spec = "D:/model_aov/GiaLa/tiktok/spec25.txt", [string]$Ghep = "ghep.py", [switch]$Chi98)
$G = "D:/model_aov/GiaLa"
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.24f1\Editor\Unity.exe"
New-Item -ItemType Directory -Force "$G/tiktok/_render" | Out-Null
$spec916 = "$G/tiktok/_render/spec_916.txt"
py -3.14 "$PSScriptRoot/mo_fov.py" $Spec $spec916
$khung = @(, @("98", 1280, $Spec))
if (-not $Chi98) { $khung += , @("916", 2560, $spec916) }
foreach ($sk in "001", "002") {
    foreach ($sz in $khung) {
        $out = "$G/tiktok/_render/${sk}_$($sz[0])"
        New-Item -ItemType Directory -Force $out | Out-Null
        & $unity -batchmode -quit -projectPath "$G/unity_$sk" -executeMethod GameKit.GameSceneBuilder.RenderAnglesCli `
            -angles $sz[2] -out $out -width 1440 -height $sz[1] -metal 0.8 -metalrim 1.8 `
            -logFile "$G/unity_$sk/Logs/tiktok.log" | Out-Null
        "$sk $($sz[0]) exit=$LASTEXITCODE anh=$((Get-ChildItem $out -Filter *.png).Count)"
        Select-String -Path "$G/unity_$sk/Logs/tiktok.log" -Pattern "error CS|\[GameKit\] thieu|Exception|OutOfMemory" | ForEach-Object { $_.Line }
    }
}
py -3.14 "$PSScriptRoot/$Ghep"
