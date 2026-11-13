# MÔ PHỎNG VÀ ĐÁNH GIÁ ÙN TẮC GIAO THÔNG TẠI NÚT GIAO HÀNG XANH BẰNG SUMO
> **Hệ thống Giao thông Thông minh (ITS) - Đề tài tiểu luận nhóm**  
> Địa điểm nghiên cứu: **Nút giao Hàng Xanh, Quận Bình Thạnh, TP. Hồ Chí Minh**  
> Công cụ mô phỏng vi mô: **SUMO (Simulation of Urban MObility)**

---

## 📌 GIỚI THIỆU DỰ ÁN
Dự án tập trung xây dựng mô hình mô phỏng vi mô nút giao Hàng Xanh – một trong những cửa ngõ giao thông huyết mạch và điểm nóng ùn tắc phức tạp nhất TP.HCM. Mô hình tích hợp:
- Cấu trúc giao thông 2 tầng: Cầu vượt thép (lưu thông trực thông) và nút giao cắt mức bên dưới với hệ thống đèn tín hiệu 4 pha.
- Đặc tính dòng xe hỗn hợp đô thị Việt Nam (tỷ lệ xe máy cao >80%, mô hình lách làn linh hoạt `lateral-resolution="0.8"`).
- Đánh giá 3 kịch bản lưu lượng: **Thấp điểm (50%)**, **Trung bình (100%)**, và **Cao điểm (175%)**.

---

## 👥 BẢNG PHÂN CÔNG NHIỆM VỤ THÀNH VIÊN & NHÁNH GIT

Mỗi thành viên làm việc trên một **nhánh Git (Branch)** độc lập, phụ trách **1 nhánh đường trong SUMO** và **1 chương trong báo cáo tiểu luận**:

| Thành viên | Tên Branch Git | File mô hình SUMO | File bài viết Markdown | Nội dung chi tiết |
|:---|:---|:---|:---|:---|
| **Nhóm trưởng** | `main` | `SUMO/hangxanh*.sumocfg` | `README.md`, `HUONG_DAN_DAY_GITHUB.md` | Quản lý khung kiến trúc, hệ thống chạy 3 kịch bản, script vẽ biểu đồ, tích hợp toàn bộ bài. |
| **Thành viên 1** | `feature/nhanh1-dbp-in` | [`SUMO/route_nhanh1_dbp_in.rou.xml`](SUMO/route_nhanh1_dbp_in.rou.xml) | [`docs/01_mo_dau_va_chuong_1_tong_quan.md`](docs/01_mo_dau_va_chuong_1_tong_quan.md) | **Nhánh ĐBP vào (Cầu Sài Gòn -> Q1):** Tinh chỉnh lưu lượng xe lên cầu vượt vs dưới đất; viết Mở đầu, Chương 1 và Kết luận bài luận. |
| **Thành viên 2** | `feature/nhanh2-dbp-out` | [`SUMO/route_nhanh2_dbp_out.rou.xml`](SUMO/route_nhanh2_dbp_out.rou.xml) | [`docs/02_chuong_2_khao_sat_hien_trang.md`](docs/02_chuong_2_khao_sat_hien_trang.md) | **Nhánh ĐBP ra (Q1 -> Cầu Sài Gòn):** Tinh chỉnh xe qua cầu vượt và rẽ Thị Nghè/Bến xe; viết Chương 2 hiện trạng hình học và đèn tín hiệu. |
| **Thành viên 3** | `feature/nhanh3-xvnt-bx` | [`SUMO/route_nhanh3_xvnt_bx.rou.xml`](SUMO/route_nhanh3_xvnt_bx.rou.xml) | [`docs/03_chuong_3_xay_dung_mo_hinh_sumo.md`](docs/03_chuong_3_xay_dung_mo_hinh_sumo.md) | **Nhánh XVNT (từ Bến xe Miền Đông cũ):** Tinh chỉnh dòng xe buýt, xe khách, xung đột rẽ trái; viết Chương 3 quy trình dựng mô hình SUMO. |
| **Thành viên 4** | `feature/nhanh4-xvnt-tn` | [`SUMO/route_nhanh4_xvnt_tn.rou.xml`](SUMO/route_nhanh4_xvnt_tn.rou.xml) | [`docs/04_chuong_4_danh_gia_ket_qua_mo_phong.md`](docs/04_chuong_4_danh_gia_ket_qua_mo_phong.md) | **Nhánh XVNT (từ Thị Nghè lên):** Tinh chỉnh xe đi thẳng, rẽ phải Q1, rẽ trái; viết Chương 4 đánh giá các chỉ số từ CSV và biểu đồ. |

---

## 🛠️ HƯỚNG DẪN DÀNH CHO 4 THÀNH VIÊN VÀO LÀM VIỆC (3 BƯỚC)

### Bước 1: Clone dự án về máy tính cá nhân
Mở terminal (Git Bash hoặc VS Code) và gõ:
```bash
git clone https://github.com/tn172406-hash/sumo-traffic-congestion-simulation.git
cd sumo-traffic-congestion-simulation
```

### Bước 2: Tạo nhánh riêng theo đúng tên của mình
Chọn câu lệnh tương ứng với bạn:
* **Thành viên 1:** `git checkout -b feature/nhanh1-dbp-in`
* **Thành viên 2:** `git checkout -b feature/nhanh2-dbp-out`
* **Thành viên 3:** `git checkout -b feature/nhanh3-xvnt-bx`
* **Thành viên 4:** `git checkout -b feature/nhanh4-xvnt-tn`

