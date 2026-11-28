# Ý định mua và đo quảng cáo

## Đọc và ghi sổ

Admin là nguồn sổ chung cho nhập hàng và đo quảng cáo. Dùng
`admin_replenishment_status` để lấy cấu hình, phiên bản và mốc theo Page;
`admin_replenishment_opportunities` để tìm lượt đã có. Khi phải đọc Messenger,
dùng [luồng quét](messenger-scan.md) cho phần thay đổi và
[cách tìm theo ngày](../../facebook-workspace/SKILL.md#chọn-truy-vấn-nguồn-có-giới-hạn)
cho khoảng lịch sử còn thiếu. Xem
[hợp đồng dữ liệu](../../weekly-replenishment/references/data-contract.md#ghi-một-đợt-đã-rà)
để ghi ý định mua, nguồn và mốc bằng `admin_replenishment_record_review`.

Xét theo thời điểm tin gốc, từ `settings.data.intent_scope.since` đến trước
mốc kết thúc của kỳ. Mốc ban đầu là 00:00 29/10/2026, giờ Việt Nam. Đọc phần
mới hoặc đã sửa và dùng ngữ cảnh để xác định lượt mua. Bộ nhớ, lời bot tự
tuyên bố chốt và tin ngữ cảnh ngoài kỳ không đủ làm bằng chứng mua trong kỳ.
Các hội thoại test của shop nằm ngoài số đo. Xem ảnh cần thiết để phân biệt
mẫu/màu. Mã SKU vận đơn liên quan có thể giúp xác định hàng đặt gửi, còn
lựa chọn ban đầu cần lời khách hoặc bằng chứng cùng lượt.

Đơn vị chung theo quyết định 27/11/2026 là **số đôi có ý định mua rõ**.
`confirmed` và `clear_intent` đủ bằng chứng cùng đóng góp q khi biết q đôi
(`clear_intent_weight=1`). Hỏi giá, xin ảnh hoặc hỏi còn hàng đơn thuần
chưa đủ. Thiếu SĐT, thiếu hàng hoặc hủy sau đó không loại nhu cầu có thật.
Khi xác định khách đã chốt, dùng cùng cách đọc lời khách trong
[điều kiện mở hồ sơ SaleNote](../../salenote-workspace/SKILL.md#điều-kiện-mở-hồ-sơ).
Dùng `confirmed` cho lời chốt rõ, kể cả chốt có điều kiện, và lưu điều kiện
cùng chứng cứ. Nếu lượt này đã có dòng `clear_intent`, cập nhật đúng dòng đó.
Số đôi chưa rõ giữ `null`. Không dùng size làm chiều thống kê của sổ này.
Giữ mức độ, lựa chọn gốc/cuối, hàng thực đặt gửi, lý do chuyển và kết quả
riêng. Ghi cùng ID khi nhắc đơn, đổi lựa chọn hoặc cập nhật hậu mãi. Đổi size,
bảo hành và gửi lại không tạo ý định mua mới. Mua thêm độc lập chỉ cộng
đúng lượng mới. Dùng `is_voided` cho dòng ghi sai và giữ dấu vết.

Phân bổ nhu cầu cho nhập hàng:

- Khi A là lựa chọn gốc, A thiếu hàng và khách đồng ý mua B, ghi 0,7q cho A
  và 0,3q cho B, kể cả khi chỉ chuyển màu. Hàng cuối vẫn là B=q. Thiếu hàng
  rồi hủy mà chưa đồng ý thay thế thì giữ A=q.
- Chuyển vì thích B hơn thì tính B. Lý do chưa rõ giữ `unknown` và trình
  riêng phần chưa phân loại hoặc chỉ biết lựa chọn cuối. Với nhiều lần thay
  do thiếu hàng, giữ bằng chứng và đánh dấu cần rà thay vì chia lặp.

Quy tắc 7/3 áp cho cơ cấu sản phẩm. Phép đo quảng cáo dùng quan hệ liên
quan dưới đây. Khi bổ sung dữ liệu hiện hành, chỉ cập nhật dòng có
bằng chứng mới; giữ lịch sử và các phương án nhập đã chốt.

## Gắn nguồn quảng cáo

Đọc `source_ad_ids` và `ad_source_scope` cấp hội thoại từ `facebook_read`
khi schema có trả. Nếu thiếu, thử `facebook_browse(view="detail")` cho
hội thoại liên quan. Facebook MCP đọc được nguồn đã có mà không cần token
ads. Giữ bằng chứng theo đúng phạm vi đang biết. Danh sách ad ID của hội
thoại chưa chứng minh nguồn hoặc thời điểm nhấp của từng lượt mua. Nguồn
thiếu/hỗn hợp ghi theo dữ kiện; tránh suy từ mẫu giày, tên hoặc bài dùng chung.
Nguồn mới xuất hiện không tự thay liên kết của một lượt mua cũ.

Dùng `data.ad_links` theo schema hiện hành. `scope=conversation` khi chỉ
biết nguồn hội thoại, `purchase_episode` khi có bằng chứng cho lượt mua.
Ghi `observed_at` là lúc thấy, `referral_at` chỉ khi có bằng chứng thời
điểm nguồn. Mỗi cặp ý định mua–quảng cáo ghi một lần. Giữ toàn bộ liên kết
có căn cứ khi cập nhật; bỏ trường hoặc `null` để giữ liên kết, `[]` chỉ
dùng khi chủ ý xóa. Ghi cùng ý định mua và đúng phiên bản. Nếu công cụ chưa
hỗ trợ, báo phần chưa lưu được và giữ việc đối soát để tiếp tục.

## Cập nhật và đọc báo cáo ads

1. Kiểm cùng Page, tài khoản, phạm vi ngày, độ mới và phần thiếu của sổ
   ý định mua. Nếu được giao cập nhật, rà phần Messenger còn thiếu bằng
   mốc của sổ này. Nếu chỉ được giao đọc báo cáo, nêu phạm vi sẵn có.
2. Dùng `admin_intent_report` để tìm danh mục và chi phí đã lưu. Chỉ tra
   Meta khi cần xác minh ánh xạ quảng cáo → ad set → chiến dịch → tài khoản
   hoặc đọc chi tiêu/thuế/phí kỳ được giao. Tận dụng ánh xạ đã kiểm chứng.
   Ghi danh mục/chi phí qua [Admin](../../admin-workspace/SKILL.md#ý-định-mua-và-quảng-cáo)
   nếu được giao, giữ mốc và nguồn. Dữ liệu thiếu giữ chưa rõ, tách số thực
   tế với ước tính và tránh cộng lại thuế/phí.
3. Báo kết quả liên quan. Một ý định mua có thể đóng góp đủ q cho mỗi ad
   liên quan. Khi nhóm theo ad set, chiến dịch, tài khoản hoặc nội dung,
   tính trên tập ý định mua duy nhất trong nhóm. Dùng `totals` của báo cáo
   cho tổng chung. Giá trị q × giá tham chiếu là số quy đổi; giữ cơ sở giá
   và thời điểm khi dùng. Báo chi phí và phần liên quan trên phạm vi dữ liệu
   đã biết, tránh coi toàn bộ chi tiêu của một ad là chi phí riêng của từng
   mẫu giày.

SaleNote giữ hồ sơ công việc theo tiêu chí riêng. Không thêm hồ sơ hoặc
ghi lại ghi chú nguồn cũ chỉ để làm số liệu ads. Chi phí báo cáo thuộc
dữ liệu ads; phiếu thu chi chỉ ghi theo tiền thực. Luồng này dùng quyền
được giao để rà, đo và lưu số liệu.
