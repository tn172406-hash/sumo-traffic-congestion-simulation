# CHƯƠNG 2: KHẢO SÁT HIỆN TRẠNG VÀ THU THẬP DỮ LIỆU NÚT GIAO HÀNG XANH

**Người thực hiện:** Thành viên 2

**Phụ trách kỹ thuật:** Thu thập dữ liệu hiện trạng và xây dựng bộ lưu lượng phương tiện cho nhánh Điện Biên Phủ hướng ra Cầu Sài Gòn phục vụ mô phỏng SUMO.

---

## 2.1. Đặc điểm hình học và tổ chức giao thông nút giao Hàng Xanh

### 2.1.1. Vị trí địa lý và cấu trúc các nhánh đường tiếp cận

Nút giao Hàng Xanh nằm trên địa bàn quận Bình Thạnh, Thành phố Hồ Chí Minh. Đây là một trong những nút giao thông quan trọng của khu vực cửa ngõ phía Đông thành phố, đóng vai trò kết nối trung tâm Quận 1 với Thành phố Thủ Đức và các tỉnh miền Đông Nam Bộ.

Nút giao được hình thành bởi sự giao cắt giữa hai tuyến đường chính là Điện Biên Phủ và Xô Viết Nghệ Tĩnh. Trong đó, đường Điện Biên Phủ là tuyến giao thông huyết mạch theo hướng Đông - Tây, kết nối trung tâm thành phố với Xa lộ Hà Nội và các khu vực lân cận. Đường Xô Viết Nghệ Tĩnh giữ vai trò kết nối khu vực Bình Thạnh, Thanh Đa và Bến xe Miền Đông cũ với trung tâm thành phố.

Để giảm áp lực cho nút giao mặt đất, cầu vượt Hàng Xanh được đưa vào khai thác nhằm tách dòng phương tiện lưu thông theo hướng thẳng trên trục Điện Biên Phủ. Công trình này góp phần nâng cao năng lực thông hành, giảm thời gian chờ và hạn chế các xung đột giao thông tại khu vực giao cắt.

### 2.1.2. Phân làn, luồng tuyến và hiện trạng tổ chức giao thông

Tổ chức giao thông tại nút giao Hàng Xanh được xây dựng theo nguyên tắc phân tách các luồng phương tiện nhằm giảm thiểu giao cắt trực tiếp giữa các hướng lưu thông.

Các phương tiện đi thẳng trên tuyến Điện Biên Phủ được ưu tiên lưu thông qua cầu vượt. Các hướng rẽ trái, rẽ phải và chuyển hướng được điều tiết trên hệ thống đường mặt đất bằng đèn tín hiệu giao thông kết hợp với vạch dẫn hướng.

Một số nhánh được bố trí làn rẽ phải liên tục nhằm tăng khả năng giải tỏa phương tiện. Hệ thống biển báo, biển chỉ dẫn và vạch sơn mặt đường được lắp đặt tương đối đầy đủ, hỗ trợ người tham gia giao thông lựa chọn đúng hướng di chuyển.

Tuy nhiên, vào các khung giờ cao điểm, mật độ xe máy lớn cùng hiện tượng chuyển làn và nhập làn thường xuyên làm giảm tốc độ lưu thông và làm gia tăng nguy cơ ùn tắc cục bộ.

### 2.1.3. Chu kỳ và biểu đồ pha đèn tín hiệu hiện hữu

Hệ thống đèn tín hiệu giao thông tại nút giao Hàng Xanh có vai trò điều phối lưu lượng phương tiện giữa các hướng giao cắt và bảo đảm an toàn giao thông.

Trong phạm vi nghiên cứu, chu kỳ đèn tín hiệu được mô phỏng với tổng thời gian 90 giây. Chu kỳ này được sử dụng làm cơ sở xây dựng mô hình điều khiển giao thông trong SUMO.

Phân bổ thời lượng các pha đèn được thiết lập như sau:

