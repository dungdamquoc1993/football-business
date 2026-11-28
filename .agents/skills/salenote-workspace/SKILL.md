---
name: salenote-workspace
description: Đọc và ghi hồ sơ công việc chung của Yêu Bóng Đá Shop, tiến độ, mốc tiến độ thu thập do người vận hành báo và liên kết vận đơn hiện có.
---

Dùng SaleNote MCP riêng. Máy khách mới kết nối Streamable HTTP tới `/mcp/salenote/` trên máy chủ shop bằng API key cá nhân. Lấy cấu hình truy cập còn thiếu từ người vận hành. Không cần mã nguồn ứng dụng hoặc cầu nối Python trên máy. Kiểm tra công cụ thực tế và `salenote_status`, có mã triển khai chưa chứng minh máy chủ đã cập nhật. SaleNote không tự lấy nội dung Messenger hoặc website. Yêu cầu lịch sử/thủ công có thể ghi mà không cần con trỏ tiến độ nguồn, mốc ngày hay vận đơn. Ghi sổ không tự gửi khách, tạo vận đơn, ghi kho hoặc thu chi.

SaleNote là sổ công việc chung. Mỗi lượt mua/yêu cầu riêng có một hồ sơ, trao đổi lặp về cùng lượt mua cập nhật hồ sơ đó. Hậu mãi liên quan có thể mở lại hồ sơ trong chu kỳ xử lý mới. Tìm tham chiếu nguồn và thông tin liên hệ để xác định hồ sơ ứng viên, không định danh khách. Không gộp hồ sơ chỉ vì trùng tên/SĐT hoặc tạo một hồ sơ cho cả inbox/một người.

Đọc hồ sơ đang mở/liên quan và tiến độ con người cập nhật mới nhất trước. Thông tin từ điện thoại, Zalo hoặc thực tế đều hợp lệ dù không có Messenger. Không lấy tin cũ ghi đè điều chỉnh mới của con người. Mở lại hồ sơ không tự cấp quyền gửi thêm hàng. Chỉ tiếp tục việc được giao, không tự nhận mọi hồ sơ đang mở.

## Thu thập Messenger

Dùng [luồng quét chung](../shop-operations/references/messenger-scan.md) để chọn
phạm vi, lấy mốc từng sổ và đọc chứng cứ Messenger một lần. Khi kết luận thiếu
liên hệ, kiểm lịch sử hội thoại và hồ sơ khách trong Page. Giữ điều chỉnh mới
nhất của Dũng, kể cả từ điện thoại hoặc Zalo.

### Điều kiện mở hồ sơ

Bắt buộc có SĐT đã được xác nhận từ hội thoại, hồ sơ khách hoặc điều chỉnh của
Dũng. Khi có SĐT, mở hoặc cập nhật hồ sơ ngay trong lượt rà nếu khách đã chốt
mua hoặc shop đã nhận việc cụ thể như hẹn báo khi đúng size về. Nếu vẫn thiếu
SĐT sau khi kiểm lịch sử và hồ sơ khách, giữ việc trong bộ nhớ Messenger.

Đọc lời khách theo mạch của cùng lượt mua. Khách có thể chốt bằng lời nhờ
gửi đúng đôi đã chọn, câu đồng ý ngắn hoặc sticker/emoji như 👍 trả lời câu
hỏi xác nhận một đơn cụ thể. Đọc câu hỏi ngay trước đó và lời khách sau đó
để xác định dấu hiệu đồng ý đang trả lời việc đặt hàng. Nếu tin trống nhưng
có tệp đính kèm ở đúng vị trí đó, mở tệp để kiểm tra trước khi phân loại.

Ví dụ khách đã chọn mẫu và size, gửi SĐT và địa chỉ, dặn chỉ nhận nếu đế có
độ đàn hồi, rồi gửi 👍 khi shop trả lời điều kiện và hỏi xác nhận đơn. Ghi
đơn vào SaleNote, lưu nguyên điều kiện của khách và giao đầu việc kiểm đế
trước khi gửi. Áp dụng tương tự khi đơn đã chốt còn chờ hàng hoặc còn thiếu
chi tiết giao. Ghi đúng việc đang chờ theo tiến độ thực tế. Việc tạo vận đơn
theo quyền Dũng giao và kiểm tra của đợt gửi.

