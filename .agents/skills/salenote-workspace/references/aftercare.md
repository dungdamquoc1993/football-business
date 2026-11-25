# Đổi trả, bảo hành và thu hồi hàng

Đọc khi thực hiện hậu mãi trên hồ sơ SaleNote gốc. Chốt hàng, khoản còn thu và
phương án với khách trước khi thao tác. Vận đơn, ghi chú hay trạng thái hãng không
chứng minh đã nhận hàng hoặc thu tiền. Khi kiện về, kiểm thực nhận rồi dùng
[skill Admin](../../admin-workspace/SKILL.md) để nhập đúng lượng còn bán được.

## Chọn đúng nhánh xử lý

- **Đổi size · Hoàn đơn cũ.** Khi khách yêu cầu gửi đơn mới và SuperAI xác nhận
  đơn cũ đã vào luồng hoàn, tạo đơn mới với đủ COD đã chốt. Có thể gửi đơn mới trước
  khi kiện cũ về. Tiếp tục theo dõi kiện cũ trên cùng hồ sơ.
- **Đổi size · Khách gửi lại.** Gắn mã gửi của khách. Sau khi nhận và kiểm đúng đôi
  của đơn gốc, tạo vận đơn đổi. COD 0đ áp dụng khi đã xác nhận khách thanh toán đủ,
  đổi ngang giá và hết khoản cần thu. Khai giá theo giá trị hàng.
- **Đổi size · Thu hồi tại cửa.** Dùng `exchange3` cho hậu mãi giao đôi mới và
  lấy lại đôi cũ. Chọn thao tác hãng theo [quy trình bên dưới](#đổi-size--thu-hồi-tại-cửa).
- **Giao một phần.** Dùng `partial` khi khách nhận một phần hàng của đơn đang
  giao và trả phần còn lại. Xác nhận món giữ, món trả và COD sau điều chỉnh.
  SuperAI có thể báo Đã giao toàn bộ. Gắn mã hoàn thực tế, theo dõi kiện về và
  ghi nhập hoàn theo lượng đã kiểm.
- **Bảo hành.** Đối chiếu đơn gốc với ảnh lỗi và xin video nếu cần. Chốt sửa hay
  đổi, địa chỉ gửi và cước hai chiều trước khi khách gửi. Chờ xưởng xác nhận khi
  cần. Gắn mã kiện khách gửi, kiểm đúng đôi và lỗi rồi thực hiện phương án đã
  duyệt. Để riêng đôi lỗi, chỉ đưa vào tồn bán được sau khi đạt kiểm tra.

## Đổi size · Thu hồi tại cửa

Mở lại hồ sơ gốc ở `exchange3`. Giữ vận đơn đã giao và ghi riêng đôi gửi đổi,
đôi thu hồi, số lượng, phụ kiện đi kèm và khoản khách đồng ý trả. Tiến độ đóng
hàng, bàn giao và thu hồi nằm trên hồ sơ đổi size. Tên nút trên app hãng không
quyết định loại hồ sơ SaleNote.

- **Tạo đơn COD dương rồi thu hồi trong ca giao.** Khi Dũng chọn luồng này, tạo
  kiện gửi đôi mới với COD ban đầu do Dũng chốt. Ghi rõ hàng giao, hàng thu hồi
  và yêu cầu shipper kiểm tra COD sau điều chỉnh trước khi giao. Gắn mã kiện mới
  và lưu đầu việc theo dõi trong SaleNote. Ngay khi kiện mới vào nhóm
  **Đã lấy hàng – Đang giao hàng** trên app, tạo **Sửa COD / Thu hồi NVC**, hạ
  COD về khoản thực thu đã chốt và tích thu hồi. Kiểm tra tác vụ đã ghi nhận và
  COD đúng trước khi giao. Nếu chưa xác minh được tác vụ, báo người phụ trách xử
  lý trước khi shipper thu COD ban đầu. Ghi chú trên đơn không kích hoạt tác vụ.
- **Tạo đơn đổi trả COD 0đ.** Khi hai bên đã xác nhận thanh toán đủ và hết khoản
  phải thu, có thể chọn **Đổi trả** ngay lúc tạo trên app và ghi hàng cần thu
  hồi. Theo hướng dẫn J&T nhận ngày 22/11/2026, luồng này có mã thu hồi dạng
  `TR-…` và phụ phí đổi bằng 50% cước giao, còn luồng sửa COD/thu hồi trong ca
  giao có thể ra mã hậu tố `-001` và miễn phí thu hồi khi tác vụ được ghi nhận.
  Đối chiếu phí và mã trên đơn thực tế.

Ở cả hai luồng, gắn mã thu hồi do hãng cấp, theo dõi đôi cũ về và kiểm thực nhận
trước khi ghi nhập hoàn. Dùng app cho thao tác đổi trả hoặc sửa COD/thu hồi.
Việc tạo kiện gửi đôi mới qua API chưa xác nhận các thao tác đó thành công.
