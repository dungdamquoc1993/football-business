---
name: shop-operations
description: Điều phối việc của Yêu Bóng Đá Shop qua Messenger, SaleNote, SuperAI và Admin. Dùng khi quét hằng ngày, rà việc còn chờ, cập nhật sổ ý định mua, đo quảng cáo, lên đợt gửi hoặc đối chiếu kho và thu chi.
---

# Vận hành Yêu Bóng Đá Shop

Chọn phần theo việc Dũng giao. Khi một lượt gồm nhiều việc, đọc chứng cứ chung
một lần và dùng lại trong lượt. Mỗi hệ thống ghi kết quả và giữ mốc tiến độ của
chính nó. Chỉ dùng nguồn cần để xác minh hoặc thực hiện phần được giao.

- **Quét Messenger hằng ngày / cập nhật SaleNote:** dùng
  [luồng quét chung](references/messenger-scan.md). Một lượt quét thường ngày
  cập nhật cả hồ sơ SaleNote và sổ ý định mua; nếu Dũng chỉ định một nhánh, làm
  nhánh đó. Rà cả vận đơn cần chăm sóc khi quét Messenger và SuperAI hoặc rà
  vận hành SaleNote.
- **Cập nhật ý định mua / đo quảng cáo:** dùng
  [sổ ý định mua và quảng cáo](references/purchase-intent.md). Rà bổ sung phần
  Messenger chưa xử lý nếu cần. Đọc và lưu chi tiêu theo kỳ được giao.
- **Lập đơn đặt xưởng:** dùng
  [nhập hàng hằng tuần](../weekly-replenishment/SKILL.md). Dùng lại ý định mua
  đã lưu, bổ sung phạm vi còn thiếu, rồi lấy tồn mới và cam kết chưa xuất.
- **Chốt đợt gửi / tạo vận đơn:** dùng
  [luồng chốt đợt gửi](references/reconciliation.md#chốt-đợt-gửi) và
  [skill SuperAI](../superai-workspace/SKILL.md). Làm địa chỉ và kiểm SKU theo
  từng đơn. Đơn đủ điều kiện tiếp tục xử lý dù đơn khác còn vướng.
- **Đối chiếu hàng và tiền:** dùng
  [luồng kho và thu chi](references/reconciliation.md#đối-chiếu-kho-và-thu-chi)
  và mở phần cần thiết của [skill Admin](../admin-workspace/SKILL.md).

Messenger sở hữu lời khách, ảnh và thông tin đã trao đổi. SaleNote sở hữu đầu
việc và điều chỉnh mới của Dũng. SuperAI sở hữu biên nhận tạo vận đơn và trạng
thái hãng. Admin sở hữu danh mục, tồn thực, phiếu kho, tiền thực tế, sổ ý định
mua và số liệu quảng cáo. Đối chiếu theo Page/hội thoại, lượt mua, SKU, mã vận
đơn hoặc phiếu phù hợp. Trùng tên hoặc số điện thoại chỉ giúp tìm ứng viên.

Quyền đọc và quyền ghi theo việc Dũng giao. Tiếp tục các phần độc lập có thể
hoàn thành. Báo kết quả đã xác minh và nêu đúng dữ kiện còn thiếu để xử lý phần
dở. Giữ chứng cứ khách hàng trong hệ thống sở hữu.
