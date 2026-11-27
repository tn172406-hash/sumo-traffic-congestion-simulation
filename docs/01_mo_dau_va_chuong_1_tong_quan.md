# PHẦN MỞ ĐẦU & CHƯƠNG 1: TỔNG QUAN VỀ ÙN TẮC GIAO THÔNG VÀ MÔ PHỎNG SUMO

**Người thực hiện:** Thành viên 1  
**Phụ trách kỹ thuật SUMO:** `SUMO/route_nhanh1_dbp_in.rou.xml` (Nhánh Điện Biên Phủ vào trung tâm Q1)

---

## PHẦN MỞ ĐẦU

### 1. Lý do chọn đề tài

Nói đến giao thông thông minh (ITS), người ta thường nghĩ ngay đến camera, cảm biến hay trung tâm điều khiển đèn tín hiệu. Nhưng trước khi đầu tư vào bất kỳ công nghệ nào, người quản lý cần trả lời được một câu hỏi rất cơ bản: nút giao này đang quá tải đến mức nào, và nếu lưu lượng tăng thêm thì chuyện gì xảy ra? Ngoài hiện trường, câu hỏi đó khó trả lời, vì không ai có thể cho đổ thêm 75% lượng xe vào một nút giao đang vận hành chỉ để xem nó kẹt ra sao. Mô phỏng vi mô là cách làm thí nghiệm đó trên máy tính, và đây cũng là lý do nhóm chọn hướng tiếp cận này.

Địa điểm nhóm chọn là nút giao Hàng Xanh, nơi đường Điện Biên Phủ cắt đường Xô Viết Nghệ Tĩnh trong khu vực Bình Thạnh (trước đây là quận Bình Thạnh), TP. Hồ Chí Minh. Đây là cửa ngõ phía Đông Bắc của thành phố: dòng xe từ cầu Sài Gòn, từ hướng Thủ Đức, Bình Dương, Đồng Nai đổ về trung tâm đều phải đi qua đây, và ngược lại. Xung quanh nút giao là khu dân cư đông đúc, nhiều trường đại học (trong đó có HUTECH, cũng là nơi nhóm học tập), tuyến xe buýt và khu vực Bến xe Miền Đông cũ. Nhiều loại nhu cầu đi lại khác nhau dồn vào cùng một điểm, nên nút giao này rất hợp để làm đối tượng nghiên cứu.

Chính quyền thành phố đã can thiệp bằng hạ tầng từ lâu. Cầu vượt thép Hàng Xanh khởi công ngày 10/10/2012 với tổng vốn 183 tỷ đồng từ ngân sách thành phố, và được khánh thành cùng cầu vượt thép ngã tư Thủ Đức, hai cầu vượt thép đầu tiên của TP.HCM [1]. Thế nhưng tình trạng ùn ứ ở đây chưa bao giờ biến mất hẳn. Báo chí ghi nhận ùn ứ kéo dài, có lúc hàng trăm xe đứng chờ trong tối Giáng sinh 24/12/2021 [2]. Một đề xuất khác của cơ quan quản lý nhắm vào việc xe buýt dừng đậu trên đoạn đường Điện Biên Phủ từ đường D2 đến cầu vượt thép, nơi lòng đường hẹp gây ùn ứ cục bộ [3]. Cần phân biệt: sự kiện Giáng sinh là một ngày đặc biệt, còn việc xe buýt dừng đậu là vấn đề tổ chức diễn ra thường xuyên. Hai chuyện này không cùng bản chất, và mô hình của nhóm tập trung vào loại thứ hai (ùn tắc do nhu cầu và tổ chức nút giao) chứ không mô phỏng sự kiện bất thường.

Cũng nên thận trọng với những con số đẹp. Một bài báo trích dẫn cơ quan quản lý cho rằng tại các nút như Hàng Xanh hay Thủ Đức, cầu vượt thép giúp giảm kẹt xe khoảng 70–80% so với trước [4]. Con số này khó kiểm chứng độc lập, và một bài báo khác lại chỉ ra rằng ở một số nút có cầu vượt, bản thân nút giao có đỡ hơn nhưng khu vực lân cận trở nên phức tạp hơn vì các công trình không đồng bộ [5]. Nói cách khác, "có cầu vượt" chưa đồng nghĩa với "hết kẹt", và ta cần số liệu của chính mình thay vì chỉ trích lại nhận định của người khác. Đó là khoảng trống mà đề tài muốn lấp một phần.

Về mặt môn học, đề tài nằm đúng nội dung của Hệ thống giao thông thông minh: mô hình hóa dòng xe, đo lường hiệu quả vận hành bằng các chỉ số định lượng, và dùng kết quả đó làm cơ sở cho các biện pháp điều khiển, tổ chức giao thông. Công cụ SUMO phù hợp vì mã nguồn mở, nhập được bản đồ thật từ OpenStreetMap, và có giao diện lập trình TraCI để sau này có thể thử nghiệm điều khiển đèn thích ứng.

### 2. Mục tiêu nghiên cứu

Mục tiêu tổng quát là xây dựng và khai thác một mô hình mô phỏng vi mô của nút giao Hàng Xanh để đánh giá mức độ ùn tắc theo lưu lượng. Cụ thể:

- Mô phỏng vi mô hoạt động của dòng giao thông hỗn hợp tại nút giao Hàng Xanh, trong đó xe máy chiếm đa số và có hành vi lách làn đặc trưng của đô thị Việt Nam.
- Đánh giá tác động của các mức lưu lượng phương tiện khác nhau đến mức độ ùn tắc, thông qua ba kịch bản: thấp điểm (50% lưu lượng cơ sở), trung bình (100%) và cao điểm (175%).
- Xác định ngưỡng quá tải và đề xuất giải pháp tổ chức giao thông.

