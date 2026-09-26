import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle

# ---- Tham số ----
B1    = 0.35   # băng thông không gian (chu kỳ/pixel), giới hạn |F1| <= B1
v1    = 1.0    # vận tốc vùng chuyển động (pixel/khung)
alpha = 1/4    # hệ số bộ lọc đệ quy ở vùng tĩnh
HIEN_TIEU_DE = True   # đặt False nếu dùng caption của Word thay cho tiêu đề trong ảnh

# Tần số cắt -3 dB của bộ lọc đệ quy H(z) = alpha / (1 - (1-alpha) z^-1)
Fc = np.arccos((1 + (1 - alpha)**2 - 2 * alpha**2) / (2 * (1 - alpha))) / (2 * np.pi)
Bt = B1 * abs(v1)

INK, BLUE, RED, NOISE, MUTED = "#0b0b0b", "#2a78d6", "#e34948", "#a3a29c", "#52514e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
NHAN = dict(fontsize=11.5, bbox=dict(fc="white", ec="none", alpha=.92, pad=3), zorder=6)

# Nhiễu trắng: chấm ngẫu nhiên rải đều khắp miền tần số (cùng một bộ chấm cho cả 3 hình)
nhieu = np.random.default_rng(7).uniform(-.5, .5, size=(420, 2))

H_GIU = Line2D([], [], color=INK, lw=4, label="Phổ tín hiệu được giữ lại")
H_CAT = Line2D([], [], color=RED, lw=4, ls=(0, (3, 1.5)), label="Phổ tín hiệu bị cắt")
H_DAI = Patch(color=BLUE, alpha=.35, label="Dải thông bộ lọc")
H_NHIEU = Line2D([], [], color=NOISE, marker="o", ls="", ms=5, label="Nhiễu (trải khắp)")
H_TIN_HIEU = Line2D([], [], color=INK, lw=4, label="Phổ tín hiệu (cảnh vật)")


def ve_hinh(ten_file, tieu_de, dai, v, chu_thich):
    fig, ax = plt.subplots(figsize=(6.6, 7.4))
    ax.scatter(nhieu[:, 0], nhieu[:, 1], s=9, color=NOISE, lw=0, zorder=1)
    if dai is None:          # không dùng bộ lọc: không vẽ dải thông, giữ toàn bộ tín hiệu
        dai = .5
    else:
        ax.add_patch(Rectangle((-.5, -dai), 1, 2 * dai, color=BLUE, alpha=.35, lw=0, zorder=2))
        if dai < .5:
            for y in (dai, -dai):
                ax.axhline(y, color=BLUE, ls="--", lw=1.2, zorder=2)
    ax.axhline(0, color="#8a8984", lw=.8, zorder=2)
    ax.axvline(0, color="#8a8984", lw=.8, zorder=2)

    # Phổ tín hiệu: đoạn Ft = -v*F1 với |F1| <= B1; phần ngoài dải thông vẽ đỏ nét đứt
    F1 = np.linspace(-B1, B1, 801)
    Ft = -v * F1
    trong = np.abs(Ft) <= dai
    ax.plot(F1[trong], Ft[trong], color=INK, lw=4, zorder=4, solid_capstyle="butt")
    for nua in (F1 < 0, F1 > 0):
        sel = nua & ~trong
        if sel.any():
            ax.plot(F1[sel], Ft[sel], color=RED, lw=4, ls=(0, (3, 1.5)), zorder=4)

    ax.set(xlim=(-.5, .5), ylim=(-.5, .5), aspect="equal",
           xlabel=r"Tần số không gian $F_1$ (chu kỳ/pixel)",
           ylabel=r"Tần số thời gian $F_t$ (chu kỳ/khung)")
    if HIEN_TIEU_DE:
        ax.set_title(tieu_de, fontsize=13.5, pad=10)
    handles = chu_thich(ax)
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False, fontsize=11.5)
    fig.tight_layout(rect=(0, .08, 1, 1))
    fig.savefig(ten_file + ".png", dpi=220)
    fig.savefig(ten_file + ".svg")
    plt.close(fig)


