# Lịch sử cấu hình và kết quả quảng cáo 29/10/2026

Đợt thử trên Page Giày Đá Bóng - Yêu Bóng Đá Shop, tài khoản quảng cáo `814094494973387`. Tạo ngày 29/10: hai campaign theo cách trình bày sản phẩm **nhiều màu** và **một màu**, mỗi campaign có một nhóm tương tác và một nhóm Messenger, mỗi nhóm sáu ads: tổng **2 campaign / 4 ad set / 24 ads**. Các ID và payload tại [ads-state.json](ads-state.json). Các trạng thái PAUSED trong hai hồ sơ đó là snapshot lúc tạo, không có nghĩa quảng cáo chưa chạy.

## Cấu hình lúc tạo

- Đối tượng: Việt Nam, nam 18–44, không lọc sở thích; audience rộng trong giới hạn tuổi và giới tính. Chiến lược giá thầu lấy kết quả nhiều nhất, không đặt trần.
- Mỗi nhóm tương tác: 100.000đ/ngày, tối ưu tương tác bài. Mỗi nhóm Messenger: 200.000đ/ngày, tối ưu hội thoại. Ngân sách theo ad set, không chia sẻ; nếu bật cả bốn thì tổng cấu hình 600.000đ/ngày. Đây không phải giới hạn chi tiêu cứng từng ngày.
- Hồ sơ ban đầu ghi Facebook Feed cho cả bốn nhóm. Ngày 08/11, UI live của hai nhóm Messenger cũ hiển thị nhiều nền tảng và vị trí được chọn; không suy ra thay đổi xảy ra khi nào. Số thực chi theo vị trí bên dưới là bằng chứng về phân phối, không thay thế lịch sử cấu hình.
- Dũng báo ngày 30/10 chỉ giữ Messenger khoảng 400.000đ/ngày; ngày 02/11 ảnh cho thấy hai campaign tắt để nghỉ đợt thử. Không suy từ các mốc này ra trạng thái hiện tại.

## Kết quả Meta: snapshot ngày 09/11

Truy vấn Marketing API chỉ đọc ngày 09/11/2026, kỳ Meta trả về 29/10–09/11 (`date_preset=maximum`), cấp bốn ad set. Đây là số quy kết theo Meta, có thể cập nhật; không phải doanh thu, tiền đã thu, lợi nhuận hay xác nhận giao hàng. Không cộng reach của các nhóm thành reach duy nhất vì có thể trùng người.

| Nhóm cũ | Chi tiêu | Hiển thị | Chỉ số Meta | Chi phí/chỉ số |
| --- | ---: | ---: | ---: | ---: |
| Nhiều màu — tương tác | 130.642đ | 2.515 | 125 post engagements | ~1.045đ |
| Một màu — tương tác | 107.936đ | 1.395 | 80 post engagements | ~1.349đ |
| Nhiều màu — Messenger | 915.518đ | 39.222 | 108 cuộc hội thoại bắt đầu trong 7 ngày | ~8.477đ |
| Một màu — Messenger | 856.399đ | 35.620 | 98 cuộc hội thoại bắt đầu trong 7 ngày | ~8.739đ |

Hai nhóm tương tác chi **238.578đ**, tổng 205 `post_engagement`; chỉ số này bao gồm các loại tương tác như xem ảnh và click, không chỉ like/comment. Hai nhóm Messenger chi **1.771.917đ**, tổng 206 `onsite_conversion.messaging_conversation_started_7d`, tương đương khoảng **8.601đ/hội thoại** theo phép chia tổng; không mặc định 206 là khách duy nhất hay 206 đơn. Tổng chi cả bốn nhóm **2.010.495đ**. Meta còn báo sự kiện mua/đơn qua nhắn tin, nhưng chưa đối soát với đơn thực và giá trị giao thành công nên không dùng để kết luận CPA, ROAS hay lợi nhuận.

### Vị trí hiển thị thực tế

Breakdown `publisher_platform,platform_position` cùng kỳ: hai nhóm tương tác đã chi 238.578đ (**100%**) ở Facebook Feed. Hai nhóm Messenger chi 1.739.845đ (**98,2%**) ở Facebook Feed; Facebook Reels 25.538đ (**1,44%**), các vị trí khác nhận phần còn lại. Feed có 202 hội thoại bắt đầu và Reels 4 theo breakdown. Mẫu Reels nhỏ, kết quả không phải thử nghiệm ngẫu nhiên, không kết luận vị trí nào tốt hơn từ chi phí đơn vị.

## Nguồn và giới hạn

- [Performance 02/11](PERFORMANCE-2026-11-02.md) là snapshot ảnh 03/10–01/11, chỉ thấy 9/12 ads Messenger; khác kỳ và mức tổng hợp nên không thay bằng số mới.
- [Hồ sơ cấu hình đợt 08/11](../2026-11-08-dot-moi/README.md) ghi cách áp dụng bài học, quyết định hiện tại và các đính chính.
- Chưa có báo cáo hiệu quả đầy đủ cho từng ad, doanh thu thực quy kết, chi phí hoàn/giá vốn hay lợi nhuận. Số Meta có thể thay đổi do quy kết; ngày chụp không tự chứng minh trạng thái đang chạy.
