# CHƯƠNG 3: XÂY DỰNG MÔ HÌNH VÀ THIẾT LẬP KỊCH BẢN MÔ PHỎNG TRÊN SUMO

**Người thực hiện:** Thành viên 3  
**Phụ trách kỹ thuật:** Xây dựng mạng lưới đường và thiết lập mô phỏng SUMO cho nhánh Xô Viết Nghệ Tĩnh từ Bến xe Miền Đông.

## 3.1. Quy trình xây dựng mạng lưới đường trên SUMO

### 3.1.1. Chuyển đổi bản đồ OSM sang tệp mạng đường (.net.xml) bằng NETCONVERT

Để xây dựng mô hình giao thông, dữ liệu bản đồ được thu thập từ OpenStreetMap (OSM) tại khu vực nút giao Hàng Xanh và tuyến đường Xô Viết Nghệ Tĩnh, khu vực kết nối với Bến xe Miền Đông.

Quá trình chuyển đổi được thực hiện bằng công cụ NETCONVERT tích hợp trong SUMO.

Các bước thực hiện:

- Truy cập OpenStreetMap và xác định khu vực nghiên cứu.
- Xuất dữ liệu bản đồ dưới định dạng OSM (.osm).
- Sử dụng NETCONVERT để chuyển đổi dữ liệu bản đồ sang định dạng mạng lưới SUMO (.net.xml).
- Kiểm tra các tuyến đường, nút giao và hướng lưu thông trên mạng lưới sau khi chuyển đổi.

Tệp đầu ra là tệp mạng lưới đường có định dạng `.net.xml`, chứa các thông tin về nút giao, cạnh đường, làn đường, chiều lưu thông và các thuộc tính hình học.

### 3.1.2. Chỉnh sửa, kết nối làn và hoàn thiện hình học bằng NETEDIT

Sau khi chuyển đổi dữ liệu OSM, mạng lưới đường được đưa vào NETEDIT để chỉnh sửa và hoàn thiện.

Các công việc thực hiện:

- Khai báo và kiểm tra các nhánh đường tiếp cận trong tệp `hangxanh.edg.xml`.
- Khai báo các nút giao thông trong tệp `hangxanh.nod.xml`.
- Kiểm tra sự kết nối giữa các đoạn đường và bảo đảm phương tiện có thể di chuyển liên tục.
- Cấu hình tầng cầu vượt thép để tách biệt với các nút giao trên mặt đất.
- Kiểm tra và điều chỉnh liên kết làn xe (lane connections) cho các hướng rẽ trái, rẽ phải và đi thẳng.
- Loại bỏ các đoạn đường bị lỗi kết nối hoặc có hình học không phù hợp.

Sau khi chỉnh sửa, sử dụng NETCONVERT để tạo lại tệp mạng lưới hoàn chỉnh và kiểm tra trực quan trên SUMO-GUI.

## 3.2. Cài đặt thông số phương tiện và tín hiệu điều khiển

### 3.2.1. Khai báo thuộc tính các loại phương tiện (vType) và lộ trình (routes)

Trong mô hình giao thông, ba loại phương tiện chính được sử dụng gồm xe máy, ô tô con và xe buýt.

Các thông số được khai báo trong tệp `hangxanh.vTypes.xml` như sau:

| Loại phương tiện | Chiều dài | Chiều rộng | Gia tốc | Khoảng cách tối thiểu |
|---|---:|---:|---:|---:|
| Xe máy (motorcycle) | 1,9 m | 0,8 m | 2,6 m/s² | 0,5 m |
| Ô tô con (passenger) | 4,5 m | 1,8 m | Theo cấu hình SUMO | 1,5 m |
| Xe buýt (bus) | 10,5 m | 2,5 m | Theo cấu hình SUMO | 2,0 m |

Các thông số được sử dụng nhằm mô phỏng sự khác biệt về kích thước và khả năng di chuyển của từng loại phương tiện.

