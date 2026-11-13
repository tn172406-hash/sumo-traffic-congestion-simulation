# CHƯƠNG 3: XÂY DỰNG MÔ HÌNH VÀ THIẾT LẬP KỊCH BẢN MÔ PHỎNG TRÊN SUMO
**Người thực hiện:** Thành viên 3  
**Phụ trách kỹ thuật SUMO:** `SUMO/route_nhanh3_xvnt_bx.rou.xml` (Nhánh Xô Viết Nghệ Tĩnh từ Bến xe Miền Đông)

---

## 3.1. Quy trình xây dựng mạng lưới đường trên SUMO
### 3.1.1. Chuyển đổi bản đồ OSM sang tệp mạng đường (.net.xml) bằng NETCONVERT
* Sử dụng dữ liệu trích xuất từ OpenStreetMap khu vực nút giao Hàng Xanh.
* Chuyển đổi các thẻ đường và nút giao sang định dạng mạng lưới SUMO.

### 3.1.2. Chỉnh sửa, kết nối làn và hoàn thiện hình học bằng NETEDIT
* Khai báo các nhánh đường tiếp cận (`hangxanh.edg.xml`) và các nút giao (`hangxanh.nod.xml`).
* Cấu hình tầng cầu vượt thép tách biệt khỏi nút giao đèn tín hiệu mặt đất.
* Tinh chỉnh liên kết các làn xe (`lane connections`) cho các hướng rẽ trái, rẽ phải, đi thẳng.

---

## 3.2. Cài đặt thông số phương tiện và tín hiệu điều khiển
### 3.2.1. Khai báo thuộc tính các loại phương tiện (vType) và lộ trình (routes)
* Khai báo trong `hangxanh.vtypes.xml`:
  * Xe máy (`motorcycle`): kích thước 1.9m x 0.8m, gia tốc 2.6 m/s2, minGap 0.5m.
  * Ô tô con (`passenger`): kích thước 4.5m x 1.8m, minGap 1.5m.
  * Xe buýt (`bus`): kích thước 10.5m x 2.5m, minGap 2.0m.
* Cấu hình tính năng lách làn cho xe máy (`lateral-resolution="0.8"`).

### 3.2.2. Thiết lập chương trình đèn tín hiệu cố định (traffic_lights)
* Khai báo đèn `TL_HANGXANH` với 4 pha tín hiệu chuẩn 90 giây:
  * Pha 1: Xanh trục Điện Biên Phủ (42s) + Vàng (3s)
  * Pha 2: Xanh trục Xô Viết Nghệ Tĩnh (42s) + Vàng (3s)

---

## 3.3. Thiết lập các kịch bản mô phỏng theo mức lưu lượng
### 3.3.1. Kịch bản 1: Mức lưu lượng thấp (50% - Giờ thấp điểm)
* Áp dụng scale factor = 0.5 để đánh giá tình trạng giao thông thông thoáng.

### 3.3.2. Kịch bản 2: Mức lưu lượng trung bình (100% - Tiệm cận dung lượng thiết kế)
* Áp dụng scale factor = 1.0 làm kịch bản cơ sở so sánh.

### 3.3.3. Kịch bản 3: Mức lưu lượng cao (175% - Áp lực giờ cao điểm)
* Áp dụng scale factor = 1.75 để mô phỏng tình trạng quá tải và ùn tắc nghiêm trọng.

---

## 3.4. Vận hành mô phỏng, kiểm chứng và trích xuất dữ liệu
### 3.4.1. Chạy thử nghiệm và hiệu chỉnh lỗi logic di chuyển (Validation)
### 3.4.2. Cấu hình trích xuất dữ liệu chỉ số đầu ra (tripinfo-output, summary-output, queue-output)
