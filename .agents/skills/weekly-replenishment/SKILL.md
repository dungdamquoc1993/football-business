---
name: weekly-replenishment
description: Lập kế hoạch nhập giày cho Yêu Bóng Đá Shop từ nhu cầu Messenger và tồn Admin; lưu cấu hình, kết quả rà và kế hoạch trên máy chủ qua Admin MCP, xuất Excel có ảnh. Không cần clone repo.
---

# Lượt nhập hàng hằng tuần

Dùng khi Dũng yêu cầu rà nhu cầu nhập, tính tồn mong muốn hoặc lập đơn đặt xưởng.
Dữ liệu thuộc máy chủ và được thao tác qua MCP. Đọc
[sổ ý định mua dùng chung với quảng cáo](../shop-operations/references/purchase-intent.md)
khi cần bổ sung nguồn Messenger; chỉ rà phần còn thiếu của kỳ được giao.
Lập kế hoạch và xuất Excel không tự gửi xưởng, tạo vận đơn, ghi kho hoặc chạy lịch.

## Mở đúng nguồn

Bắt đầu bằng `admin_replenishment_status(page_id)` cho Page được giao; Page chính Yêu Bóng Đá Shop là `693218564214489`. Lấy `workspace_fingerprint`, `settings.data`, cấu hình `version`, `review_revision`, coverage/checkpoint và các lượt gần nhất. Nếu thiếu công cụ hoặc `initialized=false`, báo máy chủ chưa được nâng cấp/nhập dữ liệu cho Page; không tự tạo cấu hình mặc định hoặc dùng file máy khác làm nguồn hiện hành.

Đọc sổ dữ liệu bằng `admin_replenishment_opportunities(filters={page_id,...})`, phân trang đến hết khi cần đủ cơ cấu. Đọc lượt cũ bằng `admin_replenishment_runs(page_id,run_id)`; stock trong đó chỉ là bản chụp dữ liệu. `migration_source_state` và `import_provenance` chỉ giải thích nguồn lịch sử, không yêu cầu mở đường dẫn trên máy trong đó. Không cần repo, `.work`, cầu nối Python hoặc script của lượt cũ để tiếp tục công việc. [Hợp đồng dữ liệu](references/data-contract.md) đi cùng bộ skill, không cần docs của ứng dụng.

Kết nối trực tiếp Streamable HTTP tới `/mcp/admin/` bằng API key cá nhân đã cấu hình; dùng MCP Facebook, SaleNote và SuperAI hiện có khi cần đối chiếu. Không đưa key vào file kế hoạch, prompt hoặc log. Bridge trong repo chỉ là lựa chọn máy khách, không phải điều kiện vận hành.

## Sáu công cụ nhập hàng

- `admin_replenishment_status`: cấu hình, phiên bản, summary các mốc tiến độ và lượt gần nhất. Phân trang mốc tiến độ; chọn đúng `checkpoint_key` để trả dấu nhận diện dữ liệu đầy đủ.
- `admin_replenishment_save_settings(request,workspace_fingerprint)`: lưu đầy đủ cấu hình và ngoại lệ Dũng chốt, `expected_version` hiện hành, lý do, UUID thao tác. Không dùng số mặc định trong skill để ghi đè cấu hình.
- `admin_replenishment_opportunities(filters)`: lọc Page, ID lượt mua, hộp, confirmed/clear_intent, phân trang. Exact ID trả audit; `include_voided=true` khi rà dòng đã loại.
- `admin_replenishment_record_review(request,workspace_fingerprint)`: ghi tối đa100 lượt mua/100 mốc tiến độ cùng transaction. Pin `settings_version`, `expected_review_revision` và `expected_version` từng dòng; ghi summary/lý do. Batch không có ý định mua mới vẫn ghi mốc tiến độ kèm kết quả đã rà, không tạo lượt mua giả.
- `admin_replenishment_runs(page_id,run_id?,offset?,limit?)`: danh sách hoặc chi tiết kế hoạch có basis, mục tiêu, input kho/cam kết, quyết định và phạm vi bao quát. Lượt cũ/import được giữ nguyên.
- `admin_replenishment_save_run(request,workspace_fingerprint)`: UUID run ổn định, `expected_version` (0 khi mới), `settings_version`, `review_revision`, label, state draft/completed, phạm vi bao quát, source_cutoff, target, order, decisions, notes. Server chụp ledger/config/checkpoint hiện hành. Đây là lưu phương án do agent tính, không tự tính mục tiêu hoặc gửi xưởng.

Mọi lệnh ghi giữ nguyên UUID/payload/fingerprint để thử lại khi mất phản hồi. Stale version/basis thì đọc lại và đối chiếu thay đổi, không đổi UUID để vượt lỗi. Thay cấu hình mới không sửa lịch sử; lượt completed hoặc nhập từ nguồn cũ không sửa, muốn tính lại tạo ID mới. Completed là chốt bản kế hoạch, không chứng minh đã rà hết nguồn, gửi xưởng, nhận hàng hoặc thanh toán. Luôn giữ phần phạm vi bao quát chưa đủ riêng.

## Dùng sổ ý định mua để tính cơ cấu

- Dùng dữ liệu đã lưu và [luồng rà ý định mua](../shop-operations/references/purchase-intent.md)
  để bổ sung phần mới, phần đã sửa hoặc phần lịch sử còn thiếu. Một lượt chỉ
  lập đơn nhập không cần cập nhật SaleNote hay dấu đã đọc Messenger.
- Dùng cùng cửa sổ cho mọi mẫu. Mặc định giữ phạm vi tích lũy từ 29/10 của
  lượt đầu và nêu mốc kết thúc; có thể trình thêm kỳ gần đây nếu hữu ích.
