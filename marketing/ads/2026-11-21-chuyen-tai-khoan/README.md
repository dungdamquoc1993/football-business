# Chuyển sang tài khoản phụ — 21–25/11/2026

## Đối chiếu hàng đi và chi tiêu — 26/11/2026

- Dũng giao rà từ thứ Sáu20/11 đến26/11, đặt số giày đi mỗi ngày cạnh chi tiêu thực tế của cả tài khoản cũ và mới. Chỉ đọc dữ liệu, không thay đổi quảng cáo hoặc nghiệp vụ.
- Kiểm chứng khoảng10:45 ngày26/11, giờ Việt Nam: Meta Insights cấp tài khoản, từng ngày, cả hai tài khoản có múi giờ Asia/Ho_Chi_Minh và tiền VND. Cũ `814094494973387`:1.937.678đ; mới `1554033896044468`:1.257.203đ; tổng3.194.881đ. Tài khoản mới có chi tiêu trong kỳ từ21/11. Đây là chi tiêu phân phối, chưa đối soát hóa đơn/VAT hoặc khoản trừ thẻ.
- Admin MCP ghi nhận43 đôi xuất trong kỳ:39 đôi có phiếu SuperAI khớp vận đơn inventory issued,4 đôi thủ công; trong đó có1 đôi đổi size trực tiếp ngày24/11. Cơ cấu36 Tiempo,2 Messi,5 Vapor;5 đôi tất và1 túi tách khỏi số giày. Chưa trừ hoàn, chưa xác nhận đây là43 đôi bán mới hoặc đã giao thành công.
- Đọc100 phiếu kho gần nhất tới14/11 và chi tiết43 phiếu issue tạo trong kỳ; loại1 phiếu thực giao19/11 dù tạo20/11. Ngày22/11 có1 phiếu thủ công xác nhận đã nhận nhưng chưa rõ ngày gửi. Các ngày khác dùng thời điểm ghi nhận xuất kho. Đọc đủ124 snapshot vận đơn đã biết, không thay cho toàn bộ tài khoản hãng.
- Dữ liệu từng ngày, định nghĩa, giới hạn và tham chiếu đối chiếu nằm ở [snapshot tổng hợp](performance-2026-11-26.json). Ngày26/11 chưa kết thúc. Không lưu danh tính khách hoặc bản xuất vận hành riêng vào Git.
- Quan sát:20–22/11 ghi nhận31 đôi, ads1.519.279đ;23–25/11 ghi nhận12 đôi (gồm1 đôi đổi), ads1.579.827đ. Đây là tín hiệu cần theo dõi, chưa đủ kết luận tài khoản mới kém hơn vì chưa nối nguồn từng đơn và có độ trễ giữa ads/chốt/gửi. Chưa quyết định đổi ngân sách trong lượt rà này.

## Messenger Tiempo tài khoản phụ — 25/11/2026

### Rà chất lượng sau chuyển —26/11/2026

- Dũng báo leads hôm25 và sáng26/11 rất kém, nghi liên quan việc tăng tài khoản mới/giảm tài khoản cũ từ23/11. Đây là quan sát vận hành của Dũng, chưa phải tỷ lệ lead đủ chuẩn đã đo. Dũng cho biết billing tài khoản mới ở Trung Quốc và không bị cộng10% VAT; chưa kiểm chứng hóa đơn/thuế.
- Đọc live Meta API sau bảng tổng hợp sáng26/11: Tiempo cũ effective_status CAMPAIGN_PAUSED; Tiempo mới ACTIVE350k/ngày và Messi/Vapor mới ACTIVE150k/ngày; tương tác mới CAMPAIGN_PAUSED. Nhóm Messenger hai bên đều tối ưu CONVERSATIONS, địa lý VN; cũ attribution7 ngày nhấp+1 ngày xem, mới1 ngày nhấp. Chưa chứng minh khác attribution gây khác chất lượng.
- Breakdown23/11 mới: Messenger Messi/Vapor175.057đ,21 hội thoại; tương tác120.892đ,1 hội thoại.24/11 mới: Messenger167.076đ,16 hội thoại; tương tác108.437đ,không có hội thoại. Tương tác chi229.329/571.462đ hai ngày, khoảng40,1%; tổng chi tài khoản mới tăng không đồng nghĩa tiền tìm hội thoại tăng cùng mức.
-25/11 Tiempo mới171.743đ/10 hội thoại (khoảng17,2k); Messi/Vapor mới162.199đ/17 (khoảng9,5k); tương tác57.167đ. Campaign Messenger cũ129.386đ/10 (khoảng12,9k). Không mặc định campaign cũ chỉ có Tiempo trong toàn ngày nếu chưa đọc breakdown ad set; chỉ số hội thoại dùng onsite_conversion.messaging_conversation_started_7d, theo cấu hình quy kết từng bên.
- Agent nhận định cần ưu tiên khôi phục nguồn khách có khả năng mua, so Tiempo cùng dòng/cùng bài và đánh giá hội thoại đủ chuẩn/đơn chốt mới theo ngày tạo lead; số xuất kho có độ trễ. Đề xuất quay Tiempo cũ về mức240k/ngày làm đối chứng và tạm dừng Tiempo mới, giữ thử Messi/Vapor hữu hạn; chưa được Dũng chọn và chưa thực hiện. Không có thay đổi quảng cáo trong lượt tư vấn này.