Để mục tiêu không bị chung chung, nhóm đặt ra ba câu hỏi nghiên cứu cần trả lời bằng số liệu: (a) từ mức lưu lượng nào các chỉ số vận hành (tốc độ, thời gian chờ) xấu đi đột ngột chứ không còn tăng từ từ; (b) loại phương tiện nào chịu thiệt hại lớn nhất về thời gian chờ khi ùn tắc xuất hiện; (c) trong ba kịch bản, kịch bản nào cho thấy nút giao đã vượt năng lực thông hành.

### 3. Đối tượng và phạm vi nghiên cứu

- **Đối tượng:** Dòng phương tiện hỗn hợp (xe máy, ô tô, xe buýt) và tổ chức giao thông tại nút giao Hàng Xanh.
- **Phạm vi:** Không gian nút giao cắt mức và cầu vượt thép Hàng Xanh; thời gian mô phỏng 1 giờ cao điểm (3.600 giây).

Về giới hạn, cần nói thẳng ngay từ đầu. Mô hình dựng từ dữ liệu OpenStreetMap nên hình học khá sát thực tế, nhưng lưu lượng đầu vào là số liệu nhóm thiết lập cho ba kịch bản chứ không phải kết quả đếm xe thực địa nhiều ngày liên tục. Hành vi xe máy trong SUMO là một sự xấp xỉ, không thể tái hiện hoàn toàn mọi tình huống ngoài đường. Vì vậy, kết quả của đề tài đáng tin nhất khi được dùng để **so sánh tương đối giữa các kịch bản** và chỉ ra xu hướng, chứ không nên được đọc như dự báo chính xác từng giây hay từng mét hàng xe chờ.

<!-- Ghi chú cho nhóm: nếu nhóm đã có số đếm xe thực tế để hiệu chuẩn lưu lượng thì sửa đoạn trên cho khớp, nêu rõ nguồn số đếm và ngày giờ đếm. -->

---

## CHƯƠNG 1: TỔNG QUAN VỀ ÙN TẮC GIAO THÔNG VÀ MÔ PHỎNG SUMO

### 1.1. Khái niệm và nguyên nhân gây ùn tắc giao thông tại nút giao đô thị

#### 1.1.1. Định nghĩa ùn tắc và đặc điểm dòng xe hỗn hợp đô thị

Ở nghĩa đơn giản nhất, ùn tắc xảy ra khi nhu cầu đi lại trên một đoạn đường hay nút giao vượt quá khả năng phục vụ của nó, khiến phương tiện phải giảm tốc, dừng và xếp hàng. Cái khó là "khả năng phục vụ" không phải hằng số: nó thay đổi theo thời tiết, sự cố, cách bố trí làn, pha đèn và cả hành vi của người lái. Cục Đường cao tốc Liên bang Mỹ (FHWA) vì thế phân loại ùn tắc theo bảy nguồn gốc: điểm nghẽn vật lý về hình học, dao động bình thường của lưu lượng, sự cố giao thông, khu vực thi công, thời tiết, sự kiện đặc biệt và thiết bị điều khiển giao thông chưa hợp lý [6]. Có thể gộp lại thành hai nhóm lớn: ùn tắc **thường xuyên** (lặp lại theo giờ, do nhu cầu vượt năng lực) và ùn tắc **không thường xuyên** (do sự cố, sự kiện). Đề tài này nghiên cứu nhóm thứ nhất.

Điểm khác biệt lớn nhất khi áp dụng lý thuyết giao thông vào Việt Nam là thành phần dòng xe. Phần lớn giáo trình và tiêu chuẩn nước ngoài được xây dựng cho dòng xe chủ yếu là ô tô con đi theo làn. Ở các đô thị lớn của ta, xe máy chiếm tuyệt đại đa số, và theo cách đặt giả thiết của nhóm, tỷ lệ này vượt 80% dòng xe tại nút giao Hàng Xanh. Hành vi của loại xe này khác xe ô tô ở nhiều điểm thực chất:

| Loại xe | Hành vi đặc trưng | Hệ quả với mô hình |
|---|---|---|
| Xe máy | Kích thước nhỏ, gia tốc tốt, không bám làn cố định, len vào khe hở giữa các xe lớn, đứng chờ đèn đỏ thành đám rộng thay vì hàng một | Cần mô hình có chuyển động ngang liên tục (sublane); không thể gán cho mỗi xe một làn rời rạc |
| Ô tô con | Chiếm bề rộng gần cả một làn, bám làn tương đối chặt, gia tốc thấp hơn xe máy | Có thể dùng mô hình bám xe cổ điển |
| Xe buýt | Dài, nặng, dừng đón trả khách trên làn xe chạy, che chắn tầm nhìn và chặn dòng xe phía sau | Gây điểm nghẽn cục bộ, nhất là ở đoạn lòng đường hẹp |

Một hệ quả đáng chú ý của việc xe máy tụ đặc ở vạch dừng khi đèn đỏ là hiện tượng "xả" rất nhanh khi đèn chuyển xanh: lượng xe đi qua vạch dừng trong vài giây đầu cao hơn nhiều so với những gì công thức cho dòng ô tô dự đoán. Điều này có hai mặt. Một mặt, nút giao có thể thông hơn ta tưởng. Mặt khác, chính sự dồn ép này làm xung đột rẽ trái và nhập dòng trở nên dày đặc hơn và khó dự báo hơn.