- Tính tỷ trọng mẫu/màu bằng trọng số của lựa chọn chia tổng trọng số trong cùng
  phạm vi. Giữ phần chưa rõ riêng. So cơ cấu gốc, cơ cấu đã phân bổ và lựa chọn
  cuối khi khác biệt đáng kể. Dòng lịch sử chưa có lý do chuyển vẫn cần bằng
  chứng để áp quy tắc phân bổ. Số giao/xuất không dùng thay nhu cầu hoặc doanh thu.

## Dựng mục tiêu rồi đơn đặt

Dùng cấu hình máy chủ và quyết định mới của Dũng, không lấy bản chụp dữ liệu kho cũ làm hiện hành. Config sở hữu số đôi/ngày, base_quantity, mẫu/màu duy trì, ngưỡng size và ngoại lệ. Lượt đầu từng tính126đôi từ9đôi/ngày × (7ngày giữa hai lượt đặt +4ngày chờ hàng +3ngày dự phòng); đây là lịch sử, không ghi đè mục tiêu đã sửa. Dũng ước tính4ngày gồm1ngày xưởng soạn và3ngày vận chuyển. Đây là giả định lập kế hoạch. Dùng số bán đo được và quyết định mới của Dũng khi điều chỉnh nhịp hoặc vốn.

Tiempo tính theo tỷ trọng mẫu/màu. Messi đen vàng/bạc giữ phần tỷ trọng của chính chúng, không renormalize toàn phần Messi cho2màu. Các màu Messi khác, Vapor/Bata: mỗi size đã có SKU trong catalog một đôi, loại44. Size38–43 cố định10/15/22/25/18/10%; làm tròn phần dư lớn nhất giữ đúng tổng màu. Chấp nhận0 ở SKU yếu, không ép phủ đều.

Ngoại lệ44: dùng ngưỡng từng mẫu/màu trong `size44_minimums` của planning cấu hình, cộng ngoài cơ cấu38–43. Các ngưỡng size khác và màu ngừng duy trì cũng lấy từ cấu hình và quyết định mới nhất của Dũng. Không mở44 cho màu thử. Khi thay dữ liệu, phân biệt mục tiêu thử với nhập bù: không tự đặt thêm nếu đã có.

Khi Dũng yêu cầu lập đơn, đọc tồn Admin mới và tính từng SKU `MAX(0,target-stock+customer_commitments_not_issued)`, theo công thức Dũng xác nhận23/11/2026. Phần cộng gồm hàng chuẩn bị giao và hàng đã hẹn/giữ cho khách còn chưa xuất kho. Đối chiếu SaleNote, hội thoại và liên kết phiếu xuất SuperAI; cùng nghĩa vụ chỉ cộng một lần, hàng đã trừ kho không cộng lại. Lượt tạo chưa rõ kết quả có đơn thay thế đã xuất không tạo thêm nghĩa vụ. Hàng đang về hoặc cam kết chưa đủ dữ liệu xác nhận phải ghi rõ phần chưa tính; không tự coi đã nhận. Nếu đã biết lô mua chưa nhận, đối chiếu tránh đặt trùng; hàng xưởng quên đóng chưa có bằng chứng vận chuyển phải được đối chiếu riêng với tổng số cần nhận.

Lọc dòng mẫu–màu theo ngưỡng hiện hành trong planning cấu hình. Khi Dũng yêu cầu bù đủ cơ cấu đang duy trì, giữ cả dòng tổng thiếu1đôi; chỉ bỏ dòng tổng đặt0. Không bỏ từng ô size1 trong dòng còn lại. Tồn mục tiêu và thiếu có dấu vẫn giữ ở bảng đối chiếu; tổng đơn phải bằng các dòng thực giữ.

## Kết quả và lưu lượt

Lưu từng đợt đã rà bằng `record_review`, không chờ tới khi xuất Excel mới ghi. Lưu scope/cutoff/freshness, phạm vi bao quát chưa đủ, nguồn và phiên bản tồn/cam kết, tỷ trọng, mục tiêu, input đặt và quyết định bằng `save_run`. Ledger là cumulative, không cộng tổng qua các run. Đọc một phần ghi rõ partial và chỉ tiến mốc tiến độ qua phần thực sự xử lý; mốc review mới không tự nâng con trỏ tiến độ cũ. Trước khi hoàn tất kế hoạch, kiểm tra trùng ID, evidence, tổng trọng số, công thức và tổng các dòng. Không chạy builder cũ hoặc sửa run cũ để thay lịch sử.

Khi xuất Excel dùng skill Spreadsheets và thư mục giao file của môi trường đang làm, không đòi outputs hoặc repo trên máy. File giao không có thông tin khách. Bảng xưởng: **ảnh →38,39,40,41,42,43,44→tổng**, chỉ dòng giữ lại, ảnh đúng màu nhúng trong file. Dùng URL/ID ảnh catalog đã duyệt; không dùng image_path của máy cũ, không suy ảnh đúng chỉ từ tên màu. Thiếu ảnh đúng báo phần thiếu. Bảng đối chiếu có SKU, mục tiêu, tồn, thiếu thô/công thức để kiểm tra. Giữ công thức, kiểm tra phépMAX khi dư kho, đối soát tổng, kết xuất ảnh để rà bố cục rồi giao. Không tính giá nếu chưa được yêu cầu; nếu cần giá mà chưa có chính sách được cung cấp thì lấy nguồn chính sách trước, không suy từ giá bản chụp dữ liệu.

Báo ngắn phạm vi đã đọc, tổng đơn và thay đổi đáng kể/unknown. Cập nhật quyết định vào hồ sơ kinh doanh; dữ liệu riêng chỉ giữ reference ngoài Git. Không coi việc gọi skill là quyền gửi đơn hoặc đặt lịch tự động.
