# CHƯƠNG 4: PHÂN TÍCH VÀ ĐÁNH GIÁ KẾT QUẢ MÔ PHỎNG
**Người thực hiện:** Thành viên 4  
**Phụ trách kỹ thuật SUMO:** `SUMO/route_nhanh4_xvnt_tn.rou.xml` (Nhánh Xô Viết Nghệ Tĩnh từ Thị Nghè)

---

## 4.1. Phân tích diễn biến giao thông tổng thể qua các kịch bản
### 4.1.1. Diễn biến dòng xe tại Kịch bản 1 (Thấp điểm - 50%)
- Trên nhánh XVNT (từ Thị Nghè lên): Dòng phương tiện phân tách làn rõ ràng giữa nhóm đi thẳng lên cầu vượt thép Hàng Xanh và nhóm đi đường gom bên dưới để rẽ trái sang Điện Biên Phủ hoặc rẽ phải sang XVNT (hướng về Bến xe Miền Đông).

- Tại khu vực nút giao: Dòng xe lưu thông thông thoáng trên cả cầu vượt và dưới ngã tư. Hàng xe chờ tại vạch dừng đèn đỏ trên đường gom nhánh XVNT ngắn, giải tỏa hoàn toàn chỉ trong 1 chu kỳ đèn, không xảy ra hiện tượng dồn ứ ngược về phía cầu Thị Nghè.

### 4.1.2. Diễn biến dòng xe tại Kịch bản 2 (Trung bình - 100%)
- Trên nhánh XVNT (từ Thị Nghè lên): Lưu lượng tăng gấp đôi khiến khu vực chuyển làn trước chân cầu vượt bắt đầu xuất hiện xung đột nhẹ. Các phương tiện kích thước lớn (xe buýt, ô tô) chuyển làn từ giữa đường vào đường gom để rẽ trái/rẽ phải làm giảm tốc độ của dòng xe máy đi phía sau.

- Tại khu vực nút giao: Xuất hiện hiện tượng xếp hàng chờ kéo dài tại nhánh Điện Biên Phủ và đường gom nhánh XVNT. Một bộ phận phương tiện dưới ngã tư phải chờ sang chu kỳ đèn thứ 2 mới thoát qua được nút. Riêng dòng xe đi thẳng qua cầu vượt thép vẫn vận hành ổn định, không bị xung đột giao cắt.

### 4.1.3. Diễn biến dòng xe tại Kịch bản 3 (Cao điểm - 175%)
- Trên nhánh XVNT (từ Thị Nghè lên): Hàng xe chờ dưới đường gom vượt quá sức chứa thiết kế của đoạn dẫn trước nút giao, tạo thành nút thắt cổ chai kéo ngược về phía cầu Thị Nghè và che lấp lối lên cầu vượt thép.

- Tại khu vực nút giao: Xung đột rẽ trái dưới ngã tư (đặc biệt là luồng từ XVNT rẽ trái vào Điện Biên Phủ giao cắt với luồng đối diện) kết hợp với hiện tượng khóa nút (gridlock) gây tắc nghẽn kéo dài lan tỏa sang toàn bộ các nhánh tiếp cận.

### 4.1.4. Hình ảnh trực quan hóa tình trạng giao thông trên giao diện SUMO-GUI
*(Chèn ảnh chụp màn hình từ SUMO-GUI: `images/hien_trang_un_tac_gui.png`)*
- Phân tích trực quan: Quan sát trên giao diện SUMO-GUI tại Kịch bản 3 cho thấy mật độ phương tiện tập trung dày đặc (hiển thị bằng dải màu đỏ/vàng liên tục) trên đoạn đường gom nhánh XVNT từ Thị Nghè lên. Các xe buýt có kích thước lớn nằm chắn ngang khu vực chuyển tiếp trước nút giao khiến dòng xe máy phía sau bị dồn nén cục bộ và không thể luồn lách thoát nút.
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
Từ bảng số liệu CSV và Biểu đồ 1, thời gian chờ trung bình cho thấy sự phân hóa rõ rệt giữa các nhóm phương tiện:

- Nhóm xe buýt chịu ảnh hưởng nặng nề nhất: Thời gian chờ của xe buýt tăng liên tục qua cả 3 kịch bản (275,2s → 297,6s → 427,3s). Đáng chú ý, khi chuyển từ mức trung bình (KB2) sang cao điểm (KB3), thời gian chờ xe buýt tăng đột biến thêm 129,7 giây (tương đương mức tăng 43,6%, xấp xỉ ngưỡng tăng đột biến ~55% so với trạng thái lưu thông cơ sở ở KB1). Nguyên nhân là do trên nhánh XVNT từ Thị Nghè lên, xe buýt bắt buộc phải đi đường gom bên dưới để vào trạm dừng hoặc rẽ hướng, đồng thời kích thước lớn khiến xe buýt không thể chuyển làn linh hoạt khi dòng xe bão hòa.

