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
1. **Mở bằng ảnh đẹp nhất.** Cảnh kéo vĩ với hạt vàng (A06) là ảnh gây dừng lướt mạnh nhất.
2. **Xen kẽ sáng và tối.** Đêm → trời → trời → trời → đêm → trời → trời. Mỗi lần đổi nền là một "cú giật mắt" giữ sự chú ý.
3. **Tăng dần độ gần.** Toàn thân → gót → lưng → gáy → tay → mặt → **mắt**. Cảnh cuối cận nhất, là phần thưởng cho người lướt hết.
4. **Chừa một "bí mật".** Lưng trần (cảnh 4) đặt ở giữa bài: người xem đoán được sẽ còn góc bất ngờ nên không thoát ra.

## Từng slide
Mã trong `spec_viral.txt`: `V<n>T` = ô trên (toàn cảnh), `V<n>Z` = ô dưới (phóng to).

| Slide | Skin | Cảnh | Ô trên (toàn cảnh) | Ô dưới (phóng to) | Vai trò giữ người xem |
|---|---|---|---|---|---|
| 1 | 001 | 1. Kéo vĩ | Cảnh game Come@9.5: kéo vĩ giữa hạt vàng, nền đêm (A06) | Mặt nghiêng lúc kéo vĩ, cùng phía camera | **Hook:** ảnh đẹp nhất, nền tối nổi bật giữa feed sáng |
| 2 | 002 | 1. Kéo vĩ | như trên | như trên | So sánh ngay lập tức, người xem biết bài là "so skin" và sẽ lướt tiếp |
| 3 | 001 | 2. Sảnh | Toàn thân chính diện giữa vòm pha lê (A05) | Mặt chính diện (C21) | Nền trời sáng sau cảnh đêm, "giật mắt" |
| 4 | 002 | 2. Sảnh | như trên | như trên | So mặt chính diện, điểm khác rõ nhất giữa 2 skin |
| 5 | 001 | 3. Dáng | Toàn thân góc thấp, nhiều trời (A09) | Giày cao gót trên biển mây (B13) | Chi tiết nhỏ mà ảnh toàn thân không thấy rõ |
| 6 | 002 | 3. Dáng | như trên | như trên | |
| 7 | 001 | 4. Quay lưng | Nhân vật quay lưng, toàn thân (B17) | Gáy, tóc búi, viền sáng (B15) | **Bất ngờ giữa bài:** lần đầu thấy phía sau |
| 8 | 002 | 4. Quay lưng | như trên | như trên | |
| 9 | 001 | 5. Cello đêm | Cảnh game Come@12: ánh xanh ngược sáng (A07) | Tay cầm vĩ trên dây đàn | Quay lại nền tối, nhịp chậm như đoạn nhạc lặng |
| 10 | 002 | 5. Cello đêm | như trên | như trên | |
| 11 | 001 | 6. Giữa trời | Cảnh game Come@15: ruy băng chéo khung (A08) | Mặt giữa trời | Mở rộng không gian trước khi vào cảnh kết |
| 12 | 002 | 6. Giữa trời | như trên | như trên | |
| 13 | 001 | 7. Kết | Nửa người chính diện (B16 mới) | **Đôi mắt** cận nhất (A03) | **Phần thưởng:** góc gần nhất cả bài |
| 14 | 002 | 7. Kết | như trên | như trên | Slide cuối, người xem vừa so xong và muốn bình luận chọn team |

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
- Riêng cảnh kéo vĩ, nếu lượt dò `do_goc.ps1` tìm được góc thấy rõ mặt hơn, thay số của `V1Z` bằng góc đó.
