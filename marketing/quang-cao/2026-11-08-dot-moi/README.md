# Nháp quảng cáo đợt mới — 08/11/2026

## Cấu hình đã chốt và trạng thái ghi nhận gần nhất — 09/11

Hai campaign / ba ad set / 23 ads, dùng bài đã đăng trên Page chính. Nhóm tương tác có 12 ads (5 Tiempo, 6 Messi, 1 Bata), 100.000đ/ngày, mục tiêu tương tác, chỉ Facebook Feed. Nhóm Messenger Tiempo có 5 ads, Messi có 6 ads; mỗi nhóm 180.000đ/ngày, tối ưu số cuộc hội thoại, đích Messenger, không ngày kết thúc và không chia khung giờ. Không đưa Bata vào Messenger. Ngân sách theo ad set, không chia sẻ; khi cả hai campaign cùng hoạt động, tổng ngân sách ngày cấu hình là 460.000đ trong thời gian chạy tương tác, sau đó 360.000đ. Meta có thể chi cao hơn ngân sách ngày trong một số ngày.

Cả ba nhóm: Việt Nam, nam 18–44, không custom audience, không lọc sở thích, mọi ngôn ngữ; tuổi và giới tính là giới hạn, không phải suggestions. Hai nhóm Messenger để Facebook, Instagram, Audience Network và Threads cùng các nhóm vị trí Feed, Stories/Reels, in-stream, search và apps/sites. Nhóm tương tác chỉ Facebook Feed và không cho chi sang vị trí đã loại. Giữ cấu hình này theo kết quả cũ; [số liệu và phạm vi đợt 29/10](../2026-10-29-lich-su-va-ket-qua.md).

11 ads Messenger dùng mẫu `YBDS | 4 cau hoi | 08-11-2026`, bốn câu về tư vấn size, kiểm tra khi nhận, bảo hành và freeship; không gắn câu trả lời tự động. Toàn văn tại [mẫu hội thoại](../MAU-HOI-THOAI.md); mã từng ads, ngân sách và snapshots ở [ads-draft-state.json](ads-draft-state.json), bài nguồn ở [verified-posts.json](verified-posts.json).

**Lịch và bàn giao:** Dũng báo đã tự đặt nhóm tương tác bắt đầu **12:00 trưa, chạy ba ngày** và sẽ tự Publish. Chưa đọc lại lịch sau khi Dũng tự sửa, nên không khẳng định ngày bắt đầu/kết thúc thực tế từ snapshot cũ. Dũng dự định Publish Messenger sau khi làm lại Meta Agent; đây là dự định, không phải đã bật. Lần kiểm tra UI trước khi Dũng tự chỉnh: cả hai campaign là draft và tắt; cần kiểm tra live khi hỏi trạng thái sau đó. Không tự Publish hoặc thay đổi lịch.

Các mục bên dưới là **nhật ký theo thời điểm**: số 150k, ngày 08/11 và template Meta gợi ý ở các mục cũ đã được quyết định sau đó thay thế, không phải cấu hình hiện hành.

Dũng báo tự đăng đủ 12 bài trên Page chính và gắn Messenger. Đã đọc lại đủ 12 bài qua MCP: công khai, caption khớp bản duyệt, có call_to_action.type=MESSAGE_PAGE. Chi tiết ID, link, số ảnh và revision nằm trong verified-posts.json; dữ liệu live gốc tại .work/main-page-2026-11-08/. Chưa kiểm tra trực quan hoặc bấm thử nút.

Caption và thứ tự ảnh của T01–T05, M01–M06 và B01 nằm trong [bộ 12 bài](../../bai-dang/2026-11-08-chien-dich-12-bai/README.md).

Dũng yêu cầu bàn cách chia chiến dịch trước. Chưa tạo campaign/ad set/ad, chưa bật ads; ngân sách, lịch chạy, đối tượng và tập bài chạy chưa chốt. Hướng hai mục tiêu tương tác/Messenger trước đây cần được bàn lại trong lần này, chưa áp cấu hình cũ.

## Ngân sách Dũng nêu — 08/11

Dự định 400.000đ/ngày: 100.000đ tương tác bài viết trong 3 ngày rồi tắt; 300.000đ/ngày Messenger. Chưa xác định ngày bắt đầu/kết thúc Messenger. Chưa triển khai Meta. Cấu trúc campaign/ad set/ad đang thảo luận, chưa được duyệt.

## Đã dựng bản nháp trong Ads Manager — 08/11

Đã tạo qua Chrome theo yêu cầu sau khi token API không truy cập được ad account cũ. Hai campaign / ba ad set / 23 ads; cả hai campaign In draft, công tắc tắt, chưa bấm Publish. Mở lại Ads Manager vẫn thấy Review and publish (28), tương ứng 2+3+23 đối tượng. ID và ngân sách tại ads-draft-state.json.