Khi khách mới để lại liên hệ, chỉ hỏi hàng hoặc đang cân nhắc, kiểm xem có
lời chốt hay một việc shop đã nhận trong các tin liền kề. Nếu chưa có, giữ
trong Messenger và ghi điểm còn mơ hồ khi cần theo dõi. Thẻ chuyển người
thật và lời AI báo đã nhận đơn là tín hiệu để mở hội thoại rà lại. Kết luận
khách đã chốt dựa vào lời khách hoặc xác nhận của Dũng. Đối chiếu liên hệ
trong hội thoại cũ cho đơn đã có hoặc ca hậu mãi.

Dùng `salenote_record_collection` một lần cho mỗi trang sự kiện có giới hạn đã rà hết, với operation UUID ổn định, phiên bản thu thập dự kiến, `from_cursor` từ nguồn và `to_cursor` bằng `next_cursor` nguồn trả về, tóm tắt ngắn, quyết định cho mọi sự kiện (`change_sequence` lấy từ `sequence` nguồn, `source_id`, `object_id`, `fingerprint`, `disposition`, `case_ids`, `note`) và toàn bộ ảnh chụp hồ sơ cần thiết trong changes. Tin chỉ làm ngữ cảnh không là quyết định. Không hành động vẫn cần ghi quyết định. Chỉ mở hồ sơ theo điều kiện tiếp nhận phía trên. Ghi rõ tồn kho, địa chỉ hoặc cam kết khách chưa giải quyết. Người vận hành đã xác thực chịu trách nhiệm báo bằng chứng, sổ không tự kiểm chứng Facebook/ngữ nghĩa con trỏ tiến độ. Không tiến qua sự kiện chưa rà. Giảm số sự kiện mỗi trang khi cần.

Cập nhật hồ sơ, biên nhận thu thập và mốc tiến độ được lưu nguyên tử. Mất phản hồi thì thử lại đúng UUID/payload. Status có UUID/tóm tắt/cursor thao tác cuối. Xung đột phiên bản thì đọc lại status và hồ sơ bị ảnh hưởng. Nếu người khác đã xử lý trang thì dùng tiến độ đó. Nếu con người đã sửa hồ sơ, giữ điều chỉnh và thử lại phần thu thập còn chờ với phiên bản hiện hành. Tin/sửa tin về sau vẫn là sự kiện mới. Tham chiếu nguồn giúp tìm hồ sơ ứng viên, không định danh khách hoặc tự tạo lượt mua mới. Dấu đã đọc Facebook không thay biên nhận thu thập, hoàn tất thu thập không đánh dấu Facebook đã đọc.

Ý định mua và nguồn ads thuộc sổ Admin. Giữ ghi chú nguồn cũ trong SaleNote
làm lịch sử. Việc thủ công/tồn đọng cũ Dũng giao dùng `salenote_save` hoặc
`salenote_progress`, không tiến con trỏ thu thập Messenger.

## Ghi hồ sơ và tiến độ

**Phân công SaleNote — cập nhật 20/11/2026:** Dũng phụ trách hồ sơ và đầu việc, kể cả khi cần gọi khách vì vận đơn bị hoãn. Giữ lịch sử phân công và kết quả đã ghi. Chỉ đổi người phụ trách trên hồ sơ hiện có khi xử lý đầu việc liên quan; không mở lại hồ sơ đã đóng chỉ để đổi phân công.

Dùng `salenote_save` với `expected_revision` mới nhất và đầy đủ trường. Yêu cầu độc lập mới dùng revision 0. Giữ việc, nguồn, hàng và tiến độ người khác. Bổ sung quan sát độc lập bằng `salenote_progress`. Cả hai có biên nhận thao tác bền vững. Hồ sơ mở cần hành động tiếp theo cụ thể, hồ sơ đóng cần kết quả cụ thể. Mở lại tự bắt đầu chu kỳ mới. Admin và agent có quyền ghi sổ tương đương. Danh tính người ghi lấy từ xác thực.

