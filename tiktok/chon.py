"""Ghi bien the da chon trong spec_do.txt (tao_do.py) de len dong cung ma trong spec.
Dung: py chon.py [--spec spec_viral.txt] V04Z=c V07Z=b ...   (a = giu nguyen)"""
import os
import sys

GOC = os.path.dirname(os.path.abspath(__file__))


def main(args):
    spec = os.path.join(GOC, "spec_viral.txt")
    if args[:1] == ["--spec"]:
        spec, args = args[1], args[2:]
    if not os.path.isabs(spec):
        spec = os.path.join(GOC, spec)
    do = {l.split("|")[0]: l.rstrip("\r\n") for l in open(os.path.join(GOC, "spec_do.txt"), encoding="utf-8") if l.strip()}
    dong = [l.rstrip("\r\n") for l in open(spec, encoding="utf-8")]
    ma_dong = {l.split("|")[0]: i for i, l in enumerate(dong) if l.strip() and not l.startswith("#")}
    loi = 0
    for a in args:
        ma, _, v = a.partition("=")
        if ma not in ma_dong or ma + v not in do:
            print("bo qua", a, "(khong co ma trong spec hoac bien the trong spec_do.txt)")
            loi = 1
            continue
        moi = "|".join([ma] + do[ma + v].split("|")[1:])
        print(f"{ma}: {dong[ma_dong[ma]]}\n   -> {moi}")
        dong[ma_dong[ma]] = moi
    with open(spec, "w", encoding="ascii", newline="\n") as f:
        f.write("\n".join(dong) + "\n")
    return loi


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