- Pha xanh hướng Điện Biên Phủ: 45 giây.
- Pha xanh hướng Xô Viết Nghệ Tĩnh: 35 giây.
- Đèn vàng và thời gian chuyển pha: 10 giây.

Việc ưu tiên thời gian xanh cho hướng Điện Biên Phủ phản ánh đặc điểm lưu lượng thực tế khi đây là hướng có mật độ phương tiện lớn nhất tại khu vực nghiên cứu.

---

## 2.2. Phân tích hiện trạng lưu thông và tình trạng ùn tắc

### 2.2.1. Diễn biến giao thông trong các khung giờ cao điểm sáng và chiều

Kết quả khảo sát cho thấy lưu lượng giao thông tại nút giao Hàng Xanh biến động đáng kể theo từng thời điểm trong ngày.

Trong khoảng thời gian từ 07h00 đến 08h30, lượng phương tiện từ Thành phố Thủ Đức, Đồng Nai và Bình Dương tập trung di chuyển vào trung tâm Thành phố Hồ Chí Minh. Dòng xe chủ yếu lưu thông trên tuyến Điện Biên Phủ hướng về Quận 1, làm gia tăng áp lực lên hệ thống đèn tín hiệu và các làn chờ tại nút giao.

Ngược lại, trong khoảng thời gian từ 17h00 đến 18h30, dòng phương tiện từ khu vực trung tâm di chuyển về Thành phố Thủ Đức và các khu vực phía Đông tăng mạnh. Đây là giai đoạn nhánh Điện Biên Phủ hướng ra Cầu Sài Gòn có lưu lượng giao thông cao nhất trong ngày.

Trong các khung giờ cao điểm, tốc độ lưu thông trung bình giảm rõ rệt, thời gian chờ tại đèn tín hiệu tăng lên và thường xuất hiện hiện tượng xếp hàng kéo dài tại các hướng tiếp cận nút giao.

### 2.2.2. Các điểm nóng xung đột gây nghẽn xe

Qua quá trình khảo sát hiện trạng, một số vị trí thường xuyên xảy ra xung đột và ùn tắc giao thông được xác định như sau.

Khu vực thứ nhất là giao điểm giữa dòng xe rẽ trái từ Điện Biên Phủ sang Xô Viết Nghệ Tĩnh với dòng xe đi thẳng trên tuyến chính. Lưu lượng lớn từ nhiều hướng khiến khu vực này thường xuyên hình thành hàng xe chờ kéo dài.

Khu vực thứ hai là chân cầu vượt Hàng Xanh. Tại vị trí này, các phương tiện từ cầu vượt đi xuống phải nhập vào dòng xe đang lưu thông ở mặt đất, làm phát sinh hiện tượng giảm tốc độ và ùn ứ cục bộ.

Khu vực thứ ba là vùng chờ đèn tín hiệu trong giờ cao điểm. Khi số lượng phương tiện vượt quá khả năng giải tỏa của nút giao, hàng xe kéo dài không chỉ ảnh hưởng đến khu vực giao cắt mà còn tác động đến các tuyến đường tiếp cận xung quanh.

Những điểm xung đột này là nguyên nhân chính làm suy giảm năng lực thông hành và gia tăng thời gian di chuyển qua nút giao Hàng Xanh.

---

## 2.3. Phương pháp thu thập dữ liệu phục vụ mô phỏng

### 2.3.1. Thu thập dữ liệu hình học mạng đường (OpenStreetMap và Google Maps)

Dữ liệu hình học mạng đường được thu thập từ OpenStreetMap (OSM) kết hợp với ảnh vệ tinh và dữ liệu giao thông trên Google Maps.

Quá trình thực hiện bao gồm việc xác định phạm vi nghiên cứu, kiểm tra số lượng làn xe, hướng lưu thông, vị trí các nhánh rẽ và khu vực cầu vượt Hàng Xanh. Sau khi hoàn tất quá trình hiệu chỉnh, dữ liệu được chuyển đổi sang định dạng mạng lưới SUMO bằng công cụ NETCONVERT.

