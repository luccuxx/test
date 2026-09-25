"""Anh bia toan than 2 skin dung canh nhau (1080x1920): trai 001 MAC DINH, phai 002 TUYET SAC, huy hieu VS giua,
tieu de "CHON TEAM NAO?" (bia.TIEU_DE), watermark; tat ca trong vung an toan TikTok va trong o luoi 3:4 trang ca nhan.
Nguon: anh 9:16 cua 2 skin: <nguon>/<skin>_916/<ma>.png (render_tiktok) hoac _kho/<skin>/<ma>.png (kho.ps1, vd TOAN_05).
Render goc mac dinh: render_tiktok.ps1 -Spec spec_bia.txt -Ghep bia_toan.py
Dung: py bia_toan.py [ma = BIA] [nguon = _render] [ra = bai_dang] -> <ra>/00_bia_toan.jpg"""
import os
import sys
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
from bia import TIEU_DE, LUOI, VANG, TRANG, DEN, chu_giua
from ghep import fit, AT, GOC
from nhan import NHAN
from wm import _font, dong_dau
from xuat_tiktok import toi_uu, SRGB

KHE = 16


def tim(nguon, sk, ma):
    for p in (f"{nguon}/{sk}_916/{ma}.png", f"{nguon}/{sk}/{ma}.png"):
        if os.path.exists(p):
            return p
    raise SystemExit(f"khong thay anh 9:16 cua {sk} {ma} trong {nguon}")


def main(ma, nguon, ra):
    nguon, ra = (p if os.path.isabs(p) else os.path.join(GOC, p) for p in (nguon, ra))
    nen = Image.new("RGB", (1080, 1920))
    for k, sk in enumerate(("001", "002")):
        nen.paste(fit(tim(nguon, sk, ma), 540, 1920), (540 * k, 0))
    g = ImageEnhance.Brightness(nen.filter(ImageFilter.GaussianBlur(30))).enhance(0.45)
    d = ImageDraw.Draw(g)
    tren = chu_giua(d, LUOI + 12, TIEU_DE, 92, VANG, 8) + 24
    day = AT[3] - 10
    w = (AT[2] - AT[0] - KHE) // 2
    h = day - tren
    khung = [(AT[0] + k * (w + KHE), tren, w, h) for k in range(2)]
    f = _font(51)
    for k, (sk, (x, y, kw, kh)) in enumerate(zip(("001", "002"), khung)):
        g.paste(fit(tim(nguon, sk, ma), kw, kh), (x, y))
        d.rectangle((x - 3, y - 3, x + kw + 2, y + kh + 2), outline=TRANG, width=3)
        chu = NHAN[sk]                                                   # ten skin can giua, o khoang troi tren dau
        x0, y0, x1, y1 = d.textbbox((0, 0), chu, font=f, stroke_width=5)
        d.text((x + (kw - (x0 + x1)) // 2, y + 20 - y0), chu, font=f, fill=TRANG, stroke_width=5, stroke_fill=DEN)
    cx, cy, r = (AT[0] + AT[2]) // 2, tren + h // 2, 62                  # huy hieu VS giua 2 khung
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(220, 30, 50), outline=TRANG, width=6)
    fv = _font(64)
    x0, y0, x1, y1 = d.textbbox((0, 0), "VS", font=fv, stroke_width=3)
    d.text((cx - (x0 + x1) // 2, cy - (y0 + y1) // 2), "VS", font=fv, fill=TRANG, stroke_width=3, stroke_fill=DEN)
    x, y, kw, kh = khung[1]
    g = dong_dau(g, x + kw, y + kh)
    os.makedirs(ra, exist_ok=True)
    out = os.path.join(ra, "00_bia_toan.jpg")
    toi_uu(g).save(out, quality=95, subsampling=0, optimize=True, icc_profile=SRGB)
    print("xong:", out)


if __name__ == "__main__":
    a = sys.argv[1:]
    sys.exit(main(a[0] if a else "BIA", a[1] if len(a) > 1 else "_render", a[2] if len(a) > 2 else "bai_dang"))
