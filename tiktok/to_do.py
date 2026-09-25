"""To do goc: ghep _do/{001,002}/<ma>.png thanh _do/to_do_N.jpg (khong chu, chi de chon goc).
Moi o = 1 dong spec: trai 001, phai 002, da doi tam vao vung an toan giong anh cuoi. COT o moi hang, HANG hang moi trang,
theo thu tu dong spec: trai sang phai, tren xuong duoi. Nen xam = o trong (thieu anh). In ra ma cua tung o va o nen den.
Dung: py to_do.py [spec] [so cot = 3] [so hang moi trang = 5] [khung 916|98]
(spec tu tao_do.py: dung 5 cot = a..e cua 1 goc tren 1 hang; khung 98 = o 9:8 giong anh ghep/viral)"""
import os
import sys
import numpy as np
from PIL import Image
from ghep import fit, TAM
from mo_fov import K

GOC = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(GOC, "_do")
GAP = 24


def main(spec, cot=3, hang=5, khung="916"):
    codes = [l.split("|")[0] for l in open(spec, encoding="utf-8") if l.strip() and not l.startswith("#")]
    if khung == "98":
        W, H = (320, 284) if cot <= 3 else (240, 213)
    else:
        W, H = (270, 480) if cot <= 3 else (180, 320)
    moi_trang = cot * hang
    for tr in range(0, len(codes), moi_trang):
        phan = codes[tr:tr + moi_trang]
        rows = (len(phan) + cot - 1) // cot
        sheet = Image.new("RGB", (cot * (2 * W + GAP) - GAP, rows * (H + GAP) - GAP), (128, 128, 128))
        so_trang = tr // moi_trang + 1
        for i, c in enumerate(phan):
            x0, y0 = (i % cot) * (2 * W + GAP), (i // cot) * (H + GAP)
            ghi = []
            for k, sk in enumerate(("001", "002")):
                p = f"{D}/{sk}/{c}.png"
                if not os.path.exists(p):
                    ghi.append(f"{sk} thieu")
                    continue
                im = fit(p, 1080, 960) if khung == "98" else fit(p, 1080, 1920, K, TAM)   # giong het anh cuoi
                m = np.asarray(im).max(2) <= 6    # nen den chi tinh o mep (toc/vo den o giua khong tinh)
                if max(m[:40].mean(), m[-40:].mean(), m[:, :40].mean(), m[:, -40:].mean()) > 0.05:
                    ghi.append(f"{sk} nen den")
                sheet.paste(im.resize((W, H), Image.LANCZOS), (x0 + k * W, y0))
            print(f"trang {so_trang}, hang {i // cot + 1}, cot {i % cot + 1}: {c}", *ghi)
        out = os.path.join(D, f"to_do_{so_trang}.jpg")
        sheet.save(out, quality=88)
        print("xong:", out)


if __name__ == "__main__":
    a = sys.argv[1:]
    sys.exit(main(a[0] if a else os.path.join(GOC, "spec_do.txt"), int(a[1]) if len(a) > 1 else 3, int(a[2]) if len(a) > 2 else 5, a[3] if len(a) > 3 else "916"))
