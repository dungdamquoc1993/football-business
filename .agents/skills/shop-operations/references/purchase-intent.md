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
biết khách từng vào hội thoại từ ads, `purchase_episode` khi có bằng chứng
quảng cáo thuộc đúng lượt mua đang ghi. Nguồn `conversation` vẫn dùng cho
báo cáo intent.
Ghi `observed_at` là lúc thấy, `referral_at` chỉ khi có bằng chứng thời
điểm nguồn. Mỗi cặp ý định mua–quảng cáo ghi một lần. Giữ toàn bộ liên kết
có căn cứ khi cập nhật; bỏ trường hoặc `null` để giữ liên kết, `[]` chỉ
dùng khi chủ ý xóa. Ghi cùng ý định mua và đúng phiên bản. Nếu công cụ chưa
hỗ trợ, báo phần chưa lưu được và giữ việc đối soát để tiếp tục.

### Gắn đơn SaleNote đã đối soát

Ghi `data.sale_case_id` qua `admin_replenishment_record_review` khi đã xác
minh hồ sơ cùng lượt mua. Hồ sơ cần có `confirmed_at` và tham chiếu Messenger
đúng Page, đúng ID hội thoại. Cùng hội thoại, tên, mẫu hoặc một ca hậu mãi
riêng chưa đủ. Nếu lượt mua đã có `shipment_operation_id` liên kết đúng
fulfillment SaleNote, báo cáo có thể tự đối soát qua liên kết đó. Gắn đơn và
gắn ads là hai việc cần chứng cứ riêng. Khi chưa biết ads của lượt mua, giữ
nguồn ở `conversation` dù đã xác minh được đơn.

Bỏ trường `sale_case_id` để giữ liên kết đã lưu. Chỉ gửi chuỗi rỗng khi chủ ý
gỡ liên kết và tắt đối soát tự động cho lượt đó. Cập nhật đúng ID intent
hiện có, dùng phiên bản hiện hành và giữ các chứng cứ vẫn còn hiệu lực.

## Cập nhật và đọc báo cáo ads

1. Kiểm cùng Page, tài khoản, phạm vi ngày, độ mới và phần thiếu của sổ
   ý định mua. Nếu được giao cập nhật, rà phần Messenger còn thiếu bằng
   mốc của sổ này. Nếu chỉ được giao đọc báo cáo, nêu phạm vi sẵn có.
2. Gọi `admin_intent_report` với `filters.view="report"`, đúng `page_id`,
   `date_from` và `date_to` theo giờ Việt Nam, tính cả hai ngày. Chọn
   `group_by` theo cấp cần xem: `account` → `campaign` → `adset` → `ad`.
   Khi đi xuống cấp con, lọc theo ID cấp cha. Dùng `creative` để xem bài
   hoặc nội dung (khóa ưu tiên `content_key`, `post_id`, rồi `creative_id`)
   và `model` để xem mẫu giày. Dùng `day` với cùng bộ lọc để xem các ngày
   có dữ liệu. Khi hỏi số của một đối tượng cụ thể, lọc theo ID,
   `creative_key` hoặc `model` tương ứng và đọc `totals`. Khi so nhiều đối
   tượng cùng cấp, đọc dòng trực tiếp của từng đối tượng. So hai kỳ bằng
   hai báo cáo và đọc `totals` từng kỳ. Dùng tổng trực tiếp của phạm vi
   được hỏi để tránh cộng trùng giữa các dòng.
3. Khi Dũng hỏi “chạy bao tiền, ra bao nhiêu đơn”, dùng `cost_vnd` và
   `confirmed_order_count` ở đúng phạm vi. Chi phí gồm thuế/phí đã phân bổ
   theo dữ liệu ghi nhận. Nếu chi phí là `null`, nói chưa có chi phí ghi nhận
   ở phạm vi đó. Nếu số đơn là `null`, nói **chưa đối soát**. Số đơn dương
   chỉ đếm hồ sơ SaleNote duy nhất đã khớp lượt mua. Khi lọc theo nguồn ads,
   đơn cần bằng chứng `purchase_episode`. `purchase_count` đếm lượt intent,
   `intent_quantity` đếm số đôi, và `cost_per_confirmed_order_vnd` là chi phí
   trên đơn đã đối soát ở dòng có trường này. Đơn theo ngày chốt, intent
   theo ngày đầu có ý định mua, chi phí theo ngày phân phối. Giá trị intent
   là quy đổi theo giá tham chiếu. Chi phí quảng cáo nhiều mẫu giữ chung
   theo nhãn ads, không tự chia cho từng mẫu.
4. Dùng `view="catalog"` và `view="costs"` để kiểm ánh xạ và chi phí đã lưu.
   Chỉ tra Meta khi cần xác minh ánh xạ hoặc đọc chi phí kỳ được giao. Ghi
   danh mục hoặc chi phí theo [skill Admin](../../admin-workspace/SKILL.md#ý-định-mua-và-quảng-cáo)
   nếu được giao. Tách số thực tế với ước tính và tránh cộng lại thuế/phí.

SaleNote giữ hồ sơ công việc theo tiêu chí riêng. Không thêm hồ sơ hoặc
ghi lại ghi chú nguồn cũ chỉ để làm số liệu ads. Chi phí báo cáo thuộc
dữ liệu ads; phiếu thu chi chỉ ghi theo tiền thực. Luồng này dùng quyền
được giao để rà, đo và lưu số liệu.
