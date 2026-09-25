"""Tao spec do quanh tung dong cua 1 spec, de tim goc khong bi tay/vi/dan che. Moi dong -> 5 bien the, ma = ma goc + a..e:
  xuong (bone):    a goc | b az-25 | c az+25 | d el+20 | e giay+0.5 (tay da di cho khac)
  camera game (-): a goc | b giay-0.5 | c giay+0.5 | d giay+1 | e giay+1.5
az giu trong [-60, 60] (xa hon la nen den), el <= 45, giay >= 0.
Dung: py tao_do.py [spec vao = spec_viral.txt] [spec ra = spec_do.txt]
      roi do_goc.ps1 -Cot 5 -W 720 -H 1280; chon xong: py chon.py V04Z=c V07Z=b ..."""
import os
import sys

GOC = os.path.dirname(os.path.abspath(__file__))


def so(x):
    return f"{x:g}"


def bien_the(dong):
    f = dong.rstrip("\r\n").split("|")
    ma, t = f[0], float(f[2])
    if f[3] == "-":
        return [(ma + v, f[:2] + [so(max(0, t + d))] + f[3:]) for v, d in zip("abcde", (0, -0.5, 0.5, 1, 1.5))]
    az, el = float(f[4]), float(f[5])
    thu = [(0, 0, 0), (-25, 0, 0), (25, 0, 0), (0, 20, 0), (0, 0, 0.5)]
    return [(ma + v, f[:2] + [so(t + dt)] + [f[3], so(max(-60, min(60, az + da))), so(min(45, el + de))] + f[6:])
            for v, (da, de, dt) in zip("abcde", thu)]


def main(vao, ra):
    dong = [l for l in open(vao, encoding="utf-8") if l.strip() and not l.startswith("#")]
    with open(ra, "w", encoding="ascii", newline="\n") as out:
        for l in dong:
            for ma, f in bien_the(l):
                out.write("|".join([ma] + f[1:]) + "\n")
    print(len(dong), "goc x 5 bien the ->", ra)


if __name__ == "__main__":
    a = sys.argv[1:]
    main(a[0] if a else os.path.join(GOC, "spec_viral.txt"), a[1] if len(a) > 1 else os.path.join(GOC, "spec_do.txt"))