Để so sánh các loại xe trên cùng một thang đo, kỹ thuật giao thông thường quy đổi về "đơn vị xe con tiêu chuẩn" (PCU, passenger car unit). Hệ số quy đổi của xe máy trong các nghiên cứu ở Việt Nam thường nằm quanh khoảng 0,2–0,3 (tùy tiêu chuẩn và mật độ dòng xe), còn xe buýt lớn thường được quy đổi từ 2 trở lên. Nhóm lưu ý rằng các hệ số này không cố định mà thay đổi theo điều kiện giao thông; chính vì sự không ổn định đó mà mô phỏng vi mô, vốn theo dõi từng xe riêng lẻ và không cần quy đổi, có lợi thế rõ so với các phương pháp tính tay theo PCU.

#### 1.1.2. Các nguyên nhân và dạng xung đột tại nút giao cắt mức

Nút giao cắt mức là nơi các dòng xe buộc phải chia sẻ cùng một không gian, và gần như mọi vấn đề của nó quy về số điểm xung đột. Với một nút bốn nhánh không có điều khiển, sách giáo khoa chỉ ra 32 điểm xung đột giữa các xe: 16 điểm cắt nhau, 8 điểm nhập dòng và 8 điểm tách dòng. Đèn tín hiệu không làm các xung đột biến mất mà tách chúng theo thời gian, và đó là lý do pha đèn quan trọng đến vậy.

Ba dạng xung đột cơ bản:

- **Cắt dòng (crossing):** hai dòng xe giao nhau ở một góc lớn, ví dụ xe đi thẳng trên đường này cắt dòng xe đi thẳng trên đường kia. Đây là dạng nguy hiểm nhất và là lý do nhiều nút giao được tách mức, như cầu vượt thép ở Hàng Xanh nhằm lấy dòng xe thẳng trên Điện Biên Phủ ra khỏi mặt bằng nút.
- **Nhập dòng (merging):** hai dòng hợp lại thành một, thường gặp khi xe rẽ phải hòa vào làn chính. Với dòng hỗn hợp, xe máy nhập dòng bằng cách chen vào khe hở rất nhỏ, kéo theo các xe khác phải phanh.
- **Tách dòng (diverging):** một dòng chia thành nhiều hướng. Tự nó ít nguy hiểm, nhưng nếu làn rẽ quá ngắn thì hàng xe chờ rẽ sẽ tràn ngược lại chặn cả làn đi thẳng.

Trong điều kiện giao thông đi bên phải của Việt Nam, **rẽ trái** là xung đột đáng quan tâm nhất, vì xe rẽ trái phải cắt qua dòng xe ngược chiều. Nếu nút giao không có pha riêng cho rẽ trái, hoặc pha này quá ngắn so với lượng xe rẽ, hàng xe chờ rẽ trái sẽ lấn sang các làn khác. Ở Hàng Xanh, các hướng rẽ trái từ Điện Biên Phủ vào Xô Viết Nghệ Tĩnh (hướng đi cầu Bình Triệu) đã được báo chí nhiều lần nhắc đến như một nguồn gây kẹt [7].

Ngoài hình học và pha đèn, còn có các nguyên nhân khác mà mô hình của nhóm cần tính đến: xe buýt dừng đậu trên đoạn đường hẹp [3]; hàng xe chờ phía hạ lưu tràn ngược về nút giao (hiện tượng spillback), đặc biệt ở hướng đi về cầu Bình Triệu; và lưu lượng tăng đột biến theo giờ hoặc theo sự kiện. Nếu chỉ nhìn bản thân nút giao, ta dễ bỏ sót những nguyên nhân nằm ngoài nút nhưng ảnh hưởng ngược trở lại, một điểm mà cũng chính nhận định ở nguồn [5] đã cảnh báo.

### 1.2. Các thông số dòng giao thông và chỉ số đánh giá ùn tắc

#### 1.2.1. Các thông số cơ bản: Lưu lượng, Tốc độ, Mật độ

Ba đại lượng nền tảng của lý thuyết dòng giao thông là lưu lượng $q$ (số xe qua một mặt cắt trong một đơn vị thời gian, thường tính xe/giờ), mật độ $k$ (số xe trên một đơn vị chiều dài đường, xe/km) và tốc độ $v$ (km/h). Chúng gắn với nhau bằng quan hệ cơ bản:

$$q = k \cdot v$$

Ở đây $v$ là tốc độ trung bình theo không gian, tức tốc độ trung bình của các xe đang có mặt trên một đoạn đường tại một thời điểm, chứ không phải tốc độ đo tại một điểm. Hai loại này khác nhau và hay bị nhầm khi xử lý số liệu.

Mô hình đơn giản nhất mô tả mối quan hệ giữa tốc độ và mật độ là mô hình tuyến tính của Greenshields (1935) [8]:

$$v = v_f \left(1 - \frac{k}{k_j}\right) \quad\Rightarrow\quad q = v_f \, k \left(1 - \frac{k}{k_j}\right)$$

