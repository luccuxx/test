import numpy as np
import matplotlib.pyplot as plt

# Mô phỏng 1 hàng ảnh: "xe" là khối sáng chạy sang phải trên nền tối (không thêm nhiễu cho dễ nhìn)
W, NEN, XE, RONG = 240, 50.0, 200.0, 30   # số pixel, độ sáng nền, độ sáng xe, bề rộng xe
v, alpha, T, SO_KHUNG = 4, 1/4, 20, 35    # px/khung, hệ số lọc, ngưỡng phát hiện, số khung

INK, ORANGE, BLUE, MUTED = "#0b0b0b", "#eb6834", "#2a78d6", "#52514e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
NHAN = dict(fontsize=11.5, bbox=dict(fc="white", ec="none", alpha=.92, pad=3), zorder=6)


def khung(t):
    x = np.full(W, NEN)
    x[10 + v * t: 10 + v * t + RONG] = XE
    return x


y_thuong = khung(0)       # bộ lọc đệ quy α cố định
y_thich_ung = khung(0)    # bộ lọc thích ứng chuyển động: |d| > T thì α = 1
for t in range(1, SO_KHUNG):
    x = khung(t)
    y_thuong = y_thuong + alpha * (x - y_thuong)
    d = np.abs(x - y_thich_ung)
    a = np.where(d > T, 1.0, alpha)
    y_thich_ung = y_thich_ung + a * (x - y_thich_ung)

px = np.arange(W)
dau = 10 + v * (SO_KHUNG - 1)            # mép sau của xe ở khung cuối
fig, ax = plt.subplots(figsize=(10, 6.2))
ax.plot(px, y_thich_ung, color=BLUE, lw=5, alpha=.55, drawstyle="steps-mid",
        label="Lọc thích ứng chuyển động (|d| > T → α = 1)")
ax.plot(px, x, color=INK, lw=1.6, drawstyle="steps-mid", label="Khung vào (vị trí thật của xe)")
ax.plot(px, y_thuong, color=ORANGE, lw=2.4, label=f"Lọc thông thấp α = 1/{round(1/alpha)} cố định")

ax.annotate("Đuôi bóng ma phía sau xe\n(vị trí cũ của xe vẫn còn trong bộ nhớ)",
            xy=(dau - 16, y_thuong[dau - 16]), xytext=(12, 150),
            arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
ax.annotate("Xe bị mờ, trong suốt\n(không đạt độ sáng thật)",
            xy=(dau + 22, y_thuong[dau + 22]), xytext=(W - 2, 178), ha="right",
            arrowprops=dict(arrowstyle="->", lw=1.2), **NHAN)
ax.annotate("", xy=(dau + RONG + 32, 62), xytext=(dau + RONG + 6, 62),
            arrowprops=dict(arrowstyle="-|>", lw=2, color=MUTED))
ax.text(dau + RONG + 6, 68, f"v = {v} px/khung", color=MUTED, fontsize=11.5)

ax.set(xlim=(0, W - 1), ylim=(35, 215), xlabel="Vị trí pixel trên một hàng ảnh",
       ylabel="Độ sáng Y")
ax.set_title(f"Mặt cắt độ sáng sau {SO_KHUNG} khung khi xe chạy sang phải", fontsize=13.5, pad=10)
fig.legend(loc="lower center", ncol=2, fontsize=11, frameon=False)
fig.tight_layout(rect=(0, .1, 1, 1))
fig.savefig("hinh_ghosting_mat_cat.png", dpi=220)
fig.savefig("hinh_ghosting_mat_cat.svg")
