# Kế hoạch TikTok: Gia La 50808 — Skin 001 vs 002, cùng góc máy (25 slide 9:16, mỗi slide 2 ô 9:8)

## 1. Định dạng
- Mỗi slide là một khung TikTok dọc **1080×1920 (9:16)**, **chia 2 ô 1080×960 (9:8)**: ô trên 001, ô dưới 002, cùng tư thế,
  cùng giây, cùng camera. Mỗi ô render 1440×1280 (MSAA 4x) rồi thu nhỏ.
  - 25 slide = 25 góc (mỗi slide có cả 2 skin).
  - **3 bài**: A (slide 1–10), B (slide 11–20), C (slide 21–25: chuỗi 5 góc mặt).
- Vùng an toàn của TikTok (giao diện che mép khung):
  - Chữ: x 60–960, y 150–1500.
  - Không đặt mặt hay điểm nhấn ở 420 px dưới cùng (caption, nút) hoặc 130 px mép phải (cột icon).
- **Không chữ, không watermark trên ảnh.** Tên góc chỉ dùng trong kế hoạch; caption viết ở phần mô tả bài đăng.
- Giới hạn nội dung: gợi cảm kiểu nghệ thuật (đường cong, da trần ở vai, lưng, gáy; chân, hông), nhân vật mặc nguyên trang phục gốc. Không quay từ dưới lên trong váy, không đặt tâm khung vào háng hay vùng kín. Như vậy ảnh không bị TikTok hạn chế hiển thị.

## 2. Công cụ (thư mục `D:/model_aov/GiaLa/tiktok`)
- `spec25.txt`: 25 góc **đang dùng** (nguồn đúng; bảng mục 5 là ý đồ gốc, số liệu có thể đã chỉnh).
  - Mỗi dòng: `tên|clip|giây|xương|az|el|dist|fov|dy`. Xương ghi `-` nghĩa là dùng camera game.
  - "Trước mặt" là hướng ngang từ xương tới camera game, nên 2 skin luôn cùng góc.
  - az: độ quanh trục đứng (+ = về phía tay phải nhân vật). el: độ nâng (+ = camera cao hơn). dist: mét.
  - fov: góc nhìn **dọc** (độ). dy: nâng/hạ điểm nhìn (m).
  - Nhân vật tự căn giữa ngang (`CenterOnCharacter`), trừ góc nhắm Head/Neck.
- `render_tiktok.ps1`: render batchmode `GiaLa/unity_001` và `unity_002` (phải đóng Unity Editor), 1440×1280 và 1440×2560,
  ánh kim (`-metal 0.8 -metalrim 1.8`) vào `_render/`, rồi gọi `ghep.py`.
- `ghep.py`: cắt viền đen, hậu kỳ vàng `vang.py` (`vang_bong(1.8, 0.8)`: vàng nhạt, bóng, phản chiếu nhẹ), ghép vào `anh/`:
  `ghep_anhkim_NN.png` (1080×1920, trên 001, dưới 002) và `rieng_anhkim_NN_00X.png` (1080×1920 từng skin). Báo ảnh có nền đen >1%.
- Số đo ở Idleshow@0: đầu 1,80 m, hông 1,25 m, gối khoảng 0,72 m, bàn chân 0,2–0,35 m (nhân vật đang bay). Camera game ở phía −z.
- Khoảng cách tham khảo ở fov 30 cho khung dọc:
  - toàn thân: 4,0–4,4 m;
  - từ hông trở lên: 2,0 m;
  - chân dung: 0,7–0,9 m;
  - đùi, hông: 1,1–1,4 m.

