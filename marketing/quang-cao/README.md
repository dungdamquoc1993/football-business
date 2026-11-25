# Quảng cáo Facebook

## Điều chỉnh chiến dịch tương tác tài khoản phụ — 22/11/2026

- Dũng chốt đổi nhóm tương tác sáu bài `120252937293610732` trên tài khoản phụ sang 100.000đ/ngày và chạy không ngày kết thúc. Dũng yêu cầu dùng Marketing API qua `META_ADS_USER_ACCESS_TOKEN`.
- Sau khi Dũng thay token, Meta từ chối đổi loại ngân sách trực tiếp (100/1885256). Đã tạo ad set `120252944848170732` trong cùng campaign `120252937293170732`, dùng lại đúng sáu creative và targeting, tạm dừng ad set cũ rồi bật ad set mới.
- Đọc lại qua API xác nhận campaign và ad set mới ACTIVE, ngân sách 100.000đ/ngày, không có ngày kết thúc. Sáu ads đang xử lý hoặc chờ duyệt. Insights hôm nay chưa có dòng chi tiêu tại lần kiểm tra sau khi bật. Receipt lưu riêng trong `.work/ads-migrate-20261121/engagement-daily-receipt.json`.

## Định hướng tài khoản quảng cáo — 21/11/2026

- Dũng báo đã thêm tài khoản phụ, dự kiến dùng làm tài khoản chạy quảng cáo chính về sau. Lý do Dũng nêu là tài khoản phụ không bị Meta cộng 10% VAT. Chưa đối chiếu hóa đơn và cách tính thuế áp dụng cho shop.
- Phương án Dũng đang cân nhắc là giảm dần ngân sách tài khoản cũ, chạy thử ngân sách nhỏ ở tài khoản phụ trong 1–2 ngày, sau đó đưa chiến dịch mới sang nếu chạy ổn. Đây là phương án đang bàn. Chưa chốt chiến dịch thử, mức ngân sách hay ngày chuyển.
- Lần đọc Meta API ngày 21/11 trả mã 190/463 (token quảng cáo hết hạn). Chưa xác nhận ngân sách hiện tại hoặc quyền trên tài khoản phụ. Chưa thay đổi quảng cáo trên Meta.

## Rà nhu cầu trước khi chia ngân sách — 21/11/2026

- Dũng muốn dựa vào ý định mua thật trước khi chốt ngân sách theo dòng giày, loại quảng cáo và sau đó mới chia giữa hai tài khoản. Phương án đang bàn là 75% Tiempo và 25% dùng chung cho Messi/Vapor, tách riêng màu khi có nhu cầu lặp lại và đủ hàng.
- Messenger Page chính từ 10:20 ngày 17/11 đến 12:00 ngày 21/11 ghi nhận khách xác nhận 24 đôi Tiempo, 4 Messi và 4 Vapor. Hai đôi Tiempo trong số này chuyển từ ý định kỳ trước sang đã chốt. Số tích lũy theo lựa chọn cuối từ 29/10 là 66/15/4 đôi; đây là xác nhận mua trong chat, bao gồm ca thiếu size, đổi/trả hoặc chưa rõ giao. Vapor kỳ cũ rà theo tên mẫu và ID quảng cáo đã biết. Bằng chứng và phạm vi lưu riêng ở `.work/ads-intent/2026-11-21/summary.json`.
- Admin ngày 21/11: Tiempo 86 đôi, Messi 46 đôi, Vapor 19 đôi tồn vật lý. Tiempo xanh nhạt móc chanh có 11 lượt chốt kỳ mới và 31 đôi tồn. Vapor đỏ/hồng có hai lượt chốt mỗi màu, cả hai đang thiếu size 41 và mỗi màu còn thiếu thêm một size trong 40–42.
- Đề xuất lấy 75/25 làm mốc thử cho ngân sách Messenger, dùng nhóm tương tác khi có mục tiêu riêng và khoản thử hữu hạn. Cần chi tiêu theo ad cùng kỳ và số đơn hoặc lượt muốn mua có thể gắn nguồn để đo hiệu quả. Chưa chốt ngân sách hay chỉnh quảng cáo.

## Phương án chuyển sang tài khoản phụ — 21/11/2026

- Dũng đặt mục tiêu ngân sách Messenger 600.000đ/ngày sau chuyển đổi, gồm 450.000đ Tiempo và 150.000đ dùng chung Messi/Vapor. Đợt này chuẩn bị sáu bài Page chính gồm bốn bài Tiempo một màu, một bài Tiempo tổng hợp và một bài Messi tổng hợp đủ sáu màu. [Caption chờ duyệt](../bai-dang/2026-11-21-nhap-caption-tiempo-messi.md).
- Token nick chính mới đọc được cả hai tài khoản, có `ads_read`, `ads_management` và tác vụ `ADVERTISE`/`MANAGE` trên mỗi tài khoản. Dũng báo đã chọn được Page chính trong bản nháp Ads Manager ở tài khoản phụ. Chưa xác nhận tài khoản phụ đã qua yêu cầu xác minh điện thoại hoặc phát sinh phân phối/thanh toán.
- Đọc live 21/11, tài khoản chính `814094494973387` đang cấu hình Messenger 480.000đ/ngày, gồm Tiempo 240.000đ, Messi 120.000đ và Vapor 120.000đ. Nhóm tương tác 50.000đ/ngày đã qua thời điểm kết thúc 19/11. Tài khoản phụ `1554033896044468` chưa có campaign.
- Phương án ba ngày đầu gồm tài khoản phụ chạy Messenger Messi/Vapor 150.000đ/ngày với 12 quảng cáo (5 bài Vapor, 6 bài Messi đơn và bài Messi tổng hợp mới thay bài gom cũ) và tương tác sáu bài mới khoảng 100.000đ/ngày. Tài khoản chính giữ Tiempo 240.000đ/ngày sau khi dừng campaign Vapor và ad set Messi trong campaign Messenger 360k. Tổng cấu hình hai bên khoảng 490.000đ/ngày, trong đó Messenger 390.000đ/ngày.
- Đề xuất xác nhận nhóm Messenger trên tài khoản phụ có phân phối và chi tiêu trước khi dừng Vapor/Messi cũ. Đặt ngân sách trọn đời 300.000đ trong 72 giờ cho tương tác. Sau ba ngày, khi tương tác đã kết thúc, bật campaign Messenger Tiempo mới với năm bài và 450.000đ/ngày. Khi nhóm Tiempo mới có phân phối, tạm dừng ad set Tiempo cũ để về 600.000đ/ngày trên tài khoản phụ. Ba ngày là mốc kiểm tra vận hành. Đánh giá hiệu quả Messenger theo tin hỏi mua thật và đơn chốt gắn nguồn khi có đủ dữ liệu.
- Dũng đang xin ý kiến về cách triển khai. Chưa xuất bản bài, tạo chiến dịch, chỉnh ngân sách hay dừng quảng cáo trong lượt này.

