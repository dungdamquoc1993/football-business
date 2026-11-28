# Dữ liệu nhập hàng trên máy chủ

Tài liệu này đi cùng skill; thao tác qua Admin MCP, không cần repo hoặc `.work`
của máy cũ. Kiểm tra công cụ và `admin_replenishment_status(page_id)` trước. Thiếu
tool/chưa initialized thì báo đúng phần triển khai/import còn thiếu.

## Nơi sở hữu và phiên bản

- Settings: `status.settings.data`, `settings.version`, `settings.review_revision`.
  Config sở hữu mục tiêu và ngoại lệ; số ví dụ trong skill chỉ là lịch sử.
- Opportunities: phân trang `admin_replenishment_opportunities`. Mỗi dòng có
  `data`, `version`, `is_voided`; exact opportunity_id trả `history`.
- Checkpoints: `status.checkpoints` phân trang; chọn exact `checkpoint_key` để lấy
  dấu nhận diện dữ liệu đầy đủ. Key đang dùng cho luồng thay đổi là `messenger-changes:<page_id>`. Key
  `conversation:<id>` hoặc `messenger-sent-window:<page_id>` giữ phạm vi lịch sử riêng. Không lấy mốc tiến độ Facebook/SaleNote thay cho mốc tiến độ nhập hàng.
- Runs: `admin_replenishment_runs` trả danh sách nhẹ, exact ID trả snapshot/audit.
  Snapshot giữ ledger/config và phiên bản cơ sở, target, order, decisions,
  mốc kết thúc, phạm vi bao quát. Không cộng kết quả cumulative của nhiều run.

Giữ Page ID chính xác, không gộp khách xuyên Page bằng tên/SĐT. MCP dùng API key
cá nhân đã cấu hình; không chép credentials vào kế hoạch/notes.

## Ghi một đợt đã rà

`admin_replenishment_record_review(request,workspace_fingerprint)` nhận:

- `page_id`, `operation_id` UUID ổn định, `change_reason`, `summary`;
- `settings_version` và `expected_review_revision` vừa đọc;
- `opportunities`: mỗi phần tử `{expected_version, data, is_voided}`;
- `checkpoints`: mỗi phần tử `{source_key, expected_version, data}`.

Tối đa100 phần tử mỗi danh sách, payload tối đa1MiB. Tạo mới expected_version=0;
sửa dùng version hiện hành. Batch có thể chỉ có mốc tiến độ nếu đã rà mà không có
ý định mua mới, summary phải nói rõ. Không tiến mốc tiến độ chỉ vì fetch thành công.
Kết quả và mốc tiến độ lưu cùng transaction, lỗi bất kỳ thì không lưu cả đợt.
Kết quả trả review_revision mới và phiên bản các dòng đã ghi.

Checkpoint data gồm `coverage` bắt buộc, `through_sequence` khi dùng change feed,
`last_sent_at` có timezone khi dùng mốc tin, `fingerprints` map message_id → hash;
giữ scope/page/cursor và giới hạn history_complete, late sync/edited messages khi
có. Server không cho lùi sequence/thời gian, giữ dấu nhận diện dữ liệu cũ và merge phần mới.
Cursor không chứng minh toàn bộ Meta đã đồng bộ. Chỉ qua đợt đã xử lý mới tiến
con trỏ tiến độ; cần bổ sung lịch sử riêng cho phần trước phạm vi bao quát của feed.

Retry mất phản hồi: dùng đúng operation_id/payload/fingerprint, nhận replay. Đổi
payload cùng UUID bị từ chối. Stale config/review/version: đọc lại, giữ sửa đổi của
người khác rồi lập đợt có chủ ý mới; không thử lại mù hoặc nâng mốc tiến độ cho qua.

## Một lượt mua

`data` có opportunity_id ổn định, conversation_id, quantity (integer dương hoặc
null), level confirmed/clear_intent, original_model/color, final_model/color,
outcome, reason, anchor_at, evidence[{message_id,quote}], uncertainties.

