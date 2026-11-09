# Hướng dẫn làm slide thuyết trình bài báo IEEE

Cập nhật: 2026-11-09

Bài thuyết trình gồm 20 slide do 1 người trình bày, dựa trên bài báo "Privacy-Preserving Federated Synthetic Data Generation for Intrusion Detection in MQTT-Based IoT Gateways". Mọi con số dưới đây lấy từ bài báo trên nhánh IEEE, bản `main.pdf` 10 trang.

## Cấu trúc và thời lượng

Thời lượng giả định là 15 phút. Phần kết quả chiếm nhiều thời gian nhất vì đó là phần người nghe quan tâm nhất.

| Phần | Slide | Số slide | Thời lượng |
| --- | --- | --- | --- |
| Mở đầu, bài toán, câu hỏi nghiên cứu | 1 đến 4 | 4 | 2 phút 50 giây |
| Phương pháp | 5 đến 10 | 6 | 4 phút 40 giây |
| Dữ liệu và cách đánh giá | 11 đến 12 | 2 | 1 phút 25 giây |
| Kết quả RQ1 đến RQ4 | 13 đến 18 | 6 | 4 phút 55 giây |
| Hạn chế và kết luận | 19 đến 20 | 2 | 1 phút 10 giây |

Nếu thời lượng ngắn hơn, ẩn slide 7, 10, 14 và 16 trước, sau đó rút ngắn lời nói ở các slide còn lại. Không thêm slide quá 20.

Tiêu đề slide viết bằng tiếng Anh cho khớp bài báo. Cột "Đặt lên slide" và "Ý phải nói" ghi bằng tiếng Việt cho dễ chuẩn bị; khi đưa lên slide thì dịch sang tiếng Anh.

## Quy tắc về hình ảnh

Cả bộ slide chỉ dùng đúng 4 hình của bài báo, mỗi hình một lần. Không vẽ hình mới, không thêm ảnh minh họa, biểu tượng hay ảnh từ mạng.

| Hình trong bài báo | File trong repo | Dùng ở slide |
| --- | --- | --- |
| Fig. 1: Kiến trúc PP-FedData | `graphics/paper/fig1_architecture.pdf` | 5 |
| Fig. 2: Giao thức ba lần gửi | `graphics/paper/Fig2.pdf` | 6 |
| Fig. 3: TSTR macro-F1 theo ε | `graphics/paper/Fig3_python.pdf` | 15 |
| Fig. 4: Macro-F1 theo tổng lưu lượng | `graphics/paper/Fig4_python.pdf` | 18 |

- **Không dùng** các ảnh khác có trong repo: `graphics/Image/logo.jpg`, `graphics/chapter1/`, `graphics/chapter2/` và `huong_dan/minh_hoa/`. Những ảnh này không nằm trong bài báo.
- **Không dùng hình của đồ án** trên nhánh main. Hình và số thứ tự hình của đồ án khác bài báo.
- **Các slide còn lại** chỉ gồm chữ, công thức và bảng rút gọn gõ lại từ bài báo.
- **Giữ nguyên nội dung hình:** chỉ được phóng to, không sửa chữ, màu hay chú thích trong hình. File PDF là hình vector, chèn vào vẫn nét.

## Quy tắc trình bày

- **Thông điệp:** mỗi slide một ý, và tiêu đề chính là ý đó.
- **Bảng:** chỉ giữ các dòng được nêu ở cột "Đặt lên slide". Không dán nguyên bảng của bài báo.
- **Số liệu:** chép đúng số và nhãn cấu hình trong bài báo. Không lấy số của đồ án, vì hai tài liệu trình bày các phạm vi khác nhau.
- **Công thức:** chỉ dùng ở slide 7, 8, 9 và 12, giữ số công thức và trích nguồn theo bài báo, ví dụ [17, Cor. 3.6].
- **Thuật ngữ:** viết "client-side DP" như bài báo, không viết "Local DP" cho MGl.

## Lộ trình 20 slide