**Trạng thái SaleNote:** Theo tiến độ thật, chọn `stock` (Chờ hàng về), `create` (Chờ tạo vận đơn), `pack` (Chờ đóng hàng) hoặc `dispatch` (Chờ bàn giao). Tạo vận đơn thành công thì gắn mã và chuyển sang `pack`. Chỉ dùng `closed` khi đã ghi kết quả và hết việc phải xử lý hoặc theo dõi trong đợt. Webhook không tự chuyển các trạng thái này.

## Liên kết vận đơn và hậu mãi

Khi phát sinh giao lỗi, giao một phần hoặc hậu mãi, dùng lại hồ sơ gốc. Chọn `deliveryFailed`, `partial`, `exchange1` (hoàn đơn cũ), `exchange2` (khách gửi lại), `exchange3` (thu hồi tại cửa) hoặc `warrantyEvidence` (bảo hành). Ghi mã thật, hàng cần theo dõi và việc còn lại. Khi thực hiện hậu mãi, đọc [quy trình đổi trả và thu hồi](references/aftercare.md).

**Phân loại theo việc của khách.** Dùng `partial` khi khách nhận một phần hàng của đơn đang giao và trả phần còn lại. Dùng `exchange3` khi hậu mãi đổi size và giao đôi mới đồng thời thu đôi cũ, kể cả khi thao tác trên app hãng mang tên “Giao một phần” hoặc “Sửa COD / Thu hồi NVC”. Ghi tiến độ đóng hàng, bàn giao và thu hồi trên chính hồ sơ `exchange3`. Xem [quy trình thu hồi tại cửa](references/aftercare.md#đổi-size--thu-hồi-tại-cửa).

Kiện hoàn ngoài sổ có thể chỉ còn việc nhập lại kho. Đổi trực tiếp tại shop có thể đổi cả mẫu và size. Ghi đúng việc thực tế vào hồ sơ gốc, không ép vào một nhánh giao nhận hoặc tạo vận đơn mới. Dùng [quy trình kho của Admin](../admin-workspace/SKILL.md#nhập-lại-ngoài-sổ-và-đổi-trực-tiếp-tại-shop) và ghi tham chiếu phiếu, hàng đã đổi, khoản chênh lệch thực nhận nếu có. Còn phiếu cần ghi thì lưu đầu việc đó trước khi kết thúc xử lý.

Khi Dũng giao chốt đợt gửi, dùng
[luồng chốt đợt gửi](../shop-operations/references/reconciliation.md#chốt-đợt-gửi)
và [skill SuperAI](../superai-workspace/SKILL.md). Trích yêu cầu mới đã xác nhận
trước khi kiểm tồn. Ưu tiên xác nhận đủ điều kiện cũ nhất, trừ khi Dũng chỉ định
khác. `size_sent` khác `size_ordered` cần bằng chứng khách đồng ý.

Ghi riêng chặng đi/về thực tế và hàng, lượng, COD, khai giá từng chặng. Khi được giao tạo qua API, đọc hồ sơ/correction mới nhất, chốt SKU/lượng/COD/khai giá trên chặng rồi chỉ gửi qua `superai_submit_operation` với một operation UUID ổn định. Ghi ngay UUID bằng `salenote_link_shipment(create_operation_id=...)`. Liên kết không gửi hãng và nhận cả thao tác queued/unknown. Nếu gián đoạn trước khi liên kết, tìm đúng thao tác SuperAI cũ, không tạo lại. Gửi yêu cầu chỉ là vào hàng đợi. Kiểm tra SuperAI tới succeeded có mã hoặc đối soát chưa rõ kết quả trên cùng thao tác. Ghi kết quả/tiến độ SaleNote, chỉ đóng khi hết việc được giao. Mất phản hồi liên kết/lưu thì thử lại đúng operation ID/payload của sổ. Xung đột do con người sửa sau khi gửi thì đọc lại, ghi việc đã thực xảy ra, giữ điều chỉnh và không gửi thêm vận đơn. Không có giao dịch phân tán giữa sổ và vận chuyển.

Dùng `salenote_link_shipment(provider_code=...)` cho vận đơn tạo nơi khác. Thao tác chỉ ghi tham chiếu, không gửi yêu cầu hoặc nhận đã xác minh. Nhiều chặng logic có thể dùng cùng mã ngoài, nhưng một mã không được gắn nhiều hồ sơ. Lần thử thất bại/đã hủy vẫn giữ lịch sử. Kiểm kết quả chắc chắn trước khi tạo thay thế. Giữ ảnh chụp chặng đã thực hiện, thêm chặng mới khi nghĩa vụ thay đổi.

Khi thấy một dòng cũ `unknown` có `replacement_shipment_code` và
`replacement_verified_at`, đọc mã thay thế để tiếp tục việc của hồ sơ. Dòng
cũ còn trong lịch sử và đã được gỡ khỏi danh sách yêu cầu cần đối soát.
Nếu thấy bằng chứng mã cũ xuất hiện, xử lý khả năng có hai kiện theo
[luồng SuperAI](../superai-workspace/SKILL.md#tạo-hủy-và-đối-soát).

Dùng app hãng cho giao một phần và thu hồi tại cửa. Khi Dũng chọn luồng J&T thêm tác vụ thu hồi trong ca giao, có thể tạo kiện đi đã được giao quyền qua SuperAI trước. Giữ việc app còn mở tới khi xác minh và gắn mã hoàn thực tế khi được cấp. Hàng bảo hành thuộc khách dùng `stock_policy=none` kèm lý do và không tham gia xuất kho shop tự động. Hàng hoàn cần kiểm thực nhận/ghi kho. Trạng thái hãng chưa làm hàng trở thành tồn bán được. COD 0 không có nghĩa khai giá 0.

`superai_release_commitment` đối soát bằng chứng hủy/thất bại dứt khoát hoặc đã xuất thực tế, không chỉ dựa vào đóng sổ. Create chưa rõ kết quả vẫn giữ cam kết. Không xuất kho thủ công khi liên kết xuất tự động còn chờ. Sửa sổ không cấp quyền tự ghi tiền hoặc gửi khách.

Báo riêng yêu cầu mới xác nhận, vận đơn tạo thành công, lý do chưa tạo, việc đang chờ/chưa rõ và vận đơn có sẵn. Correction và việc tồn cũ được chỉ định rõ nằm ngoài số mới. Lưu việc dở trên SaleNote. Dừng khi hết nguồn, người khác đã tiến mốc tiến độ hoặc phần còn lại cần người khác. Không tự thiết lập lịch chạy lặp.

## Rà vận chuyển để chăm sóc khách

Khi được giao rà SaleNote, kiểm cả Messenger và SuperAI để phát hiện đơn hoãn giao cần chăm sóc. Đọc status, phân trang các mã đã biết và xem `mapping_status`/`mapping_status_name`; trạng thái tổng23/Đang Vận Chuyển có thể che mapping14/Hoãn Giao Hàng. Làm mới mã liên quan và chờ kết quả xác minh trước khi kết luận hiện trạng. Đọc events để lấy lý do hãng báo, phân biệt webhook chưa xác thực với trạng thái API và lời khách; không coi lý do hãng là khách đã xác nhận.

Đối chiếu mã vận đơn/create operation với hồ sơ hiện có, đọc điều chỉnh mới nhất. Cùng lần mua thì cập nhật/mở lại hồ sơ cũ cho đợt chăm sóc, giữ kết quả đóng/gửi trước đó; không tạo hồ sơ hay vận đơn trùng. Ghi mã, trạng thái, thời điểm xác minh, lý do và việc cần làm cụ thể. Nếu cần gọi khách vì đơn bị hoãn, ghi việc đó cho Dũng. Trạng thái hãng hết hoãn không tự chứng minh việc chăm sóc đã hoàn tất. Báo phạm vi mã đã biết và phần chưa truy cập; luồng này không tự gửi khách, sửa/hủy/tạo đơn, ghi kho/tiền hoặc lập lịch chạy định kỳ.
