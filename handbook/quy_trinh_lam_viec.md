# Quy trình làm việc — Yêu Bóng Đá Shop

Dũng phụ trách toàn bộ vận hành, agent hỗ trợ theo đầu việc được giao. Cập nhật ngày 23/11/2026.

## Checklist mỗi ngày

### 11h — Xử lý khách và việc tồn

- [ ] Mở Messenger, xử lý các cuộc trò chuyện AI chuyển lại và yêu cầu mới cần người thật.
- [ ] Cho agent [quét Messenger và SuperAI](../.agents/skills/shop-operations/references/messenger-scan.md).
  Dùng cùng phần Messenger đã đọc để cập nhật SaleNote và sổ ý định mua. Mỗi
  sổ tiếp nối mốc tiến độ riêng.
- [ ] Mở SaleNote, làm các việc đến hẹn. Gọi/nhắn khách cần xác nhận, ghi kết quả và hẹn tiếp nếu chưa xong.

### 16h30–17h — Chốt đợt gửi chiều

- [ ] Rà khách thêm một lượt, xử lý tin mới và cập nhật các việc còn chờ.
- [ ] Chốt danh sách gửi hôm nay. Kiểm đủ thông tin khách, hàng thực có thể gửi, số lượng, giá và COD; thiếu gì xử lý trước khi tạo đơn.

### 17h–18h30 — Tạo đơn, đóng và gửi hàng

- [ ] Cho agent tạo vận đơn trên SuperAI khoảng 17h–17h30. Đối chiếu địa chỉ
  nhận với [danh mục ba cấp của hãng](../.agents/skills/superai-workspace/references/recipient-address.md).
  Kiểm mã đơn thành công và đối soát yêu cầu còn chờ trước khi tạo thay thế.
- [ ] In nhãn, lấy hàng và đối chiếu **mẫu–màu–size, số lượng, phụ kiện/quà đã xác nhận, người nhận và COD** trước khi đóng.
- [ ] Khoảng 18h30 bàn giao/mang ra bưu cục, cập nhật SaleNote. Thứ Bảy và Chủ nhật gửi sớm theo giờ nhận của bưu cục.

### Trước khi nghỉ — Khép lại việc trong ngày

- [ ] Kiểm các kiện đã bàn giao có phiếu xuất kho; đơn thuộc luồng tự xuất SuperAI thì kiểm kết quả, tránh xuất tay trùng. Hàng xưởng/hàng hoàn đã về cần kiểm và ghi nhập đúng lượng.
- [ ] Ghi tiền thực thu/chi còn thiếu trên Admin, kiểm khoản COD đã tự ghi trước khi thêm tay.
- [ ] Rà SaleNote lần cuối. Việc xong ghi kết quả và đóng; việc chưa xong có hành động tiếp theo và mốc hẹn.

Giao gấp và sự cố đang diễn ra được xử lý theo cam kết với khách, không chờ tới lượt rà kế tiếp.

## Cách giữ việc để ngày mai tiếp tục được

**Messenger** để trao đổi với khách, **SaleNote** để giữ việc, **SuperAI/app hãng** để xử lý giao nhận, **Admin** để ghi kho và tiền.

