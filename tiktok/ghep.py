"""Ghep anh TikTok (khong chu, khong watermark):
  ghep_anhkim_NN.png      1080x1920: 001 tren (1080x960, 9:8), 002 duoi
  rieng_anhkim_NN_00X.png 1080x1920 tung skin
Nguon: _render/{001,002}_{98,916}/<ma>.png (RenderAnglesCli, spec25.txt)."""
import os
import sys
import numpy as np
from PIL import Image
from vang import vang_bong

GOC = os.path.dirname(os.path.abspath(__file__))
R, OUT = os.path.join(GOC, "_render"), os.path.join(GOC, "anh")


def fit(path, w, h):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).max(2)
    rows, cols = np.where(a.max(1) > 6)[0], np.where(a.max(0) > 6)[0]
    cut = max(rows[0], a.shape[0] - 1 - rows[-1]), max(cols[0], a.shape[1] - 1 - cols[-1])   # vien den, cat doi xung
    im = im.crop((cut[1], cut[0], im.width - cut[1], im.height - cut[0]))
    if im.width / im.height > w / h:
        nw = round(im.height * w / h); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = round(im.width * h / w); y = (im.height - nh) // 2; im = im.crop((0, y, im.width, y + nh))
    return vang_bong(im.resize((w, h), Image.LANCZOS), 1.8, 0.8)


def main():
    os.makedirs(OUT, exist_ok=True)
    codes = [l.split("|")[0] for l in open(os.path.join(GOC, "spec25.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]
    thieu = [f"{sk}_{sz}/{c}.png" for c in codes for sk in ("001", "002") for sz in ("98", "916") if not os.path.exists(f"{R}/{sk}_{sz}/{c}.png")]
    if thieu:
        print("thieu anh trong _render (render du 25 goc truoc):", thieu)
        return 1
    den = []
    for i, c in enumerate(codes, 1):
        g = Image.new("RGB", (1080, 1920))
        for k, sk in enumerate(("001", "002")):
            g.paste(fit(f"{R}/{sk}_98/{c}.png", 1080, 960), (0, 960 * k))
            r = fit(f"{R}/{sk}_916/{c}.png", 1080, 1920)
            r.save(f"{OUT}/rieng_anhkim_{i:02d}_{sk}.png")
            m = np.asarray(r).max(2) <= 6   # nen den (troi het) chi o mep; toc/vo den o giua khong tinh
            if max(m[:40].mean(), m[-40:].mean(), m[:, :40].mean(), m[:, -40:].mean()) > 0.05: den.append(f"{c}_{sk}")
        g.save(f"{OUT}/ghep_anhkim_{i:02d}.png")
    print("xong", len(codes), "slide; nen den >1%:", den or "khong")


if __name__ == "__main__":
    sys.exit(main())
