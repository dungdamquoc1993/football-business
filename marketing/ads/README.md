# Ads — hồ sơ làm việc và lịch sử

Dũng chốt ngày 25/11/2026: giữ lịch sử ads có cấu trúc tại đây, chủ yếu phục vụ
agent tra cứu và tiếp tục công việc. Làm ads trong repo với credentials riêng ở
`.env`; không đưa token vào hồ sơ. Trạng thái trên Meta phải đọc lại trước thao tác.

## Mở đúng hồ sơ

- [Chuyển sang tài khoản phụ, 21–25/11](2026-11-21-chuyen-tai-khoan/README.md):
  kế hoạch chuyển, Messenger Messi/Vapor, tương tác và Tiempo mới; giữ các quyết
  định và việc còn chờ theo từng thời điểm.
- [Bổ sung Vapor và Messi, 15/11](2026-11-15-bo-sung/README.md).
- [Đợt 08/11](2026-11-08-dot-moi/README.md): cấu hình, các lần chỉnh và ID đối tượng.
- [Đợt 29/10](2026-10-29/README.md): ID, kết quả và giới hạn số liệu của đợt đầu.
- [Mẫu hội thoại](templates/MAU-HOI-THOAI.md): các phiên bản đã dùng; không mặc định
  mẫu cũ là mẫu đang chạy. Bài, caption và kết quả đăng thuộc [bài đăng](../fanpage-posts/README.md).

## Cách lưu sau mỗi lượt làm ads

Mỗi đợt hoặc mục tiêu có một thư mục `YYYY-MM-DD-ten-dot/`, dùng ngày bắt đầu.
Tiếp tục hồ sơ đó khi chỉnh ngân sách, thay ads hoặc kiểm tra kết quả; không mở
một thư mục mới cho mỗi phiên agent.

`README.md` của hồ sơ giữ các mục rõ ràng:

- Mục tiêu và phạm vi: tài khoản/Page, yêu cầu và quyết định của Dũng; tách đề xuất
  chưa chốt khỏi việc được giao.
- Đối tượng: `account_id`, `campaign_id`, `adset_id`, `ad_id`, `post_id` có liên quan.
- Diễn biến theo ngày: điều đã làm, lý do và kết quả; không viết lại lịch sử cũ
  theo kết quả mới. Quyết định mới cần nói rõ phần nào được thay thế.
- Kiểm chứng: `verified_at` kèm múi giờ, nguồn đọc, trạng thái đã quan sát và giới
  hạn. Bật cấu hình, được duyệt và đã phân phối là các kết quả riêng.
- Việc còn chờ: điều kiện tiếp tục, ID cần tra và hành động chưa được thực hiện.

Chỉ thêm JSON khi cần danh sách ID hoặc dữ liệu có cấu trúc để dùng lại; JSON là
snapshot có thời điểm, không thay trạng thái live. Tránh chép lại cùng kết luận
ở nhiều file. Payload, script, log và bản đọc trung gian dùng `.work/<việc>/`;
lưu outcome/ID cần thiết vào hồ sơ rồi dọn file tạm theo quy ước chung.
