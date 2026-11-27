# Dữ liệu nhập hàng trên server

Tài liệu này đi cùng skill; thao tác qua Admin MCP, không cần repo hoặc `.work`
của máy cũ. Kiểm tra tool và `admin_replenishment_status(page_id)` trước. Thiếu
tool/chưa initialized thì báo đúng phần triển khai/import còn thiếu.

## Nơi sở hữu và phiên bản

- Settings: `status.settings.data`, `settings.version`, `settings.review_revision`.
  Config sở hữu mục tiêu và ngoại lệ; số ví dụ trong skill chỉ là lịch sử.
- Opportunities: phân trang `admin_replenishment_opportunities`. Mỗi dòng có
  `data`, `version`, `is_voided`; exact opportunity_id trả `history`.
- Checkpoints: `status.checkpoints` phân trang; chọn exact `checkpoint_key` để lấy
  fingerprint đầy đủ. Key `conversation:<id>` hoặc key nguồn/feed ổn định do lượt
  rà chọn. Không lấy checkpoint Facebook/SaleNote thay cho checkpoint nhập hàng.
- Runs: `admin_replenishment_runs` trả danh sách nhẹ, exact ID trả snapshot/audit.
  Snapshot giữ ledger/config và phiên bản cơ sở, target, order, decisions,
  cutoff, coverage. Không cộng kết quả cumulative của nhiều run.

Giữ Page ID chính xác, không gộp khách xuyên Page bằng tên/SĐT. MCP dùng API key
cá nhân đã cấu hình; không chép credentials vào kế hoạch/notes.

## Ghi một batch đã rà

`admin_replenishment_record_review(request,workspace_fingerprint)` nhận:

- `page_id`, `operation_id` UUID ổn định, `change_reason`, `summary`;
- `settings_version` và `expected_review_revision` vừa đọc;
- `opportunities`: mỗi phần tử `{expected_version, data, is_voided}`;
- `checkpoints`: mỗi phần tử `{source_key, expected_version, data}`.

Tối đa100 phần tử mỗi danh sách, payload tối đa1MiB. Tạo mới expected_version=0;
sửa dùng version hiện hành. Batch có thể chỉ có checkpoint nếu đã rà mà không có
intent mới, summary phải nói rõ. Không tiến checkpoint chỉ vì fetch thành công.
Kết quả và checkpoint lưu cùng transaction, lỗi bất kỳ thì không lưu cả batch.
Kết quả trả review_revision mới và phiên bản các dòng đã ghi.

Checkpoint data gồm `coverage` bắt buộc, `through_sequence` khi dùng change feed,
`last_sent_at` có timezone khi dùng mốc tin, `fingerprints` map message_id → hash;
giữ scope/page/cursor và giới hạn history_complete, late sync/edited messages khi
có. Server không cho lùi sequence/thời gian, giữ fingerprint cũ và merge phần mới.
Cursor không chứng minh toàn bộ Meta đã đồng bộ. Chỉ qua batch đã xử lý mới tiến
cursor; cần backfill riêng cho phần trước coverage của feed.

Retry mất phản hồi: dùng đúng operation_id/payload/fingerprint, nhận replay. Đổi
payload cùng UUID bị từ chối. Stale config/review/version: đọc lại, giữ sửa đổi của
người khác rồi lập batch có chủ ý mới; không retry mù hoặc nâng checkpoint cho qua.

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

Từ quyết định27/11/2026, đơn vị chung là intent mua hàng rõ ràng theo số đôi:
confirmed và clear_intent đủ bằng chứng đều đóng góp tổngq; settings lưu
clear_intent_weight=1 và intent_measurement.rule_version=clear-purchase-intent-v1.
Giữ intent có thật dù thiếu hàng/hủy; hậu mãi bảo hành/đổi size không tạo thêm
intent. Mua thêm thật chỉ cộng lượng mới; quantity=null không được coi1.
Chỉ dùng0,7q gốc/0,3q cuối khi có bằng chứng thiếu hàng và khách đồng ý mua thay
thế; hủy mà không có thay thế thì giữ nhu cầu gốc=q. Đây là phân bổ sản phẩm,
không phải chia credit giữa nguồn ads. Lý do chưa rõ giữ pending; không gọi cơ
cấu final là weighted đầy đủ. Nhiều lựa chọn trung gian không tạo thêm đôi.
Không coi ledger/run lịch sử đã được rà lại chỉ vì config đổi. SuperAI chỉ chứng
minh hàng đặt gửi, không tự chứng minh intent gốc, nhận hàng hoặc tiền.