- Nhóm xe máy và ô tô con: Ở Kịch bản 2 và Kịch bản 3, thời gian chờ của xe máy lần lượt là 136,6s và 159,6s (tăng 16,84%); ô tô con là 108,2s và 112,6s (tăng 4,07%). Sở dĩ giá trị trung bình toàn mạng của hai nhóm này thấp hơn xe buýt (và thấp hơn mức tích lũy cục bộ ở KB1) là do một tỷ lệ lớn xe máy và ô tô con đi thẳng qua cầu vượt thép Hàng Xanh, giúp rút ngắn thời gian dừng chờ dưới nút giao. Tuy nhiên, phần phương tiện đi đường gom bên dưới nhánh XVNT vẫn chịu trễ lớn khi lưu lượng đạt 175%.

### 4.2.2. Đánh giá sự suy giảm của tốc độ trung bình (Mean Speed)
*(Chèn biểu đồ: `SUMO/bieu_do_2_van_toc_va_un_tac.png`)*
- Xu hướng suy giảm tuyến tính: Tốc độ trung bình toàn mạng lưới giảm liên tục từ 5,32 km/h (KB1) xuống 4,39 km/h (KB2, giảm 17,48%) và chạm đáy ở mức 3,75 km/h (KB3, giảm tổng cộng 29,51% so với KB1).

- Nguyên nhân kỹ thuật: Vận tốc dưới 4 km/h ở Kịch bản 3 tương đương với tốc độ đi bộ, phản ánh trạng thái dòng xe di chuyển nhích từng đoạn ngắn (stop-and-go). Mật độ phương tiện dừng đỗ tăng cao khiến số xe kẹt lớn nhất (halting vehicles) đạt đỉnh 1.633 xe, triệt tiêu khả năng tăng tốc của dòng xe ngay cả khi tín hiệu đèn chuyển sang pha xanh.
### 4.2.3. Đánh giá độ dài hàng xe chờ và thời gian hành trình trên các nhánh tiếp cận
- Độ dài hàng xe chờ (Queue Length): Trên nhánh XVNT hướng từ Thị Nghè lên, hàng xe chờ tại đường gom tăng tỷ lệ thuận với lưu lượng đầu vào. Ở Kịch bản 3, chiều dài hàng chờ vượt quá chiều dài đoạn đường gom từ chân cầu vượt đến vạch dừng ngã tư, gây tràn hàng chờ ngược lên khu vực phân luồng trước cầu vượt.

- Thời gian hành trình (Travel Time): Thời gian hành trình của các lộ trình rẽ trái/rẽ phải qua đường gom nhánh XVNT tăng gấp 2,5 đến 3 lần so với Kịch bản 1 do phải trải qua nhiều chu kỳ đèn mới thoát khỏi vùng xung đột.
---

## 4.3. Xác định ngưỡng lưu lượng gây ùn tắc tại nút giao Hàng Xanh.
### 4.3.1. Phân tích tương quan giữa mức tăng lưu lượng và mức độ suy giảm dịch vụ
Đối chiếu dữ liệu từ Bao_Cao_Tong_Hop_3_Kich_Ban.csv và hai biểu đồ phân tích, mối tương quan giữa mức tải lưu lượng và chất lượng khai thác tại nút giao Hàng Xanh chia làm 2 giai đoạn rõ rệt:

- Giai đoạn từ 50% lên 100% lưu lượng (KB1 → KB2): Lưu lượng tăng gấp đôi nhưng tốc độ trung bình chỉ giảm 0,93 km/h (từ 5,32 xuống 4,39 km/h) và số xe kẹt tăng thêm 63 xe (+4,15%). Điều này chứng tỏ tại ngưỡng 100% lưu lượng, hạ tầng hiện hữu (cầu vượt thép kết hợp điều khiển đèn tín hiệu dưới nút) vẫn còn khả năng tự điều tiết và giải tỏa dòng xe.

- Giai đoạn từ 100% lên 175% lưu lượng (KB2 → KB3): Khi lưu lượng vượt ngưỡng 100%, hệ thống bước vào trạng thái mất ổn định phi tuyến. Tốc độ trung bình tụt xuống 3,75 km/h, số xe kẹt chạm mốc 1.633 xe, và đặc biệt thời gian chờ của xe buýt tăng vọt từ 297,6s lên 427,3s.

### 4.3.2. Xác định điểm tới hạn dẫn đến ùn tắc kéo dài
Từ kết quả phân tích định lượng và quan sát thực tế dòng xe trên nhánh XVNT (từ Thị Nghè lên), có thể xác định ngưỡng lưu lượng tới hạn của nút giao Hàng Xanh như sau:

- Ngưỡng lưu lượng tới hạn (Critical Demand Threshold): Nằm ngay sau mức tải 100% lưu lượng thiết kế (Kịch bản 2) và bắt đầu kích hoạt tình trạng ùn tắc kéo dài không thể tự giải tỏa khi lưu lượng tiến vào vùng 120% – 130% trở lên (đạt đỉnh ùn tắc nghiêm trọng tại 175% - Kịch bản 3).

Dấu hiệu nhận diện điểm tới hạn trên nhánh XVNT:

- Thời gian chờ trung bình của phương tiện công cộng (xe buýt) vượt ngưỡng 300 giây/xe (5 phút).

- Vận tốc lưu thông trung bình toàn mạng giảm xuống dưới ngưỡng 4,0 km/h.

- Dòng xe chờ tại đường gom nhánh XVNT (từ Thị Nghè lên) lấp đầy đoạn dẫn trước ngã tư, gây cản trở vật lý đối với dòng xe chuyển hướng lên cầu vượt thép Hàng Xanh.