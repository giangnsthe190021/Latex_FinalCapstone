# Hướng dẫn làm slide thuyết trình bài báo IEEE

Cập nhật: 2026-11-09

Bài thuyết trình gồm 20 slide do 1 người trình bày, đi đúng thứ tự các mục của bài báo "Privacy-Preserving Federated Synthetic Data Generation for Intrusion Detection in MQTT-Based IoT Gateways". Mọi con số dưới đây lấy từ bài báo trên nhánh IEEE, bản `main.pdf` 10 trang.

## Cấu trúc và thời lượng

Slide đi lần lượt từ Mục I đến Mục VI, không đảo thứ tự. Thời lượng giả định là 15 phút.

| Mục trong bài báo | Slide | Số slide | Thời lượng |
| --- | --- | --- | --- |
| I. Introduction | 1 đến 3 | 3 | 2 phút 05 giây |
| II. Related Work | 4 đến 6 | 3 | 2 phút 00 giây |
| III. System Model and Methodology | 7 đến 10 | 4 | 3 phút 35 giây |
| IV. Experimental Setup | 11 đến 12 | 2 | 1 phút 25 giây |
| V. Results and Discussion | 13 đến 19 | 7 | 5 phút 25 giây |
| VI. Conclusion | 20 | 1 | 30 giây |

Nếu thời lượng ngắn hơn, ẩn slide 5, 14 và 16 trước, vì mỗi mục vẫn còn slide khác để giữ mạch. Sau đó rút ngắn lời nói ở các slide còn lại. Không thêm slide quá 20.

Tiêu đề slide viết bằng tiếng Anh cho khớp bài báo. Cột "Đặt lên slide" và "Ý phải nói" ghi bằng tiếng Việt cho dễ chuẩn bị; khi đưa lên slide thì dịch sang tiếng Anh.

## Quy tắc về hình ảnh

Cả bộ slide chỉ dùng đúng 4 hình của bài báo, mỗi hình một lần. Không vẽ hình mới, không thêm ảnh minh họa, biểu tượng hay ảnh từ mạng.

| Hình trong bài báo | File trong repo | Dùng ở slide |
| --- | --- | --- |
| Fig. 1: Kiến trúc PP-FedData | `graphics/paper/fig1_architecture.pdf` | 7 |
| Fig. 2: Giao thức ba lần gửi | `graphics/paper/Fig2.pdf` | 8 |
| Fig. 3: TSTR macro-F1 theo ε | `graphics/paper/Fig3_python.pdf` | 15 |
| Fig. 4: Macro-F1 theo tổng lưu lượng | `graphics/paper/Fig4_python.pdf` | 18 |

- **Không dùng** các ảnh khác có trong repo: `graphics/Image/logo.jpg`, `graphics/chapter1/`, `graphics/chapter2/` và `huong_dan/minh_hoa/`. Những ảnh này không nằm trong bài báo.
- **Không dùng hình của đồ án** trên nhánh main. Hình và số thứ tự hình của đồ án khác bài báo.
- **Các slide còn lại** chỉ gồm chữ, công thức và bảng rút gọn gõ lại từ bài báo.
- **Giữ nguyên nội dung hình:** chỉ được phóng to, không sửa chữ, màu hay chú thích trong hình. File PDF là hình vector, chèn vào vẫn nét.

## Quy tắc trình bày

- **Thông điệp:** mỗi slide một ý, và tiêu đề chính là ý đó.
- **Mạch:** ghi tên mục của bài báo ở góc slide, ví dụ "II. Related Work", để người nghe biết đang ở đâu.
- **Bảng:** chỉ giữ các dòng được nêu ở cột "Đặt lên slide". Không dán nguyên bảng của bài báo.
- **Số liệu:** chép đúng số và nhãn cấu hình trong bài báo. Không lấy số của đồ án, vì hai tài liệu trình bày các phạm vi khác nhau.
- **Công thức:** chỉ dùng ở slide 8, 9, 10 và 12, giữ số công thức và trích nguồn theo bài báo, ví dụ [17, Cor. 3.6].
- **Thuật ngữ:** viết "client-side DP" như bài báo, không viết "Local DP" cho MGl.

## Lộ trình 20 slide

### I. Introduction: slide 1 đến 3

