"""Hau ky vang kim loai: mat na mem theo mau vang, tang do bong, nhat mau (nhat), them diem sang am."""
import numpy as np
from PIL import Image


def vang_bong(im, s=1.0, nhat=0.0):
    a = np.asarray(im.convert("RGB"), np.float32) / 255
    mx, mn = a.max(2), a.min(2)
    c = mx - mn
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    h = np.where(mx == r, (g - b) / (c + 1e-6) % 6, np.where(mx == g, (b - r) / (c + 1e-6) + 2, (r - g) / (c + 1e-6) + 4)) * 60
    sat = c / (mx + 1e-6)
    wh = np.clip(1 - abs(h - 45) / 18, 0, 1)
    ws = np.clip((sat - 0.18) / 0.15, 0, 1)
    wv = np.clip((mx - 0.25) / 0.2, 0, 1)
    w = np.clip(wh * ws * wv * s, 0, 1)[..., None]
    k = max(s, 1)
    t = a * (1 + 0.18 * k)
    t = (t - 0.5) * (1 + 0.22 * k) + 0.5 + 0.04 * k
    lum = (t * [0.299, 0.587, 0.114]).sum(2, keepdims=True)
    t = lum + (t - lum) * (1 + 0.08 * k) * (1 - 0.45 * nhat) + 0.06 * nhat
    lum = (t * [0.299, 0.587, 0.114]).sum(2, keepdims=True)
    spec = np.clip((lum - (0.78 - 0.08 * k)) / 0.28, 0, 1) ** 2 * min(0.35 * k, 0.8)
    t = t * (1 - spec) + np.array([1, 0.97, 0.88]) * spec
    out = a * (1 - w) + np.clip(t, 0, 1) * w
    return Image.fromarray((np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8))


if __name__ == "__main__":
    x = Image.new("RGB", (4, 1), (200, 160, 40))   # vang -> bi doi
    y = Image.new("RGB", (4, 1), (40, 80, 200))    # xanh -> giu nguyen
    assert vang_bong(x, 1.8, 0.8).getpixel((0, 0)) != x.getpixel((0, 0))
    assert vang_bong(y, 1.8, 0.8).getpixel((0, 0)) == y.getpixel((0, 0))
    print("ok")
