# HƯỚNG DẪN QUẢN LÝ GITHUB & PHÂN CHIA COMMIT CHO 4 THÀNH VIÊN
================================================================================

Tài liệu này giúp Nhóm trưởng và 4 thành viên có đầy đủ MINH CHỨNG ĐÓNG GÓP (Git Commits, Branches, Pull Requests) trên GitHub để nộp cho Giảng viên chấm điểm cá nhân.

--------------------------------------------------------------------------------
BƯỚC 1: KHỞI TẠO VÀ ĐẨY BỘ CODE KHUNG LÊN GITHUB (NHÓM TRƯỞNG LÀM)
--------------------------------------------------------------------------------
Nhóm trưởng mở terminal (PowerShell / Git Bash) tại thư mục `C:\Users\ACER\Desktop\ITS` và chạy:

```bash
cd "C:\Users\ACER\Desktop\ITS"
git init
git add .
git commit -m "feat(core): Khoi tao he thong mo phong SUMO nut giao Hang Xanh va khung tai lieu"
git branch -M main
# Thay URL_GITHUB_CUA_NHOM bang link repo GitHub tren web (vi du: https://github.com/username/ITS_HangXanh.git)
git remote add origin URL_GITHUB_CUA_NHOM
git push -u origin main
```

--------------------------------------------------------------------------------
BƯỚC 2: PHÂN CHIA NHIỆM VỤ COMMIT ĐỘC LẬP CHO 4 THÀNH VIÊN
--------------------------------------------------------------------------------
(Mỗi thành viên clone repo về, tạo branch riêng của mình, chỉnh sửa file và push lên để lấy lịch sử đóng góp)

### 👤 THÀNH VIÊN 1:
* **Tên Branch:** `feature/nhanh1-dbp-in`
* **File phụ trách chỉnh sửa & commit:**
  1. `SUMO/route_nhanh1_dbp_in.rou.xml` (tinh chỉnh lưu lượng xe nhánh Điện Biên Phủ vào).
  2. `docs/01_mo_dau_va_chuong_1_tong_quan.md` (soạn thảo Mở đầu + Chương 1 + Kết luận).
  3. Thêm ảnh chụp màn hình nhánh 1 vào `images/nhanh1_csg_q1.png`.
* **Câu lệnh Git thực hiện:**
  ```bash
  git checkout -b feature/nhanh1-dbp-in
  # (Sửa các file trên xong thi chay lenh sau)
  git add SUMO/route_nhanh1_dbp_in.rou.xml docs/01_mo_dau_va_chuong_1_tong_quan.md images/
  git commit -m "feat(tv1): Tinh chinh luu luong nhanh 1 DBP vao va hoan thien Chuong 1"
  git push origin feature/nhanh1-dbp-in
  ```

---

### 👤 THÀNH VIÊN 2:
* **Tên Branch:** `feature/nhanh2-dbp-out`
* **File phụ trách chỉnh sửa & commit:**
  1. `SUMO/route_nhanh2_dbp_out.rou.xml` (tinh chỉnh lưu lượng xe nhánh Điện Biên Phủ ra).
  2. `docs/02_chuong_2_khao_sat_hien_trang.md` (soạn thảo Chương 2 khảo sát hiện trạng, pha đèn).
  3. Thêm ảnh chụp Google Maps hoặc mặt cắt ngang nút giao vào `images/hien_trang_mat_cat.png`.
* **Câu lệnh Git thực hiện:**
  ```bash
  git checkout -b feature/nhanh2-dbp-out
  git add SUMO/route_nhanh2_dbp_out.rou.xml docs/02_chuong_2_khao_sat_hien_trang.md images/
  git commit -m "feat(tv2): Cau hinh nhanh 2 DBP ra va hoan thien Chuong 2 khao sat"
  git push origin feature/nhanh2-dbp-out
  ```

---

### 👤 THÀNH VIÊN 3:
* **Tên Branch:** `feature/nhanh3-xvnt-bx`
* **File phụ trách chỉnh sửa & commit:**
  1. `SUMO/route_nhanh3_xvnt_bx.rou.xml` (tinh chỉnh lưu lượng xe buýt/khách nhánh Bến xe dồn về).
  2. `docs/03_chuong_3_xay_dung_mo_hinh_sumo.md` (soạn thảo Chương 3 dựng mạng lưới SUMO).
  3. Thêm ảnh chụp NETEDIT hoặc cấu hình mạng vào `images/netedit_hangxanh.png`.
* **Câu lệnh Git thực hiện:**
  ```bash
  git checkout -b feature/nhanh3-xvnt-bx
  git add SUMO/route_nhanh3_xvnt_bx.rou.xml docs/03_chuong_3_xay_dung_mo_hinh_sumo.md images/
  git commit -m "feat(tv3): Tinh chinh nhanh 3 XVNT Ben xe va hoan thien Chuong 3 mo hinh"
  git push origin feature/nhanh3-xvnt-bx
  ```

---

### 👤 THÀNH VIÊN 4:
* **Tên Branch:** `feature/nhanh4-xvnt-tn`
* **File phụ trách chỉnh sửa & commit:**
  1. `SUMO/route_nhanh4_xvnt_tn.rou.xml` (tinh chỉnh lưu lượng nhánh Thị Nghè lên nút giao).
  2. `docs/04_chuong_4_danh_gia_ket_qua_mo_phong.md` (soạn thảo Chương 4 phân tích kết quả).
  3. Chèn 2 biểu đồ (`bieu_do_1_thoi_gian_cho.png`, `bieu_do_2_van_toc_va_un_tac.png`) vào báo cáo.
* **Câu lệnh Git thực hiện:**
  ```bash
  git checkout -b feature/nhanh4-xvnt-tn
  git add SUMO/route_nhanh4_xvnt_tn.rou.xml docs/04_chuong_4_danh_gia_ket_qua_mo_phong.md
  git commit -m "feat(tv4): Cau hinh nhanh 4 XVNT Thi Nghe va hoan thien Chuong 4 ket qua"
  git push origin feature/nhanh4-xvnt-tn
  ```

--------------------------------------------------------------------------------
BƯỚC 3: MERGE PULL REQUEST TRÊN GITHUB (LÀM ĐẸP LỊCH SỬ DỰ ÁN)
--------------------------------------------------------------------------------
1. Sau khi cả 4 thành viên push branch của mình lên GitHub, từng người nhấn nút **Create Pull Request** (PR).
2. Nhóm trưởng vào tab **Pull Requests** trên GitHub, review và nhấn **Merge Pull Request** vào nhánh `main`.
3. Khi giảng viên bấm vào mục **Insights -> Contributors** hoặc **Network Graph** trên GitHub sẽ thấy:
   - Cả 5 thành viên (Nhóm trưởng + 4 thành viên) đều có commits, có branches và pull requests rõ ràng.
   - Không bị trùng lặp file gây merge conflict.
