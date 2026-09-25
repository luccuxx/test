# Do goc nhanh: render spec_do.txt cho 2 skin, chi khung 9:8, vao _do/ (khong dung _render/ va anh/);
# roi to_do.py ghep _do/to_do.jpg (khong chu) de chon goc. Unity Editor phai dong 2 project GiaLa/unity_00X.
param([string]$Spec = "D:/model_aov/GiaLa/tiktok/spec_do.txt")
$G = "D:/model_aov/GiaLa"
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.24f1\Editor\Unity.exe"
foreach ($sk in "001", "002") {
    $out = "$G/tiktok/_do/$sk"
    New-Item -ItemType Directory -Force $out | Out-Null
    & $unity -batchmode -quit -projectPath "$G/unity_$sk" -executeMethod GameKit.GameSceneBuilder.RenderAnglesCli `
        -angles $Spec -out $out -width 1440 -height 1280 -metal 0.8 -metalrim 1.8 `
        -logFile "$G/unity_$sk/Logs/tiktok_do.log" | Out-Null
    "$sk exit=$LASTEXITCODE anh=$((Get-ChildItem $out -Filter *.png).Count)"
    Select-String -Path "$G/unity_$sk/Logs/tiktok_do.log" -Pattern "error CS|\[GameKit\] thieu|Exception|OutOfMemory" | ForEach-Object { $_.Line }
}
py -3.14 "$PSScriptRoot/to_do.py" $Spec
