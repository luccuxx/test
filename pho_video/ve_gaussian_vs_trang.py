import numpy as np
import matplotlib.pyplot as plt

# So sánh hai tính chất độc lập của nhiễu:
#   Gaussian -> mật độ xác suất của BIÊN ĐỘ (histogram hình quả chuông)
#   Trắng    -> mật độ phổ công suất theo TẦN SỐ (phổ phẳng)
rng = np.random.default_rng(3)
N, SO_LAN, SIGMA = 256, 4000, 10.0


def awgn(n):
    return rng.normal(0, SIGMA, n)


def gaussian_khong_trang(n):
    # Nhiễu Gaussian đi qua bộ lọc làm mượt: vẫn hình chuông nhưng dồn về tần số thấp
    x = rng.normal(0, 1, n + 200)
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = 0.85 * y[i - 1] + x[i]
    y = y[200:]
    return y / np.sqrt(1 / (1 - 0.85**2)) * SIGMA


def trang_khong_gaussian(n):
    # Nhiễu xung (muối tiêu): mỗi mẫu độc lập, nhưng biên độ chỉ nhận 0 hoặc ±A
    p = 0.1
    A = SIGMA / np.sqrt(p)
    return rng.choice([-A, 0.0, A], size=n, p=[p / 2, 1 - p, p / 2])


HANG = [
    ("Gaussian + trắng (AWGN)", awgn, "Gaussian ✓   Trắng ✓"),
    ("Gaussian, không trắng", gaussian_khong_trang, "Gaussian ✓   Trắng ✗"),
    ("Trắng, không Gaussian (nhiễu xung)", trang_khong_gaussian, "Gaussian ✗   Trắng ✓"),
]

BLUE, INK, MUTED = "#2a78d6", "#0b0b0b", "#52514e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11.5})
fig, axs = plt.subplots(3, 3, figsize=(13, 9.6))
Ft = np.fft.rfftfreq(N)

for r, (ten, ham, nhan) in enumerate(HANG):
    mau = ham(N)
    P = np.mean([np.abs(np.fft.rfft(ham(N)))**2 / N for _ in range(SO_LAN)], axis=0)
    gia_tri = np.concatenate([ham(N) for _ in range(200)])

    a, b, c = axs[r]
    a.plot(np.arange(60), mau[:60], color=BLUE, lw=1.6, marker="o", ms=3)
    a.axhline(0, color="#8a8984", lw=.8)
    a.set(ylim=(-45, 45), ylabel="Giá trị nhiễu")
    a.set_title(ten, loc="left", fontsize=12, fontweight="bold")

    b.hist(gia_tri, bins=np.arange(-45, 46, 2.5), density=True, color=BLUE, alpha=.85,
           edgecolor="white", linewidth=.6)
    b.set(xlim=(-45, 45), yticks=[])

    c.plot(Ft[1:], P[1:] / SIGMA**2, color=BLUE, lw=2)
    c.set(xlim=(0, .5), ylim=(0, 8), ylabel="Công suất (chuẩn hóa)")
    c.text(.97, .88, nhan, transform=c.transAxes, ha="right", fontsize=11.5, color=INK,
           bbox=dict(fc="white", ec="#c9c8c2", pad=4))

    if r == 2:
        a.set_xlabel("Khung hình (thời gian)")
        b.set_xlabel("Giá trị nhiễu (biên độ)")
        c.set_xlabel(r"Tần số thời gian $F_t$ (chu kỳ/khung)")

axs[0, 0].text(0, 1.28, "① Nhiễu theo thời gian\n(60 khung đầu)", transform=axs[0, 0].transAxes, fontsize=13,
               va="bottom")
axs[0, 1].text(0, 1.28, "② Mật độ xác suất của BIÊN ĐỘ\n→ quyết định có Gaussian hay không",
               transform=axs[0, 1].transAxes, fontsize=13, va="bottom")
axs[0, 2].text(0, 1.28, "③ Mật độ phổ công suất theo TẦN SỐ\n→ quyết định có trắng hay không",
               transform=axs[0, 2].transAxes, fontsize=13, va="bottom")
fig.tight_layout(rect=(0, 0, 1, .95), h_pad=2.2)
fig.savefig("hinh_gaussian_vs_trang.png", dpi=200)
fig.savefig("hinh_gaussian_vs_trang.svg")