| Slide | Giây | Tiêu đề | Đặt lên slide | Nguồn trong bài báo | Ý phải nói |
| --- | --- | --- | --- | --- | --- |
| 1 | 30 | Privacy-Preserving Federated Synthetic Data Generation for Intrusion Detection in MQTT-Based IoT Gateways | Tên bài báo, 8 tác giả, Faculty of Information Assurance, FPT University. Không có logo | Trang đầu | Giới thiệu đề tài và kết luận chính: dữ liệu sinh có giá trị ở nơi lưu lượng thô phải ở lại gateway |
| 2 | 50 | Rare attacks are scattered, and each protection answers a different threat | MQTT và DoS/DDoS [1]; FL giữ dữ liệu tại chỗ [2] nhưng gradient có thể lộ dữ liệu [3]; lớp hiếm phân tán non-IID; SecAgg+ che từng gateway [5], [6]; DP giới hạn điều đầu ra tiết lộ [7] | Mục I | Mô hình sâu trao đổi cả mô hình qua nhiều vòng. Bảng đếm là tổng theo bản ghi, đúng thứ SecAgg tính được |
| 3 | 45 | Four research questions, no new synthesis algorithm | RQ1 đến RQ4, mỗi câu một dòng; ba đóng góp: giao thức ba lần gửi, so sánh có kiểm soát, hướng dẫn cấu hình | Mục I | Đóng góp là kết hợp cho gateway IoT và so sánh có kiểm soát. Bốn câu này là lộ trình của Mục V |

### II. Related Work: slide 4 đến 6

| Slide | Giây | Tiêu đề | Đặt lên slide | Nguồn trong bài báo | Ý phải nói |
| --- | --- | --- | --- | --- | --- |
| 4 | 40 | Privacy protection in FL: DP, secure aggregation, and both | DP [7], client-side DP, DP-SGD [12], RDP [21]; SecAgg [5], SecAgg+ [6]; DP phân tán [16], [17] | Mục II-A | Khảo sát [4] nêu năm nhóm kỹ thuật; ba nhóm MPC, TEE, blockchain quá nặng với gateway nên bài báo dùng DP và SecAgg. Client-side DP khác local DP cổ điển |
| 5 | 40 | Synthetic data for IDS, and the marginal alternative | Bên trái: SMOTE [22], GAN và VAE [8], [9], [10], [11]. Bên phải: PrivBayes [13], MST [14], AIM [15], FLAIM [18], CaPS [19] | Mục II-B, II-C | Các nghiên cứu sinh dữ liệu cho IDS chưa dùng secure aggregation cho cập nhật của bộ sinh. FLAIM và CaPS chủ yếu đánh giá trên bảng dữ liệu tổng quát |
| 6 | 40 | No prior study combines these on IoT-MQTT traffic | Table I rút gọn: [9], [10], [11], FLAIM, CaPS, PP-FedData; ba khoảng trống (i), (ii), (iii) | Mục II-D, Table I | Luôn nói kèm "tìm kiếm không hệ thống, theo hiểu biết của nhóm" |

### III. System Model and Methodology: slide 7 đến 10

| Slide | Giây | Tiêu đề | Đặt lên slide | Nguồn trong bài báo | Ý phải nói |
| --- | --- | --- | --- | --- | --- |
| 7 | 45 | Gateways keep raw traffic, the server sees only protected releases | Fig. 1; K = 5 gateway; chia non-IID Dirichlet α_dir = 0.5 [23]; server honest-but-curious | Fig. 1, Mục III-A | Hai nhánh sinh dùng chung kiến trúc. Poisoning và Byzantine nằm ngoài phạm vi. Nhãn, quota và thống kê tiền xử lý nằm ngoài ε |
| 8 | 70 | Three noisy releases build one Chow-Liu tree | Fig. 2 ở nửa trên; công thức (2) và (3) [20] ở nửa dưới; d = 37 thuộc tính, 64 bin mịn, 666 cặp | Fig. 2, Mục III-B | Lần 1 một chiều theo lớp, lần 2 theo cặp gộp mọi lớp để giữ tín hiệu mỗi ô, lần 3 theo cạnh cây và lớp. Mẫu sinh đi từ gốc đến lá theo từng lớp. Hậu xử lý MGr không tốn thêm ngân sách |
| 9 | 50 | Exact accounting: sensitivity, Rényi bound, conversion | Công thức (4), (5) [17, Cor. 3.6], (6) [24] | Mục III-C | Mỗi gói tin cộng một vào một ô của mỗi bảng, nên độ nhạy đã biết. Thiết lập chọn theo validation: 16, 16 và 8 bin ở ε = 1, 5, 10 |
| 10 | 50 | Integer noise is split across gateways; the CVAE baseline cannot do this | Mỗi gateway thêm Sk(μ/t); công thức (7) trên Z_(2^32); MGl thêm đủ μ; CVAE: B3, M1, M2, M3, 30 vòng, 2 epoch cục bộ | Mục III-C, III-D | Chia nhiễu hợp lệ vì mỗi lần gửi là một tổng. DP-SGD thêm nhiễu ở mọi bước cục bộ, nên dù dùng SecAgg+ thì CVAE vẫn chỉ có client-side DP |

