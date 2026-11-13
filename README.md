# MÔ PHỎNG VÀ ĐÁNH GIÁ ÙN TẮC GIAO THÔNG TẠI NÚT GIAO HÀNG XANH BẰNG SUMO
> **Hệ thống Giao thông Thông minh (ITS) - Đề tài tiểu luận nhóm**  
> Địa điểm nghiên cứu: **Nút giao Hàng Xanh, Quận Bình Thạnh, TP. Hồ Chí Minh**  
> Dữ liệu mô phỏng: **Bản đồ thực tế OpenStreetMap (OSM) tích hợp cảnh quan 3D tòa nhà HUTECH**  
> Công cụ mô phỏng vi mô: **Eclipse SUMO (Simulation of Urban MObility)**

---

## 📌 GIỚI THIỆU DỰ ÁN
Dự án tập trung xây dựng mô hình mô phỏng vi mô nút giao Hàng Xanh – một trong những cửa ngõ giao thông huyết mạch và điểm nóng ùn tắc phức tạp nhất TP.HCM. Mô hình tích hợp:
- **Bản đồ thực tế OpenStreetMap:** Tái hiện 100% hình học thực tế, cầu vượt thép trực thông Điện Biên Phủ, nút giao cắt mức bên dưới và các công trình xung quanh (ĐH HUTECH, các tòa nhà, công viên).
- **Đặc tính dòng xe hỗn hợp đô thị Việt Nam:** Xe máy (chiếm đa số >80%, mô hình lách làn `lateral-resolution="0.8"`), Ô tô con, Xe buýt.
- **Đánh giá 3 kịch bản lưu lượng:**
  * **Kịch bản 1 (Thấp điểm - 50%):** Giao thông thông thoáng giờ thấp điểm.
  * **Kịch bản 2 (Trung bình - 100%):** Lưu lượng tiệm cận năng lực thông hành thiết kế.
  * **Kịch bản 3 (Cao điểm - 175%):** Áp lực giao thông giờ cao điểm, xuất hiện ùn tắc và hàng xe chờ kéo dài.

---

## 👥 PHÂN CÔNG NHIỆM VỤ THÀNH VIÊN & NHÁNH GIT

Mỗi thành viên làm việc trên một **nhánh Git (Branch)** độc lập, phụ trách **1 nhánh đường** và **1 chương trong báo cáo tiểu luận**:

| Thành viên | Tên Branch Git | File bài viết Markdown | Trách nhiệm chính trong đề tài |
|:---|:---|:---|:---|
| **Nhóm trưởng** | `main` | `README.md`, `HUONG_DAN_DAY_GITHUB.md` | Quản lý khung kiến trúc, hệ thống chạy 3 kịch bản bản đồ thật, script trích xuất số liệu và vẽ biểu đồ. |
| **Thành viên 1** | `feature/nhanh1-dbp-in` | [`docs/01_mo_dau_va_chuong_1_tong_quan.md`](docs/01_mo_dau_va_chuong_1_tong_quan.md) | **Nhánh ĐBP vào (Cầu Sài Gòn -> Q1):** Viết Phần Mở đầu, Chương 1 (Tổng quan ùn tắc, dòng xe hỗn hợp, phần mềm SUMO) và Phần Kết luận. |
| **Thành viên 2** | `feature/nhanh2-dbp-out` | [`docs/02_chuong_2_khao_sat_hien_trang.md`](docs/02_chuong_2_khao_sat_hien_trang.md) | **Nhánh ĐBP ra (Q1 -> Cầu Sài Gòn):** Viết Chương 2 (Hiện trạng hình học nút giao Hàng Xanh, phân làn, cầu vượt, chu kỳ đèn tín hiệu 90s). |
| **Thành viên 3** | `feature/nhanh3-xvnt-bx` | [`docs/03_chuong_3_xay_dung_mo_hinh_sumo.md`](docs/03_chuong_3_xay_dung_mo_hinh_sumo.md) | **Nhánh XVNT (từ Bến xe Miền Đông cũ):** Viết Chương 3 (Quy trình dựng mô hình SUMO từ bản đồ thật OSM qua NETCONVERT, NETEDIT, vType xe máy lách làn, thiết lập 3 kịch bản). |
| **Thành viên 4** | `feature/nhanh4-xvnt-tn` | [`docs/04_chuong_4_danh_gia_ket_qua_mo_phong.md`](docs/04_chuong_4_danh_gia_ket_qua_mo_phong.md) | **Nhánh XVNT (từ Thị Nghè lên):** Viết Chương 4 (Đánh giá các chỉ số vận tốc, thời gian chờ theo loại xe, xác định ngưỡng lưu lượng tới hạn gây ùn tắc từ CSV và biểu đồ). |

---

## 🛠️ HƯỚNG DẪN DÀNH CHO 4 THÀNH VIÊN VÀO LÀM VIỆC (3 BƯỚC)

### Bước 1: Clone dự án về máy tính
Mở terminal (Git Bash hoặc VS Code) và gõ:
```bash
git clone https://github.com/tn172406-hash/sumo-traffic-congestion-simulation.git
cd sumo-traffic-congestion-simulation
```