Bổ sung khi có bằng chứng: first_intent_at, last_evidence_at, fulfillment_model/color,
requested_change_color/status, transition_reason stockout/preference/unknown/none,
reason_evidence, weighting_status classified/needs_review/final_only,
weighting_rule_version và demand_allocations. `final_only` chỉ biết lựa chọn cuối,
không chứng minh đã tính tỷ trọng stockout. Sửa lựa chọn/hậu mãi dùng lại cùng ID;
mua thêm thật mới có ID mới. Loại dòng sai bằng is_voided, giữ audit, không xóa.

Quy tắc nhận ý định mua, phân bổ sản phẩm và đo nguồn ads nằm ở
[sổ ý định mua](../../shop-operations/references/purchase-intent.md).
Cấu hình lưu `clear_intent_weight=1` và
`intent_measurement.rule_version=clear-purchase-intent-v1`.

`data.ad_links` nhận danh sách đầy đủ
`{ad_id,scope,observed_at,referral_at?,evidence}`; bỏ trường hoặc `null` giữ
liên kết, `[]` xóa có chủ ý. Đọc opportunities trả liên kết hiện hành và lọc
được `ad_id`/`account_id`. Trường bổ sung gồm `first_intent_at`,
`reference_unit_price_vnd`, `price_basis` và `intent_kind`. Client cũ không
gửi các trường mới thì giữ giá, ngày, loại và liên kết đã có. Dùng các trường
theo schema của máy chủ đang kết nối.

## Lưu kế hoạch

`admin_replenishment_save_run` nhận UUID run, expected_version, settings_version,
review_revision, label, state draft/completed, phạm vi bao quát bắt buộc, source_cutoff,
target, order, decisions, notes; cùng page_id/operation_id/change_reason và dấu nhận diện dữ liệu.
Agent tính cơ cấu theo cấu hình và evidence, backend lưu/chụp cơ sở hiện hành;
công cụ này không tự tính nhu cầu, lấy kho mới hoặc tạo giao dịch.

Trong order lưu dòng SKU với target, stock, đang chờ, order, thời điểm/phiên bản
nguồn kho, tham chiếu nghĩa vụ chưa xuất và lý do ngoại lệ. Tính
MAX(0,target-stock+confirmed_unissued_customer_commitments); cùng nghĩa vụ chỉ
tính một lần, đã xuất không cộng lại, đang về đối chiếu tránh đặt trùng. Snapshot
kho cũ không là hiện hành. Target/order dùng catalog media URL/ID; máy chủ từ chối
image_path/local_path/asset_root trong kế hoạch mới.

Run completed và mọi run import là lịch sử không sửa. Muốn tính lại tạo UUID mới.
Completed là chốt một phương án, không phải xác nhận gửi xưởng/nhận hàng/thu tiền
hoặc đủ toàn bộ nguồn. Coverage thiếu vẫn phải nêu rõ.

## Dữ liệu chuyển từ Mac

Import giữ nguyên sổ dữ liệu hiện hành, mốc tiến độ gốc, từng run và quyết định hỗ trợ.
Lượt17/11 và23/11 có phạm vi bao quát khác nhau; không nâng cursor17/11 thành23/11 chỉ vì
ledger/kế hoạch mới hơn. Thiếu bản cấu hình đầy đủ ở thời điểm run cũ thì
settings_version=NULL và bản chụp dữ liệu.settings=null, không giả tạo bằng cấu hình mới.
`import_provenance` và `migration_source_state` giải thích lịch sử; đường dẫn trong
đó không là phụ thuộc phải truy cập trên máy mới.

Tin gốc đầy đủ thuộc Facebook; không chép archive, script thử, ảnh, log hoặc
credentials vào bảng nhập hàng. Excel xuất tại máy đang làm là bản giao có thể
tạo lại từ dữ liệu máy chủ; chưa xây thêm kho file trong đợt này.
