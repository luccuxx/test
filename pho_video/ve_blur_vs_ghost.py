import numpy as np
import matplotlib.pyplot as plt

# Cùng một bộ lọc đệ quy α = 1/4, cùng một vật (khối sáng rộng 20 px), chỉ khác vận tốc.
# Bản chất: ngõ ra = chồng chập các vị trí quá khứ của vật, trọng số giảm dần.
#   Vật chậm  -> các bản sao chồng lên nhau -> biên nhòe (motion blur)
#   Vật nhanh -> các bản sao tách rời nhau  -> bóng ma (ghosting)
W, NEN, VAT, RONG, alpha = 300, 50.0, 200.0, 20, 1/4
INK, ORANGE, MUTED = "#0b0b0b", "#eb6834", "#52514e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12.5})
NHAN = dict(fontsize=11.5, bbox=dict(fc="white", ec="none", alpha=.92, pad=3), zorder=6)


def mo_phong(v, so_khung, x0):
    def khung(t):
        x = np.full(W, NEN)
        x[x0 + v * t: x0 + v * t + RONG] = VAT
        return x
    y = np.full(W, NEN)                  # bộ lọc bắt đầu từ nền, chưa có vật
    for t in range(so_khung):
        y = y + alpha * (khung(t) - y)
    return khung(so_khung - 1), y


fig, (a, b) = plt.subplots(2, 1, figsize=(10.5, 8.6), sharey=True)
px = np.arange(W)

x, y = mo_phong(v=1, so_khung=60, x0=150)
a.plot(px, x, color=INK, lw=1.6, drawstyle="steps-mid", label="Vị trí thật của vật")
a.plot(px, y, color=ORANGE, lw=2.4, label="Ngõ ra bộ lọc")
a.set_title("(a) Vật chậm, v = 1 px/khung: các vị trí cũ chồng lên nhau → nhòe (motion blur)",
            loc="left", fontsize=12.5)
a.annotate("Biên trước dốc thoai thoải\n(chậm hiện cái mới)", xy=(226, y[226]), xytext=(297, 92), ha="right",
           arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
a.annotate("Đuôi ngắn, dính liền vào vật\n(chậm quên cái cũ)", xy=(204, y[204]), xytext=(40, 130),
           arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)

x, y = mo_phong(v=25, so_khung=11, x0=10)
b.plot(px, x, color=INK, lw=1.6, drawstyle="steps-mid", label="Vị trí thật của vật")
b.plot(px, y, color=ORANGE, lw=2.4, label="Ngõ ra bộ lọc")
b.set_title("(b) Vật nhanh, v = 25 px/khung: các vị trí cũ tách rời → bóng ma (ghosting)",
            loc="left", fontsize=12.5)
b.annotate("Các bản sao mờ dần tại vị trí cũ\n= bóng ma", xy=(219, y[219]), xytext=(40, 150),
           arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
b.annotate("Vật hiện tại chỉ còn\nkhoảng 1/4 độ tương phản", xy=(270, y[270]), xytext=(205, 160),
           arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
b.set_xlabel("Vị trí pixel trên một hàng ảnh")

for ax in (a, b):
    ax.set(xlim=(0, W - 1), ylim=(35, 215), ylabel="Độ sáng Y")
    ax.legend(loc="upper left", fontsize=11, frameon=False)
fig.tight_layout(h_pad=2)
fig.savefig("hinh_blur_vs_ghost.png", dpi=200)
fig.savefig("hinh_blur_vs_ghost.svg")