### IV. Experimental Setup: slide 11 đến 12

| Slide | Giây | Tiêu đề | Đặt lên slide | Nguồn trong bài báo | Ý phải nói |
| --- | --- | --- | --- | --- | --- |
| 11 | 40 | 39 million packets, six classes, 60:1 training imbalance | Table II rút gọn: số gói thô, tỉ lệ, train 88,500, val 12,000, test 30,000 | Table II, Mục IV-A | Normal xuất từ PCAP theo thiết lập của tác giả, khớp 47/48 capture. Đã bỏ định danh. Không cột nào đạt macro-F1 trên 0.9 |
| 12 | 45 | Every comparison uses one test set and one decision rule | Table III rút gọn; TRTR, TSTR, TAug, tăng cường cục bộ; công thức (9); 3 seed; 1,000 lần bootstrap | Table III, Mục IV-B, IV-C, IV-D | Có hiệu ứng khi CI 95% không chứa 0 và chênh lệch lớn hơn độ lệch chuẩn theo seed. Mỗi kết luận được kiểm tra lại với bootstrap theo cả stream |

### V. Results and Discussion: slide 13 đến 19

| Slide | Giây | Tiêu đề | Đặt lên slide | Nguồn trong bài báo | Ý phải nói |
| --- | --- | --- | --- | --- | --- |
| 13 | 45 | RQ1: With pooled real data, synthetic rows add almost nothing | Mốc thật: B0 0.448, B1a 0.496, B1b 0.505. Không DP: MG 0.459, CVAE 0.413. TAug với RF: 2/13, tối đa +0.001, SMOTE +0.057 | Mục V-A | Nói thẳng đây là kết quả âm. Các mốc dữ liệu thật đều cần gộp lưu lượng thô |
| 14 | 45 | RQ1: The value appears where traffic must stay local | Tăng cường cục bộ: 0.384 lên 0.423, 0.426, 0.427; 11, 13, 13 trên 15. FedMLP DP-FedSGD 0.350, 0.369, 0.389 so với MG (MLP) 0.337, 0.425, 0.433 | Mục V-A | Số đếm 11, 13, 13 là chênh lệch thô, chưa qua công thức (9). Lộ trình trực tiếp cần 2,593 vòng và khoảng 7.7 GB |
| 15 | 60 | RQ2: FedDP-Marginal leads the CVAE at every budget | Fig. 3; MG 0.366, 0.425, 0.433; CVAE 0.176, 0.254, 0.275; MGl 0.267, 0.397, 0.406; 0.48 đến 0.53 MB so với 13.6 đến 72.4 MB | Fig. 3, Table IV, Mục V-B | So sánh công bằng cùng mô hình tin cậy là MGl với CVAE: hơn 0.092, 0.143, 0.131. Chia sẻ nhiễu làm khoảng cách tăng thêm |
| 16 | 45 | RQ3: SecAgg+ is cheap, and DP measurably reduces table leakage | SecAgg+ với MG: 1.39 lần byte, 1.06 lần thời gian. AUC 0.573 không DP; 0.515, 0.525, 0.539 ở ε = 1, 5, 10; kiểm chứng dương 0.835 | Mục V-C | Tổng an toàn bằng đúng tổng thật nên độ hữu ích không đổi. Rò rỉ tuyệt đối nhỏ. SecAgg+ không đổi các số AUC này |
| 17 | 45 | RQ3: The guarantee depends on honest gateways and on the unit | Table V rút gọn: MGr-eps5, MGr-t3-eps5, MGl-eps5, MGr-strm1-eps5, MGr-cap50-eps5 | Table V, Mục V-C | ε = 5 thành 14.2 nếu chỉ một gateway trung thực. Bảo vệ stream mất 0.03 đến 0.05; capture chỉ còn 0.09 đến 0.18 |
| 18 | 45 | RQ4: The choice depends on trust, privacy and bandwidth | Fig. 4; 3 đến 4 dòng của Table VI; 17/18 cấu hình Pareto là FedDP-Marginal | Fig. 4, Table VI, Mục V-D | Quy tắc gồm năm bước, từ lọc hợp lệ đến chọn trên Pareto front. Mọi biến thể MG dưới 1.4 MB mỗi lần chạy, các nhánh CVAE từ 8.4 đến 191 MB |
| 19 | 40 | Discussion and limitations | Vì sao marginal chịu DP tốt hơn; một bộ dữ liệu, mức gói tin; mô phỏng trên một máy; 3 seed; tiền xử lý và chọn siêu tham số ngoài ε; chưa so FLAIM, AIM, CVAE nhiễu phân tán | Mục V-E | Ba lần gửi, mỗi lần một tổng có độ nhạy đã biết. Đổi lại, nhánh marginal chỉ nắm phụ thuộc theo cặp qua một cây. Tự nêu hạn chế trước khi bị hỏi |

