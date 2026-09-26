import numpy as np
import matplotlib.pyplot as plt

# ---- Tham số ----
B1    = 0.35   # băng thông không gian (chu kỳ/pixel), giới hạn |F1| <= B1
v1    = 1.0    # vận tốc vùng chuyển động (pixel/khung)
alpha = 1/4    # hệ số bộ lọc đệ quy ở vùng tĩnh

# Tần số cắt -3 dB của bộ lọc đệ quy H(z) = alpha / (1 - (1-alpha) z^-1)
c  = (1 + (1 - alpha)**2 - 2 * alpha**2) / (2 * (1 - alpha))
Fc = np.arccos(c) / (2 * np.pi)          # ~0.046 chu kỳ/khung với alpha = 1/4
Bt = B1 * abs(v1)                         # băng thông thời gian vùng chuyển động

GRAY, BLUE, RED, INK = "#dcdbd6", "#2a78d6", "#e34948", "#0b0b0b"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})


def khung_pho(ax, title, band):
    """Vẽ nền nhiễu (xám, trải đều) và dải thông bộ lọc (xanh, |Ft| <= band)."""
    ax.add_patch(plt.Rectangle((-.5, -.5), 1, 1, color=GRAY, zorder=0))
    ax.add_patch(plt.Rectangle((-.5, -band), 1, 2 * band, color=BLUE, alpha=.45, zorder=1))
    ax.axhline(0, color="#8a8984", lw=.8, zorder=2)
    ax.axvline(0, color="#8a8984", lw=.8, zorder=2)
    ax.set(xlim=(-.5, .5), ylim=(-.5, .5), aspect="equal", title=title,
           xlabel=r"Tần số không gian $F_1$ (chu kỳ/pixel)",
           ylabel=r"Tần số thời gian $F_t$ (chu kỳ/khung)")
    ax.title.set_fontsize(12.5)


fig, axs = plt.subplots(2, 2, figsize=(11, 10.5))
(a, b), (c_, d) = axs

# (a) Đáp ứng tần số |H(Ft)| của bộ lọc đệ quy
Ft = np.linspace(-.5, .5, 1001)
for al, col, lab in [(1, "#8a8984", "α = 1 (không lọc)"),
                     (1/4, BLUE, "α = 1/4"),
                     (1/8, "#eb6834", "α = 1/8")]:
    H = al / np.abs(1 - (1 - al) * np.exp(-2j * np.pi * Ft))
    a.plot(Ft, H, color=col, lw=2, label=lab)
a.axhline(1 / np.sqrt(2), color=INK, ls=":", lw=1)
a.text(-.49, 1 / np.sqrt(2) + .02, "−3 dB", color="#52514e")
a.axvline(Fc, color=BLUE, ls="--", lw=1)
a.annotate(f"$F_c$ ≈ {Fc:.3f}", xy=(Fc, .35), xytext=(.15, .35),
           arrowprops=dict(arrowstyle="->", color=BLUE), color=BLUE)
a.set(xlim=(-.5, .5), ylim=(0, 1.08), title="(a) Đáp ứng tần số của bộ lọc đệ quy",
      xlabel=r"Tần số thời gian $F_t$ (chu kỳ/khung)", ylabel=r"$|H(F_t)|$")
a.title.set_fontsize(12.5)
a.legend(loc="upper right", bbox_to_anchor=(1, .9), fontsize=10.5, frameon=False)
a.text(.13, .62, "Nhiễu còn lại\n(vùng tĩnh) = α/(2−α):\nα = 1/4 → 1/7\nα = 1/8 → 1/15",
       va="top", fontsize=10, color="#52514e")

# (b) Vùng tĩnh: phổ nằm trên Ft = 0, nằm gọn trong dải thông
khung_pho(b, "(b) Vùng tĩnh (v = 0), lọc với α = 1/4", Fc)
b.plot([-B1, B1], [0, 0], color=INK, lw=3.5, zorder=3, solid_capstyle="round")
b.annotate("Phổ tín hiệu: nằm trọn trong\ndải thông → giữ nguyên chi tiết",
           xy=(.2, 0), xytext=(-.45, .25), arrowprops=dict(arrowstyle="->"), fontsize=10.5)
b.text(-.47, .07, r"Dải thông bộ lọc $|F_t| \leq F_c$", color=BLUE, fontsize=10.5)
b.text(-.45, -.4, "Vùng xám ngoài dải xanh:\nnhiễu bị loại bỏ", fontsize=10.5, color="#52514e")

# (c) Vùng chuyển động, vẫn lọc mạnh: phổ nghiêng Ft = -v1*F1 bị cắt
khung_pho(c_, f"(c) Vùng chuyển động (v₁ = {v1:g} px/khung), vẫn α = 1/4", Fc)
F1 = np.linspace(-B1, B1, 400)
Ft_line = -v1 * F1
inside = np.abs(Ft_line) <= Fc
c_.plot(F1[inside], Ft_line[inside], color=INK, lw=3.5, zorder=4)
for m in (F1 < 0, F1 > 0):
    sel = m & ~inside
    c_.plot(F1[sel], Ft_line[sel], color=RED, lw=3.5, ls=(0, (3, 1.5)), zorder=3)
for y in (Bt, -Bt):
    c_.axhline(y, color=INK, ls=":", lw=1)
c_.text(.48, Bt + .015, r"$B_t = B_1|v_1|$", ha="right", fontsize=10.5)
c_.annotate("Phần phổ bị cắt\n→ ghosting / nhòe",
            xy=(-.17, .17), xytext=(.03, .2), color=RED, fontsize=10.5,
            arrowprops=dict(arrowstyle="->", color=RED))
c_.text(-.47, -.25, r"Đường $F_t = -v_1 F_1$", fontsize=10.5)

# (d) Vùng chuyển động, bộ phát hiện chuyển α = 1: dải thông mở toàn miền
khung_pho(d, "(d) Vùng chuyển động, bộ phát hiện đặt α = 1", .5)
d.plot(F1, Ft_line, color=INK, lw=3.5, zorder=3)
d.text(-.45, .42, "Dải thông mở toàn miền", color=INK, fontsize=10.5)
d.text(-.45, -.43, "Tín hiệu giữ nguyên (không ghosting)\nnhưng nhiễu cũng không được lọc",
       fontsize=10.5)

fig.tight_layout()
fig.savefig("pho_video_bo_loc.png", dpi=200)
print(f"Fc = {Fc:.4f} chu kỳ/khung, Bt = {Bt:.2f} chu kỳ/khung")
