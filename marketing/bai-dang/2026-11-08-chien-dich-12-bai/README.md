# Chiến dịch 12 bài — bản duyệt 08/11/2026

Trạng thái 08/11: Đã đăng và kiểm tra 12 bài trên mỗi trong bốn Page phụ, tổng 48 bài; Dũng đồng ý các bài này không có nút Messenger. Page chính Giày Đá Bóng - Yêu Bóng Đá Shop để Dũng tự đăng và gắn nút. Chưa tạo/bật quảng cáo. Chi tiết ID, link và kiểm tra nằm trong publication-state.json.

## Quyết định của Dũng

- Tiempo 8: bốn bài một màu và một bài gom, tổng năm bài.
- Messi: năm bài một màu và một bài gom, tổng sáu bài.
- Bata: một bài gom ba màu, không đánh mạnh dòng này.
- Caption có giá, không gắn link sản phẩm. Quyết định có giá thay cho ý định bỏ giá đã bàn trước.
- Bài đơn dùng đủ tám ảnh; ảnh hút mắt và giới thiệu dáng đứng trước, ảnh cận phía sau. Bài gom Tiempo/Messi mỗi màu một ảnh cùng pose; Bata mỗi màu hai góc, ba ảnh chọn màu trước, ba ảnh góc bên sau.
- Hướng phát hành sau duyệt: 12 bài trên cả năm Page (dự kiến 60 lượt đăng), chỉ chạy ads cho một Page. Chưa đối chiếu danh sách/ID năm Page và Page được chọn chạy ads trong lượt soạn này.
- Giữ hướng hai chiến dịch: tương tác bài và Messenger. Bài cần nút Messenger ngay từ đầu; kiểm chứng khả năng giữ CTA và dùng lại bài giữa hai mục tiêu trước khi làm hàng loạt.

## Cách triển khai đang đề xuất, chưa chốt

Mỗi bài gom giúp so màu trong cùng mẫu; bài riêng cho xem kỹ một phối màu. Không cố giấu ảnh để kiếm inbox xin ảnh. CTA tập trung vào kiểm tra size, tư vấn và đặt hàng.

Thứ tự ảnh trong từng file là đề xuất theo vai trò/tên file của bộ đã duyệt; chưa kiểm tra trực quan lại từng thứ tự hoặc bố cục Facebook trên điện thoại. Ảnh đầu cùng dùng 01-hero-pair ở các màu để nhất quán; có thể đổi sau duyệt ảnh. Không khẳng định thứ tự này đã tối ưu hiệu quả quảng cáo.

Không tự áp phương án cũ tám bài/năm bài chạy hoặc tỷ lệ ngân sách 85–90%: đó là đề xuất trước, chưa được Dũng chốt. Chưa chốt ngân sách, lịch, đối tượng, tập bài chạy và phân tiền hai chiến dịch. Lợi nhuận sau chi phí phục vụ/ads và đơn giao thành công là căn cứ đánh giá; hội thoại và tương tác chỉ là tín hiệu trung gian.

## Giá dùng trong bản nháp

Tiempo 8: 398.066đ; Messi: 291.462đ; Bata ráp đế: 168.993đ mỗi đôi. Nguồn: [chính sách giá](../../../../yeubongdashop/docs/operations/pricing.md). Đây là số ghi nhận để soạn; chưa đọc catalog live trong lượt này. Kiểm tra lại trước phát hành, không tự làm tròn hoặc ghi đè ngoại lệ Tiempo/Bata.

Không tự hứa freeship/đủ size/có sẵn cả 12 màu. Bộ ảnh có bảy màu từng nhập và năm màu Dũng báo có thể bổ sung nhanh; đây không phải tồn hiện tại. Kiểm tra SKU/khả năng cung ứng trước phát hành, bổ sung thời gian chờ theo màu nếu cần. Không đưa tính năng hiệu năng/chất liệu chưa được xác minh vào caption.

## Caption và ảnh để duyệt

Phần “Caption để đăng” trong mỗi file là nội dung công khai. Những mục còn lại chỉ là ghi chú nội bộ. Đường dẫn ảnh là tài liệu chuẩn bị, không chèn vào caption. Tổng 87 vị trí ảnh, tái sử dụng từ bộ ảnh đã duyệt; không tạo thêm hoặc thay ảnh nguồn.

- [T01 — Tiempo trắng–vàng](T01.md)
- [T02 — Tiempo xanh dương–bạc](T02.md)
- [T03 — Tiempo đỏ–đen](T03.md)
- [T04 — Tiempo xanh da trời–chanh](T04.md)
- [T05 — Tiempo gom bốn màu](T05.md)
- [M01 — Messi bạc sọc đen](M01.md)
- [M02 — Messi xanh da trời](M02.md)
- [M03 — Messi đen–vàng](M03.md)
- [M04 — Messi đỏ–trắng](M04.md)
- [M05 — Messi xanh than–bạc, sọc cam](M05.md)
- [M06 — Messi gom năm màu](M06.md)
- [B01 — Bata gom ba màu](B01.md)

[manifest.json](manifest.json) giữ thứ tự đường dẫn ảnh chính xác cho lần triển khai, chưa phải nhật ký đăng. Khi thực sự phát hành cần lưu Page ID, post ID/permalink và kết quả riêng từng bài/từng Page để tránh trùng khi thử lại. Chỉ Page được chọn mới gắn quảng cáo; không coi 60 lượt đăng là 60 quảng cáo.

Trước phát hành: Dũng duyệt caption/ảnh/giá; đối chiếu năm Page và Page ads; kiểm tra tồn/đặt hàng, phí giao, preview và nút Messenger trên một bài thử đã được giao thực hiện, sau đó mới nhân rộng. Tài liệu này không tự cấp quyền đăng bài thử.

