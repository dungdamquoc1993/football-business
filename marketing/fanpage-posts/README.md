# Fanpage posts — caption và lịch sử đăng bài

Mỗi đợt có một thư mục theo ngày. Marketing chỉ giữ text và metadata; ảnh nằm
trong `photo-workshop/`, không thêm bản sao ảnh hoặc dữ liệu ảnh base64 vào đây.

## Mở bài gần đây

- [21/11 — 6 bài Tiempo và Messi](2026-11-21/README.md).
- [15/11 — 6 bài Vapor và Messi trắng–hồng](2026-11-15/README.md).
- [08/11 — 12 bài Tiempo, Messi và Bata](2026-11-08/README.md).
- [29/10 — 12 bài cũ, Dũng báo đã xoá sau đó](2026-10-29/README.md).

## Đọc và dùng lại

- `captions/<mã>.md`: chỉ chứa caption công khai, mở ra có thể sao chép cả file.
- `posts.json`: tiêu đề, file caption, Page/post ID, permalink, nguồn và thời điểm
  kiểm chứng, thứ tự ảnh cùng đường dẫn/SHA-256. Đường dẫn ảnh tính từ gốc repo;
  đường dẫn caption tính từ thư mục đợt.
- `caption-variants/` chỉ có khi bản Desktop hoặc bản chuẩn bị khác bản đã đăng;
  metadata ghi rõ nguồn, không âm thầm ghi đè một bản bằng bản khác.

Caption chính ưu tiên bản Page chính đọc được khi đối chiếu; giữ trạng thái từng
Page riêng. Bản nháp thử, bộ giao để tự đăng và bài công khai là các loại kết quả
khác nhau. Metadata lưu điều đã quan sát tại thời điểm ghi, không thay trạng thái
live trên Meta. Trước khi đăng lại cần kiểm tra giá, phạm vi và quyền đã được giao.

Ảnh của một bài được ghim bằng SHA-256, không thay bằng ảnh mới chỉ vì cùng tên
mẫu/màu. Khi một release chuyển chỗ, cập nhật đường dẫn nhưng giữ hash và lịch sử.
`desktop_handoff` giữ lựa chọn từng thấy trong bộ giao; không tự coi các file
người dùng thêm vào Desktop là ảnh thực sự đã đăng.

Ba bộ Desktop ngày 08, 15 và 21/11 đã được đối chiếu để gom vào đây. Có thể xuất
lại một bộ caption + ảnh từ metadata khi cần; bản giao Desktop chỉ giữ trong lúc
dùng và dọn sau đó. Git giữ text/metadata, thư viện ảnh local tiếp tục thuộc workshop.
