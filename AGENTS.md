# Football Business — hướng dẫn agent

Workspace này sở hữu chi tiết thương mại/vận hành của Yêu Bóng Đá Shop.
Đọc `README.md`, rồi hồ sơ đúng việc; không lấy ghi chép lịch sử làm trạng thái live.
Phân biệt dữ kiện, giả định, đề xuất và quyết định của Dũng. Chủ động làm hết việc
được giao, nói thẳng và cụ thể; không hỏi lại quyền đã có.

## Nguồn đúng theo việc

- Ba tài liệu nền tảng là `chinh_sach_ban_hang.md` (điều kiện bán), `quy_trinh_lam_viec.md` (checklist vận hành và xử lý phát sinh) và `meta_ai_prompt.md` (hướng dẫn AI Meta). Đọc phần liên quan khi sửa chính sách, quy trình hoặc prompt và giữ nhất quán giữa ba tài liệu. Hiện Dũng tự vận hành toàn bộ, các đầu việc được tổ chức để có thể bàn giao về sau.
- Lập kế hoạch nhập hàng: `.agents/skills/weekly-replenishment/SKILL.md`.
- Báo giá và điều khoản xưởng: `supplier-quotes/README.md`.
- Phần mềm: `../yeubongdashop/README.md`, tài liệu trong `../yeubongdashop/docs/`.
- Messenger/đơn/bộ nhớ khách: `.agents/skills/facebook-workspace/SKILL.md`.
- Sản phẩm/giá/kho/thu chi: `.agents/skills/admin-workspace/SKILL.md`.
- Vận đơn: `.agents/skills/superai-workspace/SKILL.md`.
- Ảnh: `photo-workshop/AGENTS.md`; marketing giữ chiến dịch và kết quả đăng.

Dữ liệu khách, đơn, kho và vận đơn hiện hành thuộc backend tương ứng; query nguồn
phù hợp trước khi nhận biết trạng thái hiện tại. Git không thay thế database.
Không suy ra xuất kho/thu tiền từ đơn Facebook hoặc trạng thái giao hàng.
Việc đọc/tư vấn hội thoại không tự cấp quyền gửi tin.
Trước khi định giá, đọc `../yeubongdashop/docs/operations/pricing.md`.

## Git và vận hành nhiều máy

Repo business là thư mục này, nhánh `main`; remote `dungdamquoc1993/football-business`.
Repo code và lịch sử cũ ở `../yeubongdashop/`, remote `dungdamquoc1993/yeubongdashop`.
Làm/commit/push trực tiếp main theo quyết định của Dũng; không tự tạo PR/nhánh phụ.
Pull fast-forward; giữ thay đổi không liên quan. Không rewrite lịch sử hoặc force push.
Năm skill chuẩn nằm ở `.agents/skills/` tại gốc workspace; không tạo bản sao phân kỳ.

Giữ credentials, dữ liệu khách xuất riêng, `.work`, runtime và backup ngoài Git.
Không in secret khi kiểm tra cấu hình. `outputs/` chỉ dành bản giao phù hợp để lưu
trong repo, không thêm dữ liệu khách hoặc bản xuất vận hành riêng vào đây.
Mọi lệnh Compose/deploy của ứng dụng chạy từ `../yeubongdashop/`.
Đổi mã nguồn/push không đồng nghĩa được yêu cầu deploy hoặc tạo giao dịch thử.

Living Map và archive Zalo thuộc hệ thống riêng, không nằm trong repo này.
Nếu nhiệm vụ liên quan đời sống/ưu tiên xuyên dự án, dùng Map khi có quyền truy cập;
không giả định máy mới có các nguồn riêng của Mac.
