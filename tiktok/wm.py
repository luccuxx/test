"""Dong dau chu (watermark) len anh xuat: chu trang ban trong suot, bong mo, can phai-duoi tai (phai, day).
Doi WM = "" de tat."""
from PIL import Image, ImageDraw, ImageFilter, ImageFont

WM = "howtocheckmap"
CO = 34          # co chu (px, tren khung 1080x1920)
LE = 18          # cach mep o / vung an toan


def _font(co):
    for f in ("segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(f, co)
        except OSError:
            pass
    return ImageFont.load_default(co)


def dong_dau(im, phai, day, chu=WM, co=CO):
    """Tra ve anh moi co chu, mep phai cua chu tai x = phai - LE, mep duoi tai y = day - LE."""
    if not chu:
        return im
    f = _font(co)
    x0, y0, x1, y1 = f.getbbox(chu)
    x, y = phai - LE - x1, day - LE - y1
    lop = Image.new("L", im.size, 0)
    ImageDraw.Draw(lop).text((x, y), chu, font=f, fill=255)
    bong = lop.filter(ImageFilter.GaussianBlur(3))
    out = im.convert("RGB")
    out.paste((0, 0, 0), mask=bong.point(lambda v: v * 45 // 100))
    out.paste((255, 255, 255), mask=lop.point(lambda v: v * 70 // 100))
    return out
