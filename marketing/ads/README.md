# Ads — hồ sơ làm việc và lịch sử

Dũng chốt ngày 25/11/2026: giữ lịch sử ads có cấu trúc tại đây, chủ yếu phục vụ
agent tra cứu và tiếp tục công việc. Làm ads trong repo với credentials riêng ở
`.env`; không đưa token vào hồ sơ. Trạng thái trên Meta phải đọc lại trước thao tác.

## Kết nối API — kiểm chứng 27/11/2026

- Theo yêu cầu Dũng, đã đổi token ads ngắn hạn mới sang token người dùng dài hạn
  và thay trực tiếp `META_ADS_USER_ACCESS_TOKEN` trong `.env`; các biến khác giữ nguyên.
- Meta Debug Token xác nhận token mới hợp lệ, cùng app/người dùng với token nguồn,
  có `ads_read` và `ads_management`; hạn token là 15:30:49 ngày 25/01/2027,
  giờ Việt Nam. Đây là hạn trả về lúc kiểm chứng, không bảo đảm token không bị thu hồi sớm.
- Đọc trực tiếp cả hai tài khoản `814094494973387` và `1554033896044468` bằng
  token mới, xác nhận tác vụ `ADVERTISE` và `MANAGE`. Không thay đổi quảng cáo.
- Chỉ token trong file local đã được thay; chưa thiết lập tự gia hạn hoặc cập nhật
  credentials của dịch vụ/server. Hồ sơ không chứa giá trị token.

## Đo hiệu quả — Dũng chốt và sửa phạm vi27/11/2026

Đơn vị kết quả chung là **intent mua hàng rõ ràng theo số đôi**, dùng cho nhập
hàng và đo ads từ ad lên ad set, campaign, tài khoản, kể cả nhiều tài khoản chạy
cùng bài. q đôi có intent thật đóng góp q; khách mua thêm chỉ cộng lượng mới,
nhắc lại không đếm thêm. Thiếu hàng/hủy không xóa intent có thật. Bảo hành,
đổi size và gửi lại thuộc hậu mãi không tạo intent mới. Chuyển mẫu/màu do thiếu
hàng và khách đồng ý mua thay thế giữ0,7q gốc/0,3q cuối, tổngq; không có thay thế
thì giữ nhu cầu gốc=q. Quy tắc7/3 phân bổ sản phẩm, không chia credit giữa ads.
Không dùng đơn chốt/giao thành công làm thang kết quả riêng của phép đo đã chọn.

Sổ intent và cấu hình thuộc Admin MCP qua skill weekly-replenishment. Đã lưu
rule clear-purchase-intent-v1 và clear_intent_weight=1 tại settings version2
ngày27/11; không coi ledger cũ đã được rà lại hoặc tự sửa kế hoạch nhập cũ.
SaleNote vẫn là sổ xử lý công việc độc lập, không là nguồn dữ liệu hoặc nơi ghi
attribution mới cho phép đo này. Ghi chú nguồn cũ trong SaleNote giữ làm lịch sử.

Khi Dũng giao lượt quét Messenger/SuperAI hằng ngày, dùng cùng phần Messenger
đã thực sự đọc để cập nhật intent; mỗi nghiệp vụ giữ checkpoint riêng. Nhập hàng
tiếp tục theo tuần. Đây không phải yêu cầu tạo lịch tự động hoặc sửa ngân sách.

Facebook MCP đã kiểm tra có source_ad_ids ở facebook_browse(view=detail) từ
explicit referrals, không cần token ads local. Lần kiểm tra facebook_read không
trả referral trên từng tin; chưa có bằng chứng timestamp referral gắn từng lần
mua. Thiếu/multiple sources giữ unknown/mixed, không suy từ mẫu giày/post và
không đếm trùng intent cho nhiều ads. Thêm hierarchy account/campaign/adset/ad
bằng mapping được xác minh qua Meta khi gặp ID mới; giữ lại để tra dùng tiếp.
Quy ước trường nguồn và phép tổng hợp chưa được kiểm chứng ghi/đọc trên intent.

