# Kịch bản bài viral: "Toàn cảnh → Phóng to" (Gia La 50808, 001 vs 002)

## Ý tưởng
- **Mỗi slide = 1 skin, 2 ô:** ô trên là **toàn cảnh**, ô dưới là **phóng to cùng khoảnh khắc**.
  Mắt người xem đi từ trên xuống: thấy tổng thể rồi mới thấy chi tiết. Mỗi slide tự trả lời câu "gần hơn thì thế nào?".
- **Mỗi cảnh 2 slide liền nhau: 001 rồi 002**, cùng góc máy.
  Người xem vừa thấy 001 sẽ lướt để so với 002. Đó là lý do để lướt tiếp mà không cần chữ trên ảnh.
- **10 cảnh = 20 slide.** Dài để TikTok tính thời gian xem cao. Nhịp đổi góc liên tục nên người xem không thấy dài (TikTok cho tối đa 35 ảnh).
- **Trên ảnh chỉ có watermark `howtocheckmap`** ở góc phải dưới ô dưới (trong vùng an toàn). Mọi câu dẫn dắt nằm ở caption và bình luận ghim.
- Hai ô nằm gọn trong vùng an toàn (x 60–950, y 150–1500), không bị caption hay cột icon che.

## Nhịp giữ người xem
Thứ tự được sắp theo 5 nguyên tắc:
1. **Mở bằng chuyển động mạnh nhất.** Khoảnh khắc nhân vật giáng xuống (Come@1) làm người xem dừng lướt.
2. **Không có 2 cảnh liền nhau cùng kiểu góc.** Ô phóng to lần lượt: nhìn từ dưới lên → tay → từ trên xuống → vai ngang → lưng chéo → ngoảnh lại → mặt trong đêm → nửa người từ trên → mặt lúc nghỉ → mắt cận.
   Mỗi slide mới là một cách nhìn mới, người xem không đoán được slide sau.
3. **Theo đúng dòng thời gian của đoạn Come:** giáng xuống → hạt vàng → cello đêm → ruy băng → bước vào sảnh.
   Người xem cảm giác đang xem một câu chuyện và muốn biết đoạn kết.
4. **Chèn cảnh bất ngờ ở giữa bài:** góc cao (cảnh 3), vai ngang (cảnh 4), quay lưng rồi **ngoảnh lại** (cảnh 5→6: một mini-câu chuyện, người xem lướt để xem nhân vật quay lại), dáng nghỉ (cảnh 9) phá nhịp các cảnh game.
5. **Kết bằng góc cận nhất** (mắt, cảnh 10), là phần thưởng cho người lướt hết.

**Toàn bộ góc trong bài này là góc mới, không trùng góc nào trong `spec25.txt`.**

## Từng slide
Mã trong `spec_viral.txt`: `V<n>T` = ô trên (toàn cảnh), `V<n>Z` = ô dưới (phóng to). Mỗi cảnh 2 slide: 001 rồi 002.

| Slide | Cảnh | Ô trên (toàn cảnh) | Ô dưới (phóng to) | Vai trò giữ người xem |
|---|---|---|---|---|
| 1–2 | 1. Giáng xuống | Camera game Come@1: nhân vật từ trời đáp xuống | Mặt, camera thấp nhìn lên (el −10) | **Hook:** chuyển động mạnh, góc hùng vĩ |
| 3–4 | 2. Hạt vàng | Camera game Come@10: kéo vĩ giữa hạt vàng (khác giây với A06) | Bàn tay cầm vĩ, lệch phải 20° | Chi tiết tay mà ảnh toàn cảnh không thấy |
| 5–6 | 3. Từ trên cao | Toàn thân, camera cao 20° nhìn chéo từ bên trái (az −45) | Mặt nhìn từ trên xuống (el 25): mắt to, cằm thon | **Bất ngờ:** lần đầu có góc cao |
| 7–8 | 4. Vai trần nghiêng | Nửa người nhìn ngang từ bên phải (az 55) | Vai và cổ nhìn ngang (az 55) | Góc ngang đầu tiên, đường vai và cổ rõ nhất |
| 9–10 | 5. Quay lưng | Toàn thân quay lưng, chéo từ bên trái (az −30) | Lưng trên và vai, nhìn chéo từ trên (el 15) | Góc phía sau, người xem chờ nhân vật quay lại |
| 11–12 | 6. Ngoảnh lại | Turn2@1.75 lúc đầu ngoảnh, nửa người chéo phải (az 40) | Mặt ngoảnh lại (az 40) | **Trả lời cảnh 5**, cao trào giữa bài |
| 13–14 | 7. Cello đêm | Camera game Come@13: ánh xanh ngược sáng | Mặt nghiêng nhẹ (az 15) trong ánh đêm | Nền tối, nhịp chậm lại |
| 15–16 | 8. Ruy băng | Camera game Come@16: ruy băng giữa trời | Nửa người, camera hơi cao (el 10) | Mở rộng không gian |
| 17–18 | 9. Dáng nghỉ | Rest2@3 toàn thân, chéo trái từ trên (az −35, el 10) | Mặt lúc nghỉ (az −35) | Nhịp thư giãn trước cảnh kết |
| 19–20 | 10. Vào sảnh | Camera game Come@20: bước vào sảnh | **Đôi mắt** cận nhất (dist 0.6, fov 25) | **Phần thưởng:** góc gần nhất, mời bình luận chọn team |

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
- Ảnh ra: `tiktok/anh_viral/viral_01.png` … `viral_20.png` (1080×1920).
- Ô phóng to lệch hoặc xấu: chỉnh dòng `V<n>Z` trong `spec_viral.txt` (az/el/dist/dy như `spec25.txt`) rồi chạy lại.
- Các ô camera game (`V01T`, `V02T`, `V07T`, `V08T`, `V10T`) muốn đổi khoảnh khắc thì chỉ cần đổi giây (cột 3), nhớ đổi giây ở dòng `Z` cùng cảnh cho khớp.

## Sửa góc bị tay, vĩ hoặc đàn che
1. Tạo 5 biến thể cho mỗi góc: `py -3.14 tao_do.py` → `spec_do.txt` (100 dòng).
   - Góc bám xương: a = gốc, b = xoay trái 25°, c = xoay phải 25°, d = nâng camera 20°, e = chờ thêm 0,5 giây.
   - Góc camera game: a = gốc, b = sớm 0,5 giây, c/d/e = muộn 0,5 / 1 / 1,5 giây.
2. Render nhanh ở đúng khung ô 9:8: `powershell -File do_goc.ps1 -Cot 5 -Khung 98 -Nhanh`
   → `_do/to_do_1.jpg` … `to_do_4.jpg`. Mỗi hàng là một góc (theo thứ tự V01T, V01Z, V02T…), 5 cột là a–e, mỗi ô có trái 001, phải 002.
3. Chọn biến thể không bị che: `py -3.14 chon.py V04Z=c V07Z=b ...` (ghi thẳng vào `spec_viral.txt`; góc nào ổn thì không cần ghi).
4. Render lại bài viral như mục Render ở trên.