## Sửa nội dung sau góp ý của Dũng — 08/11

Dũng đánh giá bản đầu hời hợt, hook bị lệ thuộc cuộc bàn nội bộ; giữ cấu trúc/độ dài nhưng cần viết theo nhu cầu người mua. Đã viết lại cả 12 caption sau khi xem đủ 12 contact sheet (96 ảnh thu nhỏ), chưa kiểm tra lại từng ảnh ở độ phân giải gốc. Hướng nội dung: nhu cầu thay giày, niềm vui có đôi mới, phối với đồ đi đá và lựa chọn trong ngân sách. Từng bài dùng chi tiết ngoại hình quan sát được làm lý do quan tâm; CTA hỗ trợ chọn size. Messi đen–vàng được mô tả thêm sọc cam đúng ảnh. Các hướng này là giả thuyết sáng tạo để duyệt, chưa có dữ liệu chứng minh chuyển đổi. Không suy độ êm, bền, bám sân, fit hoặc cảm giác bóng từ ảnh. Giá, cơ cấu bài và danh sách ảnh giữ nguyên; chưa đăng.

## Publication preparation update

User approved all 12 captions for publication to all five Pages, but requires a Messenger button BEFORE publication. Posting first without the button was explicitly rejected. No Meta uploads or post writes were made in this preparation turn.

Frozen release: photo-workshop/03-READY/By-campaign/2026-11-08-12-posts-v01/release.json. All 78 unique images (87 ordered slots across 12 posts) match approved release hashes. publication-state.json holds the exact captions, assets, five Page IDs and stable upload/draft/publish operation UUIDs. All remain not_sent.

Production needs the follow-up 22-tool release: create unpublished Messenger draft, read back CTA, then publish only when the CTA is verified. Real Meta support for CTA on multi-photo posts remains unproven. Do not bypass the requirement if Meta rejects or ignores CTA.

## Production upload check after deployment

Production confirmed 22 tools with messenger_cta and facebook_publish_post. First T01 image upload (1,900,395 PNG bytes / 2,533,860 base64 bytes) was rejected HTTP 413 by backend RequestBoundaryMiddleware before MCP execution. A read-only operation lookup confirmed operation_not_found; no asset, draft or public post was created. Code fix raises only the authenticated Facebook MCP body allowance for base64 overhead. Waiting for backend redeploy before resuming the same stored operation UUID. Read-only probe evidence: .work/facebook-pricing-2026-11-08/upload-proxy-probe.json.

## Messenger draft pilot outcome

All eight T01 photo uploads succeeded via production MCP. Draft 693218564214489_1444181707927770 remains unpublished. Caption and Messenger CTA match, but Meta returned a Page-share attachment instead of the eight ordered photos. No publish was attempted. Receipts/live snapshot are saved in publication-state.json. Waiting for a backend follow-up that guards caption/photo IDs/order and supports an experimental CTA request without the optional m.me link. Existing draft is retained; no automatic deletion or claim of successful publication.

## Second Messenger draft result (production)

After server 6031fdb, the explicit no-link CTA variant created draft 693218564214489_1444190097926931. Live Meta read confirms unpublished, exact caption and all eight original photo IDs in the requested order. However, call_to_action is absent. No publication was attempted. The linked CTA draft retains CTA but only a Page share; the no-link draft retains photos but no CTA. These observations establish that neither tested request meets the user requirement, not that every possible Meta surface/API is incapable. Both drafts are retained; no more speculative code/deploy changes or bulk posting were performed. Publication remains blocked by the user requirement to have a Messenger button first.

## Manual publication handoff

User chose manual publication and manual Messenger button setup. Delivered a disposable Desktop package at /Users/dung/Desktop/Bai Facebook - 12 bai - 08-11-2026: 12 post folders, 87 ordered PNG copies verified against approved SHA-256, and one Caption.md per post containing only the unchanged approved public caption. No headings/internal notes in caption files. User plans to delete this Desktop copy after use; canonical campaign captions and approved images remain in the project. No agent publication is pending under this handoff; two pilot drafts remain unpublished and were not deleted. Manual publication completion is not yet reported.

## Đăng bốn Page phụ — 08/11

Dũng đổi phạm vi: tự đăng Page chính Giày Đá Bóng - Yêu Bóng Đá Shop (693218564214489) và đồng ý để agent đăng 12 bài lên từng Page phụ không có nút Messenger. Đã đăng thành công 48/48 bài qua MCP, kiểm tra live caption, trạng thái công khai và ID/thứ tự ảnh. Mỗi bài gom dùng ảnh tải riêng: thử dùng lại ảnh bài đơn cho T05 bị Meta từ chối; lần tải riêng thành công. ID, permalink, operation và kết quả kiểm tra từng bài lưu trong [publication-state.json](publication-state.json). Page chính vẫn có hai bản nháp thử cũ chưa công khai; Dũng tự đăng bài mới. Không tạo quảng cáo. Kiểm tra qua API không xác nhận bố cục hiển thị trên điện thoại.

## Xác nhận Page chính và chuẩn bị ads — 08/11

Dũng đã tự đăng 12 bài và gắn Messenger. Đã đọc live đủ 12 bài qua private MCP: công khai, caption khớp bản duyệt, có CTA MESSAGE_PAGE. Hồ sơ nháp quảng cáo local và ID bài nằm tại marketing/quang-cao/2026-11-08-dot-moi/. Chưa kiểm tra trực quan/bấm nút; chưa tạo hoặc bật quảng cáo. Dũng yêu cầu thảo luận cấu trúc chiến dịch trước.