Ngoài ra, mô hình thiết lập chức năng lách làn cho xe máy bằng tham số:

`lateral-resolution="0.8"`

Chức năng này hỗ trợ mô phỏng hành vi di chuyển ngang của xe máy trong điều kiện giao thông hỗn hợp.

Các tuyến đường di chuyển được khai báo trong tệp `routes.xml`. Mỗi tuyến đường xác định điểm xuất phát, các đoạn đường đi qua và điểm kết thúc của phương tiện.

### 3.2.2. Thiết lập chương trình đèn tín hiệu cố định (traffic_lights)

Mô hình sử dụng chương trình đèn tín hiệu cố định với chu kỳ 90 giây, được khai báo trong tệp `TL_HANGXANH`.

Chương trình điều khiển gồm hai pha chính:

**Pha 1: Hướng Điện Biên Phủ**

- Đèn xanh: 42 giây.
- Đèn vàng: 3 giây.
- Cho phép phương tiện di chuyển theo hướng được điều khiển.

**Pha 2: Hướng Xô Viết Nghệ Tĩnh**

- Đèn xanh: 42 giây.
- Đèn vàng: 3 giây.
- Cho phép phương tiện di chuyển theo hướng được điều khiển.

Tổng chu kỳ đèn:

T = 42 + 3 + 42 + 3 = 90 giây.

Việc thiết lập chu kỳ đèn cố định giúp mô hình đánh giá ảnh hưởng của tín hiệu giao thông đến khả năng lưu thông và tình trạng ùn tắc tại khu vực nút giao.

## 3.3. Thiết lập các kịch bản mô phỏng theo mức lưu lượng

Để đánh giá khả năng hoạt động của mạng lưới đường trong những điều kiện giao thông khác nhau, ba kịch bản mô phỏng được xây dựng dựa trên hệ số lưu lượng (scale factor).

### 3.3.1. Kịch bản 1: Mức lưu lượng thấp (50% - Giờ thấp điểm)

Kịch bản 1 mô phỏng tình trạng giao thông trong khoảng thời gian thấp điểm, khi số lượng phương tiện tham gia giao thông tương đối ít.

- Hệ số lưu lượng: `scale factor = 0.5`.
- Lưu lượng phương tiện bằng 50% so với kịch bản cơ sở.
- Mật độ phương tiện thấp.
- Khả năng di chuyển tương đối thông thoáng.
- Thời gian chờ tại nút giao dự kiến thấp hơn so với các kịch bản còn lại.

Mục đích của kịch bản là đánh giá khả năng hoạt động bình thường của mạng lưới khi lưu lượng phương tiện không cao.

### 3.3.2. Kịch bản 2: Mức lưu lượng trung bình (100% - Tiệm cận dung lượng thiết kế)

Đây là kịch bản cơ sở được sử dụng để làm mốc so sánh với các kịch bản khác.

- Hệ số lưu lượng: `scale factor = 1.0`.
- Giữ nguyên lưu lượng phương tiện theo dữ liệu đầu vào.
- Mật độ giao thông ở mức trung bình.
- Các phương tiện bắt đầu chịu ảnh hưởng của mật độ giao thông tại những vị trí có lưu lượng lớn.

Kịch bản này giúp đánh giá hiệu quả hoạt động của mạng lưới trong điều kiện lưu lượng giao thông cơ sở.

### 3.3.3. Kịch bản 3: Mức lưu lượng cao (175% - Áp lực giờ cao điểm)

Kịch bản 3 mô phỏng tình trạng giao thông trong giờ cao điểm, khi số lượng phương tiện tăng cao và gây áp lực lớn lên năng lực thông hành của tuyến đường.

- Hệ số lưu lượng: `scale factor = 1.75`.
- Lưu lượng phương tiện tăng lên 175% so với kịch bản cơ sở.
- Mật độ phương tiện tăng cao.
- Khả năng xuất hiện hàng chờ tại các nút giao lớn hơn.
- Thời gian chờ và nguy cơ ùn tắc có thể tăng đáng kể.