### Bước 2: Tạo nhánh riêng của mình
* **Thành viên 1:** `git checkout -b feature/nhanh1-dbp-in`
* **Thành viên 2:** `git checkout -b feature/nhanh2-dbp-out`
* **Thành viên 3:** `git checkout -b feature/nhanh3-xvnt-bx`
* **Thành viên 4:** `git checkout -b feature/nhanh4-xvnt-tn`

### Bước 3: Soạn thảo bài viết & Commit đẩy lên GitHub
Sau khi viết xong nội dung vào file markdown tương ứng trong thư mục `docs/`:
```bash
git add docs/
git commit -m "feat: Hoan thien noi dung bao cao cua [Ten_Cua_Ban]"
git push origin <TEN_NHANH_CUA_BAN>
```
*Sau khi push xong, vào trang GitHub của dự án và nhấn **"Compare & pull request"** để Nhóm trưởng duyệt và gộp vào nhánh `main`.*

---

## 🚦 HƯỚNG DẪN CHẠY MÔ PHỎNG SUMO BẢN ĐỒ THỰC TẾ

1. **Quan sát trực quan giao diện 2D/3D (SUMO-GUI):**
   * Nhấp đúp vào `SUMO/XEM_THAT_KB1_THAP.bat`: Xem bản đồ thật Kịch bản 1 (50%).
   * Nhấp đúp vào `SUMO/XEM_THAT_KB2_TRUNGBINH.bat`: Xem bản đồ thật Kịch bản 2 (100%).
   * Nhấp đúp vào `SUMO/XEM_THAT_KB3_CAODIEM.bat`: Xem bản đồ thật Kịch bản 3 (175% - ùn tắc thực tế).

2. **Chạy ngầm toàn bộ và tự động xuất số liệu, biểu đồ:**
   * Nhấp đúp vào `SUMO/CHAY_THAT_3_KICH_BAN.bat`.
   * Kết quả tự động lưu tại:
     * Bảng số liệu: `SUMO/Bao_Cao_Tong_Hop_3_Kich_Ban.csv`
     * Biểu đồ thời gian chờ theo loại xe: `SUMO/bieu_do_1_thoi_gian_cho.png`
     * Biểu đồ tương quan tốc độ & ùn tắc: `SUMO/bieu_do_2_van_toc_va_un_tac.png`

---

## 📂 CẤU TRÚC THƯ MỤC DỰ ÁN
```
├── docs/                                  # Bài viết từng chương cho 4 thành viên
│   ├── 01_mo_dau_va_chuong_1_tong_quan.md # Thành viên 1
│   ├── 02_chuong_2_khao_sat_hien_trang.md # Thành viên 2
│   ├── 03_chuong_3_xay_dung_mo_hinh_sumo.md # Thành viên 3
│   └── 04_chuong_4_danh_gia_ket_qua_mo_phong.md # Thành viên 4
├── images/                                # Thư mục chứa ảnh minh chứng, sơ đồ nút giao
├── SUMO/                                  # Thư mục mã nguồn và dữ liệu mô phỏng SUMO
│   ├── hangxanh_real.net.xml              # Bản đồ mạng đường thực tế OpenStreetMap
│   ├── hangxanh_buildings.poly.xml        # Cảnh quan nhà cửa HUTECH, công viên
│   ├── hangxanh_real.rou.xml              # Lộ trình dòng phương tiện thực tế
│   ├── hangxanh.vtypes.xml                # Khai báo thông số xe máy lách làn, ô tô, buýt
│   ├── hangxanh.view.xml                  # Cấu hình góc nhìn trực quan
│   ├── hangxanh_real_kb1_thap.sumocfg     # Kịch bản 1 Thấp điểm (50%)
│   ├── hangxanh_real_kb2_trungbinh.sumocfg# Kịch bản 2 Trung bình (100%)
│   ├── hangxanh_real_kb3_caodiem.sumocfg  # Kịch bản 3 Cao điểm (175%)
│   ├── XEM_THAT_KB1_THAP.bat              # Mở SUMO-GUI Kịch bản 1
│   ├── XEM_THAT_KB2_TRUNGBINH.bat         # Mở SUMO-GUI Kịch bản 2
│   ├── XEM_THAT_KB3_CAODIEM.bat           # Mở SUMO-GUI Kịch bản 3
│   ├── CHAY_THAT_3_KICH_BAN.bat           # Chạy ngầm 3 kịch bản & tự động xuất biểu đồ
│   ├── tong_hop_va_ve_bieu_do.py          # Script phân tích & vẽ biểu đồ tự động
│   ├── Bao_Cao_Tong_Hop_3_Kich_Ban.csv    # Bảng số liệu tổng hợp sạch
│   ├── bieu_do_1_thoi_gian_cho.png        # Biểu đồ thời gian chờ theo loại xe
│   ├── bieu_do_2_van_toc_va_un_tac.png    # Biểu đồ tốc độ & số xe kẹt
│   ├── output_real/                       # Dữ liệu xuất chi tiết từ mô phỏng
│   └── archive_du_phong/                  # Thư mục lưu trữ bản đồ vẽ tay và file cũ để dự phòng
├── Dàn ý tiểu luận-Minh Tuan.docx        # Đề cương chi tiết được duyệt
├── HUONG_DAN_DAY_GITHUB.md                # Tài liệu chi tiết hướng dẫn Git và PR
└── README.md                              # Giới thiệu và phân công nhóm
```