với $v_f$ là tốc độ dòng tự do và $k_j$ là mật độ kẹt (xe đứng im). Từ đó lưu lượng cực đại (năng lực thông hành) là $q_{max} = v_f k_j / 4$, đạt khi $k = k_j/2$. Ý nghĩa quan trọng nhất của đồ thị này là: khi mật độ vượt qua điểm giữa, tăng thêm xe vào đường không làm tăng lưu lượng mà làm **giảm** lưu lượng, và dòng xe chuyển sang trạng thái ùn tắc. Cần nói rõ đây là mô hình lý tưởng hóa; dữ liệu thực, nhất là với dòng xe hỗn hợp nhiều xe máy, thường không nằm trên một đường thẳng gọn gàng như vậy. Nhóm dùng mô hình này để hiểu hiện tượng, không để tính toán trực tiếp.

Với nút giao có đèn tín hiệu, năng lực thông hành của một nhánh tính theo công thức:

$$c = s \cdot \frac{g}{C}$$

trong đó $s$ là lưu lượng bão hòa (số xe tối đa qua vạch dừng trong một giờ khi đèn xanh liên tục), $g$ là thời gian xanh hiệu dụng và $C$ là chu kỳ đèn. Tỷ số $x = q / c$ gọi là độ bão hòa. Khi $x$ tiến gần 1, hàng xe chờ bắt đầu tích lũy, và khi $x > 1$, hàng chờ tăng mãi theo thời gian vì mỗi chu kỳ có nhiều xe đến hơn xe được xả. Ba kịch bản 50%, 100% và 175% của nhóm có thể được hiểu là ba vị trí khác nhau của $x$ trên thang này. Giá trị $s$ trong sổ tay Highway Capacity Manual được lấy tham khảo ở mức 1.900 xe con quy đổi mỗi giờ mỗi làn [9], nhưng đây là con số cho dòng ô tô, không phải xe máy. Đây cũng là một lý do để không áp dụng máy móc các con số nước ngoài.

Cuối cùng là bài toán tối ưu chu kỳ đèn: công thức Webster (1958) cho chu kỳ tối ưu theo tiêu chí cực tiểu hóa chậm trễ trung bình [10]:

$$C_o = \frac{1{,}5\,L + 5}{1 - Y}$$

với $L$ là tổng thời gian mất mát trong chu kỳ (giây) và $Y$ là tổng các tỷ số lưu lượng tới hạn của các pha. Công thức này cho thấy khi $Y$ tiến về 1 (nút giao gần quá tải), chu kỳ tối ưu tăng rất nhanh, nghĩa là không có cách "chỉnh đèn" nào cứu được nút giao khi tổng nhu cầu vượt quá năng lực. Hệ quả này sẽ được dùng khi nhóm bàn về ngưỡng quá tải ở các chương sau.

#### 1.2.2. Các chỉ số hiệu quả vận hành: Thời gian chờ (Waiting time), chiều dài hàng xe (Queue length), tốc độ hành trình (Travel speed)

Lưu lượng, mật độ và tốc độ cho biết dòng xe đang ở trạng thái nào, nhưng người quản lý và người đi đường quan tâm đến những chỉ số gần với trải nghiệm hơn. Nhóm dùng ba chỉ số chính.

**Thời gian chờ (waiting time).** Trong SUMO, thời gian chờ của một xe là tổng thời gian xe đó di chuyển với tốc độ không quá 0,1 m/s, tức gần như đứng yên. Chỉ số này đo trực tiếp thời gian bị mất do đèn đỏ và ùn tắc. Cần phân biệt với `timeLoss` (thời gian mất đi so với việc chạy ở tốc độ lý tưởng), chỉ số này bao gồm cả lúc xe đi chậm chứ không chỉ lúc dừng hẳn, nên thường lớn hơn thời gian chờ.

**Chiều dài hàng xe (queue length).** Là khoảng cách từ vạch dừng đến xe cuối hàng đang xếp hàng. Đây là chỉ số quan trọng cho thiết kế, vì hàng chờ dài hơn đoạn đường sẵn có sẽ tràn qua nút giao phía trước, gây khóa nút liên hoàn. Với dòng xe máy đứng thành đám rộng, "chiều dài" hàng xe thấp hơn so với số xe thực sự đang chờ, nên khi đọc chỉ số này cần kèm số xe đứng im (halting) để tránh đánh giá thấp mức độ ùn.

**Tốc độ hành trình (travel speed).** Là quãng đường chia cho thời gian đi hết quãng đường đó, bao gồm cả thời gian dừng. Khác với tốc độ tức thời, chỉ số này phản ánh đúng thời gian người đi đường mất để đi hết một đoạn.

Về đánh giá mức phục vụ, Highway Capacity Manual phân loại nút giao có đèn thành sáu bậc từ A đến F theo thời gian chậm trễ kiểm soát trung bình trên mỗi xe [9]:

| Mức phục vụ | Chậm trễ kiểm soát (giây/xe) | Đánh giá |
|---|---|---|
| A | ≤ 10 | Rất thông thoáng |
| B | > 10 – 20 | Thông thoáng |
| C | > 20 – 35 | Chấp nhận được |
| D | > 35 – 55 | Bắt đầu nặng nề |
| E | > 55 – 80 | Ở ngưỡng năng lực |
| F | > 80 | Quá tải |

Dù có bảng này, nhóm cần thẳng thắn: ngưỡng của HCM được xây dựng cho dòng xe chủ yếu là ô tô và mức chịu đựng chậm trễ của người Mỹ, không có gì đảm bảo nó áp dụng đúng cho người đi xe máy ở TP.HCM. Vì vậy trong các chương sau, bảng này chỉ dùng như một **thước tham chiếu**, không dùng để "chấm điểm" nút giao một cách cứng nhắc.