Mục tiêu là xác định khả năng đáp ứng của mạng lưới đường khi lưu lượng phương tiện vượt mức cơ sở.

## 3.4. Vận hành mô phỏng, kiểm chứng và trích xuất dữ liệu

### 3.4.1. Chạy thử nghiệm và hiệu chỉnh lỗi logic di chuyển (Validation)

Sau khi hoàn thiện mạng lưới, khai báo phương tiện, tuyến đường và chương trình đèn tín hiệu, mô hình được chạy thử nghiệm trên SUMO-GUI.

Quá trình kiểm chứng được thực hiện theo các nội dung:

- Kiểm tra các phương tiện có thể xuất hiện tại vị trí xuất phát và di chuyển đúng tuyến đường đã khai báo.
- Kiểm tra khả năng kết nối giữa các đoạn đường và làn đường.
- Kiểm tra phương tiện có thể thực hiện các hướng đi thẳng, rẽ trái và rẽ phải.
- Kiểm tra hoạt động của hệ thống đèn tín hiệu theo chu kỳ 90 giây.
- Kiểm tra hiện tượng phương tiện bị dừng bất thường hoặc không thể di chuyển do lỗi kết nối.
- Quan sát tình trạng giao thông trong cả ba kịch bản lưu lượng.

Nếu phát hiện lỗi, tiến hành điều chỉnh mạng lưới đường, tuyến di chuyển hoặc thông số phương tiện trước khi chạy mô phỏng chính thức.

### 3.4.2. Cấu hình trích xuất dữ liệu chỉ số đầu ra

Để phục vụ việc đánh giá và so sánh kết quả giữa ba kịch bản, mô hình sử dụng các tệp dữ liệu đầu ra của SUMO.

Các loại dữ liệu cần trích xuất gồm:

**1. Tripinfo-output**

Tệp này lưu trữ thông tin về hành trình của từng phương tiện, bao gồm:

- Thời điểm phương tiện bắt đầu và kết thúc hành trình.
- Tổng thời gian di chuyển.
- Thời gian phương tiện bị dừng.
- Tổng chiều dài hành trình.

**2. Summary-output**

Tệp này cung cấp các chỉ số tổng hợp theo từng bước thời gian mô phỏng, bao gồm:

- Số lượng phương tiện đang hoạt động.
- Số lượng phương tiện đã hoàn thành hành trình.
- Số lượng phương tiện chưa hoàn thành.
- Thời gian chờ và các thông tin tổng hợp về tình trạng giao thông.

**3. Queue-output**

Tệp này ghi nhận tình trạng hàng chờ phương tiện tại các làn đường, hỗ trợ đánh giá:

- Số lượng phương tiện trong hàng chờ.
- Chiều dài hàng chờ.
- Sự thay đổi hàng chờ theo thời gian.
- Các vị trí thường xuyên xảy ra ùn tắc.

Các dữ liệu đầu ra được lưu riêng cho từng kịch bản để thuận tiện cho việc phân tích.

### Kết luận chương 3

Trong chương 3, quy trình xây dựng mô hình giao thông trên SUMO được trình bày từ bước thu thập dữ liệu bản đồ OSM, chuyển đổi mạng lưới đường, chỉnh sửa hình học, khai báo phương tiện và thiết lập tín hiệu đèn giao thông.

Bên cạnh đó, ba kịch bản mô phỏng với mức lưu lượng 50%, 100% và 175% được xây dựng nhằm đánh giá sự thay đổi của tình trạng giao thông trong những điều kiện khác nhau.

Cuối cùng, các dữ liệu đầu ra như Tripinfo, Summary và Queue được sử dụng làm cơ sở để đánh giá thời gian di chuyển, tình trạng hàng chờ và mức độ ùn tắc tại khu vực nghiên cứu.