## Đã dựng hai chiến dịch trên tài khoản phụ — 21/11/2026

- Dũng đã đăng sáu bài và giao dựng ads trên tài khoản phụ `1554033896044468`. Tài khoản chính chỉ dùng làm nguồn đọc. Đã xác nhận đủ sáu bài mới trên Page chính qua API.
- Messenger Messi/Vapor `120252937280520732`, ad set `120252937281760732`, 150.000đ/ngày, 12 ads gồm bài Messi tổng hợp mới `693218564214489_1458069663205641`. Targeting và mẫu mở Messenger khớp nguồn live. Meta từ chối cửa sổ ghi nhận cũ; ad set mới dùng 1 ngày sau nhấp theo yêu cầu API.
- Tương tác `120252937293170732`, ad set `120252937293610732`, 300.000đ trọn đời, sáu ads dùng lại đúng bài mới, targeting như nguồn live. Lịch 13:32:23 ngày 21/11 đến 13:32:23 ngày 24/11, giờ Việt Nam.
- Đã đọc lại đủ 18 ads. Cả hai campaign đang PAUSED, quảng cáo đang xử lý hoặc chờ duyệt. Chưa dựng Messenger Tiempo 450.000đ của giai đoạn tiếp theo. Cấu hình và receipt riêng tại `.work/ads-migrate-20261121/`.

## Tra cứu lịch sử set ads

- [Bổ sung 15/11: Vapor, Messi hồng và phân bổ ngân sách](2026-11-15-bo-sung.md): đã dựng, Dũng tự bật; Vapor 120k/ngày, Tiempo 240k, Messi 120k; tương tác sáu bài 50k/ngày bốn ngày. Đã kiểm tra live và sửa tên khớp ngân sách.

- [Đợt 29/10: cấu hình và kết quả Meta đến 09/11](2026-10-29-lich-su-va-ket-qua.md): hai campaign cũ, bốn ad set, chi phí, hội thoại và phân bổ placements; ghi rõ giới hạn quy kết.
- [Đợt 08/11: cấu hình và nhật ký quyết định](2026-11-08-dot-moi/README.md): hai campaign mới, ngân sách, audience, placements, mẫu hội thoại và tình trạng bàn giao cho Dũng. Trạng thái chỉ là snapshot theo thời điểm ghi.

## Mốc trạng thái đã biết

- 29/10: tạo 2 campaign / 4 ad set / 24 ads, đều paused lúc kiểm chứng ban đầu.
- 30/10: Dũng báo đã chạy, chỉ giữ Messenger, khoảng 400k/ngày; hai nhóm tương tác đã tắt theo ảnh.
- 02/11: ảnh Dũng cung cấp hiển thị hai campaign tắt; Dũng muốn nghỉ ads đợt test, nhận đơn lẻ và chạy đợt tiếp khi có hàng.

Đây là các mốc đã ghi, không phải trạng thái live ngày 05/11. Chưa có xác nhận bật lại hoặc ngân sách mới.

## File cần dùng

- [Performance 02/11](PERFORMANCE-2026-11-02.md): số đọc từ ảnh, kỳ 03/10–01/11, 9/12 dòng Messenger; chưa đủ để tính CPA/ROAS/lợi nhuận.
- [Mẫu hội thoại](MAU-HOI-THOAI.md): ba câu mở Dũng chọn, đã gắn cho 12 Messenger ads ngày 29/10.
- `ads-state.json`: ID campaign/ad set/ad, giữ để tra và tránh tạo trùng; trạng thái trong file là snapshot cũ.
- `messenger-template.json`: payload mẫu hội thoại đã chuẩn bị.
- [Bài và link Facebook](../bai-dang/README.md): nguồn 12 bài đã dùng cho ads.

Hai campaign: Nhiều màu `120254476314060057`, Một màu `120254476321520057`; ad set Messenger tương ứng `120254476317410057` và `120254476340700057`. Tài khoản `814094494973387`.

Chi tiết cấu hình 29/10, log thử CTA/API, screenshot và bản đọc kiểm chứng đã gom tại `.work/meta-setup-2026-10/quang-cao/` ở root. Không dùng snapshot paused ban đầu để suy rằng ads chưa từng chạy. Meta có thể dùng ID hiển thị riêng cho ads; chưa xác nhận gộp social proof với bài gốc.