Cũng có hai cái bẫy khi đọc số liệu từ SUMO mà nhóm cần lưu ý ngay từ đầu. Thứ nhất, nếu phương tiện bị kẹt quá lâu (mặc định khoảng 300 giây), SUMO có thể "dịch chuyển tức thời" xe đó khỏi vị trí tắc để giải phóng mạng lưới; những xe này làm méo thời gian chờ và tốc độ nên số lượng xe bị teleport phải được kiểm tra trong từng kịch bản. Thứ hai, khi mạng đã đầy, xe mới có thể không được đưa vào mô hình đúng giờ, nên thời gian trễ khi xuất phát (`departDelay`) cũng phải được xem xét; một kịch bản cao điểm có thể trông "đỡ hơn thực tế" chỉ vì xe chưa vào được mạng để bị tính thời gian chờ. Hai điểm này sẽ được Thành viên 4 đối chiếu khi phân tích kết quả ở Chương 4.

### 1.3. Tổng quan về công cụ mô phỏng vi mô SUMO

#### 1.3.1. Giới thiệu phần mềm SUMO và nguyên lý mô phỏng vi mô

Mô hình giao thông chia làm ba cấp độ chi tiết. Mô hình **vĩ mô** coi dòng xe như chất lưu liên tục, chỉ quan tâm đến $q$, $k$, $v$ trung bình. Mô hình **trung mô** (mesoscopic) theo dõi từng nhóm xe nhưng bỏ qua tương tác chi tiết. Mô hình **vi mô** theo dõi từng phương tiện riêng lẻ với vị trí, vận tốc và quyết định của nó ở từng bước thời gian. Với nút giao có xe máy lách làn, chỉ mô hình vi mô mới đủ chi tiết, vì hành vi từng xe quyết định kết quả chung.

SUMO (Simulation of Urban MObility) là phần mềm mô phỏng giao thông vi mô, không gian liên tục và thời gian rời rạc (bước thời gian mặc định là 1 giây). Dự án được Trung tâm Hàng không Vũ trụ Đức (DLR) khởi xướng từ năm 2001, là phần mềm mã nguồn mở và hiện nằm trong hệ sinh thái Eclipse với tên Eclipse SUMO [11]. SUMO mô phỏng nhiều phương thức: ô tô, xe buýt, xe máy, xe đạp, người đi bộ và cả tàu điện. So với các công cụ thương mại như VISSIM hay Aimsun, SUMO không có sẵn giao diện thân thiện bằng, nhưng bù lại miễn phí, kiểm soát được từng chi tiết qua tệp cấu hình XML và có thể điều khiển ngay trong lúc chạy qua giao diện TraCI (Traffic Control Interface), thường dùng với Python. Khả năng này khiến SUMO đặc biệt phù hợp cho ITS: có thể viết thuật toán điều khiển đèn thích ứng và thử nó ngay trong mô hình, trước khi nghĩ đến việc đặt ra ngoài hiện trường.

Cũng cần nói đến hạn chế. SUMO được phát triển ban đầu trong bối cảnh giao thông châu Âu, và xe máy trong SUMO là một loại phương tiện đặc biệt được xấp xỉ bằng mô hình chuyển động ngang chứ không phải hành vi được hiệu chuẩn sẵn cho Việt Nam. Do đó các thông số xe (kích thước, gia tốc, khoảng cách tối thiểu, độ ngẫu nhiên của người lái) đều phải được chọn và nêu căn cứ, đây chính là phần việc của Chương 3.

#### 1.3.2. Cấu trúc mạng lưới đường và mô hình chuyển động của phương tiện (Car-following model, Lane-changing model)

**Cấu trúc mạng lưới.** Mạng đường trong SUMO là một đồ thị có hướng, lưu trong tệp `.net.xml`. Các thành phần chính là nút giao (junction), đoạn đường (edge, mỗi hướng một edge), làn (lane, nằm trong edge) và các liên kết (connection) cho biết làn nào được rẽ sang làn nào tại nút giao. Mỗi nút giao có quy tắc nhường đường và, khi có đèn, một chương trình đèn (`tlLogic`) gồm các pha, mỗi pha là một chuỗi ký tự trạng thái cho từng liên kết (xanh, đỏ, vàng) kèm thời lượng. Nhu cầu đi lại (demand) được khai báo riêng trong tệp lộ trình `.rou.xml`: loại xe (vType), lộ trình (route) và lưu lượng (flow). Tách mạng đường khỏi nhu cầu giúp chạy nhiều kịch bản trên cùng một bản đồ, đúng cách nhóm đang làm với ba kịch bản.

**Mô hình bám xe (car-following).** Mô hình này quyết định xe tăng, giảm tốc thế nào theo xe đi trước. Mô hình mặc định của SUMO là mô hình Krauß, do Stefan Krauß đề xuất năm 1998 và được thiết kế để đảm bảo không xảy ra va chạm [12]. Ý tưởng cốt lõi: ở mỗi bước, xe tính một "tốc độ an toàn" sao cho vẫn dừng kịp nếu xe trước phanh gấp, rồi chọn tốc độ nhỏ nhất trong ba giá trị là tốc độ tối đa cho phép, tốc độ có thể đạt được với gia tốc cho phép, và tốc độ an toàn; cuối cùng trừ đi một đại lượng ngẫu nhiên để mô tả sự không hoàn hảo của người lái. Các tham số chính của loại xe (vType) gồm: gia tốc `accel`, giảm tốc `decel`, thời gian phản ứng mong muốn `tau`, khoảng cách tối thiểu `minGap`, độ không hoàn hảo `sigma`, chiều dài và chiều rộng. Với xe con, giá trị mặc định của SUMO có `tau` = 1 giây, `minGap` = 2,5 m và `sigma` = 0,5. Xe máy khác xe con ở hầu hết các tham số này (nhỏ hơn, gia tốc lớn hơn, khoảng cách thu nhỏ hơn), và các giá trị cụ thể mà nhóm chọn nằm trong tệp `hangxanh.vtypes.xml`, được giải thích kỹ ở Chương 3. SUMO cũng cung cấp các mô hình khác như IDM hay Wiedemann nếu cần thay thế.

