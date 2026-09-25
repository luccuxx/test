"""Chu ten skin tren anh so sanh: chu to trang vien den, dat o goc it chi tiet nhat cua o (khong de len nhan vat).
Ca 2 o dung chung 1 goc cho dong deu; bo goc phai-duoi (cho watermark)."""
import numpy as np
from PIL import ImageDraw
from wm import _font

NHAN = {"001": "MẶC ĐỊNH", "002": "TUYỆT SẮC"}
CO, VIEN, LE = 64, 6, 22    # co chu, do day vien den, cach mep o (px tren khung 1080x1920)


def _nang_luong(g, box):
    x0, y0, x1, y1 = box
    v = g[y0:y1, x0:x1]
    return np.abs(np.diff(v, axis=0)).mean() + np.abs(np.diff(v, axis=1)).mean()


def gan_nhan(slide, o, chu):
    """slide: anh ghep 1080x1920; o: [(x, y, rong, cao)] cua tung o; chu: [chu cho tung o]. Tra ve (anh, goc da chon)."""
    f = _font(CO)
    d = ImageDraw.Draw(slide)
    g = np.asarray(slide.convert("L"), np.float32)
    kich = [d.textbbox((0, 0), c, font=f, stroke_width=VIEN) for c in chu]

    def vi_tri(goc, k):
        x, y, w, h = o[k]
        bx0, by0, bx1, by1 = kich[k]
        tx = x + LE - bx0 if goc[1] == "T" else x + w - LE - bx1
        ty = y + LE - by0 if goc[0] == "T" else y + h - LE - by1
        return tx, ty, (tx + bx0, ty + by0, tx + bx1, ty + by1)

    goc = min(("TT", "TP", "DT"), key=lambda gc: sum(_nang_luong(g, vi_tri(gc, k)[2]) for k in range(len(o))))
    for k, c in enumerate(chu):
        tx, ty, _ = vi_tri(goc, k)
        d.text((tx, ty), c, font=f, fill=(255, 255, 255), stroke_width=VIEN, stroke_fill=(0, 0, 0))
    return slide, goc