Sổ intent phục vụ nhập hàng và đo ads, độc lập SaleNote. Quy tắc bằng chứng và
giới hạn source_ad_ids ở cấp hội thoại xem phần Nguồn ads trong SKILL.md. Chưa
mặc định các dòng lịch sử có hierarchy hoặc thời điểm referral; việc bổ sung
trường nguồn phải được kiểm chứng đọc/ghi trước khi báo đã triển khai.
Capability đã kiểm thử local27/11, chờ xem UI/deploy: `data.ad_links` là danh
sách đầy đủ `{ad_id,scope,observed_at,referral_at?,evidence}`. Bỏ/null giữ links,
`[]` xóa có chủ ý; ghi cùng transaction/version của intent. Đọc opportunities
trả links hiện hành và lọc được ad_id/account_id. Trường bổ sung:
first_intent_at, reference_unit_price_vnd, price_basis, intent_kind. Client cũ
không gửi các trường mới thì giữ giá/ngày/loại và links đã có. Chỉ áp dụng khi
schema server đang kết nối đã nâng cấp, không suy từ việc source local đã có.
Correction tiếp theo27/11: quan hệ intent–ad là nhiều–nhiều, mỗi cặp chỉ một
lần. Thống kê bản đầu là liên quan, chưa phân chia credit: q được tính cho mỗi
ad liên quan; tổng một nhóm lấy tập intent duy nhất trong nhóm và tính q một
lần. Không cộng các dòng liên quan chồng lấn thành tổng intent toàn shop.

## Lưu kế hoạch

`admin_replenishment_save_run` nhận UUID run, expected_version, settings_version,
review_revision, label, state draft/completed, coverage bắt buộc, source_cutoff,
target, order, decisions, notes; cùng page_id/operation_id/change_reason và fingerprint.
Agent tính cơ cấu theo config và evidence, backend lưu/chụp cơ sở hiện hành;
tool này không tự tính nhu cầu, lấy kho mới hoặc tạo giao dịch.

Trong order lưu dòng SKU với target, stock, pending, order, thời điểm/phiên bản
nguồn kho, tham chiếu nghĩa vụ chưa xuất và lý do ngoại lệ. Tính
MAX(0,target-stock+confirmed_unissued_customer_commitments); cùng nghĩa vụ chỉ
tính một lần, đã xuất không cộng lại, đang về đối chiếu tránh đặt trùng. Snapshot
kho cũ không là live. Target/order dùng catalog media URL/ID; server từ chối
image_path/local_path/asset_root trong kế hoạch mới.

Run completed và mọi run import là lịch sử không sửa. Muốn tính lại tạo UUID mới.
Completed là chốt một phương án, không phải xác nhận gửi xưởng/nhận hàng/thu tiền
hoặc đủ toàn bộ nguồn. Coverage thiếu vẫn phải nêu rõ.

## Dữ liệu chuyển từ Mac

Import giữ nguyên ledger hiện hành, checkpoint gốc, từng run và quyết định hỗ trợ.
Lượt17/11 và23/11 có coverage khác nhau; không nâng cursor17/11 thành23/11 chỉ vì
ledger/kế hoạch mới hơn. Thiếu bản config đầy đủ ở thời điểm run cũ thì
settings_version=NULL và snapshot.settings=null, không giả tạo bằng config mới.
`import_provenance` và `migration_source_state` giải thích lịch sử; đường dẫn trong
đó không là phụ thuộc phải truy cập trên máy mới.

Tin gốc đầy đủ thuộc Facebook; không chép archive, script thử, ảnh, log hoặc
credentials vào bảng nhập hàng. Excel xuất tại máy đang làm là bản giao có thể
tạo lại từ dữ liệu server; chưa xây thêm kho file trong đợt này.