## 3. Quy tắc góc 
- Giữ |az| ≤ 60°. Từ 90° trở ra sau thì nền **đen**, vì trời chỉ dựng phía trước camera game.
- Muốn thấy lưng, mông, gáy: dùng tư thế `Idleshow_Turn1/Turn2/Rest1/Rest2` vào giây nhân vật tự quay lưng hoặc nghiêng về camera. Hoặc dùng đoạn Come có nền bao quanh (dò ở bước B1).
- Ảnh đùi lấy góc 30–60°, tâm giữa đùi (`Bip001 L Thigh`, dy −0,35). Không lấy góc chính diện ngang háng.
- 002 có clip riêng, nên cùng giây có thể lệch tư thế một chút. Camera bám theo xương nên góc vẫn giống. Chọn giây mà cả 2 skin cùng có tư thế cần.

## 4. Hướng nghệ thuật
- **Bố cục:**
  - Chủ thể theo đường 1/3.
  - Chừa khoảng trời trống phía hướng nhìn hoặc hướng chuyển động.
  - Dùng đường chéo (vĩ, dây đàn, ruy băng, đường chân) để dẫn mắt.
- **Ánh sáng:**
  - Ưu tiên giây có đèn ngược hoặc viền sáng: đoạn cello đêm Come@11–13 có ánh xanh sau lưng, đoạn kéo vĩ Come@9–10 có hạt vàng.
  - Da trần (vai, lưng, gáy) đẹp nhất khi có viền sáng.
- **Tiền cảnh:** đặt hạt sáng, ruy băng, tinh thể mờ ở mép khung tạo chiều sâu (đoạn Come@14–16 có ruy băng xanh).
- **Nhịp bài:** mở bằng ảnh đẹp nhất để giữ người xem → toàn cảnh → cận → chi tiết → kết bằng chân dung kèm câu hỏi chọn team.
- **Màu:** giữ nguyên tone-map của game để 2 skin so sánh công bằng, không lọc màu riêng.

## 5. Danh sách 25 góc (mỗi góc = 2 ảnh: 001 rồi 002)
Cột "Pose" ghi `clip@giây`. `(dò)` = giây chọn ở bước B1. Cột "Góc" ghi `xương | az | el | dist | fov | dy`; `camera game` = dùng camera của clip.

### Bài A: "Cùng một góc: 001 và 002" (ảnh 1–20)
| Góc | Ảnh | Nhóm | Pose | Góc | Ý đồ nghệ thuật / tên góc |
|---|---|---|---|---|---|
| A1 | 1–2 | Hook chân dung | Idleshow@0 | Bip001 Head \| 20 \| 5 \| 0.8 \| 28 \| −0.05 | Mặt trên đường 1/3 trên, tóc bay; tên: Ánh nhìn |
| A2 | 3–4 | Mặt nghiêng | Idleshow@0 | Bip001 Head \| 60 \| 0 \| 0.8 \| 28 \| 0 | Profile chừa trời trước mặt; tên: Góc nghiêng |
| A3 | 5–6 | Mắt cận | Idleshow@0 | Bip001 Head \| 0 \| 0 \| 0.35 \| 25 \| +0.03 | Khung chặt mắt + trán; tên: Đôi mắt |
| A4 | 7–8 | Vai – xương quai xanh | Idleshow@0 | Bip001 Neck \| −40 \| 10 \| 0.9 \| 32 \| −0.1 | Đường vai chéo, da có viền sáng; tên: Vai trần |
| A5 | 9–10 | Game: sảnh | Idleshow@0 | camera game (cắt dọc) | Toàn thân giữa vòm pha lê; tên: Sảnh |
| A6 | 11–12 | Game: kéo vĩ | Come@9.5 | camera game | Hạt vàng tiền cảnh; tên: Kéo vĩ |
| A7 | 13–14 | Game: cello đêm | Come@12 | camera game | Ánh xanh ngược sáng; tên: Khúc cello |
| A8 | 15–16 | Game: bầu trời | Come@15 | camera game | Ruy băng chéo khung; tên: Giữa trời |
| A9 | 17–18 | Toàn thân góc thấp | Idleshow@0 | Bip001 Pelvis \| 20 \| −10 \| 4.2 \| 30 \| 0 | Dáng cao vươn lên trời, nhiều khoảng trời; tên: Nữ thần |
| A10 | 19–20 | Outro | Idleshow@0 | Bip001 Head \| −20 \| 5 \| 0.85 \| 28 \| 0 | Chân dung ngược hướng A1; tên: Team 001 hay 002? |