Việc sử dụng đồng thời nhiều nguồn dữ liệu giúp bảo đảm mô hình giao thông xây dựng có mức độ tương đồng cao với điều kiện thực tế tại khu vực nghiên cứu.

### 2.3.2. Thu thập dữ liệu vận hành đèn tín hiệu

Dữ liệu về hệ thống đèn tín hiệu được xây dựng dựa trên quá trình khảo sát hiện trạng kết hợp với quan sát trực tiếp tại khu vực nút giao.

Các thông số được ghi nhận bao gồm tổng chu kỳ đèn, thời gian đèn xanh, đèn đỏ, đèn vàng và trình tự hoạt động của các pha tín hiệu. Sau khi được tổng hợp và chuẩn hóa, dữ liệu này được sử dụng để xây dựng mô hình điều khiển đèn giao thông trong môi trường SUMO.

---

## 2.4. Xây dựng bộ số liệu lưu lượng phương tiện đầu vào

### 2.4.1. Cơ sở khảo sát và chuẩn hóa số liệu lưu lượng phương tiện

Do điều kiện khảo sát thực địa còn hạn chế, bộ số liệu lưu lượng phương tiện được xây dựng dựa trên quan sát thực tế tại nút giao Hàng Xanh kết hợp với các đặc điểm giao thông điển hình của Thành phố Hồ Chí Minh.

Quá trình chuẩn hóa dữ liệu được thực hiện nhằm bảo đảm tính hợp lý của mô hình và phản ánh đúng đặc điểm giao thông đô thị. Các kịch bản mô phỏng tập trung vào các giai đoạn cao điểm, là thời điểm thường xuyên xảy ra ùn tắc và có ý nghĩa phân tích lớn đối với nghiên cứu.

Các dữ liệu sau khi xử lý được sử dụng làm đầu vào cho mô hình mô phỏng SUMO và phục vụ việc đánh giá hiệu quả vận hành của nút giao.

### 2.4.2. Phân bổ thành phần dòng xe

Dựa trên đặc điểm giao thông đô thị tại Thành phố Hồ Chí Minh, thành phần phương tiện tham gia giao thông trong mô hình được phân bổ theo tỷ lệ tương đối như sau:

- Xe máy: khoảng 80%.
- Ô tô con: khoảng 15%.
- Xe buýt: khoảng 5%.

Các tỷ lệ trên được sử dụng để xây dựng tệp tuyến lưu lượng:

`SUMO/route_nhanh2_dbp_out.rou.xml`

Việc duy trì tỷ lệ xe máy ở mức cao giúp mô hình phản ánh sát đặc điểm lưu thông thực tế của khu vực nghiên cứu. Đồng thời, tỷ lệ ô tô con và xe buýt được bổ sung nhằm tái hiện đầy đủ cơ cấu phương tiện thường gặp trên tuyến Điện Biên Phủ hướng ra Cầu Sài Gòn.

---

## 2.5. Kết luận chương

Chương 2 đã trình bày đặc điểm hình học, hiện trạng tổ chức giao thông và tình hình lưu thông tại nút giao Hàng Xanh. Các yếu tố như cấu trúc mạng đường, hệ thống đèn tín hiệu và điều kiện vận hành thực tế đã được khảo sát và phân tích.

Bên cạnh đó, dữ liệu về mạng lưới giao thông, chu kỳ đèn tín hiệu và cơ cấu phương tiện tham gia giao thông cũng đã được thu thập, xử lý và chuẩn hóa phục vụ cho quá trình mô phỏng.

Nhánh Điện Biên Phủ hướng ra Cầu Sài Gòn được lựa chọn làm đối tượng nghiên cứu do có lưu lượng phương tiện lớn và thường xuyên xảy ra ùn tắc trong các khung giờ cao điểm. Bộ dữ liệu được xây dựng trong chương này sẽ là cơ sở để thiết lập luồng phương tiện, xây dựng kịch bản mô phỏng và đánh giá hiệu quả vận hành của nút giao trong các chương tiếp theo.
