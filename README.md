# Football Business — Yêu Bóng Đá Shop

**Trước khi định giá hàng mới hoặc đổi giá:** đọc [chính sách giá](chinh_sach_gia.md) — mặc định chi phí phục vụ theo C1 ×1,8; giữ ngoại lệ và giá chốt riêng của Dũng.

## Phạm vi và nguồn dữ liệu

Repo này giữ chính sách, quy trình, tài sản kinh doanh và năm skills chuẩn tại
[.agents/skills](.agents/skills). Tài liệu và skills dùng độc lập, không yêu cầu
repo phần mềm nằm cạnh bên hoặc đọc docs của repo khác. Remote:
`dungdamquoc1993/football-business`, làm trực tiếp trên `main`.

Dữ liệu khách, đơn, kho, vận đơn và kế hoạch nhập hàng hiện hành thuộc server,
đọc/ghi qua MCP đã cấu hình. Repo và bản xuất local không thay database.
Các nghiệp vụ đã có hướng dẫn và tools MCP dùng bộ skills cùng quyền MCP;
không cần lấy `.work` hoặc provider credentials từ máy Mac. Chính sách chưa
có trong skill/MCP cần được cung cấp khi giao việc liên quan. Deploy và phát
triển ứng dụng là nhiệm vụ riêng, không thực hiện trong repo này.

Mục tiêu Dũng nêu ngày 25/11/2026: hơn 90% thao tác vận hành số thường xuyên
có thể giao cho agent hoàn thành bằng bộ skills và MCP được cấp quyền, không
cần đọc code hoặc lấy file làm việc từ máy cũ. Đây là mục tiêu, chưa phải tỷ lệ
đã đo. Đánh giá theo lượt việc thực tế hoàn thành, không theo số lượng tools.

Phạm vi Dũng chốt cùng ngày: đăng bài và làm ads tiếp tục mở repo này, dùng
tài sản local và credentials trong `.env`; chưa yêu cầu các việc đó chạy chỉ
bằng skills + MCP. Chưa có quyết định đưa toàn bộ tài liệu hoặc tài sản lên server.

## Mở theo việc

- **Ba tài liệu nền tảng:** [Chính sách bán hàng](chinh_sach_ban_hang.md), [Quy trình làm việc hằng ngày và phát sinh](quy_trinh_lam_viec.md), [Meta Agent](marketing/meta-agent/README.md). Hiện Dũng vận hành toàn bộ; quy trình chia theo đầu việc để có thể bàn giao về sau.
- **Nhập hàng hằng tuần:** [skill lập kế hoạch và xuất Excel đặt xưởng](.agents/skills/weekly-replenishment/SKILL.md),
  dùng dữ liệu server qua Admin MCP. Nguồn nhập hàng cũ đã được import và kiểm tra
  luồng đọc/ghi production ngày 25/11/2026; tiếp tục công việc từ server.
- **Ảnh sản phẩm:** [Photo workshop](photo-workshop/README.md) — bỏ ảnh vào, xem duyệt, lấy bộ đã duyệt; hồ sơ nguồn/prompt ở hậu trường.
- **Giá và nguồn hàng:** [supplier quotes](supplier-quotes/README.md) — báo giá và ghi chú xưởng. Sản phẩm và tồn hiện hành tra Admin MCP.
- **Bài Facebook:** [fanpage-posts](marketing/fanpage-posts/README.md) — caption, metadata và lịch sử từng đợt; ảnh tra workshop.
- **Quảng cáo và nhận diện:** [ads](marketing/ads/README.md), [logo và ảnh bìa](marketing/nhan-dien/README.md).
- **Messenger và Facebook:** [skill Facebook](.agents/skills/facebook-workspace/SKILL.md).
- **Hồ sơ công việc:** [skill SaleNote](.agents/skills/salenote-workspace/SKILL.md).
- **Catalog, kho và thu chi:** [skill Admin](.agents/skills/admin-workspace/SKILL.md).
- **Vận chuyển:** [skill SuperAI](.agents/skills/superai-workspace/SKILL.md).

## File làm việc và dữ liệu riêng

- `.work/<việc>/`: file tạm, Git bỏ qua; dọn sau khi kiểm chứng và lưu kết quả
  theo [quy ước agent](AGENTS.md). Dữ liệu nhập hàng đã chuyển lên production;
  tiếp tục qua Admin MCP, không dùng bản local cũ làm trạng thái hiện hành.
  File chưa thể dọn phải có lý do trong `.work/README.md`.
- Facebook: dữ liệu/bản nhớ hiện hành thuộc server, truy cập qua MCP theo skill
  Facebook. Thư mục Messenger/SQLite cũ đã xoá theo yêu cầu 06/11.
- Credentials và cache riêng giữ ngoài Git; không chép vào tài liệu hoặc log.

## Ảnh local — 25/11/2026

Theo quyết định của Dũng, các file ảnh chỉ giữ trên máy và được Git ignore.
Tài liệu, caption, prompt và metadata vẫn nằm trong repo; clone/pull không mang
theo ảnh. Chưa chuyển ảnh sang app hoặc kho file khác. Giữ nguyên thư mục ảnh
local hiện có; Git không phải bản sao lưu bộ ảnh này.