### Bài B: "Đường cong: 001 vs 002" (ảnh 21–40)
| Góc | Ảnh | Nhóm | Pose | Góc | Ý đồ nghệ thuật / tên góc |
|---|---|---|---|---|---|
| B1 | 21–22 | Hook: đường chân | Idleshow@0 | Bip001 L Calf \| 45 \| −5 \| 2.0 \| 32 \| +0.2 | Chân dài chéo khung từ hông tới gót; tên: Đường chân |
| B2 | 23–24 | Đùi 3/4 | Idleshow@0 | Bip001 L Thigh \| 40 \| 0 \| 1.2 \| 30 \| −0.35 | Đùi qua khe váy, vải voan tiền cảnh; tên: Đùi |
| B3 | 25–26 | Giày cao gót | Idleshow@0 | Bip001 R Foot \| 20 \| 10 \| 0.8 \| 30 \| 0 | Mũi giày chỉ xuống biển mây, nhiều khoảng trống; tên: Gót |
| B4 | 27–28 | Eo và hông | Idleshow@0 | Bip001 Pelvis \| 40 \| 5 \| 1.3 \| 30 \| +0.1 | Đường eo cong chữ S theo chiều dọc; tên: Eo thon |
| B5 | 29–30 | Gáy | Turn@(dò, quay lưng) | Bip001 Neck \| 15 \| 10 \| 0.7 \| 30 \| +0.05 | Tóc búi, gáy trần, viền sáng; tên: Gáy |
| B6 | 31–32 | Lưng trần | Turn@(dò, quay lưng) | Bip001 Spine1 \| 10 \| 10 \| 1.2 \| 30 \| +0.05 | Đường sống lưng giữa khung, hoa văn vàng; tên: Lưng trần |
| B7 | 33–34 | Mông từ sau | Turn@(dò, quay lưng) | Bip001 Pelvis \| 0 \| 0 \| 1.4 \| 30 \| −0.08 | Váy ôm hông, nếp vải theo chuyển động; tên: Phía sau |
| B8 | 35–36 | Hông 3/4 sau | Turn@(dò, quay lưng) | Bip001 Pelvis \| 35 \| 5 \| 1.6 \| 30 \| 0 | Đường hông – lưng – vai nối một mạch; tên: 3/4 sau |
| B9 | 37–38 | Liếc qua vai (mặt nghiêng) | Turn@(dò, đầu ngoảnh) | Bip001 Head \| 25 \| 10 \| 0.9 \| 30 \| 0 | Mặt nghiêng nhìn lại, vai trần tiền cảnh; tên: Ngoảnh lại |
| B10 | 39–40 | Dáng cong toàn thân | Rest@(dò, nghiêng) | Bip001 Pelvis \| 55 \| 0 \| 4.0 \| 30 \| 0 | Dáng S toàn thân trên nền trời; tên: Team 001 hay 002? |

### Bài C: "5 góc mặt: 001 vs 002" (ảnh 41–50)
| Góc | Ảnh | Nhóm | Pose | Góc | Ý đồ nghệ thuật / tên góc |
|---|---|---|---|---|---|
| C1 | 41–42 | Chính diện | Idleshow@0 | Bip001 Head \| 0 \| 0 \| 0.75 \| 28 \| 0 | Đối xứng, mắt ở đường 1/3 trên; tên: Chính diện |
| C2 | 43–44 | Nghiêng 1/3 | Idleshow@0 | Bip001 Head \| 30 \| 0 \| 0.75 \| 28 \| 0 | Chừa trời phía hướng nhìn; tên: Nghiêng 1/3 |
| C3 | 45–46 | Nghiêng 1/2 | Idleshow@0 | Bip001 Head \| 45 \| 0 \| 0.75 \| 28 \| 0 | Góc 3/4 kinh điển, rõ sống mũi; tên: Nghiêng 1/2 |
| C4 | 47–48 | Từ trên xuống | Idleshow@0 | Bip001 Head \| 10 \| 35 \| 0.8 \| 28 \| 0 | Mắt to, cằm thon; tên: Từ trên |
| C5 | 49–50 | Từ dưới lên | Idleshow@0 | Bip001 Head \| 10 \| −15 \| 0.8 \| 28 \| +0.05 | Nền trời thoáng; tên: Team 001 hay 002? |

