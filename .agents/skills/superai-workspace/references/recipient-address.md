# Chuẩn hóa địa chỉ nhận để tạo vận đơn

Với luồng hiện tại của shop, đích gửi là địa chỉ **ba cấp cũ** theo danh
mục SuperAI. Cần xác lập cả hai việc: điểm giao theo khách và bộ tên tỉnh,
huyện, xã mà SuperAI nhận cho điểm đó.

## Xác định điểm giao

1. Đọc tin gốc và ảnh liên quan tới lượt mua. Đối chiếu điều chỉnh mới nhất
   của khách hoặc Dũng trên SaleNote. Tách chi tiết giao (số nhà, đường,
   ấp/tổ, cơ quan, cổng hay mốc nhận) khỏi tên đơn vị hành chính. Dùng địa
   chỉ từ đơn giao thành công trước đó như bằng chứng bổ sung khi xác nhận
   vẫn là cùng điểm giao. Địa chỉ lưu trong hồ sơ không tự thay tin mới.
2. Chuẩn hóa cách đọc để tra: có/không dấu, viết tắt, tên gọi tắt, thứ tự,
   tiền tố Xã/Phường/Thị trấn. Ví dụ `CMT8` thường là Cách Mạng Tháng Tám;
   giữ cách khách viết nếu chưa cần mở rộng hoặc chưa chắc tên đường.
   Khi tên có dấu khác vị trí, chẳng hạn Hòa/Hoà, dùng cả hai dạng để tìm.
   Giữ nguyên chi tiết giao đã xác nhận và giá trị gốc trong nguồn.
3. Nếu khách dùng tên mới/cũ lẫn nhau hoặc thiếu cấp, tìm ứng viên theo
   phần đặc trưng nhất. Dùng nghị quyết chính thức để lấy các đơn vị cũ
   có thể tương ứng. Dùng nguồn địa phương, trang cơ quan/doanh nghiệp
   công khai hoặc bản đồ để đối chiếu mốc, đường, thôn/ấp/tổ. Nếu vẫn còn
   hai nơi, tìm dữ kiện phân biệt như đoạn đường qua một phường, cổng nhà
   máy hoặc tên ấp trong hồ sơ cũ. Tìm bằng tên địa bàn và mốc công khai
   phù hợp. Không dán tên người nhận, SĐT, số nhà riêng, toàn địa chỉ hay
   ảnh hội thoại vào công cụ tra cứu công khai.

Nghị quyết có thể cho biết một phường mới gồm nhiều phường cũ. Cần bằng
chứng ở cấp điểm giao để chọn một nhánh. Một địa chỉ do Gemini, bản đồ
hoặc công cụ chuẩn hóa đề xuất vẫn là ứng viên, trừ phần Dũng đã xác nhận
hoặc đã đối chiếu được với nguồn. Giữ mốc riêng khi khách dùng tên công ty
có nhiều cơ sở. Không thêm số nhà, tên đường hoặc tên cơ sở cụ thể chỉ vì
kết quả tìm kiếm có vẻ khớp.

## Đối chiếu tên SuperAI và điền yêu cầu

1. Dùng `superai_reference(resource="provinces")` → `districts` với
   `parent_code` tỉnh → `communes` với `parent_code` huyện. Công cụ
   không lọc theo chuỗi tên; theo `next_offset` để đọc đủ phần cần so.
   Trong một đợt, dùng lại danh sách tỉnh/huyện/xã đã tra khi nhiều đơn
   cùng địa bàn. Mỗi kết quả phải thuộc đúng cây cha–con.
