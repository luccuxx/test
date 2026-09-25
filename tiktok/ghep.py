"""Ghep anh TikTok (chi co watermark howtocheckmap, wm.py), khong dat noi dung chinh vao vung giao dien TikTok che:
  ghep_anhkim_NN.png      1080x1920: 2 o 9:8 (001 tren, 002 duoi) nam gon trong vung an toan;
                          ngoai vung an toan la chinh 2 anh do lam mo, toi di
  rieng_anhkim_NN_00X.png 1080x1920 tung skin; render 9:16 rong hon K (mo_fov.py) roi cat sao cho
                          tam khung (diem camera nhin) nam giua vung an toan
Nguon: _render/{001,002}_{98,916}/<ma>.png (RenderAnglesCli, spec25.txt)."""
import os
import sys
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from vang import vang_bong
from mo_fov import K
from wm import dong_dau

GOC = os.path.dirname(os.path.abspath(__file__))
R, OUT = os.path.join(GOC, "_render"), os.path.join(GOC, "anh")
AT = (60, 150, 950, 1500)   # vung an toan tren 1080x1920: tren 150 (tab), duoi 420 (caption, nut), phai 130 (cot icon)
TAM = ((AT[0] + AT[2]) / 2 / 1080, (AT[1] + AT[3]) / 2 / 1920)
KHE = 12                    # khe giua 2 o trong anh ghep


def fit(path, w, h, zoom=1.0, tam=(0.5, 0.5)):
    """Cat vien den, cat theo ti le w:h; zoom > 1: cat tiep 1/zoom sao cho tam anh goc roi vao vi tri tam (ti le) cua anh ra."""
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).max(2)
    rows, cols = np.where(a.max(1) > 6)[0], np.where(a.max(0) > 6)[0]
    cut = max(rows[0], a.shape[0] - 1 - rows[-1]), max(cols[0], a.shape[1] - 1 - cols[-1])   # vien den, cat doi xung
    im = im.crop((cut[1], cut[0], im.width - cut[1], im.height - cut[0]))
    if im.width / im.height > w / h:
        nw = round(im.height * w / h); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = round(im.width * h / w); y = (im.height - nh) // 2; im = im.crop((0, y, im.width, y + nh))
    if zoom > 1:
        sw, sh = im.width / zoom, im.height / zoom
        x0 = min(max(im.width / 2 - tam[0] * sw, 0), im.width - sw)
        y0 = min(max(im.height / 2 - tam[1] * sh, 0), im.height - sh)
        im = im.crop((round(x0), round(y0), round(x0 + sw), round(y0 + sh)))
    return vang_bong(im.resize((w, h), Image.LANCZOS), 1.8, 0.8)


def slide(o):
    """o: 2 anh 1080x960 (001, 002) -> 1080x1920; 2 o nam gon trong vung an toan, nen la chinh 2 anh lam mo."""
    g = Image.new("RGB", (1080, 1920))
    for k, im in enumerate(o):
        g.paste(im, (0, 960 * k))
    g = ImageEnhance.Brightness(g.filter(ImageFilter.GaussianBlur(30))).enhance(0.55)
    ch = (AT[3] - AT[1] - KHE) // 2
    cw = round(ch * 9 / 8)
    x = AT[0] + (AT[2] - AT[0] - cw) // 2
    for k, im in enumerate(o):
        g.paste(im.resize((cw, ch), Image.LANCZOS), (x, AT[1] + k * (ch + KHE)))
    return dong_dau(g, x + cw, AT[3])   # goc phai-duoi o duoi


def main():
    os.makedirs(OUT, exist_ok=True)
    codes = [l.split("|")[0] for l in open(os.path.join(GOC, "spec25.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]
    thieu = [f"{sk}_{sz}/{c}.png" for c in codes for sk in ("001", "002") for sz in ("98", "916") if not os.path.exists(f"{R}/{sk}_{sz}/{c}.png")]
    if thieu:
        print("thieu anh trong _render (render du 25 goc truoc):", thieu)
        return 1
    den = []
    for i, c in enumerate(codes, 1):
        o = []
        for sk in ("001", "002"):
            o.append(fit(f"{R}/{sk}_98/{c}.png", 1080, 960))
            r = fit(f"{R}/{sk}_916/{c}.png", 1080, 1920, K, TAM)
            dong_dau(r, AT[2], AT[3]).save(f"{OUT}/rieng_anhkim_{i:02d}_{sk}.png")   # goc phai-duoi vung an toan
            m = np.asarray(r).max(2) <= 6   # nen den (troi het) chi o mep; toc/vo den o giua khong tinh
            if max(m[:40].mean(), m[-40:].mean(), m[:, :40].mean(), m[:, -40:].mean()) > 0.05: den.append(f"{c}_{sk}")
        slide(o).save(f"{OUT}/ghep_anhkim_{i:02d}.png")
    print("xong", len(codes), "slide; nen den >1%:", den or "khong")


if __name__ == "__main__":
    sys.exit(main())
