"""Ghep cac slide thanh video TikTok 1080x1920 de giu do net (TikTok nen che do Anh manh hon video anh tinh).
Moi anh dung yen GIAY giay, cat thang (khong hieu ung), H.264 High, CRF 14 (gan nhu khong mat), 30 fps, -tune stillimage,
co am thanh im lang (TikTok them nhac sau). Can: py -3.14 -m pip install imageio-ffmpeg (1 lan).
Dung: py lam_video.py [thu muc anh = bai_dang] [giay moi anh = 2.5] -> <thu muc>/video_tiktok.mp4"""
import os
import subprocess
import sys
import tempfile
import imageio_ffmpeg

GOC = os.path.dirname(os.path.abspath(__file__))


def main(vao, giay=2.5):
    vao = vao if os.path.isabs(vao) else os.path.join(GOC, vao)
    ds = sorted(f for f in os.listdir(vao) if f.lower().endswith((".jpg", ".jpeg", ".png")))
    if not ds:
        print("khong co anh trong", vao)
        return 1
    ra = os.path.join(vao, "video_tiktok.mp4")
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        for d in ds:
            f.write(f"file '{os.path.join(vao, d)}'\nduration {giay}\n")
        f.write(f"file '{os.path.join(vao, ds[-1])}'\n")   # concat can lap anh cuoi de giu thoi luong
        ds_file = f.name
    lenh = [imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-f", "concat", "-safe", "0", "-i", ds_file,
            "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-vf", "scale=1080:1920:flags=lanczos,fps=30,format=yuv420p",
            "-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "14", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", ra]
    r = subprocess.run(lenh, capture_output=True, text=True)
    os.remove(ds_file)
    if r.returncode:
        print(r.stderr[-2000:])
        return r.returncode
    print(f"xong: {ra} ({len(ds)} anh x {giay}s, {os.path.getsize(ra) // 1024} KB)")


if __name__ == "__main__":
    a = sys.argv[1:]
    sys.exit(main(a[0] if a else "bai_dang", float(a[1]) if len(a) > 1 else 2.5))