### Bước 3: Chỉnh sửa nội dung & Commit đẩy lên GitHub
Sau khi chỉnh sửa xong file SUMO của mình và viết nội dung vào file markdown trong thư mục `docs/`:
```bash
# 1. Kiểm tra các file đã thay đổi
git status

# 2. Thêm file vào vùng chờ commit
git add .

# 3. Commit ghi rõ họ tên/nhiệm vụ
git commit -m "feat: Cap nhat luu luong va noi dung bao cao cua [Ten_Cua_Ban]"

# 4. Đẩy nhánh lên GitHub
# (Thay tên nhánh của bạn vào cuối lệnh)
git push origin <TEN_NHANH_CUA_BAN>
```
*Sau khi push xong, bạn vào trang web GitHub của dự án và nhấn **"Compare & pull request"** để Nhóm trưởng duyệt và gộp vào nhánh chính.*

---

## 🚦 HƯỚNG DẪN CHẠY MÔ PHỎNG SUMO VÀ XUẤT SỐ LIỆU

Nhóm trưởng đã cài đặt sẵn hệ thống chạy tự động cho **CẢ 2 HỆ THỐNG BẢN ĐỒ** trong thư mục `SUMO/`:

### 1. Hệ thống Bản đồ Thực tế (OpenStreetMap có nhà cửa HUTECH, cây xanh, cầu vượt thật):
* **Xem trực quan 3 kịch bản trên SUMO-GUI:**
  - Nhấp đúp chuột vào `SUMO/XEM_THAT_KB1_THAP.bat`: Xem bản đồ thật kịch bản Thấp điểm (50%).
  - Nhấp đúp chuột vào `SUMO/XEM_THAT_KB2_TRUNGBINH.bat`: Xem bản đồ thật kịch bản Trung bình (100%).
  - Nhấp đúp chuột vào `SUMO/XEM_THAT_KB3_CAODIEM.bat`: Xem bản đồ thật kịch bản Cao điểm (175% - ùn tắc thực tế).
* **Chạy ngầm xuất số liệu bản đồ thật:** Nhấp đúp vào `SUMO/CHAY_THAT_3_KICH_BAN.bat`.

### 2. Hệ thống Bản đồ Phân luồng Chuẩn hóa (Dùng để kiểm soát 4 nhánh của 4 thành viên):
* **Xem trực quan 3 kịch bản:** Mở `XEM_KICHBAN_1_THAP.bat`, `XEM_KICHBAN_2_TRUNGBINH.bat`, `XEM_KICHBAN_3_CAODIEM.bat`.
* **Chạy tự động và xuất biểu đồ:** Mở `SUMO/CHAY_TAT_CA_KICH_BAN.bat` (Kết quả lưu tại `Bao_Cao_Tong_Hop_3_Kich_Ban.csv` và 2 ảnh biểu đồ PNG).

---

## 📂 CẤU TRÚC THƯ MỤC DỰ ÁN
```
├── docs/                                  # Thư mục chứa bài viết từng chương cho 4 thành viên
│   ├── 01_mo_dau_va_chuong_1_tong_quan.md # Thành viên 1
│   ├── 02_chuong_2_khao_sat_hien_trang.md # Thành viên 2
│   ├── 03_chuong_3_xay_dung_mo_hinh_sumo.md # Thành viên 3
│   └── 04_chuong_4_danh_gia_ket_qua_mo_phong.md # Thành viên 4
├── images/                                # Thư mục chứa ảnh chụp minh chứng, sơ đồ nút giao
├── SUMO/                                  # Thư mục mã nguồn và dữ liệu mô phỏng SUMO
│   ├── route_nhanh1_dbp_in.rou.xml        # Nhánh 1 (TV1)
│   ├── route_nhanh2_dbp_out.rou.xml       # Nhánh 2 (TV2)
│   ├── route_nhanh3_xvnt_bx.rou.xml       # Nhánh 3 (TV3)
│   ├── route_nhanh4_xvnt_tn.rou.xml       # Nhánh 4 (TV4)
│   ├── hangxanh_kb1_thap.sumocfg          # Kịch bản 1 (50%)
│   ├── hangxanh_kb2_trungbinh.sumocfg     # Kịch bản 2 (100%)
│   ├── hangxanh_kb3_caodiem.sumocfg       # Kịch bản 3 (175%)
│   ├── tong_hop_va_ve_bieu_do.py          # Script phân tích số liệu & vẽ đồ thị
│   ├── Bao_Cao_Tong_Hop_3_Kich_Ban.csv    # Bảng số liệu tổng hợp cho bài luận
│   ├── bieu_do_1_thoi_gian_cho.png        # Biểu đồ thời gian chờ theo loại xe
│   └── bieu_do_2_van_toc_va_un_tac.png    # Biểu đồ tương quan tốc độ & xe kẹt
├── Dàn ý tiểu luận-Minh Tuan.docx        # Đề cương chi tiết được duyệt
├── HUONG_DAN_DAY_GITHUB.md                # Tài liệu chi tiết hướng dẫn Git và PR
└── README.md                              # Giới thiệu và phân công nhóm
```