| Slide | Giây | Tiêu đề | Đặt lên slide | Nguồn trong bài báo | Ý phải nói |
| --- | --- | --- | --- | --- | --- |
| 1 | 30 | Privacy-Preserving Federated Synthetic Data Generation for Intrusion Detection in MQTT-Based IoT Gateways | Tên bài báo, 8 tác giả, Faculty of Information Assurance, FPT University. Không có logo | Trang đầu | Giới thiệu đề tài và kết luận chính: dữ liệu sinh có giá trị ở nơi lưu lượng thô phải ở lại gateway |
| 2 | 50 | Rare attacks are scattered, and two protections answer different threats | Lớp tấn công hiếm phân tán non-IID; gradient có thể lộ dữ liệu [3]; SecAgg+ che từng gateway; DP giới hạn điều đầu ra tiết lộ | Mục I | Giữ dữ liệu tại chỗ chưa đủ. SecAgg+ và DP không thay thế nhau |
| 3 | 45 | Count tables are sums, which secure aggregation computes | Mô hình sâu trao đổi cả mô hình qua nhiều vòng; marginal đo bảng đếm bậc thấp; bảng I rút gọn còn FLAIM [18], CaPS [19], PP-FedData | Mục I, II-D, Table I | Marginal liên kết đã có nhưng chưa đo phát hiện lớp hiếm trên MQTT. Nói kèm "tìm kiếm không hệ thống, theo hiểu biết của nhóm" |
| 4 | 45 | Four research questions, no new synthesis algorithm | RQ1 đến RQ4, mỗi câu một dòng; ba đóng góp | Mục I | Đóng góp là kết hợp cho gateway IoT và so sánh có kiểm soát. Bốn câu này là lộ trình phần kết quả |
| 5 | 50 | Gateways keep raw traffic, the server sees only protected releases | Fig. 1; K = 5 gateway; server honest-but-curious | Fig. 1, Mục III-A | Hai nhánh sinh dùng chung kiến trúc. Poisoning và Byzantine nằm ngoài phạm vi. Nhãn, quota và thống kê tiền xử lý nằm ngoài ε |
| 6 | 60 | Three noisy releases replace many training rounds | Fig. 2; d = 37 thuộc tính; 64 bin mịn; 666 cặp thuộc tính | Fig. 2, Mục III-B | Lần 1 một chiều theo lớp, lần 2 theo cặp gộp mọi lớp, lần 3 theo cạnh cây và lớp. Gộp lớp ở lần 2 là có chủ đích để giữ tín hiệu mỗi ô |
| 7 | 40 | One Chow-Liu tree, sampled class by class | Công thức (2) và (3) [20] | Mục III-B | Cây dựng từ bảng đã có nhiễu. Mẫu sinh đi từ gốc đến lá theo từng lớp. Hậu xử lý MGr không tốn thêm ngân sách |
| 8 | 50 | Exact accounting: sensitivity, Rényi bound, conversion | Công thức (4), (5) [17, Cor. 3.6], (6) [24] | Mục III-C | Mỗi gói tin cộng một vào một ô của mỗi bảng, nên độ nhạy đã biết. Thiết lập chọn theo validation: 16, 16 và 8 bin ở ε = 1, 5, 10 |
| 9 | 50 | Integer noise is split across gateways and summed exactly | Mỗi gateway thêm Sk(μ/t); công thức (7) trên Z_(2^32); MGl thêm đủ phương sai μ | Mục III-C | Chia nhiễu hợp lệ vì mỗi lần gửi là một tổng. SecAgg+ không thêm sai số làm tròn và không được tính vào ngân sách riêng tư |
| 10 | 30 | The federated CVAE is the deep baseline | B3, M1, M2, M3, M1o, M3o; 30 vòng, 2 epoch cục bộ; DP-SGD thêm nhiễu ở mọi bước cục bộ | Mục III-D, Table III | CVAE là lựa chọn thiết kế ban đầu. Dù dùng SecAgg+, nhánh này chỉ có client-side DP |
| 11 | 40 | 39 million packets, six classes, 60:1 training imbalance | Bảng II rút gọn: số gói thô, tỉ lệ, train 88,500, val 12,000, test 30,000 | Table II, Mục IV-A | Normal xuất từ PCAP theo thiết lập của tác giả, khớp 47/48 capture. Đã bỏ định danh. Không cột nào đạt macro-F1 trên 0.9 |
| 12 | 45 | Every comparison uses one test set and one decision rule | TRTR, TSTR, TAug, tăng cường cục bộ; công thức (9); 3 seed; 1,000 lần bootstrap | Mục IV-C, IV-D | Có hiệu ứng khi CI 95% không chứa 0 và chênh lệch lớn hơn độ lệch chuẩn theo seed. Mỗi kết luận được kiểm tra lại với bootstrap theo cả stream |
| 13 | 45 | RQ1: With pooled real data, synthetic rows add almost nothing | Mốc thật: B0 0.448, B1a 0.496, B1b 0.505. Không DP: MG 0.459, CVAE 0.413. TAug với RF: 2/13, tối đa +0.001, SMOTE +0.057 | Mục V-A | Nói thẳng đây là kết quả âm. Các mốc dữ liệu thật đều cần gộp lưu lượng thô |
| 14 | 45 | RQ1: The value appears where traffic must stay local | Tăng cường cục bộ: 0.384 lên 0.423, 0.426, 0.427; 11, 13, 13 trên 15. FedMLP DP-FedSGD 0.350, 0.369, 0.389 so với MG (MLP) 0.337, 0.425, 0.433 | Mục V-A | Số đếm 11, 13, 13 là chênh lệch thô, chưa qua công thức (9). Lộ trình trực tiếp cần 2,593 vòng và khoảng 7.7 GB |
| 15 | 65 | RQ2: FedDP-Marginal leads the CVAE at every budget | Fig. 3; MG 0.366, 0.425, 0.433; CVAE 0.176, 0.254, 0.275; MGl 0.267, 0.397, 0.406; 0.48 đến 0.53 MB so với 13.6 đến 72.4 MB | Fig. 3, Table IV, Mục V-B | So sánh công bằng cùng mô hình tin cậy là MGl với CVAE: hơn 0.092, 0.143, 0.131. Chia sẻ nhiễu làm khoảng cách tăng thêm |
| 16 | 40 | RQ3: SecAgg+ is cheap and costs no utility | MG: 1.39 lần byte, 1.06 lần thời gian. CVAE: 1.52 lần byte, 1.12 lần thời gian; DP-SGD nhân thời gian mỗi vòng lên 1.9 | Mục V-C | Tổng an toàn bằng đúng tổng thật nên độ hữu ích không đổi. Thời gian là thời gian tính toán, chưa có độ trễ mạng |
| 17 | 50 | RQ3: DP measurably reduces leakage from the released tables | Bảng nhỏ: AUC 0.573 không DP; 0.515, 0.525, 0.539 ở ε = 1, 5, 10; kiểm chứng dương 0.835 | Mục V-C, Table V | Rò rỉ tuyệt đối nhỏ. SecAgg+ không đổi các số này. Với CVAE, DP là bảo đảm hình thức, không đo được mức giảm |
| 18 | 50 | RQ4: The choice depends on trust, privacy and bandwidth | Fig. 4; 3 đến 4 dòng của Table VI; 17/18 cấu hình Pareto là FedDP-Marginal | Fig. 4, Table V, Table VI, Mục V-D | ε = 5 thành 14.2 nếu chỉ một gateway trung thực. Bảo vệ stream mất 0.03 đến 0.05; capture chỉ còn 0.09 đến 0.18 |
| 19 | 40 | Limitations | Một bộ dữ liệu, mức gói tin; mô phỏng trên một máy; 3 seed; tiền xử lý và chọn siêu tham số ngoài ε; chưa so FLAIM, AIM, CVAE nhiễu phân tán | Mục V-E | Tự nêu hạn chế trước khi bị hỏi. Lý do marginal chịu DP tốt hơn là giải thích, không phải điều đã tách bằng thí nghiệm |
| 20 | 30 | Conclusion: useful where traffic must stay local | Ba kết luận ngắn; hướng tiếp theo; dòng "Thank you" | Mục VI | Kết bằng ý: chọn bảo vệ theo yêu cầu triển khai, và biết trước cái giá phải trả |

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
- [ ] Kiểm tra cả bộ chỉ có 4 hình, đúng ở slide 5, 6, 15 và 18
- [ ] Đối chiếu từng con số trên slide với `main.pdf` của nhánh IEEE
- [ ] Tập nói đủ giờ ít nhất hai lần
- [ ] Xuất thêm một bản PDF để dự phòng khi máy trình chiếu lỗi font