### VI. Conclusion: slide 20

| Slide | Giây | Tiêu đề | Đặt lên slide | Nguồn trong bài báo | Ý phải nói |
| --- | --- | --- | --- | --- | --- |
| 20 | 30 | Conclusion: useful where traffic must stay local | Các kết luận chính; hướng tiếp theo; dòng "Thank you" | Mục VI | Kết bằng ý: chọn bảo vệ theo yêu cầu triển khai, và biết trước cái giá phải trả |

## Những câu không được nói

Các cách nói sau vượt quá những gì bài báo đã chứng minh.

| Không nói | Nói thay bằng |
| --- | --- |
| Dữ liệu sinh cải thiện IDS | Dữ liệu sinh không cải thiện IDS khi dữ liệu thật đã gộp được. Giá trị của nó nằm ở nơi lưu lượng phải ở lại gateway |
| Bài báo đề xuất thuật toán sinh mới | Bài báo không nhận thuật toán sinh mới. Đóng góp là kết hợp cho gateway IoT, so sánh có kiểm soát và hướng dẫn cấu hình |
| MG hơn CVAE 0.16 đến 0.19 trong cùng điều kiện | Mức đó là khi MG chia nhiễu qua các gateway trung thực. Cùng mô hình tin cậy thì MGl hơn 0.092, 0.143, 0.131 |
| "ε = 5" đứng một mình | ε = 5 theo gói tin, δ = 10^-5, khi cả 5 gateway trung thực; thành 14.2 nếu chỉ một gateway trung thực |
| SecAgg+ bảo vệ dữ liệu được công bố | SecAgg+ chỉ che bảng của từng gateway, không che điều tổng tiết lộ |
| Dữ liệu sinh giống dữ liệu thật | Bộ phân loại vẫn tách được gần như hoàn toàn: C2ST AUC 0.9995 đến 1.0000 |
| FedDP-Marginal tốt hơn mô hình sâu nói chung | Bài báo so một CVAE trên một bộ dữ liệu. FLAIM, AIM và các mô hình sâu khác chưa được so |
| Đã đo trên gateway thật | Liên kết, kể cả SecAgg+, được mô phỏng trên một máy, chưa đo chi phí mạng và thiết bị thật |

## Các số dễ nhầm

| Số | Cần nhớ |
| --- | --- |
| 0.366 và 0.337 ở ε = 1 | 0.366 là bộ phân loại được chọn trong Table IV; 0.337 là MG khi so cùng MLP với lộ trình huấn luyện trực tiếp |
| 13.6 đến 72.4 MB và 8.4 đến 191 MB | Khoảng đầu là các cấu hình CVAE chính của Table IV; khoảng sau là mọi nhánh CVAE trong Fig. 4 |
| 0.376 và 0.397 khi bảo vệ stream | 0.376 là MGr-strm1-eps5 ở Table V; 0.397 là MGs-strm1-eps5 ở Table VI |
| B3 đạt 0.413 | B3 dùng decoder nhiễu dư khớp trên dữ liệu gộp; nếu dùng decoder thường là 0.407 |
| MGd-eps5 ở Table VI | Tổng an toàn của MGd được mô phỏng trong một tiến trình; cấu hình hòa chạy qua SecAgg+ thật là MGs-t3-eps5 (0.420) |
| MB/run của MGl | Là số ước tính, có dấu sao trong Table IV |

## Việc cần xong trước khi trình bày

- [ ] Hỏi thời lượng cho phép; nếu khác 15 phút thì chia lại số giây theo tỉ lệ
- [ ] Hỏi đơn vị tổ chức có mẫu slide bắt buộc hay không; nếu mẫu có logo thì quyết định lại vì bộ này không dùng ảnh ngoài bài báo
- [ ] Kiểm tra thứ tự slide khớp Mục I đến Mục VI của bài báo
- [ ] Kiểm tra cả bộ chỉ có 4 hình, đúng ở slide 7, 8, 15 và 18
- [ ] Đối chiếu từng con số trên slide với `main.pdf` của nhánh IEEE
- [ ] Tập nói đủ giờ ít nhất hai lần
- [ ] Xuất thêm một bản PDF để dự phòng khi máy trình chiếu lỗi font
