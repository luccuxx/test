"""Ghep bai viral (chi co watermark howtocheckmap o goc phai-duoi o duoi, qua ghep.slide): moi slide 1 skin, o tren = toan canh (ma ...T), o duoi = phong to
cung khoanh khac (ma ...Z); 2 o 9:8 nam gon trong vung an toan TikTok (ghep.slide).
Thu tu slide: canh 1 (001, 002), canh 2 (001, 002)... theo spec_viral.txt -> anh_viral/viral_NN.png.
Render: render_tiktok.ps1 -Spec D:/model_aov/GiaLa/tiktok/spec_viral.txt -Ghep ghep_viral.py -Chi98"""
import os
import sys
from ghep import fit, slide, R, GOC

OUT = os.path.join(GOC, "anh_viral")


def main():
    codes = [l.split("|")[0] for l in open(os.path.join(GOC, "spec_viral.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]
    canh = list(zip(codes[0::2], codes[1::2]))
    sai = [c for t, z in canh for c in (t, z) if not (t.endswith("T") and z.endswith("Z") and t[:-1] == z[:-1])]
    if len(codes) % 2 or sai:
        print("spec_viral.txt phai theo cap ...T (toan canh) roi ...Z (phong to) cung ten; sai:", sai or codes[-1])
        return 1
    thieu = [f"{sk}_98/{c}.png" for c in codes for sk in ("001", "002") if not os.path.exists(f"{R}/{sk}_98/{c}.png")]
    if thieu:
        print("thieu anh trong _render:", thieu)
        return 1
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for t, z in canh:
        for sk in ("001", "002"):
            n += 1
            slide([fit(f"{R}/{sk}_98/{t}.png", 1080, 960), fit(f"{R}/{sk}_98/{z}.png", 1080, 960)]).save(f"{OUT}/viral_{n:02d}.png")
    print("xong", n, "slide ->", OUT)


if __name__ == "__main__":
    sys.exit(main())
