"""Ghep anh so sanh 2 skin de dang TikTok: moi goc -> 1 slide 1080x1920, o tren 001 (MAC DINH), o duoi 002 (TUYET SAC),
cung goc may; chu ten skin to trang vien den o goc trong nhat (nhan.py), watermark howtocheckmap (wm.py), 2 o nam gon
trong vung an toan TikTok; toi uu chong mo/vo (xuat_tiktok.toi_uu), JPEG 95. Slide nen den -> <ra>/_nen_den/.
Nguon: <nguon>/{001,002}_98/<ma>.png (render o 9:8).
Dung: py ghep_ss.py [spec = spec_viral.txt] [nguon = _render] [ra = anh_ss]
  - theo kich ban (20 slide, thu tu spec_viral): py ghep_ss.py
  - kho nhieu goc (kho.ps1 da render _kho/*_98):  py ghep_ss.py spec_kho.txt _kho kho_ss"""
import os
import sys
import numpy as np
from ghep import fit, slide, khung_o, GOC
from nhan import NHAN, gan_nhan
from xuat_tiktok import toi_uu, SRGB


def den_mep(im):
    m = np.asarray(im).max(2) <= 6   # nen den chi tinh o mep (toc/vo den o giua khong tinh)
    return max(m[:40].mean(), m[-40:].mean(), m[:, :40].mean(), m[:, -40:].mean()) > 0.05


def main(spec, nguon, ra):
    nguon, ra = (p if os.path.isabs(p) else os.path.join(GOC, p) for p in (nguon, ra))
    codes = [l.split("|")[0] for l in open(spec if os.path.isabs(spec) else os.path.join(GOC, spec), encoding="utf-8")
             if l.strip() and not l.startswith("#")]
    thieu = [f"{sk}_98/{c}.png" for c in codes for sk in ("001", "002") if not os.path.exists(f"{nguon}/{sk}_98/{c}.png")]
    if thieu:
        print("thieu anh o 9:8 trong", nguon, ":", thieu)
        return 1
    os.makedirs(os.path.join(ra, "_nen_den"), exist_ok=True)
    so = len(str(len(codes)))
    tot, den = 0, []
    for i, c in enumerate(codes, 1):
        o = [fit(f"{nguon}/{sk}_98/{c}.png", 1080, 960) for sk in ("001", "002")]
        xau = any(den_mep(im) for im in o)
        g, _ = gan_nhan(slide(o), khung_o(), [NHAN["001"], NHAN["002"]])
        out = os.path.join(ra, "_nen_den" if xau else "", f"{i:0{so}d}_{c}.jpg")
        toi_uu(g).save(out, quality=95, subsampling=0, optimize=True, icc_profile=SRGB)
        if xau:
            den.append(c)
        else:
            tot += 1
    print(f"xong: {tot} slide -> {ra}; nen den {len(den)} -> _nen_den", den or "")


if __name__ == "__main__":
    a = sys.argv[1:]
    sys.exit(main(a[0] if a else "spec_viral.txt", a[1] if len(a) > 1 else "_render", a[2] if len(a) > 2 else "anh_ss"))
