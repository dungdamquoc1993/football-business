# Football Business — Yêu Bóng Đá Shop

**Trước khi định giá hàng mới hoặc đổi giá:** đọc [chính sách giá](../yeubongdashop/docs/operations/pricing.md) — mặc định chi phí phục vụ theo C1 ×1,8; giữ ngoại lệ và giá chốt riêng của Dũng.

## Hướng refactor và ưu tiên — Dũng chốt 25/11/2026

- Đã tách vị trí local ngày 25/11: repo này giữ tài liệu, tài sản kinh doanh,
  script và cả năm skills; repo code ở `../yeubongdashop/`, với
  code ngay tại gốc repo. Chưa dọn nội dung.
  Remote business: `dungdamquoc1993/football-business`.
- Ưu tiên đưa dữ liệu cần để tiếp tục nhập hàng từ `.work/replenishment/` lên
  server do `football-shop` quản lý, truy cập qua MCP; rút gọn tài liệu sau.
- Tiêu chí: agent có bộ skill và kết nối MCP được cấp quyền vẫn tiếp tục công
  việc vận hành trong phạm vi này từ máy khác, không cần clone hai repo hoặc
  lấy file `.work` từ máy Mac. Skill cần đủ hướng dẫn, không bắt buộc đọc docs
  trong repo hoặc chạy script local của repo để hoàn thành việc đó.
- Không xây thêm kho file hoặc chuyển bộ ảnh vào app trong đợt này. Giữ toàn bộ
  tài liệu Markdown hiện có; việc gom/rút gọn sẽ làm riêng. Chưa xóa nguồn local
  trước khi kiểm tra dữ liệu đã chuyển và khả năng tiếp tục làm từ máy khác.

## Repo và làm việc nhiều máy — 25/11/2026

Hai repo nằm cạnh nhau: `football-business/` giữ vận hành kinh doanh;
`yeubongdashop/` giữ code và toàn bộ lịch sử Git cũ, remote
`dungdamquoc1993/yeubongdashop`. Repo business khởi tạo nhánh `main` riêng,
remote `dungdamquoc1993/football-business`. Làm trực tiếp trên `main`; không rewrite lịch sử.

Cả năm skill chuẩn nằm tại [.agents/skills](.agents/skills), không sao chép sang
repo code. Clone không mang theo MCP bearer, credentials, database hoặc `.work/`.
Dữ liệu hiện hành tiếp tục thuộc backend. File riêng được giữ tại phía sở hữu cũ.

Ứng dụng ở thẳng gốc `../yeubongdashop/`; chạy Compose/deploy từ đó.
Việc tách local này chưa push hoặc deploy server; xem runbook trước khi nâng server.

## Mở theo việc

- **Ba tài liệu nền tảng:** [Chính sách bán hàng](chinh_sach_ban_hang.md), [Quy trình làm việc hằng ngày và phát sinh](quy_trinh_lam_viec.md), [Custom Instructions Meta AI](meta_ai_prompt.md). Hiện Dũng vận hành toàn bộ; quy trình chia theo đầu việc để có thể bàn giao về sau.
- **Nhập hàng hằng tuần:** [skill lập kế hoạch và xuất Excel đặt xưởng](.agents/skills/weekly-replenishment/SKILL.md),
  dùng dữ liệu server qua Admin MCP; đã import và kiểm tra luồng đọc/ghi lập kế hoạch production
  ngày25/11/2026, xem
  [runbook kỹ thuật và bàn giao](../yeubongdashop/docs/operations/replenishment.md).
- **Ảnh sản phẩm:** [Photo workshop](photo-workshop/README.md) — bỏ ảnh vào, xem duyệt, lấy bộ đã duyệt; hồ sơ nguồn/prompt ở hậu trường.
- **Giá và nguồn hàng:** [supplier quotes](supplier-quotes/README.md) — báo giá và ghi chú xưởng. Sản phẩm và tồn hiện hành tra Admin MCP.
- **Bài Facebook:** [marketing/bai-dang](marketing/bai-dang/README.md) — các đợt bài đăng, ảnh và caption.
- **Quảng cáo và nhận diện:** [quảng cáo](marketing/quang-cao/README.md), [logo và ảnh bìa](marketing/nhan-dien/README.md).
- **Messenger và Facebook:** [workspace API/admin/MCP và worker](../yeubongdashop/docs/operations/facebook.md). Ứng dụng Messenger/SQLite cũ đã bỏ; dữ liệu mới lấy trực tiếp từ Meta.
- **Website:** [football-shop](../yeubongdashop/README.md) — mã nguồn, database và hướng dẫn vận hành riêng.

## File làm việc và dữ liệu riêng

- `.work/`: nguồn riêng của các lượt nhập cũ và bản làm việc local, có dữ liệu khách,
  Git bỏ qua. Nguồn nhập hàng đã chuyển lên production và kiểm tra ngày25/11;
  giữ bản cũ để đối chiếu, tiếp tục công việc qua Admin MCP, không suy file trên
  máy này là trạng thái server.
- Facebook: dữ liệu/bản nhớ hiện hành ở PostgreSQL của `football-shop`, xem [quy trình Facebook](../yeubongdashop/docs/operations/facebook.md). Thư mục Messenger/SQLite cũ đã xóa theo yêu cầu 06/11; không có nguồn phục hồi tại đó.
- `.env` và `.private/meta/`: credentials/cache Meta, giữ riêng; không chép vào tài liệu hoặc log. Website có cấu hình riêng trong thư mục của nó.

Football Business sở hữu chi tiết thương mại/vận hành. [Living Map](../../living-map/domains/venture/cases/nguon-cung-giay/README.md) chỉ giữ vai trò, ưu tiên và cam kết nguồn lực trong đời sống.

## Ảnh local — 25/11/2026

Theo quyết định của Dũng, các file ảnh chỉ giữ trên máy và được Git ignore.
Tài liệu, caption, prompt và metadata vẫn nằm trong repo; clone/pull không mang
theo ảnh. Chưa chuyển ảnh sang app hoặc kho file khác. Giữ nguyên thư mục ảnh
local hiện có; Git không phải bản sao lưu bộ ảnh này.