**Mô hình đổi làn (lane-changing).** Mô hình đổi làn mặc định LC2013 do Jakob Erdmann xây dựng [13] quyết định xe có đổi làn hay không dựa trên bốn động cơ: đi đúng hướng lộ trình (chiến lược), nhường chỗ cho xe khác (hợp tác), muốn đi nhanh hơn (tăng tốc độ) và quay về làn phải. Tuy nhiên, mô hình này vẫn coi mỗi làn là một đơn vị rời rạc. Để mô phỏng xe máy len lỏi giữa các xe, SUMO cung cấp **mô hình sublane** (SL2015): khi người dùng đặt tham số `lateral-resolution` lớn hơn 0, mỗi làn được chia thành các dải ngang nhỏ có độ rộng bằng giá trị đó, và xe có thể đứng ở bất kỳ vị trí ngang nào thay vì chỉ ở giữa làn. Theo tài liệu của nhóm, mô hình dùng `lateral-resolution="0.8"`. Hiểu đơn giản, một làn rộng 3,2 m sẽ được chia thành bốn dải, đủ để vài xe máy đi song song trong một làn, hoặc xe máy vượt xe con ngay trong làn mà không cần sang làn khác. Giá trị này là một lựa chọn cần cân nhắc: đặt nhỏ thì tái hiện chi tiết hơn nhưng chạy chậm hơn, đặt lớn thì chạy nhanh nhưng mất khả năng lách.

#### 1.3.3. Các công cụ hỗ trợ (NETCONVERT, NETEDIT, SUMO-GUI) và định dạng dữ liệu đầu ra (tripinfo, summary, queue)

SUMO là một bộ công cụ chứ không phải một chương trình duy nhất. Những công cụ nhóm sử dụng là:

- **NETCONVERT** chuyển đổi dữ liệu mạng đường từ nhiều định dạng, trong đó có tệp OpenStreetMap, sang định dạng `.net.xml` của SUMO. Nó còn có các tùy chọn tự đoán đèn tín hiệu, hợp nhất nút giao, đoán đường dẫn lên xuống cầu vượt, đơn giản hóa hình học. Chính công cụ này giúp nhóm có bản đồ sát thực tế thay vì vẽ tay.
- **POLYCONVERT** chuyển các đối tượng không phải đường (tòa nhà, công viên) từ OSM thành đa giác để hiển thị, cho ra cảnh quan HUTECH và khu vực xung quanh trong tệp `hangxanh_buildings.poly.xml`.
- **NETEDIT** là trình soạn thảo đồ họa cho mạng đường và nhu cầu, dùng để sửa các chỗ mà dữ liệu OSM tự động dựng chưa đúng (số làn, liên kết rẽ, pha đèn).
- **SUMO-GUI** là bản chạy mô phỏng có giao diện, cho phép quan sát xe chạy, tô màu theo tốc độ hay thời gian chờ, và dừng, chạy từng bước để phân tích. Bản chạy dòng lệnh `sumo` làm cùng việc nhưng không có giao diện, nên nhanh hơn và phù hợp chạy hàng loạt kịch bản.

Điều quan trọng nhất cho việc đánh giá là dữ liệu đầu ra. SUMO có thể ghi nhiều loại tệp, trong đó ba loại sau là cơ sở cho Chương 4:

| Tệp đầu ra | Nội dung chính | Dùng để |
|---|---|---|
| `tripinfo` | Dữ liệu cho **từng xe** khi xe kết thúc hành trình: thời điểm xuất phát, thời gian hành trình, chiều dài quãng đường, thời gian chờ (`waitingTime`), thời gian mất mát (`timeLoss`), độ trễ xuất phát (`departDelay`), loại xe | Tính thời gian chờ, thời gian hành trình **theo loại xe** (xe máy, ô tô, xe buýt) |
| `summary` | Số liệu **tổng hợp toàn mạng theo từng bước thời gian**: số xe đã nạp, đang chạy, đã đến đích, số xe đứng im (`halting`), tốc độ trung bình, thời gian chờ trung bình, số xe bị teleport | Theo dõi diễn biến ùn tắc theo thời gian; kiểm tra teleport |
| `queue` | Chiều dài và thời gian xếp hàng **theo từng làn** ở từng bước thời gian | Đánh giá hàng xe chờ tại các nhánh vào nút giao |

Cần lưu ý một chi tiết dễ nhầm ở tệp `summary`: thuộc tính `waiting` là số xe đang **chờ được đưa vào mạng** (chưa xuất phát được do mạng đã đầy), còn số xe đứng im trên đường là `halting`. Nhầm hai đại lượng này sẽ dẫn đến kết luận sai về mức độ ùn tắc.

