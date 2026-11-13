# CHƯƠNG 4: PHÂN TÍCH VÀ ĐÁNH GIÁ KẾT QUẢ MÔ PHỎNG
**Người thực hiện:** Thành viên 4  
**Phụ trách kỹ thuật SUMO:** `SUMO/route_nhanh4_xvnt_tn.rou.xml` (Nhánh Xô Viết Nghệ Tĩnh từ Thị Nghè)

---

## 4.1. Phân tích diễn biến giao thông tổng thể qua các kịch bản
### 4.1.1. Diễn biến dòng xe tại Kịch bản 1 (Thấp điểm - 50%)
* Dòng xe lưu thông thông thoáng trên cả cầu vượt và dưới ngã tư.
* Hàng xe chờ tại đèn đỏ giải tỏa nhanh trong 1 chu kỳ đèn.

### 4.1.2. Diễn biến dòng xe tại Kịch bản 2 (Trung bình - 100%)
* Xuất hiện hiện tượng xếp hàng chờ tại nhánh Điện Biên Phủ và Xô Viết Nghệ Tĩnh.
* Dòng xe qua cầu vượt vận hành ổn định, không bị xung đột.

### 4.1.3. Diễn biến dòng xe tại Kịch bản 3 (Cao điểm - 175%)
* Xung đột rẽ trái dưới ngã tư gây tắc nghẽn kéo dài lan ra các nhánh tiếp cận.
* Hàng xe chờ vượt quá sức chứa của đoạn đường gom trước nút giao.

### 4.1.4. Hình ảnh trực quan hóa tình trạng giao thông trên giao diện SUMO-GUI
*(Chèn ảnh chụp màn hình từ SUMO-GUI: `images/hien_trang_un_tac_gui.png`)*

---

## 4.2. So sánh và đánh giá các chỉ số vận hành giao thông
*(Sử dụng số liệu từ file `SUMO/Bao_Cao_Tong_Hop_3_Kich_Ban.csv` và 2 biểu đồ)*

### Bảng số liệu tổng hợp:
| Chỉ số vận hành | Kịch bản 1 (Thấp) | Kịch bản 2 (Vừa) | Kịch bản 3 (Cao) |
|---|:---:|:---:|:---:|
| Vận tốc trung bình (km/h) | 5.32 | 4.39 | 3.75 |
| Số xe kẹt lớn nhất (xe) | 1.518 | 1.581 | 1.633 |
| Thời gian chờ xe máy (giây) | 239.7 | 136.6 | 159.6 |
| Thời gian chờ ô tô con (giây) | 203.6 | 108.2 | 112.6 |
| Thời gian chờ xe buýt (giây) | 275.2 | 297.6 | **427.3** |

### 4.2.1. Đánh giá sự gia tăng của thời gian chờ trung bình (Waiting Time)
*(Chèn biểu đồ: `SUMO/bieu_do_1_thoi_gian_cho.png`)*
* Nhận xét: Thời gian chờ của xe buýt tăng đột biến 55% khi chuyển từ mức trung bình sang cao điểm.

### 4.2.2. Đánh giá sự suy giảm của tốc độ trung bình (Mean Speed)
*(Chèn biểu đồ: `SUMO/bieu_do_2_van_toc_va_un_tac.png`)*
* Tốc độ trung bình toàn mạng suy giảm từ 5.32 km/h xuống còn 3.75 km/h do mật độ xe dừng đỗ tăng cao.

### 4.2.3. Đánh giá độ dài hàng xe chờ và thời gian hành trình trên các nhánh tiếp cận

---

## 4.3. Xác định ngưỡng lưu lượng gây ùn tắc tại nút giao Hàng Xanh
### 4.3.1. Phân tích tương quan giữa mức tăng lưu lượng và mức độ suy giảm dịch vụ
### 4.3.2. Xác định điểm tới hạn dẫn đến ùn tắc kéo dài
