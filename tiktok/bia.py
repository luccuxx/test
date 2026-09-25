"""Anh bia dau bai/video (1080x1920): tieu de "CHON TEAM NAO?", 2 khung canh dep nhat (tren MAC DINH, duoi TUYET SAC)
voi huy hieu VS o giua, dong cuoi "XEM HET ROI CHON NHE!", watermark; moi thu nam trong vung an toan TikTok.
Chu trang/vang vien den. Doi chu o TIEU_DE / CUOI (nhan.py: ten skin).
Dung: py bia.py [ma goc = dong dau spec_viral.txt] [nguon = _render] [ra = bai_dang] -> <ra>/00_bia.jpg (dung truoc slide 01)"""
import os
import sys
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
from ghep import fit, AT, GOC
from nhan import NHAN, gan_nhan
from wm import _font, dong_dau
from xuat_tiktok import toi_uu, SRGB

TIEU_DE = "CHỌN TEAM NÀO?"
CUOI = "XEM HẾT RỒI CHỌN NHÉ!"
LUOI = 250          # luoi trang ca nhan TikTok chi hien 3:4 giua anh (y 240-1680): tieu de phai nam duoi muc nay
VANG, TRANG, DEN = (255, 214, 64), (255, 255, 255), (0, 0, 0)


def chu_giua(d, y, chu, co, mau, vien):
    """Chu can giua vung an toan; tu thu nho neu dai hon be ngang vung an toan."""
    while True:
        f = _font(co)
        x0, y0, x1, y1 = d.textbbox((0, 0), chu, font=f, stroke_width=vien)
        if x1 - x0 <= AT[2] - AT[0] - 20 or co <= 30:
            break
        co -= 2
    cx = (AT[0] + AT[2]) // 2
    d.text((cx - (x0 + x1) // 2, y - y0), chu, font=f, fill=mau, stroke_width=vien, stroke_fill=DEN)
    return y + (y1 - y0)


def main(ma, nguon, ra):
    nguon, ra = (p if os.path.isabs(p) else os.path.join(GOC, p) for p in (nguon, ra))
    o = [fit(f"{nguon}/{sk}_98/{ma}.png", 1080, 960) for sk in ("001", "002")]
    g = Image.new("RGB", (1080, 1920))
    for k, im in enumerate(o):
        g.paste(im, (0, 960 * k))
    g = ImageEnhance.Brightness(g.filter(ImageFilter.GaussianBlur(30))).enhance(0.45)
    d = ImageDraw.Draw(g)
    tren = chu_giua(d, LUOI + 12, TIEU_DE, 92, VANG, 8) + 26               # tieu de (trong o luoi trang ca nhan)
    duoi = AT[3] - 12 - 70                                               # cho dong cuoi
    khe = 40
    ch = (duoi - 20 - tren - khe) // 2
    cw = round(ch * 9 / 8)
    x = AT[0] + (AT[2] - AT[0] - cw) // 2
    khung = [(x, tren + k * (ch + khe), cw, ch) for k in range(2)]
    for im, (kx, ky, w, h) in zip(o, khung):
        g.paste(im.resize((w, h), Image.LANCZOS), (kx, ky))
        d.rectangle((kx - 3, ky - 3, kx + w + 2, ky + h + 2), outline=TRANG, width=3)
    g, _ = gan_nhan(g, khung, [NHAN["001"], NHAN["002"]])
    d = ImageDraw.Draw(g)
    cy, r = tren + ch + khe // 2, 62                                     # huy hieu VS giua 2 khung
    cx = x + cw // 2
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(220, 30, 50), outline=TRANG, width=6)
    f = _font(64)
    x0, y0, x1, y1 = d.textbbox((0, 0), "VS", font=f, stroke_width=3)
    d.text((cx - (x0 + x1) // 2, cy - (y0 + y1) // 2), "VS", font=f, fill=TRANG, stroke_width=3, stroke_fill=DEN)
    chu_giua(d, duoi, CUOI, 60, TRANG, 6)
    kx, ky, w, h = khung[1]
    g = dong_dau(g, kx + w, ky + h)
    os.makedirs(ra, exist_ok=True)
    out = os.path.join(ra, "00_bia.jpg")
    toi_uu(g).save(out, quality=95, subsampling=0, optimize=True, icc_profile=SRGB)
    print("xong:", out)


if __name__ == "__main__":
    a = sys.argv[1:]
    ma = a[0] if a else open(os.path.join(GOC, "spec_viral.txt"), encoding="utf-8").readline().split("|")[0]
    sys.exit(main(ma, a[1] if len(a) > 1 else "_render", a[2] if len(a) > 2 else "bai_dang"))