Các tệp đầu ra đều là XML, nên được xử lý tiếp bằng Python (đọc dữ liệu bằng thư viện, tổng hợp và vẽ biểu đồ). Quy trình này nhóm đã đóng gói trong `tong_hop_va_ve_bieu_do.py`, tự động xuất bảng tổng hợp `Bao_Cao_Tong_Hop_3_Kich_Ban.csv` và hai biểu đồ phục vụ Chương 4. Ngoài ra, SUMO còn có các thiết bị đo ảo (cảm biến vòng cảm ứng, thiết bị đo hàng chờ theo vùng) có thể đặt tại vị trí cụ thể giống camera hay cảm biến thật; nếu sau này có số đếm thực địa thì có thể dùng chúng để hiệu chuẩn mô hình.

**Tiểu kết Chương 1.** Chương này đã làm rõ ba điều làm nền cho các chương sau. Một là ùn tắc tại nút giao đô thị bắt nguồn từ việc nhu cầu vượt năng lực, và với dòng xe hỗn hợp nhiều xe máy thì các công thức nước ngoài chỉ nên được coi là thước tham chiếu. Hai là có một bộ chỉ số cụ thể (lưu lượng, tốc độ, thời gian chờ, hàng xe chờ) để biến cảm giác "kẹt" thành con số. Ba là SUMO đủ khả năng mô phỏng vi mô dòng xe hỗn hợp nhờ mô hình sublane, nhưng kết quả phải được đọc cùng những giới hạn đã nêu (teleport, độ trễ xuất phát, thông số xe máy). Chương 2 sẽ khảo sát hiện trạng hình học và tổ chức đèn tín hiệu tại nút giao Hàng Xanh.

---

## KẾT LUẬN VÀ KIẾN NGHỊ (VIẾT Ở CUỐI BÀI)

### 1. Kết luận chung

Đề tài xây dựng mô hình mô phỏng vi mô nút giao Hàng Xanh bằng SUMO trên nền bản đồ OpenStreetMap, với dòng xe hỗn hợp trong đó xe máy chiếm đa số và có khả năng lách làn, rồi đánh giá nút giao dưới ba mức lưu lượng: thấp điểm (50%), trung bình (100%) và cao điểm (175%).

Về mặt cơ sở lý thuyết, nhóm đã làm rõ rằng ùn tắc tại nút giao là hệ quả của việc nhu cầu vượt năng lực thông hành, được tăng cường bởi các xung đột cắt dòng, nhập dòng, tách dòng và đặc biệt là xung đột rẽ trái, đồng thời bởi hành vi riêng của xe máy và xe buýt dừng đậu.

Về mặt kết quả mô phỏng, các chỉ số được đo là tốc độ, thời gian chờ theo loại xe và số xe đứng im. Kết quả cho thấy:

- Ở kịch bản thấp điểm (50%), nút giao vận hành **[ĐIỀN: mô tả ngắn + số, ví dụ thời gian chờ trung bình ... giây, tốc độ trung bình ... km/h, theo Chương 4]**.
- Ở kịch bản trung bình (100%), **[ĐIỀN: số liệu + nhận xét]**.
- Ở kịch bản cao điểm (175%), **[ĐIỀN: số liệu + nhận xét: có xuất hiện hàng chờ kéo dài không, loại xe nào chờ lâu nhất]**.
- Ngưỡng lưu lượng tại đó tình trạng ùn tắc bắt đầu xuất hiện rõ rệt là **[ĐIỀN: theo kết luận của Thành viên 4 ở Chương 4]**.

<!-- Ghi chú cho nhóm: các số liệu trên phải lấy từ Bao_Cao_Tong_Hop_3_Kich_Ban.csv và phần phân tích của Chương 4; Thành viên 1 không tự đặt số. Nên thống nhất nội dung này với Thành viên 4 trước khi chốt. -->

Điều đáng nhấn mạnh là những kết luận trên chỉ có giá trị trong phạm vi các giả thiết của mô hình đã nêu ở phần Mở đầu. Chúng cho thấy **xu hướng và mức chênh lệch giữa các kịch bản**, không phải dự báo tuyệt đối.

### 2. Ý nghĩa thực tiễn đối với quản lý giao thông tại nút giao Hàng Xanh

Giá trị thực tiễn đầu tiên của đề tài là một cách làm. Mô hình cho phép thử một thay đổi ngay trên máy tính, ví dụ thêm 75% lưu lượng, đổi thời lượng pha đèn hay dời điểm dừng xe buýt, rồi so sánh trước, sau bằng cùng một bộ chỉ số. Với một nút giao mà mỗi lần can thiệp hạ tầng đều tốn hàng trăm tỷ đồng như cầu vượt thép [1], khả năng sàng lọc phương án trước khi triển khai là có giá trị.

Từ góc nhìn của ITS, nhóm đề xuất một số hướng để kiểm chứng tiếp bằng chính mô hình này, không phải kết luận đã được chứng minh:

- **Điều khiển đèn tín hiệu thích ứng.** Chu kỳ cố định không theo kịp biến động lưu lượng. Mô hình có sẵn giao diện TraCI nên có thể thử một thuật toán điều chỉnh thời gian xanh theo độ dài hàng chờ và so sánh với đèn chu kỳ cố định hiện tại.
- **Tổ chức lại điểm dừng xe buýt** trên đoạn Điện Biên Phủ hẹp mà nguồn [3] đã chỉ ra, như dời vị trí hoặc dồn các tuyến dừng chung, và đo lại thời gian chờ của xe máy phía sau.
- **Xử lý hướng rẽ trái** (pha riêng hoặc điều tiết bằng dải phân cách di động dưới chân cầu vượt, một biện pháp mà cơ quan quản lý đã đề xuất [14]) bằng cách thử các phương án trong cùng mô hình.
- **Cung cấp thông tin giao thông cho người dùng**, vì một phần nhu cầu có thể chuyển sang đường khác nếu họ biết trước hướng nào đang tắc; đây là hướng mở rộng cần có số liệu hành vi, nằm ngoài phạm vi của mô hình hiện tại.