def chu_thich_khong_loc(ax):
    for x, s in ((-B1, r"$-B_1$"), (B1, r"$+B_1$")):
        ax.text(x, -.07, s, ha="center", **NHAN)
    ax.annotate("Tín hiệu vùng tĩnh nằm trọn\ntrên đường $F_t = 0$",
                xy=(.25, 0), xytext=(-.02, .2), arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
    ax.text(-.48, .43, "Mọi điểm có $F_t \\neq 0$ đều là nhiễu", **NHAN)
    ax.text(-.48, -.44, "Chưa lọc: nhiễu trải khắp, chồng lên tín hiệu", color=MUTED, **NHAN)
    return [H_TIN_HIEU, H_NHIEU]


def chu_thich_dong_khong_loc(ax):
    for y in (Bt, -Bt):
        ax.axhline(y, color=INK, ls=":", lw=1, zorder=3)
    ax.text(.48, Bt + .02, r"$+B_t = B_1|v_1|$", ha="right", **NHAN)
    ax.text(.48, -Bt - .06, r"$-B_t$", ha="right", **NHAN)
    ax.plot([-B1, -B1], [0, Bt], color=INK, ls=":", lw=1, zorder=3)
    ax.plot([B1, B1], [0, -Bt], color=INK, ls=":", lw=1, zorder=3)
    ax.text(-B1, -.06, r"$-B_1$", ha="center", **NHAN)
    ax.text(B1, .035, r"$+B_1$", ha="center", **NHAN)
    ax.annotate("Tín hiệu nằm trên đường\n$F_t = -v_1 F_1$",
                xy=(-.18, .18), xytext=(.03, .17), arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
    ax.text(-.48, .43, r"Ngoài khoảng $\pm B_t$: chỉ có nhiễu", **NHAN)
    ax.text(-.48, -.44, "Chưa lọc: nhiễu trải khắp, chồng lên tín hiệu", color=MUTED, **NHAN)
    return [H_TIN_HIEU, H_NHIEU]


def chu_thich_tinh(ax):
    ax.text(-.48, Fc + .02, rf"$|F_t| \leq F_c \approx {Fc:.3f}$", color=BLUE, **NHAN)
    for x, s in ((-B1, r"$-B_1$"), (B1, r"$+B_1$")):
        ax.text(x, -Fc - .07, s, ha="center", **NHAN)
    ax.annotate("Chi tiết mảnh, biên (F₁ lớn)\nvẫn nằm trong dải thông\n→ biên KHÔNG bị mờ",
                xy=(.3, 0), xytext=(-.02, .24), arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
    ax.text(-.48, -.44, "Nhiễu nằm ngoài dải xanh → bị loại bỏ", color=MUTED, **NHAN)
    return [H_GIU, H_DAI, H_NHIEU]


def chu_thich_dong(ax):
    for y in (Bt, -Bt):
        ax.axhline(y, color=INK, ls=":", lw=1, zorder=3)
    ax.text(.48, Bt + .02, r"$+B_t = B_1|v_1|$", ha="right", **NHAN)
    ax.text(-.48, -Bt - .06, r"$-B_t$", **NHAN)
    ax.annotate("Phần phổ bị cắt\n→ ghosting, nhòe",
                xy=(-.2, .2), xytext=(.02, .2), color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2), **NHAN)
    ax.annotate(r"Chỉ phần gần gốc lọt qua", xy=(.02, -.015), xytext=(.1, .085),
                arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
    ax.text(-.48, -.22, r"Đường $F_t = -v_1 F_1$", **NHAN)
    return [H_GIU, H_CAT, H_DAI, H_NHIEU]


def chu_thich_alpha1(ax):
    ax.text(-.48, .43, "Dải thông mở toàn miền (α = 1)", **NHAN)
    ax.annotate("Toàn bộ phổ tín hiệu lọt qua\n→ không ghosting",
                xy=(-.22, .22), xytext=(-.02, .26), arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
    ax.text(-.48, -.44, "Nhiễu cũng lọt qua → vùng động vẫn còn nhiễu", color=MUTED, **NHAN)
    return [H_GIU, H_DAI, H_NHIEU]


ve_hinh("hinh0_vung_tinh_khong_loc", "Vùng tĩnh (v = 0), chưa qua bộ lọc", None, 0,
        chu_thich_khong_loc)
ve_hinh("hinh0b_vung_dong_khong_loc", f"Vùng chuyển động (v₁ = {v1:g} px/khung), chưa qua bộ lọc",
        None, v1, chu_thich_dong_khong_loc)
ve_hinh("hinh1_vung_tinh", "Vùng tĩnh (v = 0), bộ lọc α = 1/4", Fc, 0, chu_thich_tinh)
ve_hinh("hinh2_vung_dong_loc_manh", f"Vùng chuyển động (v₁ = {v1:g} px/khung), vẫn α = 1/4",
        Fc, v1, chu_thich_dong)
ve_hinh("hinh3_vung_dong_alpha1", "Vùng chuyển động, bộ phát hiện đặt α = 1",
        .5, v1, chu_thich_alpha1)
print(f"Fc = {Fc:.4f} chu kỳ/khung, Bt = {Bt:.2f} chu kỳ/khung")
