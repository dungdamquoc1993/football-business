# Quét Messenger một lần, ghi từng sổ

## Chốt phạm vi

Page mặc định là `693218564214489`. Chọn các nhánh theo yêu cầu trong
[skill vận hành](../SKILL.md). Lấy `facebook_status` để biết độ mới nguồn.
Lấy độc lập:

- SaleNote: `salenote_status` → dòng `collections` đúng Page, lấy
  `cursor` và `revision`. Đọc [quy tắc nhận hồ sơ và ghi trang](../../salenote-workspace/SKILL.md#thu-thập-messenger).
- Ý định mua: `admin_replenishment_status(page_id, checkpoint_key=...)` →
  `messenger-changes:<page_id>`, lấy `data.cursor`, mốc đã rà và phiên bản
  tương ứng, cùng `settings.version`, `settings.review_revision` và
  `workspace_fingerprint` để ghi. Đọc
  [quy tắc nhận ý định mua và nguồn ads](purchase-intent.md).
  Nếu không có key này, kiểm các mốc nguồn đã dùng trước khi chọn điểm bắt đầu.
  Mốc lịch sử theo hội thoại hoặc theo ngày có phạm vi riêng. Phần lịch sử
  trước lúc có luồng sự kiện cần rà bổ sung riêng. Nếu Admin chưa khởi tạo
  sổ cho Page hoặc không truy cập được, báo phần đó và tiếp nhánh SaleNote
  nếu đủ dữ kiện.

Tiếp nối đúng mốc mỗi sổ, kể cả phần qua nửa đêm. Dấu đã đọc, thời điểm inbox
nhảy lên đầu và ngày báo cáo không thay mốc thu thập. Khi Dũng hỏi thống kê
một ngày, giới hạn số theo ngày tin gốc (giờ Việt Nam) và giữ riêng phần tồn
đọng. Chỉ tiến mốc liên tục qua phần đã thực sự xử lý.

## Đọc và xét hai kết quả

1. Dùng `facebook_search_messages(mode="changes", page_id, cursor, limit=20..30)`.
   Hết trang thì theo `next_cursor` trong lượt có `through_sequence` cố định.
   Hai sổ cùng cursor dùng chung trang. Khi lệch cursor, lấy chuỗi trang từ
   token của từng nhánh để giữ đúng cặp `from_cursor`/`next_cursor` mà nguồn
   trả về. Có thể xử lý phần riêng của nhánh chậm trước, hoặc đối chiếu hai
   trang theo `sequence` rồi dùng chung phần trùng. Không chế token, lấy mốc
   sổ này gán sổ kia hoặc ghi nhảy qua sự kiện. Nhánh hết sự kiện dừng riêng
   và không cần ghi mốc cho trang trống.
2. Gom ID chính xác theo hội thoại và đọc bằng `facebook_read(message_ids=...)`;
   dùng lại nội dung, ảnh đã xem và ngữ cảnh cho cả hai nhánh. Khi hai trang
   chồng nhau hoặc lệch ranh giới, dùng lại phần đã đọc theo Page, ID tin và
   phiên bản. Giữ bằng chứng ngắn cho lượt đang làm, đọc thêm lịch sử/ảnh chỉ
   khi cần. Với sự kiện bị thay thế hoặc nội dung không còn, ghi quyết định và
   lý do theo nhánh; phiên bản hiện hành có thể có sự kiện riêng. Xem
   [cách đọc nguồn Facebook](../../facebook-workspace/SKILL.md#đọc-messenger).
3. Xét riêng tính đủ điều kiện. Ví dụ khách nói mua rõ nhưng chưa tìm thấy
   SĐT có thể vào sổ ý định mua; hẹn báo hàng có SĐT có thể vào SaleNote dù
   chưa có ý định mua đủ ngưỡng. Với cùng lượt mua, tìm dòng và hồ sơ hiện có
   trước khi cập nhật. Tin cũ đồng bộ muộn dùng `sent_at` để xác định ngày và
   xét lại lượt gốc; một tin mới có thể chỉ là nhắc đơn hoặc hậu mãi.
4. Ghi từng sổ ngay sau khi rà hết trang của sổ đó. SaleNote ghi quyết định cho
   mọi sự kiện. Admin ghi thay đổi ý định mua, liên kết quảng cáo nếu đã xác
   minh và mốc đã rà; trang không có ý định mua mới vẫn ghi mốc kèm kết quả.
   Trong mốc Admin, lưu `data.cursor` bằng `next_cursor` và
   `data.through_sequence` theo sự kiện cuối đã xử lý của trang. Trường
   `through_sequence` Facebook trả là trần của cả lượt, có thể cao hơn trang
   đang xử lý. Giữ nguyên token nguồn đã trả để tiếp nối.
   Mỗi bên có UUID/phiên bản/biên nhận riêng, xử lý mất phản hồi và xung đột
   theo skill sở hữu. Nếu một bên ghi xong và bên kia lỗi, đọc lại biên nhận
   rồi tiếp nhánh chưa xong từ mốc của nó. Đừng ghi lại nhánh đã thành công.
5. Khi được giao hoàn tất lượt rà Messenger, lưu bộ nhớ/dấu đã đọc cho phần
   thật sự đã rà bằng `facebook_complete_review` theo skill Facebook. Việc
   này độc lập với hai sổ. Rà riêng vận đơn cần chăm sóc qua
   [SaleNote và SuperAI](../../salenote-workspace/SKILL.md#rà-vận-chuyển-để-chăm-sóc-khách).

Khi báo kết quả, nêu phần nguồn mới nhất đã xử lý, hồ sơ mới/cập nhật, ý định
mua mới/cập nhật, việc từ vận đơn và phần còn dở theo từng nhánh được giao.
Tách “mới phát hiện” khỏi “phát sinh hôm nay”. Ghi rõ đoạn lịch sử, ảnh hoặc
kênh chưa được đồng bộ nếu ảnh hưởng kết luận.
