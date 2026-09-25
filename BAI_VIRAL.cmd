@echo off
rem Bam dup de tao bai TikTok: kich ban viral (20 slide) + so sanh MAC DINH / TUYET SAC + watermark howtocheckmap.
rem Ket qua: tiktok\bai_dang\ (00_bia.jpg, 00_bia_toan.jpg, 01..20.jpg, video_tiktok.mp4, caption.txt). Dong Unity Editor truoc khi chay.
cd /d "%~dp0"
git pull
powershell -ExecutionPolicy Bypass -File "%~dp0tiktok\render_tiktok.ps1" -Spec "%~dp0tiktok\spec_viral.txt" -Ghep "ghep_ss.py spec_viral.txt _render bai_dang" -Chi98
copy /y "%~dp0tiktok\caption.txt" "%~dp0tiktok\bai_dang\caption.txt" >nul
py -3.14 "%~dp0tiktok\bia.py"
powershell -ExecutionPolicy Bypass -File "%~dp0tiktok\render_tiktok.ps1" -Spec "%~dp0tiktok\spec_bia.txt" -Ghep "bia_toan.py BIA _render bai_dang"
py -3.14 -m pip install -q imageio-ffmpeg
py -3.14 "%~dp0tiktok\lam_video.py" bai_dang
explorer "%~dp0tiktok\bai_dang"
pause