Dũng ưu tiên chỉ bổ sung ghi chép nguồn, không xây flow lấy chi tiêu thường trực
trong app. Chi tiêu đọc từ Meta bằng token ads hoặc UI theo kỳ khi cần tính.
Mục tiêu chi phí/intent gồm cả thuế và phí thẻ. Dũng ước tính phí khoảng9.900đ
mỗi lần charge; chưa kiểm chứng mức phí/số lần charge. Đối chiếu thuế theo từng
tài khoản/hóa đơn và tránh cộng lại nếu số đầu vào đã gồm thuế. Phân bổ thuế/phí
xuống ad theo tỷ trọng chi tiêu cùng tài khoản và cùng kỳ là đề xuất, chưa chốt.

### Các góc nhìn Dũng yêu cầu — tiếp tục trao đổi27/11

Dũng muốn xem theo mẫu giày, creative/nội dung, tài khoản, campaign, ad set và ad;
lọc chéo, so chi tiêu với intent và giá trị quy đổi từ intent×giá tham chiếu. Giá trị
này không phải doanh thu thực nhận. Cần giữ giá và thời điểm/cơ sở giá khi quy đổi.
Chỉ danh sách ad liên quan chưa đủ để chia kết quả cộng khớp giữa các nguồn.

Các điểm đang tư vấn, chưa chốt để code: quy tắc credit intent giữa nhiều ads;
gom nội dung dùng chung qua nhiều creative ID/tài khoản; phân biệt mẫu được quảng
cáo với mẫu khách có nhu cầu; cách xử lý chi tiêu quảng cáo nhiều mẫu chung. Không
tự coi toàn bộ chi tiêu của một ad là chi tiêu riêng cho từng mẫu/intent liên quan.
Dũng yêu cầu thống nhất cách count trước khi bắt đầu code. Chưa triển khai báo cáo
hoặc thay quy tắc credit nguồn trong lượt trao đổi này.

## Mở đúng hồ sơ

- [Chuyển sang tài khoản phụ, 21–25/11](2026-11-21-chuyen-tai-khoan/README.md):
  kế hoạch chuyển, Messenger Messi/Vapor, tương tác và Tiempo mới; giữ các quyết
  định và việc còn chờ theo từng thời điểm.
- [Bổ sung Vapor và Messi, 15/11](2026-11-15-bo-sung/README.md).
- [Đợt 08/11](2026-11-08-dot-moi/README.md): cấu hình, các lần chỉnh và ID đối tượng.
- [Đợt 29/10](2026-10-29/README.md): ID, kết quả và giới hạn số liệu của đợt đầu.
- [Mẫu hội thoại](templates/MAU-HOI-THOAI.md): các phiên bản đã dùng; không mặc định
  mẫu cũ là mẫu đang chạy. Bài, caption và kết quả đăng thuộc [bài đăng](../fanpage-posts/README.md).

## Cách lưu sau mỗi lượt làm ads

Mỗi đợt hoặc mục tiêu có một thư mục `YYYY-MM-DD-ten-dot/`, dùng ngày bắt đầu.
Tiếp tục hồ sơ đó khi chỉnh ngân sách, thay ads hoặc kiểm tra kết quả; không mở
một thư mục mới cho mỗi phiên agent.

`README.md` của hồ sơ giữ các mục rõ ràng:

- Mục tiêu và phạm vi: tài khoản/Page, yêu cầu và quyết định của Dũng; tách đề xuất
  chưa chốt khỏi việc được giao.
- Đối tượng: `account_id`, `campaign_id`, `adset_id`, `ad_id`, `post_id` có liên quan.
- Diễn biến theo ngày: điều đã làm, lý do và kết quả; không viết lại lịch sử cũ
  theo kết quả mới. Quyết định mới cần nói rõ phần nào được thay thế.
- Kiểm chứng: `verified_at` kèm múi giờ, nguồn đọc, trạng thái đã quan sát và giới
  hạn. Bật cấu hình, được duyệt và đã phân phối là các kết quả riêng.
- Việc còn chờ: điều kiện tiếp tục, ID cần tra và hành động chưa được thực hiện.

Chỉ thêm JSON khi cần danh sách ID hoặc dữ liệu có cấu trúc để dùng lại; JSON là
snapshot có thời điểm, không thay trạng thái live. Tránh chép lại cùng kết luận
ở nhiều file. Payload, script, log và bản đọc trung gian dùng `.work/<việc>/`;
lưu outcome/ID cần thiết vào hồ sơ rồi dọn file tạm theo quy ước chung.
