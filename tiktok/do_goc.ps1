# Do goc nhanh: render spec_do.txt cho 2 skin, khung 9:16 (1440x2560, fov mo rong nhu render_tiktok), vao _do/
# (khong dung _render/ va anh/); roi to_do.py ghep _do/to_do.jpg (khong chu) de chon goc, moi o da doi tam
# vao vung an toan TikTok giong anh rieng cuoi cung. Unity Editor phai dong 2 project GiaLa/unity_00X.
param([string]$Spec = "D:/model_aov/GiaLa/tiktok/spec_do.txt")
$G = "D:/model_aov/GiaLa"
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.24f1\Editor\Unity.exe"
New-Item -ItemType Directory -Force "$G/tiktok/_do" | Out-Null
$spec916 = "$G/tiktok/_do/spec_916.txt"
py -3.14 "$PSScriptRoot/mo_fov.py" $Spec $spec916
foreach ($sk in "001", "002") {
    $out = "$G/tiktok/_do/$sk"
    New-Item -ItemType Directory -Force $out | Out-Null
    & $unity -batchmode -quit -projectPath "$G/unity_$sk" -executeMethod GameKit.GameSceneBuilder.RenderAnglesCli `
        -angles $spec916 -out $out -width 1440 -height 2560 -metal 0.8 -metalrim 1.8 `
        -logFile "$G/unity_$sk/Logs/tiktok_do.log" | Out-Null
    "$sk exit=$LASTEXITCODE anh=$((Get-ChildItem $out -Filter *.png).Count)"
    Select-String -Path "$G/unity_$sk/Logs/tiktok_do.log" -Pattern "error CS|\[GameKit\] thieu|Exception|OutOfMemory" | ForEach-Object { $_.Line }
}
py -3.14 "$PSScriptRoot/to_do.py" $Spec