- Dũng giao tạo và bật campaign trên tài khoản phụ `1554033896044468`, dùng đúng năm link bài Tiempo ngày 21/11. Tổng ngân sách **350.000đ/ngày** cho một ad set, không đặt ngày kết thúc; mức này thay mức 450k từng dự kiến cho nhóm Tiempo mới.
- Campaign `120252988857160732` — `YBDS | 2026-11-25 | Messenger Tiempo | 350k`; ad set `120252988885520732`. Nguồn cấu hình live: campaign chính `120254658365110057`, ad set Tiempo `120254658365120057`.
- Đã đối chiếu campaign objective `OUTCOME_ENGAGEMENT`, AUCTION, ngân sách ở ad set; giữ nguyên targeting/placement live, tối ưu `CONVERSATIONS`, đích `MESSENGER`, tính phí impressions, lowest cost không cap và mẫu chào/câu hỏi từ từng creative Tiempo nguồn. Target nam 18–44, Việt Nam; Advantage+ audience tắt, không thêm giới hạn placement. Dùng bài có sẵn, không tạo lại bài Page.
- Ngoại lệ Dũng đã đồng ý: Meta từ chối attribution 7 ngày sau nhấp + 1 ngày sau xem (100/1885501), chỉ chấp nhận **1 ngày sau nhấp** cho nhóm mới. Đây là cửa sổ quy kết, không phải thời gian phải đợi để nhận báo cáo.
- Đọc lại 15:34 ngày 25/11, giờ Việt Nam: campaign/ad set ACTIVE, đủ năm ads ACTIVE ở cấp cấu hình; bốn ads PENDING_REVIEW, một IN_PROCESS. Insights hôm nay chưa có dòng chi tiêu; chưa xác nhận đã phân phối.
- Nhóm Tiempo cũ vẫn ACTIVE 240k/ngày; chưa tạm dừng trong lượt này. Theo phương án chuyển cũ, chỉ chuyển nốt sau khi nhóm mới thực sự phân phối. Tại lần đọc này tài khoản phụ còn Messenger Messi/Vapor 150k và tương tác 100k/ngày: tổng cấu hình phụ 600k, cộng Tiempo cũ 240k là 840k/ngày; đây là ngân sách cấu hình, không phải chi tiêu thực tế.

Ads đã xác nhận đúng từng link pfbid Dũng gửi qua Page API:

- Trắng–vàng: post `693218564214489_1458062029873071`, ad `120252988886350732`, creative `983700377723864`. [Link được giao](https://www.facebook.com/yeubongdashop1234/posts/pfbid02F2Hm41gpxkCsD2LnJbbhQZa8E7fFdnJtjjCCJsFVhcDLMRLRXZB5U8ac7as7zAuol).
- Xanh dương–bạc: post `693218564214489_1458063203206287`, ad `120252988886890732`, creative `3319910714859016`. [Link được giao](https://www.facebook.com/yeubongdashop1234/posts/pfbid02PDa922J1E8FpEiqQ9WXhdKxqGzVCTsbfQipA8WMowCKvb7EtkEHtyKjeRxS2HWvpl).
- Đỏ–đen: post `693218564214489_1458064083206199`, ad `120252988887200732`, creative `1728365555467648`. [Link được giao](https://www.facebook.com/yeubongdashop1234/posts/pfbid0ju8uDMCfsY1bWQRaz1A5EgqVdvtag4bAiURvuAuLo5rJorgB9xMqE2DgyN7b2vsrl).
- Xanh da trời–chanh: post `693218564214489_1458064863206121`, ad `120252988888120732`, creative `1439774401559376`. [Link được giao](https://www.facebook.com/yeubongdashop1234/posts/pfbid0tDr2eNmd6uQUY3eR38YMQuNdjEf7teaMYFzqgJDBoosA7BiT5689xSgSoTuPwdprl).
- Tổng hợp bốn màu: post `693218564214489_1458068173205790`, ad `120252988888480732`, creative `1164946439804599`. [Link được giao](https://www.facebook.com/yeubongdashop1234/posts/pfbid02QMKKU2eL7BZ7ttvYTgbSSwAb7KCUmVJnMXEF3d2vW7KcybLZQM7rBBuyg4RouQrJl).

## Điều chỉnh chiến dịch tương tác tài khoản phụ — 22/11/2026

- Dũng chốt đổi nhóm tương tác sáu bài `120252937293610732` trên tài khoản phụ sang 100.000đ/ngày và chạy không ngày kết thúc. Dũng yêu cầu dùng Marketing API qua `META_ADS_USER_ACCESS_TOKEN`.
- Sau khi Dũng thay token, Meta từ chối đổi loại ngân sách trực tiếp (100/1885256). Đã tạo ad set `120252944848170732` trong cùng campaign `120252937293170732`, dùng lại đúng sáu creative và targeting, tạm dừng ad set cũ rồi bật ad set mới.
- Đọc lại qua API xác nhận campaign và ad set mới ACTIVE, ngân sách 100.000đ/ngày, không có ngày kết thúc. Sáu ads đang xử lý hoặc chờ duyệt. Insights hôm nay chưa có dòng chi tiêu tại lần kiểm tra sau khi bật. Tra các ID Meta ở trên để đọc trạng thái hiện hành; receipt local của lượt dựng đã dọn.

## Định hướng tài khoản quảng cáo — 21/11/2026

- Dũng báo đã thêm tài khoản phụ, dự kiến dùng làm tài khoản chạy quảng cáo chính về sau. Lý do Dũng nêu là tài khoản phụ không bị Meta cộng 10% VAT. Chưa đối chiếu hóa đơn và cách tính thuế áp dụng cho shop.
- Phương án Dũng đang cân nhắc là giảm dần ngân sách tài khoản cũ, chạy thử ngân sách nhỏ ở tài khoản phụ trong 1–2 ngày, sau đó đưa chiến dịch mới sang nếu chạy ổn. Đây là phương án đang bàn. Chưa chốt chiến dịch thử, mức ngân sách hay ngày chuyển.
- Lần đọc Meta API ngày 21/11 trả mã 190/463 (token quảng cáo hết hạn). Chưa xác nhận ngân sách hiện tại hoặc quyền trên tài khoản phụ. Chưa thay đổi quảng cáo trên Meta.

## Rà nhu cầu trước khi chia ngân sách — 21/11/2026

- Dũng muốn dựa vào ý định mua thật trước khi chốt ngân sách theo dòng giày, loại quảng cáo và sau đó mới chia giữa hai tài khoản. Phương án đang bàn là 75% Tiempo và 25% dùng chung cho Messi/Vapor, tách riêng màu khi có nhu cầu lặp lại và đủ hàng.
- Messenger Page chính từ 10:20 ngày 17/11 đến 12:00 ngày 21/11 ghi nhận khách xác nhận 24 đôi Tiempo, 4 Messi và 4 Vapor. Hai đôi Tiempo trong số này chuyển từ ý định kỳ trước sang đã chốt. Số tích lũy theo lựa chọn cuối từ 29/10 là 66/15/4 đôi; đây là xác nhận mua trong chat, bao gồm ca thiếu size, đổi/trả hoặc chưa rõ giao. Vapor kỳ cũ rà theo tên mẫu và ID quảng cáo đã biết. Phạm vi gồm 530 hội thoại nền và 216 hội thoại kỳ mới, giao nhau 42; 145 hội thoại kỳ mới có lịch sử chưa đầy đủ. Bản xuất local đã dọn; tin gốc tra Facebook MCP.
- Admin ngày 21/11: Tiempo 86 đôi, Messi 46 đôi, Vapor 19 đôi tồn vật lý. Tiempo xanh nhạt móc chanh có 11 lượt chốt kỳ mới và 31 đôi tồn. Vapor đỏ/hồng có hai lượt chốt mỗi màu, cả hai đang thiếu size 41 và mỗi màu còn thiếu thêm một size trong 40–42.
- Đề xuất lấy 75/25 làm mốc thử cho ngân sách Messenger, dùng nhóm tương tác khi có mục tiêu riêng và khoản thử hữu hạn. Cần chi tiêu theo ad cùng kỳ và số đơn hoặc lượt muốn mua có thể gắn nguồn để đo hiệu quả. Chưa chốt ngân sách hay chỉnh quảng cáo.

## Phương án chuyển sang tài khoản phụ — 21/11/2026

- Dũng đặt mục tiêu ngân sách Messenger 600.000đ/ngày sau chuyển đổi, gồm 450.000đ Tiempo và 150.000đ dùng chung Messi/Vapor. Đợt này chuẩn bị sáu bài Page chính gồm bốn bài Tiempo một màu, một bài Tiempo tổng hợp và một bài Messi tổng hợp đủ sáu màu. [Caption chờ duyệt](../../fanpage-posts/2026-11-21/README.md).
- Token nick chính mới đọc được cả hai tài khoản, có `ads_read`, `ads_management` và tác vụ `ADVERTISE`/`MANAGE` trên mỗi tài khoản. Dũng báo đã chọn được Page chính trong bản nháp Ads Manager ở tài khoản phụ. Chưa xác nhận tài khoản phụ đã qua yêu cầu xác minh điện thoại hoặc phát sinh phân phối/thanh toán.
- Đọc live 21/11, tài khoản chính `814094494973387` đang cấu hình Messenger 480.000đ/ngày, gồm Tiempo 240.000đ, Messi 120.000đ và Vapor 120.000đ. Nhóm tương tác 50.000đ/ngày đã qua thời điểm kết thúc 19/11. Tài khoản phụ `1554033896044468` chưa có campaign.
- Phương án ba ngày đầu gồm tài khoản phụ chạy Messenger Messi/Vapor 150.000đ/ngày với 12 quảng cáo (5 bài Vapor, 6 bài Messi đơn và bài Messi tổng hợp mới thay bài gom cũ) và tương tác sáu bài mới khoảng 100.000đ/ngày. Tài khoản chính giữ Tiempo 240.000đ/ngày sau khi dừng campaign Vapor và ad set Messi trong campaign Messenger 360k. Tổng cấu hình hai bên khoảng 490.000đ/ngày, trong đó Messenger 390.000đ/ngày.
- Đề xuất xác nhận nhóm Messenger trên tài khoản phụ có phân phối và chi tiêu trước khi dừng Vapor/Messi cũ. Đặt ngân sách trọn đời 300.000đ trong 72 giờ cho tương tác. Sau ba ngày, khi tương tác đã kết thúc, bật campaign Messenger Tiempo mới với năm bài và 450.000đ/ngày. Khi nhóm Tiempo mới có phân phối, tạm dừng ad set Tiempo cũ để về 600.000đ/ngày trên tài khoản phụ. Ba ngày là mốc kiểm tra vận hành. Đánh giá hiệu quả Messenger theo tin hỏi mua thật và đơn chốt gắn nguồn khi có đủ dữ liệu.
- Dũng đang xin ý kiến về cách triển khai. Chưa xuất bản bài, tạo chiến dịch, chỉnh ngân sách hay dừng quảng cáo trong lượt này.

## Đã dựng hai chiến dịch trên tài khoản phụ — 21/11/2026

- Dũng đã đăng sáu bài và giao dựng ads trên tài khoản phụ `1554033896044468`. Tài khoản chính chỉ dùng làm nguồn đọc. Đã xác nhận đủ sáu bài mới trên Page chính qua API.
- Messenger Messi/Vapor `120252937280520732`, ad set `120252937281760732`, 150.000đ/ngày, 12 ads gồm bài Messi tổng hợp mới `693218564214489_1458069663205641`. Targeting và mẫu mở Messenger khớp nguồn live. Meta từ chối cửa sổ ghi nhận cũ; ad set mới dùng 1 ngày sau nhấp theo yêu cầu API.
- Tương tác `120252937293170732`, ad set `120252937293610732`, 300.000đ trọn đời, sáu ads dùng lại đúng bài mới, targeting như nguồn live. Lịch 13:32:23 ngày 21/11 đến 13:32:23 ngày 24/11, giờ Việt Nam.
- Đã đọc lại đủ 18 ads. Cả hai campaign đang PAUSED, quảng cáo đang xử lý hoặc chờ duyệt. Chưa dựng Messenger Tiempo 450.000đ của giai đoạn tiếp theo. Đây là trạng thái lúc dựng ngày 21/11; các ID campaign/ad set ở trên dùng để tra Meta, không phụ thuộc script hoặc receipt local.

## Tra cứu lịch sử set ads

- [Bổ sung 15/11: Vapor, Messi hồng và phân bổ ngân sách](../2026-11-15-bo-sung/README.md): đã dựng, Dũng tự bật; Vapor 120k/ngày, Tiempo 240k, Messi 120k; tương tác sáu bài 50k/ngày bốn ngày. Đã kiểm tra live và sửa tên khớp ngân sách.

- [Đợt 29/10: cấu hình và kết quả Meta đến 09/11](../2026-10-29/README.md): hai campaign cũ, bốn ad set, chi phí, hội thoại và phân bổ placements; ghi rõ giới hạn quy kết.
- [Đợt 08/11: cấu hình và nhật ký quyết định](../2026-11-08-dot-moi/README.md): hai campaign mới, ngân sách, audience, placements, mẫu hội thoại và tình trạng bàn giao cho Dũng. Trạng thái chỉ là snapshot theo thời điểm ghi.

## Mốc trạng thái đã biết

- 29/10: tạo 2 campaign / 4 ad set / 24 ads, đều paused lúc kiểm chứng ban đầu.
- 30/10: Dũng báo đã chạy, chỉ giữ Messenger, khoảng 400k/ngày; hai nhóm tương tác đã tắt theo ảnh.
- 02/11: ảnh Dũng cung cấp hiển thị hai campaign tắt; Dũng muốn nghỉ ads đợt test, nhận đơn lẻ và chạy đợt tiếp khi có hàng.

Đây là các mốc đã ghi, không phải trạng thái live ngày 05/11. Chưa có xác nhận bật lại hoặc ngân sách mới.

## File cần dùng

- [Performance 02/11](../2026-10-29/PERFORMANCE-2026-11-02.md): số đọc từ ảnh, kỳ 03/10–01/11, 9/12 dòng Messenger; chưa đủ để tính CPA/ROAS/lợi nhuận.
- [Mẫu hội thoại](../templates/MAU-HOI-THOAI.md): ba câu mở Dũng chọn, đã gắn cho 12 Messenger ads ngày 29/10.
- [ID đợt 29/10](../2026-10-29/ads-state.json): ID campaign/ad set/ad, giữ để tra và tránh tạo trùng; trạng thái trong file là snapshot cũ.
- [Payload mẫu hội thoại](../templates/messenger-template.json): mẫu đã chuẩn bị.
- [Bài và link Facebook](../../fanpage-posts/README.md): nguồn 12 bài đã dùng cho ads.

Hai campaign: Nhiều màu `120254476314060057`, Một màu `120254476321520057`; ad set Messenger tương ứng `120254476317410057` và `120254476340700057`. Tài khoản `814094494973387`.

Log thử CTA/API, screenshot và bản đọc kiểm chứng local cũ đã dọn; ID và kết quả cần giữ nằm trong hồ sơ từng đợt. Không dùng snapshot paused ban đầu để suy rằng ads chưa từng chạy. Meta có thể dùng ID hiển thị riêng cho ads; chưa xác nhận gộp social proof với bài gốc.
