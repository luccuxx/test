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
Thứ tự đã chỉnh theo tờ dò (`to_do_1..4.jpg`), theo 5 nguyên tắc:
1. **Mở bằng khoảnh khắc đẹp nhất, rồi mới quay về đầu câu chuyện.**
   Slide 1 là kéo cello chính diện giữa hạt sáng xanh (Come@11). Slide 3 mới quay về cảnh giáng xuống (Come@1), cảnh có nhân vật nhỏ, không hợp làm hook.
2. **Không có 2 cảnh liền nhau cùng kiểu góc.** Các ô phóng to lần lượt là:
   mặt và đàn → mặt nhìn từ dưới → mặt nhìn từ trên → vai và mặt → lưng và vai → tóc búi → mặt trong đêm → nửa người → mặt lúc nghỉ → mắt cận.
3. **Theo dòng thời gian:** giáng xuống → cello đêm → ruy băng → bước vào sảnh.
4. **Chèn cảnh bất ngờ ở giữa bài:** góc cao, vai nghiêng, quay lưng rồi tóc búi, dáng nghỉ. Các cảnh này phá nhịp các cảnh game.
5. **Kết bằng góc cận nhất** (mắt, cảnh 10), là phần thưởng cho người lướt hết.

**Toàn bộ góc là góc mới, không trùng `spec25.txt`. Các góc bị tay, vĩ hoặc đàn che và các góc nền đen đã được thay bằng biến thể sạch trong tờ dò.**

## Từng slide
Mã trong `spec_viral.txt`: `V<n>T` = ô trên (toàn cảnh), `V<n>Z` = ô dưới (phóng to). Mỗi cảnh 2 slide: 001 rồi 002. Thứ tự slide theo thứ tự dòng trong file.

| Slide | Cảnh (mã) | Ô trên (toàn cảnh) | Ô dưới (phóng to) | Vai trò giữ người xem |
|---|---|---|---|---|
| 1–2 | 1. Kéo cello (V02) | Camera game Come@11: chính diện, hạt sáng xanh | Mặt, vai và đàn | **Hook:** đẹp nhất bài |
| 3–4 | 2. Giáng xuống (V01) | Camera game Come@1: từ trời đáp xuống | Mặt nhìn từ dưới lên, chéo phải | Quay về đầu câu chuyện |
| 5–6 | 3. Từ trên cao (V03) | Toàn thân, camera cao nhìn chéo (az −20) | Mặt nhìn từ trên xuống | Góc cao đầu tiên |
| 7–8 | 4. Vai nghiêng (V04) | Nửa người chéo phải (az 30) | Vai và mặt | Đường vai, cổ |
| 9–10 | 5. Quay lưng (V05) | Toàn thân quay lưng, tay giơ | Lưng và vai | **Bất ngờ giữa bài** |
| 11–12 | 6. Tóc búi (V06) | Quay lưng dang tay (Turn2@2.25) | Tóc búi, trâm cài | Chi tiết chỉ thấy từ phía sau |
| 13–14 | 7. Cello đêm (V07) | Camera game Come@13: chơi cello, ánh xanh | Mặt trong ánh đêm | Nền tối, nhịp chậm |
| 15–16 | 8. Ruy băng (V08) | Camera game Come@16.5: nửa người dang tay | Nửa người, trọn mặt | Mở rộng không gian |
| 17–18 | 9. Dáng nghỉ (V09) | Rest2@3 toàn thân (az −10) | Mặt lúc nghỉ | Thư giãn trước cảnh kết |
| 19–20 | 10. Vào sảnh (V10) | Camera game Come@20: ruy băng xoáy | **Đôi mắt** cận nhất | **Phần thưởng**, mời bình luận chọn team |

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

**Góc chưa có trong tờ dò:** `V02Z` (mặt lúc kéo cello, Come@11) và `V08Z` (nửa người ở Come@16.5, nâng khung) là góc mới, chưa được render thử.
Xem nhanh 2 góc này: `powershell -File do_goc.ps1 -Spec D:/model_aov/GiaLa/tiktok/spec_kiem.txt -Khung 98 -Nhanh` → `_do/to_do_1.jpg`.