Thành phố cũng đang nghiên cứu cải tạo cả khu vực Hàng Xanh–Bình Triệu, gồm mở rộng đường Xô Viết Nghệ Tĩnh và nút giao Đài Liệt Sĩ [15]. Nếu các dự án này được triển khai, hạ tầng quanh nút sẽ thay đổi, nên mô hình cần cập nhật theo để kết luận không bị lạc hậu.

### 3. Hạn chế và hướng phát triển

Có ba hạn chế cần ghi nhận để người đọc đánh giá đúng kết quả. Thứ nhất, lưu lượng ba kịch bản là số liệu nhóm thiết lập, chưa được hiệu chuẩn bằng số đếm thực địa liên tục; hướng phát triển tự nhiên là đếm xe thực tế (hoặc dùng dữ liệu camera) để hiệu chuẩn lưu lượng và so khớp tốc độ mô phỏng với tốc độ đo thực. Thứ hai, mô hình xe máy là một xấp xỉ, và các thông số của nó (kích thước, khoảng cách, độ ngẫu nhiên) cần kiểm tra độ nhạy: nếu thay đổi các giá trị này mà kết luận đổi theo thì kết luận đó chưa vững. Thứ ba, mô hình chỉ tập trung vào nút giao và các nhánh gần nó, chưa phản ánh đầy đủ ảnh hưởng ngược của hàng chờ ở phía hạ lưu như hướng cầu Bình Triệu. Mở rộng phạm vi sang các nút liền kề và thêm các kịch bản có sự cố hay sự kiện đặc biệt là hướng nghiên cứu tiếp theo.

---

## TÀI LIỆU THAM KHẢO

[1] VietNamNet, "Thông xe 2 cầu vượt thép đầu tiên tại TP.HCM". https://vietnamnet.vn/thong-xe-2-cau-vuot-thep-dau-tien-tai-tphcm-107127.html

[2] Tuổi Trẻ, "Ngã tư Hàng Xanh đông nghẹt tối Giáng sinh, người dân 'lâu rồi mới thấy kẹt xe'", 24/12/2021. https://tuoitre.vn/nga-tu-hang-xanh-dong-nghet-toi-giang-sinh-nguoi-dan-lau-roi-moi-thay-ket-xe-20211224185254529.htm

[3] Báo Thanh tra, "TP.HCM muốn lập điểm trú mưa 2,2 tỷ đồng". https://thanhtra.com.vn/nha-dat-57A4B2310/tp-hcm-muon-lap-diem-tru-mua-2-2-ty-dong-4F790733.html

[4] Pháp Luật TP.HCM, "TP.HCM sắp làm 7 cầu vượt thép". https://plo.vn/tphcm-sap-lam-7-cau-vuot-thep-post910895.html

[5] Báo Đại Đoàn Kết, "Đẩy mạnh chống kẹt xe bằng cầu vượt thép". https://daidoanket.vn/dang-do-chong-ket-xe-bang-cau-vuot-thep-10230483.html

[6] Federal Highway Administration (FHWA), *Traffic Congestion and Reliability: Trends and Advanced Strategies for Congestion Mitigation*, 2005.

[7] Thương hiệu & Công luận, "Phường 26, quận Bình Thạnh (TP.HCM): Trong điểm đen kẹt xe". https://thuonghieucongluan.com.vn/phuo-ng-26-qua-n-bi-nh-tha-nh-tp-hcm-trong-die-m-den-ke-t-xe-a41857.html

[8] B. D. Greenshields, "A study of traffic capacity", *Proceedings of the Highway Research Board*, vol. 14, 1935.

[9] Transportation Research Board, *Highway Capacity Manual*, National Academies.

[10] F. V. Webster, *Traffic Signal Settings*, Road Research Technical Paper No. 39, HMSO, London, 1958.

[11] P. A. Lopez et al., "Microscopic Traffic Simulation using SUMO", *IEEE International Conference on Intelligent Transportation Systems (ITSC)*, 2018. Tài liệu chính thức: https://sumo.dlr.de/docs/

[12] S. Krauß, *Microscopic Modeling of Traffic Flow: Investigation of Collision Free Vehicle Dynamics*, luận án tiến sĩ, Đại học Köln, 1998.

[13] J. Erdmann, "SUMO's Lane-Changing Model", trong *Modeling Mobility with Open Data*, Lecture Notes in Mobility, Springer, 2015.

[14] Báo Lao Động, "Điểm kẹt xe bậc nhất TP.HCM được đề xuất làm đường trên cao, nút giao đa tầng". https://news.laodong.vn/xa-hoi/diem-ket-xe-bac-nhat-tphcm-duoc-de-xuat-lam-duong-tren-cao-nut-giao-da-tang-1691308.ldo

[15] Báo Sài Gòn Giải Phóng, "TPHCM thông xe cầu Bình Triệu 1, kỳ vọng giảm ùn tắc cửa ngõ Đông Bắc". https://www.sggp.org.vn/tphcm-thong-xe-cau-binh-trieu-1-ky-vong-giam-un-tac-cua-ngo-dong-bac-post824973.html