2. Giữ địa chỉ gốc và nguồn xác minh trong hồ sơ riêng. Điền
   `shipment.address` bằng chi tiết giao đã xác nhận. Điền
   `shipment.province`, `shipment.district`, `shipment.commune` bằng
   **tên nguyên văn** từ ba kết quả danh mục. Mã tỉnh/huyện/xã dùng để
   tra cây và đối chiếu. [API hãng](https://docs.superai.vn/guide/orders.html)
   mặc định ba cấp và nhận tên. Schema MCP hiện tại không có `area_type`
   hoặc `receiver_new_address`. Gửi mã vào các trường tên có thể bị từ
   chối dù cây địa chỉ đúng.
3. MCP kiểm cây tên trước khi xếp hàng gửi. `superai_invalid_address` chỉ
   rõ trường cần sửa; `superai_address_catalog_unavailable` cho biết
   danh mục chưa tra được. Cả hai đều xác nhận lần gửi này chưa xếp hàng
   tạo. Xử lý theo [quy trình tạo và đối soát](../SKILL.md#tạo-hủy-và-đối-soát).
4. Nếu cần kiểm cước/tuyến, dùng `superai_quote` với tên tỉnh/huyện
   gửi và nhận. Công cụ báo cước không kiểm phường/xã hoặc số nhà. Form web
   chọn được khu vực cũng chưa chứng minh payload MCP đang truyền đúng.
   Dùng kết quả kiểm địa chỉ để tiếp quy trình tạo đơn đã được giao.

## Các tình huống đối chiếu

- **Viết tắt và tên cũ đã rõ:** `CMT8, TT Võ Xu, Đức Linh, Bình Thuận`
  có thể dùng cây `Tỉnh Bình Thuận / Huyện Đức Linh / Thị trấn Võ Xu`
  khi phần chi tiết giao đã xác nhận. Không đổi tỉnh chỉ vì bản đồ hiện
  hiển thị tên mới.
- **Gửi lại đúng nơi từng nhận:** Nếu khách vẫn nhận ở ấp thuộc Trường Long
  cũ, cây hãng là `Thành phố Cần Thơ / Huyện Phong Điền / Xã Trường Long`.
  Biên nhận giao cũ giúp xác định điểm khi địa chỉ mới vẫn trỏ về đúng ấp.
- **Đơn vị cùng tên, loại đơn vị khác:** Khách ghi “xã Lai Uyên” và bằng
  chứng cùng điểm giao ở Đồng Sổ, địa bàn Bàu Bàng cũ. Cây hãng tương ứng là
  `Tỉnh Bình Dương / Huyện Bàu Bàng / Thị trấn Lai Uyên`. Điền đúng tên
  hãng và giữ chi tiết giao theo chứng cứ.
- **Địa chỉ lẫn mới và cũ:** Nếu đã xác định đúng tiểu khu của thị trấn
  Lương Sơn cũ thì cây hãng là `Tỉnh Hoà Bình / Huyện Lương Sơn /
  Thị trấn Lương Sơn`. Chỉ thấy “xã Lương Sơn, Phú Thọ” thì còn phải
  xác định điểm thuộc thị trấn cũ hay đơn vị cũ khác.
- **Một phường mới có nhiều phường cũ:** Với “phường Hà Giang 2, Tuyên
  Quang”, dùng [nghị quyết sắp xếp cấp xã](https://vanban.chinhphu.vn/?docid=214004&pageid=27160)
  để thu hẹp. Chỉ chọn `Tỉnh Hà Giang / Thành phố Hà Giang / Phường Trần Phú`
  khi điểm giao có bằng chứng thuộc Trần Phú cũ, ví dụ Dũng đã xác nhận.
  Danh mục hãng cũng có `Phường Minh Khai` trong cùng cây cũ.

Các cây trong ví dụ đã tra chỉ đọc qua SuperAI. Tra lại danh mục hiện hành
khi làm đơn. Ví dụ chỉ minh họa địa bàn và cách điền.

Khi đã xác lập một điểm giao và cây hợp lệ, xử lý đơn trong quyền đã có.
Nếu còn mơ hồ, nêu đúng thành phần cần phân biệt và những ứng viên có căn
cứ; hỏi một dữ kiện còn thiếu sau khi đã tra. Phân biệt địa chỉ chưa đủ,
không có cây tương ứng và lỗi công cụ/hãng. Nếu yêu cầu đã gửi mà bị từ
chối hoặc chưa rõ, kiểm payload và đối soát theo
[quy trình tạo và đối soát](../SKILL.md#tạo-hủy-và-đối-soát).
