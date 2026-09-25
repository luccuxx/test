# Render 25 goc (spec25.txt) cho 2 skin, 9:8 va 9:16, anh kim; roi ghep vao anh/ (khong chu).
# Unity Editor phai dong 2 project GiaLa/unity_00X. -Spec <file> de render lai vai dong (ghi de anh cung ten).
param([string]$Spec = "D:/model_aov/GiaLa/tiktok/spec25.txt")
$G = "D:/model_aov/GiaLa"
$unity = "C:\Program Files\Unity\Hub\Editor\6000.3.24f1\Editor\Unity.exe"
foreach ($sk in "001", "002") {
    foreach ($sz in @(@("98", 1280), @("916", 2560))) {
        $out = "$G/tiktok/_render/${sk}_$($sz[0])"
        New-Item -ItemType Directory -Force $out | Out-Null
        & $unity -batchmode -quit -projectPath "$G/unity_$sk" -executeMethod GameKit.GameSceneBuilder.RenderAnglesCli `
            -angles $Spec -out $out -width 1440 -height $sz[1] -metal 0.8 -metalrim 1.8 `
            -logFile "$G/unity_$sk/Logs/tiktok.log" | Out-Null
        "$sk $($sz[0]) exit=$LASTEXITCODE anh=$((Get-ChildItem $out -Filter *.png).Count)"
        Select-String -Path "$G/unity_$sk/Logs/tiktok.log" -Pattern "error CS|\[GameKit\] thieu|Exception|OutOfMemory" | ForEach-Object { $_.Line }
    }
}
py -3.14 "$PSScriptRoot/ghep.py"
