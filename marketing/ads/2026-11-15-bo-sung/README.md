# Bổ sung quảng cáo — 15/11/2026

## Dũng đã chốt và giao triển khai

- Tạo campaign tương tác mới: 50.000đ/ngày, bốn ngày, một ad set/sáu ads dùng sáu bài mới. Không yêu cầu chia đều ngân sách từng bài.
- Tạo campaign Messenger Vapor mới: 180.000đ/ngày, không ngày kết thúc, một ad set/năm ads.
- Thêm ad Messi hồng vào ad set Messenger Messi hiện có trong campaign cũ.
- Đổi ngân sách ad set Tiempo/Messi thành 240.000đ/120.000đ mỗi ngày; tắt chia sẻ ngân sách để giữ phân bổ.
- Audience, placements và gợi ý câu hỏi ads Messenger phải giống cấu hình cũ; đọc live trước khi sao chép. Dùng bài đã đăng, không đăng lại.
- Tổng ngân sách cấu hình: 590.000đ/ngày trong đợt tương tác, sau đó 540.000đ/ngày. Chưa có mốc bắt đầu/kết thúc thực tế.

## Kết quả kiểm tra quyền

15/11: API từ chối token ads local với OAuth 190/463 (hết hạn 09/11 lúc 11:00 giờ Việt Nam). Token người dùng chính bị lỗi #200 khi đọc tài khoản ads, chưa được cấp quyền ads_read/ads_management với tài khoản này. Chưa tạo hoặc sửa đối tượng Meta nào. Chờ Dũng cấp lại token ads; không cần cấp lại token Page cho công việc này. Bằng chứng riêng: `.work/ads-20261115/`.


## Đã dựng và kiểm chứng API — 15/11

Dũng đã thay token; token mới đọc và ghi được tài khoản quảng cáo. Các lỗi token ở trên là lịch sử, không còn là blocker.

- Campaign tương tác `120254779901050057`, ad set `120254779901170057`: 50.000đ/ngày, đủ sáu ads. Lịch 15/11/2026 14:07:48 đến 19/11/2026 14:07:48 giờ Việt Nam (96 giờ).
- Campaign Messenger Vapor `120254779906360057`, ad set `120254779906580057`: 180.000đ/ngày, đủ năm ads, không end_time.
- Ad Messi trắng–hồng `120254779914670057` đã thêm đúng ad set `120254658428270057`.
- Campaign cũ `120254658365110057` đã tắt chia sẻ ngân sách. Tiempo `120254658365120057`: 240.000đ/ngày; Messi: 120.000đ/ngày. Hai nhóm cũ vẫn ACTIVE; thay đổi ngân sách đã áp dụng live.
- Hai campaign mới và toàn bộ 12 ads mới đều PAUSED, chưa bật phân phối. Khi bật tương tác sau mốc bắt đầu đã định, phải dời lại cả hai mốc để đủ bốn ngày.
- Đã so sánh targeting Messenger Vapor bằng đúng dữ liệu live của nhóm Messi cũ: giống hoàn toàn (VN, nam 18–44, không Advantage audience; placements không có giới hạn riêng như nhóm nguồn). Tương tác sao chép targeting nhóm tương tác cũ, Facebook Feed.
- Sáu creative Messenger có page_welcome_message khớp nguyên chuỗi mẫu live cũ: lời chào, bốn câu hỏi và cài đặt liên quan. Không sửa các cờ AI/reengagement của mẫu nguồn. API từ chối trường standard_enhancements đã deprecated; đã bỏ riêng trường này, giữ các feature riêng khác mà API chấp nhận.
- Cả 12 ads mới dùng object_story_id của sáu bài Page chính vừa đăng; không đăng lại bài. Chưa kiểm tra trực quan Ads Manager/preview hoặc chứng minh hiển thị thực tế.
- Receipt và snapshots riêng: `.work/ads-20261115/build-state.json`, `verified.json`. Không chứa access token.


## Cập nhật ngân sách, trạng thái và tên — 15/11

Dũng tự giảm Vapor xuống 120.000đ/ngày vì mỗi SKU chỉ có một đôi. Đọc live xác nhận mức 120.000đ và hai campaign mới cùng ad Messi hồng đều ACTIVE. Theo yêu cầu rà tên, đã đổi campaign/ad set Vapor từ 180k thành 120k, thêm tên mẫu–màu cho 11 ads mới trong hai campaign, đặt Messi hồng thành MSG_M07_Messi_TrangHong nối tiếp sáu ads cũ. Chỉ sửa name. Tổng ngân sách cấu hình 530.000đ/ngày trong đợt tương tác, sau đó 480.000đ/ngày. Snapshot riêng: `.work/ads-20261115/names-verified.json`.
