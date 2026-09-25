# Kịch bản bài viral: "Toàn cảnh → Phóng to" (Gia La 50808, 001 vs 002)

## Ý tưởng
- **Mỗi slide = 1 skin, 2 ô:** ô trên là **toàn cảnh**, ô dưới là **phóng to cùng khoảnh khắc**.
  Mắt người xem đi từ trên xuống: thấy tổng thể rồi mới thấy chi tiết. Mỗi slide tự trả lời câu "gần hơn thì thế nào?".
- **Mỗi cảnh 2 slide liền nhau: 001 rồi 002**, cùng góc máy.
  Người xem vừa thấy 001 sẽ lướt để so với 002. Đó là lý do để lướt tiếp mà không cần chữ trên ảnh.
- **7 cảnh = 14 slide.** Đủ dài để TikTok tính thời gian xem cao, đủ ngắn để không bỏ giữa chừng.
- **Không chữ, không watermark trên ảnh.** Mọi câu dẫn dắt nằm ở caption và bình luận ghim.
- Hai ô nằm gọn trong vùng an toàn (x 60–950, y 150–1500), không bị caption hay cột icon che.

## Nhịp giữ người xem
Thứ tự được sắp theo 4 nguyên tắc:
1. **Mở bằng chuyển động mạnh nhất.** Khoảnh khắc nhân vật giáng xuống (Come@1) làm người xem dừng lướt.
2. **Không có 2 cảnh liền nhau cùng kiểu góc.** Ô phóng to lần lượt: nhìn từ dưới lên → tay → từ trên xuống → lưng chéo → mặt nghiêng → nửa người từ trên → mắt cận.
   Mỗi slide mới là một cách nhìn mới, người xem không đoán được slide sau.
3. **Theo đúng dòng thời gian của đoạn Come:** giáng xuống → hạt vàng → cello đêm → ruy băng → bước vào sảnh.
   Người xem cảm giác đang xem một câu chuyện và muốn biết đoạn kết.
4. **Chèn cảnh bất ngờ ở giữa bài:** góc cao nhìn xuống (cảnh 3) và quay lưng (cảnh 4) phá nhịp của các cảnh game.
5. **Kết bằng góc cận nhất** (mắt, cảnh 7), là phần thưởng cho người lướt hết.

**Toàn bộ góc trong bài này là góc mới, không trùng góc nào trong `spec25.txt`.**

## Từng slide
Mã trong `spec_viral.txt`: `V<n>T` = ô trên (toàn cảnh), `V<n>Z` = ô dưới (phóng to). Mỗi cảnh 2 slide: 001 rồi 002.

| Slide | Cảnh | Ô trên (toàn cảnh) | Ô dưới (phóng to) | Vai trò giữ người xem |
|---|---|---|---|---|
| 1–2 | 1. Giáng xuống | Camera game Come@1: nhân vật từ trời đáp xuống | Mặt, camera thấp nhìn lên (el −10) | **Hook:** chuyển động mạnh, góc hùng vĩ |
| 3–4 | 2. Hạt vàng | Camera game Come@10: kéo vĩ giữa hạt vàng (khác giây với A06) | Bàn tay cầm vĩ, lệch phải 20° | Chi tiết tay mà ảnh toàn cảnh không thấy |
| 5–6 | 3. Từ trên cao | Toàn thân, camera cao 20° nhìn chéo từ bên trái (az −45) | Mặt nhìn từ trên xuống (el 25): mắt to, cằm thon | **Bất ngờ:** lần đầu có góc cao |
| 7–8 | 4. Quay lưng | Toàn thân quay lưng, chéo từ bên trái (az −30) | Lưng trên và vai, nhìn chéo từ trên (el 15) | Góc phía sau, phía đối diện với bài chính |
| 9–10 | 5. Cello đêm | Camera game Come@13: ánh xanh ngược sáng | Mặt nghiêng nhẹ (az 15) trong ánh đêm | Nền tối, nhịp chậm lại |
| 11–12 | 6. Ruy băng | Camera game Come@16: ruy băng giữa trời | Nửa người, camera hơi cao (el 10) | Mở rộng không gian trước khi kết |
| 13–14 | 7. Vào sảnh | Camera game Come@20: bước vào sảnh | **Đôi mắt** cận nhất (dist 0.6, fov 25) | **Phần thưởng:** góc gần nhất, mời bình luận chọn team |

Nếu muốn slide 1 là skin mạnh hơn (ví dụ 002 đẹp hơn ở cảnh kéo vĩ), đổi thứ tự skin trong `ghep_viral.py` (dòng `for sk in ("001", "002")`).

## Caption (dán vào phần mô tả, không đặt lên ảnh)
> Cùng 1 góc máy, zoom sát từng chi tiết 🔍 001 hay 002? Lướt tới ảnh cuối rồi chọn team 👇
> (render fan-made từ dữ liệu game trong Unity)
>
> #王者荣耀 #伽罗 #HonorOfKings #HoK #GiaLa #skincomparison #3Drender #Unity3D

Dòng đầu caption là thứ duy nhất hiện trên ảnh 1, nên câu hỏi "001 hay 002?" và lời mời "lướt tới ảnh cuối" phải nằm ở đó.

## Bình luận ghim
> Ảnh cuối là góc gần nhất 👀 Team 001 thả ❤️ vào bình luận này, team 002 trả lời "002"

Việc này kéo tương tác (thích và trả lời bình luận), tín hiệu TikTok dùng để đẩy bài.

## Nhạc và đăng
- Nhạc: đoạn cello hoặc violin chậm đang thịnh hành. Dùng chế độ ảnh để TikTok tự chuyển ảnh theo nhịp.
- Giờ đăng: 11–13h hoặc 19–22h (giờ người xem mục tiêu).
- Sau 1–2 ngày có thể đăng bản đảo thứ tự (002 trước) với caption "Hôm qua team 001 thắng, lần này thì sao?", tạo chuỗi bài.
- Ghi rõ "fan-made": ảnh dựng từ tài nguyên của Tencent nên bài có thể bị báo bản quyền. Bạn tự đăng từ tài khoản của mình.

## Render
Đóng Unity Editor, rồi chạy:
```powershell
powershell -File D:/model_aov/GiaLa/tiktok/render_tiktok.ps1 -Spec D:/model_aov/GiaLa/tiktok/spec_viral.txt -Ghep ghep_viral.py -Chi98
```
- Ảnh ra: `tiktok/anh_viral/viral_01.png` … `viral_14.png` (1080×1920).
- Ô phóng to lệch hoặc xấu: chỉnh dòng `V<n>Z` trong `spec_viral.txt` (az/el/dist/dy như `spec25.txt`) rồi chạy lại.
- Các ô camera game (`V1T`, `V2T`, `V5T`, `V6T`, `V7T`) muốn đổi khoảnh khắc thì chỉ cần đổi giây (cột 3), nhớ đổi giây ở dòng `Z` cùng cảnh cho khớp.
