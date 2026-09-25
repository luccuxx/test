"""Tao spec_kho.txt: kho nhieu goc de tu chon anh (moi goc -> 2 anh 9:16, 001 va 002).
Ma = NHOM_SO de xem trong thu muc theo nhom. Chi dung vung goc da do la co nen (|az| nho voi Idleshow, camera game cho Come).
Dung: py tao_kho.py -> spec_kho.txt; roi kho.ps1"""
import os

GOC = os.path.dirname(os.path.abspath(__file__))


def goc(clip, t, xuong, az, el, dist, fov, dy=0):
    return [clip, f"{t:g}", xuong, f"{az:g}", f"{el:g}", f"{dist:g}", f"{fov:g}", f"{dy:g}"]


def kho():
    n = {}
    ra = []

    def them(nhom, dong):
        n[nhom] = n.get(nhom, 0) + 1
        ra.append(f"{nhom}_{n[nhom]:02d}|" + "|".join(dong))

    # Sanh (Idleshow@0), nen troi
    for az in (-20, 0, 20, 35):
        for el in (0, 15):
            them("MAT", goc("Idleshow", 0, "Bip001 Head", az, el, 0.75, 28))           # chan dung
    for az in (0, 20):
        them("MAT", goc("Idleshow", 0, "Bip001 Head", az, 5, 0.45, 25, 0.03))          # mat can
    for az in (-15, 15, 30):
        them("VAI", goc("Idleshow", 0, "Bip001 Neck", az, 5, 1.0, 30, -0.05))          # vai, co
    for az in (-20, 0, 20, 35):
        for el in (5, 20):
            them("NUA", goc("Idleshow", 0, "Bip001 Spine", az, el, 2.2, 30, 0.1))      # nua nguoi
    for az in (-20, 0, 20):
        for el in (-5, 10, 25):
            them("TOAN", goc("Idleshow", 0, "Bip001 Pelvis", az, el, 4.3, 30))         # toan than
    # Doan Come: camera game (luon co nen)
    for t in (1, 2, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14.5, 15, 15.5, 16, 16.5, 17, 19.5, 20, 20.5, 21):
        them("GAME", goc("Come", t, "-", 0, 0, 0, 0))
    # Come: mat va nua nguoi o cac giay mat dep
    for t in (11, 13, 20):
        for az in (-20, 0, 20):
            for el in (0, 10):
                them("CMAT", goc("Come", t, "Bip001 Head", az, el, 0.8, 28))
    for t in (11, 16.5):
        for az in (-15, 15):
            them("CNUA", goc("Come", t, "Bip001 Spine1", az, 10, 1.4, 30, 0.2))
    # Quay lung (Turn2), toc bui
    for t in (1.25, 1.75, 2.25):
        for az in (-30, 0, 30):
            them("LUNG", goc("Idleshow_Turn2", t, "Bip001 Spine", az, 5, 2.6, 30, 0.1))
    for az in (0, 15, 30):
        them("TOC", goc("Idleshow_Turn2", 1.75, "Bip001 Head", az, 0, 0.7, 28))
    # Dang nghi (Rest2)
    for az in (-10, 10):
        them("NGHI", goc("Idleshow_Rest2", 3, "Bip001 Pelvis", az, 10, 4.2, 30))
        them("NGHI", goc("Idleshow_Rest2", 3, "Bip001 Head", az, 5, 0.8, 28))
    return ra


if __name__ == "__main__":
    d = kho()
    p = os.path.join(GOC, "spec_kho.txt")
    with open(p, "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(d) + "\n")
    print(len(d), "goc x 2 skin =", 2 * len(d), "anh ->", p)
