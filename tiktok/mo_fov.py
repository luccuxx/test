"""Mo rong fov cua spec cho khung 9:16 them K lan (theo tan), de ghep.py cat doi tam nhan vat vao vung an toan TikTok
ma van giu du bo cuc cua spec. Dong camera game (fov 0) giu nguyen. Dung: py mo_fov.py <spec vao> <spec ra> [K]"""
import math
import sys

K = 1.15


def mo(dong, k=K):
    f = dong.rstrip("\r\n").split("|")
    fov = float(f[7])
    if fov > 0:
        f[7] = f"{2 * math.degrees(math.atan(k * math.tan(math.radians(fov / 2)))):.3f}"
    return "|".join(f)


def main(vao, ra, k=K):
    dong = [l for l in open(vao, encoding="utf-8") if l.strip() and not l.startswith("#")]
    with open(ra, "w", encoding="ascii", newline="\n") as f:
        f.write("".join(mo(l, k) + "\n" for l in dong))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else K)
