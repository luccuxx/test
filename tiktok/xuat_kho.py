"""Xuat kho anh: _kho/{001,002}/<ma>.png (render 9:16, fov mo rong) -> kho/<ma>_<skin>.jpg san sang dang TikTok:
doi tam vao vung an toan, vang kim (ghep.fit), watermark (wm.py), toi uu chong vo (xuat_tiktok.toi_uu), JPEG 95.
Anh nen den (camera ra ngoai vung troi) dua vao kho/_nen_den/ de khoi lan khi chon. Dung: py xuat_kho.py [spec_kho.txt]"""
import os
import sys
import numpy as np
from ghep import fit, AT, TAM
from mo_fov import K
from wm import dong_dau
from xuat_tiktok import toi_uu, SRGB

GOC = os.path.dirname(os.path.abspath(__file__))
VAO, RA = os.path.join(GOC, "_kho"), os.path.join(GOC, "kho")


def main(spec):
    codes = [l.split("|")[0] for l in open(spec, encoding="utf-8") if l.strip() and not l.startswith("#")]
    os.makedirs(os.path.join(RA, "_nen_den"), exist_ok=True)
    tot, den, thieu = 0, [], []
    for c in codes:
        for sk in ("001", "002"):
            p = os.path.join(VAO, sk, c + ".png")
            if not os.path.exists(p):
                thieu.append(f"{c}_{sk}")
                continue
            im = fit(p, 1080, 1920, K, TAM)
            m = np.asarray(im).max(2) <= 6   # nen den o mep (toc/vo den o giua khong tinh)
            xau = max(m[:40].mean(), m[-40:].mean(), m[:, :40].mean(), m[:, -40:].mean()) > 0.05
            out = os.path.join(RA, "_nen_den" if xau else "", f"{c}_{sk}.jpg")
            toi_uu(dong_dau(im, AT[2], AT[3])).save(out, quality=95, subsampling=0, optimize=True, icc_profile=SRGB)
            if xau:
                den.append(f"{c}_{sk}")
            else:
                tot += 1
    print(f"xong: {tot} anh -> {RA}; nen den {len(den)} -> kho/_nen_den; thieu {len(thieu)}", thieu or "")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(GOC, "spec_kho.txt")))
