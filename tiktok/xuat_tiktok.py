"""Xuat anh de dang TikTok it bi nen/mo: dung 1080x1920, lam nhe hat lap lanh li ti (de nen), lam net vien,
JPEG chat luong 95, khong giam mau (4:4:4), gan profile sRGB. Chep ca thu muc dang/ sang dien thoai bang cap/Drive.
Dung: py xuat_tiktok.py [thu muc anh vao] (mac dinh anh_viral) -> dang/<ten>.jpg"""
import os
import sys
from PIL import Image, ImageCms, ImageFilter

GOC = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()


def toi_uu(im):
    im = im.convert("RGB")
    if im.size != (W, H):
        im = im.resize((W, H), Image.LANCZOS)
    # hat li ti (lap lanh, nhieu) an het dung luong cua bo nen -> lam mem rat nhe truoc, roi lam net vien lon
    im = Image.blend(im, im.filter(ImageFilter.MedianFilter(3)), 0.35)
    return im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=3))


def main(vao):
    ra = os.path.join(GOC, "dang")
    os.makedirs(ra, exist_ok=True)
    ds = sorted(f for f in os.listdir(vao) if f.lower().endswith((".png", ".jpg", ".jpeg")))
    if not ds:
        print("khong co anh trong", vao)
        return 1
    for f in ds:
        p = os.path.join(ra, os.path.splitext(f)[0] + ".jpg")
        toi_uu(Image.open(os.path.join(vao, f))).save(p, quality=95, subsampling=0, optimize=True, icc_profile=SRGB)
        print(f"{f} -> {os.path.basename(p)} ({os.path.getsize(p) // 1024} KB)")
    print("xong", len(ds), "anh ->", ra)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(GOC, "anh_viral")))
