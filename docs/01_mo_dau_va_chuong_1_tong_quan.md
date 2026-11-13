# PHẦN MỞ ĐẦU & CHƯƠNG 1: TỔNG QUAN VỀ ÙN TẮC GIAO THÔNG VÀ MÔ PHỎNG SUMO
**Người thực hiện:** Thành viên 1  
**Phụ trách kỹ thuật SUMO:** `SUMO/route_nhanh1_dbp_in.rou.xml` (Nhánh Điện Biên Phủ vào trung tâm Q1)

---

## PHẦN MỞ ĐẦU
### 1. Lý do chọn đề tài
*(Thành viên 1 trình bày tính cấp thiết: áp lực giao thông tại nút giao Hàng Xanh - cửa ngõ Đông Bắc TP.HCM, tình trạng kẹt xe giờ cao điểm...)*

### 2. Mục tiêu nghiên cứu
* Mô phỏng vi mô hoạt động của dòng giao thông hỗn hợp tại nút giao Hàng Xanh.
* Đánh giá tác động của các mức lưu lượng phương tiện khác nhau đến mức độ ùn tắc.
* Xác định ngưỡng quá tải và đề xuất giải pháp tổ chức giao thông.

### 3. Đối tượng và phạm vi nghiên cứu
* **Đối tượng:** Dòng phương tiện hỗn hợp (xe máy, ô tô, xe buýt) và tổ chức giao thông tại nút giao Hàng Xanh.
* **Phạm vi:** Không gian nút giao cắt mức và cầu vượt thép Hàng Xanh; thời gian mô phỏng 1 giờ cao điểm (3.600 giây).

---

## CHƯƠNG 1: TỔNG QUAN VỀ ÙN TẮC GIAO THÔNG VÀ MÔ PHỎNG SUMO
### 1.1. Khái niệm và nguyên nhân gây ùn tắc giao thông tại nút giao đô thị
#### 1.1.1. Định nghĩa ùn tắc và đặc điểm dòng xe hỗn hợp đô thị
*(Nêu đặc điểm dòng xe tại Việt Nam: tỷ lệ xe máy cao >80%, khả năng len lỏi, không đi theo làn cố định...)*
#### 1.1.2. Các nguyên nhân và dạng xung đột tại nút giao cắt mức
*(Phân tích các dạng xung đột: xung đột cắt dòng, nhập dòng, tách dòng, đặc biệt là xung đột rẽ trái...)*

### 1.2. Các thông số dòng giao thông và chỉ số đánh giá ùn tắc
#### 1.2.1. Các thông số cơ bản: Lưu lượng, Tốc độ, Mật độ
#### 1.2.2. Các chỉ số hiệu quả vận hành: Thời gian chờ (Waiting time), chiều dài hàng xe (Queue length), tốc độ hành trình (Travel speed)

### 1.3. Tổng quan về công cụ mô phỏng vi mô SUMO
#### 1.3.1. Giới thiệu phần mềm SUMO và nguyên lý mô phỏng vi mô
#### 1.3.2. Cấu trúc mạng lưới đường và mô hình chuyển động của phương tiện (Car-following model, Lane-changing model)
#### 1.3.3. Các công cụ hỗ trợ (NETCONVERT, NETEDIT, SUMO-GUI) và định dạng dữ liệu đầu ra (tripinfo, summary, queue)

---

## KẾT LUẬN VÀ KIẾN NGHỊ (VIẾT Ở CUỐI BÀI)
### 1. Kết luận chung
### 2. Ý nghĩa thực tiễn đối với quản lý giao thông tại nút giao Hàng Xanh
