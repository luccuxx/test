"""To do goc: ghep _do/{001,002}/<ma>.png thanh _do/to_do.jpg (khong chu, chi de chon goc).
Moi o = 1 dong spec: trai 001, phai 002. 3 o moi hang, theo thu tu dong spec: trai sang phai, tren xuong duoi.
Nen xam = o trong (thieu anh). In ra ma cua tung o va o nao nen den."""
import os
import sys
import numpy as np
from PIL import Image

GOC = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(GOC, "_do")
W, H, GAP, COT = 360, 320, 24, 3


def main(spec):
    codes = [l.split("|")[0] for l in open(spec, encoding="utf-8") if l.strip() and not l.startswith("#")]
    rows = (len(codes) + COT - 1) // COT
    sheet = Image.new("RGB", (COT * (2 * W + GAP) - GAP, rows * (H + GAP) - GAP), (128, 128, 128))
    for i, c in enumerate(codes):
        x0, y0 = (i % COT) * (2 * W + GAP), (i // COT) * (H + GAP)
        ghi = []
        for k, sk in enumerate(("001", "002")):
            p = f"{D}/{sk}/{c}.png"
            if not os.path.exists(p):
                ghi.append(f"{sk} thieu")
                continue
            im = Image.open(p).convert("RGB")
            m = np.asarray(im).max(2) <= 6   # nen den chi tinh o mep (toc/vo den o giua khong tinh)
            if max(m[:40].mean(), m[-40:].mean(), m[:, :40].mean(), m[:, -40:].mean()) > 0.05:
                ghi.append(f"{sk} nen den")
            sheet.paste(im.resize((W, H), Image.LANCZOS), (x0 + k * W, y0))
        print(f"o {i + 1:2d} (hang {i // COT + 1}, cot {i % COT + 1}): {c}", *ghi)
    out = os.path.join(D, "to_do.jpg")
    sheet.save(out, quality=88)
    print("xong:", out)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(GOC, "spec_do.txt")))