### Góc dự phòng (thay khi góc chính xấu)
- Đùi nghiêng: L Thigh | 60 | 0 | 1.3 | 30 | −0.3.
- Gối và bắp chân góc thấp: L Calf | 25 | −8 | 1.3 | 32 | +0.25.
- Eo nhìn từ trên: Spine1 | 30 | 30 | 1.2 | 32 | 0.
- Góc chéo từ trên: Pelvis | −35 | 15 | 2.0 | 32 | +0.2.
- Toàn thân từ sau: Turn@(dò) | Pelvis | 0 | 5 | 4.2 | 30 | −0.1.
- Tay cầm vĩ: R Hand | 20 | 5 | 0.8 | 30 | 0.
- Đùi trong tư thế nghỉ: Rest1@(dò) | L Thigh | 40 | 0 | 1.2 | 30 | −0.35.
- Hông dáng tựa: Rest2@(dò) | Pelvis | 45 | 5 | 1.3 | 32 | 0.
- Come@1 giáng xuống (camera game).
- Come@20 vào sảnh (camera game).

## 6. Nội dung bài đăng
- Bài A, caption: "Gia La 50808 – hai bản skin, cùng một góc máy. Lướt từng cặp và chọn team 001 hay 002 👇 (render fan-made từ dữ liệu game trong Unity)"
- Bài B, caption: "Đường cong, góc nghiêng, bóng lưng – 001 vs 002 ✨ Lướt theo cặp 👇 (render fan-made)"
- Hashtag: #王者荣耀 #伽罗 #HonorOfKings #HoK #GiaLa #skincomparison #3Drender #Unity3D #fanservice
- Nhạc: đoạn cello/violin chậm đang thịnh hành (skin chủ đề giao hưởng), để TikTok tự chuyển ảnh theo nhịp.
- Bài C, caption: "5 góc mặt – cùng khung, hai skin. Góc nào đẹp nhất? 👇 (render fan-made)"
- Đăng A trước, sau 1–2 ngày đăng B, rồi C. Ghim bình luận dẫn qua bài trước.
- Ghi rõ "fan-made": ảnh dựng từ tài nguyên của Tencent nên bài có thể bị báo bản quyền. Bạn tự đăng từ tài khoản của mình.

## 7. Quy trình
- Tắt máy ảo (thiếu RAM làm batchmode lỗi "Failed to load Mono"), đóng Unity Editor.
- Sửa góc trong `spec25.txt` (giữ kịch bản, chỉ chỉnh số), chạy `powershell -File D:/model_aov/GiaLa/tiktok/render_tiktok.ps1`.
- Soát `anh/`: không nền đen, chủ thể trong vùng an toàn, đúng giới hạn nội dung mục 1, hai skin cùng khung, vật thể nền
  không che nhân vật. Ảnh lệch thì chỉnh az/el/dist/dy hoặc thay bằng góc dự phòng rồi chạy lại.
- Xóa `_render/` sau khi duyệt (chỉ giữ `anh/`). Bạn tự đăng; tôi không đăng hộ.

## 8. Prompt dùng lần sau
> Đọc `D:/model_aov/GiaLa/tiktok/KE_HOACH_TIKTOK.md`, chỉnh `spec25.txt` nếu cần, chạy `render_tiktok.ps1`, soát theo mục 1, 3, 4 và gửi ảnh cho tôi xem. Không chèn chữ hay watermark. Tự làm, không hỏi lại.
