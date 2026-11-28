# Đợt gửi, kho và thu chi

## Chốt đợt gửi

1. Mở đúng hồ sơ/chặng SaleNote và lời khách liên quan, gồm điều chỉnh mới
   của Dũng. Chốt người nhận, hàng, lượng, giá, COD và điều kiện giao. Dùng
   [hướng dẫn chuẩn hóa địa chỉ](../../superai-workspace/references/recipient-address.md)
   khi cần đối chiếu địa chỉ cũ/mới với SuperAI.
2. Đối chiếu từng SKU bằng Admin và tổng cam kết chưa xuất trong cả đợt. Tìm
   đúng vận đơn/chặng hoặc yêu cầu tạo trước đó bằng tham chiếu. Đối chiếu
   yêu cầu cũ và đơn thay thế để tính nghĩa vụ đã xác định một lần. Nếu có
   dấu hiệu hai kiện thực tế, xử lý sai lệch. Với trạng thái chưa rõ, làm
   theo [cách đối soát SuperAI](../../superai-workspace/SKILL.md#tạo-hủy-và-đối-soát).
3. Khi được giao tạo, gửi qua SuperAI, lưu UUID vào đúng hồ sơ/chặng, rồi
   đọc lại biên nhận. Có mã đã xác minh thì liên kết vận đơn và cập nhật
   `pack` nếu còn chờ đóng. Theo
   [cách ghi chặng SaleNote](../../salenote-workspace/SKILL.md#liên-kết-vận-đơn-và-hậu-mãi).
   Nếu Dũng chỉ giao rà, trả danh sách đủ điều kiện và việc cần xác minh.

## Đối chiếu kho và thu chi

- **Hàng xuất:** Từ danh sách kiện hoặc bàn giao Dũng xác nhận, tìm mã vận
  đơn/chặng và đúng SKU. Mở `superai_shipment.inventory` và phiếu Admin
  liên kết trước khi ghi. `issued` có phiếu đã xác minh thì dùng phiếu đó.
  Đang chờ hoặc bị chặn trong luồng tự xuất thì đối soát nguyên nhân, giữ
  việc chưa xong. Với kiện ngoài luồng tự xuất, chỉ ghi phiếu khi có bằng
  chứng thực bàn giao, SKU/lượng và quyền ghi kho.
- **Hàng nhập và hoàn:** Dùng số kiểm thực nhận. Với hàng xưởng, đối chiếu
  kế hoạch đã đặt, lô đang về, giá mua/cước đã chốt và phần xưởng còn thiếu.
  Với hàng hoàn, tìm theo mã kiện/lượt đổi trong Admin; nếu cần dùng
  SuperAI, SaleNote và tin khách để xác định đúng chặng, phiếu xuất gốc và
  mặt hàng. Dùng [luồng kiểm và nhập hoàn](../../admin-workspace/SKILL.md#hàng-hoàn--sổ-kiểm-và-nhập-kho).
- **Tiền:** Lấy số tiền/ngày thực thu hoặc chi Dũng xác nhận. Messenger,
  SaleNote và SuperAI có thể giúp nhận diện đơn hay khoản liên quan. Kiểm
  sổ Admin và biên nhận thực tế trước khi ghi, gồm COD đã tự ghi qua SHB,
  chuyển khoản, khoản trả xưởng và hoàn tiền. COD dự kiến, trạng thái giao
  hoặc chi phí quảng cáo phục vụ báo cáo không tự tạo phiếu thu chi. Xem
  [cách ghi tiền Admin](../../admin-workspace/SKILL.md#thu-chi-thực-tế).
- **Khép việc:** Kiểm lại phiếu và giá trị đã lưu. Khi phần được giao gồm
  SaleNote, gắn tham chiếu vào hồ sơ gốc và cập nhật việc còn chờ. Mỗi khoản
  tiền, một lần xuất hoặc một lần nhận hàng chỉ ghi một lần vào sổ sở hữu.