Một lần mua dùng một hồ sơ SaleNote, hậu mãi tiếp tục trên hồ sơ đó. Ghi vào
SaleNote ngay trong lượt rà khi có SĐT đã xác nhận và khách đã chốt mua hoặc
shop đã nhận một việc cụ thể. Đọc câu xác nhận theo mạch hội thoại, kể cả khi
khách trả lời bằng sticker. Đơn chốt có điều kiện vẫn vào sổ, kèm việc cần
kiểm trước khi gửi. Thiếu SĐT thì tìm lại lịch sử và hồ sơ khách. Nếu vẫn
thiếu, giữ nhu cầu trong Messenger. Xem [điều kiện mở hồ sơ](../.agents/skills/salenote-workspace/SKILL.md#điều-kiện-mở-hồ-sơ).

Sau mỗi lần gọi, nhắn hoặc thao tác, ghi kết quả vào hồ sơ. Có việc còn chờ thì ghi rõ đang chờ ai, cần làm gì và khi nào kiểm lại. Hội thoại đã xử lý có thể chuyển Done sau khi việc cần theo dõi đã được lưu.

## Khi có hàng về

- **Hàng xưởng** — Đếm thực nhận theo mẫu–màu–size, đối chiếu đơn đặt. Nhập đúng lượng và giá/cước đã xác nhận; ghi riêng phần thiếu, sai hoặc lỗi để xử lý với xưởng.
- **Hàng hoàn/khách gửi lại** — Đối chiếu mã với đơn gốc, mở kiểm đúng đôi và tình trạng. Kiện đủ điều kiện trong sổ Hàng hoàn thì chọn **Đúng đủ — nhập kho**, thao tác này đã cộng kho. Hàng ngoài sổ cần đối chiếu nguồn xuất và ghi nhập lại qua Admin. Hàng chưa rõ hoặc lỗi để riêng chờ xử lý.
- **Tiền** — Ghi khi thực thu/chi, gồm tiền bán hàng, COD, trả xưởng, phụ kiện, ads, vật tư, phần mềm và dịch vụ nội dung. Đối chiếu khoản đã ghi trước khi bổ sung.

## Khi có việc phát sinh

### Khách hỏi đơn ở đâu hoặc hãng báo giao lỗi

Tra đúng mã và trạng thái trên SuperAI/app hãng → liên hệ khách để xác nhận tình hình, còn nhận không và lịch thuận tiện → yêu cầu hãng xử lý/giao lại → ghi kết quả và hẹn kiểm tiếp. Theo dõi tới kết quả nhận hoặc hoàn rõ ràng.

### Hết hàng hoặc thiếu size đã hẹn

Kiểm tồn và hàng đã hẹn cho khách khác → gửi ảnh lựa chọn thay thế hoặc thống nhất chờ nhập → chỉ đổi hàng khi khách đồng ý → ghi lựa chọn cuối và lịch cập nhật vào SaleNote.

### Đổi size

Chốt đôi cần đổi, tình trạng, cước và khoản còn thu trước khi thực hiện. Chọn đúng tình huống.

1. **Khách hoàn nguyên kiện, chưa thanh toán** — Kiểm đơn cũ đã vào luồng hoàn. Có thể gửi đơn mới thu đủ COD đã chốt trước khi kiện cũ về. Theo dõi cả hai mã trên cùng hồ sơ.
2. **Khách đã trả tiền và tự gửi về** — Lưu mã khách gửi. Nhận và kiểm đúng đôi rồi mới gửi thay thế. COD 0đ khi đổi ngang giá, đã thanh toán đủ và hết khoản cần thu.
3. **Shop giao mới và thu hồi đôi cũ tại cửa** — Thiết lập tác vụ đổi/thu hồi trên app hãng, kiểm COD và việc thu hồi đã được ghi nhận trước khi giao. Lưu mã thu hồi thực tế, theo dõi tới khi nhận và kiểm đôi cũ. Tra hướng dẫn thao tác trước khi làm ca này.

### Khách chỉ nhận một phần kiện đang giao

Xác nhận món giữ, món trả và COD mới → xử lý trên app/kênh hãng → lưu mã hoàn và theo dõi phần trả về → kiểm thực nhận rồi nhập kho. Ca đổi size thu hồi tại cửa vẫn được ghi là đổi size dù app dùng tên “Giao một phần”.

### Bảo hành

Đối chiếu đơn gốc và ảnh lỗi, chỉ xin video nếu ảnh chưa đủ → xác nhận với xưởng khi cần → chốt sửa/đổi, cước hai chiều và nơi gửi → nhận, kiểm đúng đôi/lỗi → thực hiện phương án đã duyệt. Giữ riêng đôi lỗi; chỉ nhập tồn bán được sau khi xử lý và kiểm đạt.

### Giao gấp, trả hàng hoặc hoàn tiền

Dũng chốt thời gian, hàng, cước và số tiền với khách/hãng trước khi thực hiện. Hoàn tiền cần ghi khoản thực trả trên Admin và kết quả trong SaleNote.

## Mỗi tuần — Nhập hàng và rà lại việc

- [ ] Dùng [sổ ý định mua](../.agents/skills/shop-operations/references/purchase-intent.md)
  đã cập nhật hằng ngày. Rà bổ sung phần còn thiếu trong kỳ trước khi tính cơ cấu
  và đối chiếu tồn mục tiêu, tồn thực cùng hàng đã hẹn chưa xuất.
- [ ] Tính từng SKU bằng công thức **Số đặt = MAX(0, tồn mục tiêu − tồn hiện tại + cam kết khách chưa xuất kho)**. Kiểm lô đang về và hàng xưởng gửi thiếu để tránh đặt trùng.
- [ ] Chốt file đặt xưởng, theo dõi số thực gửi/nhận. Rà hồ sơ quá hẹn, hàng thu hồi chưa về và các phiếu kho/tiền còn thiếu.
- [ ] Sắp lịch nội dung và quảng cáo cho tuần, ghi các chi phí thực phát sinh.

## Tài liệu để tra khi cần

- [Chính sách bán hàng](chinh_sach_ban_hang.md) và [prompt Meta](../marketing/meta-agent/instructions.md).
- [Hướng dẫn tạo/xử lý vận đơn](../.agents/skills/superai-workspace/SKILL.md), [thu hồi tại cửa](../.agents/skills/salenote-workspace/references/aftercare.md#đổi-size--thu-hồi-tại-cửa) và [nhập hàng hoàn](../.agents/skills/admin-workspace/SKILL.md#hàng-hoàn--sổ-kiểm-và-nhập-kho).
- Agent bắt đầu từ [skill vận hành](../.agents/skills/shop-operations/SKILL.md) khi phối hợp nhiều nguồn và dùng [skill nhập hàng tuần](../.agents/skills/weekly-replenishment/SKILL.md) khi lập đơn đặt xưởng.

Khi có người hỗ trợ, giao từng nhóm việc theo checklist, kèm hồ sơ đang mở và phạm vi được quyết định. Kết quả tiếp tục được ghi vào các hệ thống trên.