Tương tác: 100k/ngày, 12 ads, lịch nháp 08/11 17:02 đến 11/11 17:02 GMT+7. Cần dời cả hai mốc theo giờ bật thực tế để đủ ba ngày. Messenger: Tiempo 150k/5 ads, Messi 150k/6 ads, tối ưu hội thoại, chỉ Messenger của Page chính.

Correction Dũng: giữ câu hỏi gợi ý do Meta tự suggest cho đợt này. Bỏ thay bằng mẫu ba câu cũ; không coi câu trả lời do AI gợi ý là dữ kiện tồn kho. Đối tượng/vị trí hiển thị đang giữ mặc định giao diện Vietnam/Advantage; cần Dũng rà trước chạy. Không bật ads.

## Chốt sửa ngân sách và hội thoại — 08/11

Dũng chốt Tiempo/Messi mỗi nhóm 180k/ngày, không ngày kết thúc và không chia khung giờ; tương tác giữ 100k/ngày ba ngày. Tổng 460k/ngày trong đợt tương tác, sau đó 360k/ngày; không tự chuyển thêm 100k sang Messenger. Đã sửa và đọc lại UI cả hai nhóm. Campaign Messenger đổi tên thành 360k, tắt chia sẻ ngân sách giữa nhóm.

Bỏ gợi ý AI, dùng saved template YBDS | 4 cau hoi | 08-11-2026 cho đủ 11 ads. Thứ tự: Tư vấn chọn size giúp mình với nhé? / Mình có được kiểm tra hàng khi nhận không? / Giày có được bảo hành không nhỉ? / Ship về chỗ mình có được freeship không? Không trả lời tự động; tắt follow-up và lời mời gọi tự động trong mẫu. Lời chào dùng mẫu tư vấn cởi mở đã có. Đã kiểm tra 11/11 ads đúng câu hỏi và tắt. Chưa Publish/bật quảng cáo.

## Audience và thumbnail — 08/11

Dũng yêu cầu dùng lại audience đợt cũ vì báo có kết quả tốt. Đọc live nhóm cũ 120254476317410057: Việt Nam, nam 18–44, không tệp tùy chỉnh, không lọc sở thích, mọi ngôn ngữ. Đã áp cho cả ba nhóm mới; bỏ Use as a suggestion ở tuổi/giới tính để giữ giới hạn giống nguồn cũ. Không thay placements trong lần sửa này.

Preview trực quan ENG_T01 và MSG_T01 có đúng ảnh giày trắng–vàng. Danh sách ads chỉ hiện placeholder thumbnail không đồng nghĩa thiếu ảnh; chưa xác định nguyên nhân placeholder. Chưa Publish/bật ads.

## Đối chiếu placements live — correction 08/11

Hồ sơ 29/10 ghi Facebook Feed cho mọi nhóm nhưng UI live hai nhóm Messenger cũ 120254476317410057 và 120254476340700057 hiện hiển thị Facebook/Instagram/Audience Network/Threads, các nhóm Feeds, Stories/Reels, In-stream, Search, Apps/sites đều chọn. Hai nhóm Messenger mới hiển thị cùng cấu hình nên giữ nguyên. Đây là correction theo UI hiện tại; không suy rằng cấu hình lịch sử chưa từng là Feed-only.

Nhóm tương tác cũ 120254476314180057 hiển thị Facebook, chỉ phần Feeds được chọn. Đã đổi nhóm tương tác mới sang duy nhất Facebook Feed, bỏ profile feed/Marketplace/các nhóm còn lại, tắt Allow limited spending to excluded placements. Giữ ngân sách/lịch và công tắc tắt, chưa Publish.

## Draft recovery - 2026-11-09

2026-11-09 recovery: all 3 sets restored strict Vietnam men 18-44, age/gender suggestions off. Both MSG goals changed from purchases through messaging back to conversations; 180k each/no end/no daypart. ENG 100k/day; end restored Nov9 17:02 to Nov12 17:02 GMT+7 (72h). Reopened to verify persistence. ENG Facebook Feed only, excluded-placement spending off; MSG all placement groups retained. Both campaigns off and adset budget sharing off. All 23 ad switches inspected off, all 11 MSG four-question saved-template selections inspected. No Publish.

User requested recovery after applying recommendations. Sample source posts inspected ENG_T01/T02/M06 and MSG_T01/M06; not all 23 images visually checked in this pass. Creative enhancements Adapt multi-image format/Relevant comments/Enhance CTA retained: no evidence these were newly altered. Local ads token now has correct account access; auth evidence belongs in .private/meta. UI used for unpublished drafts.
