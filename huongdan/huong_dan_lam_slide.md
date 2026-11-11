# Hướng dẫn làm slide bảo vệ đồ án PP-FedData

Cập nhật: 2026-11-09

Bài thuyết trình gồm 40 slide, chia liền mạch cho 3 người: Người 1 nêu bài toán và dữ liệu (13 slide), Người 2 trình bày phương pháp (12 slide), Người 3 trình bày kết quả và kết luận (15 slide). Mọi con số dưới đây lấy từ đồ án trên nhánh main, bản `main.pdf` 147 trang.

## Phân công

Người 3 nhận nhiều slide và nhiều thời gian nhất vì kết quả là phần hội đồng hỏi kỹ nhất.

| Người | Slide | Phần trình bày | Số slide | Thời lượng | Phần đồ án phải nắm |
| --- | --- | --- | --- | --- | --- |
| Người 1 | 1 đến 13 | Mở đầu, bài toán, tài liệu, dữ liệu | 13 | 9 phút | Chương 1, Chương 2, Mục 3.2 |
| Người 2 | 14 đến 25 | Kiến trúc, FedDP-Marginal, quyền riêng tư, CVAE, quy trình đánh giá | 12 | 9 phút | Mục 3.1, Mục 3.3 |
| Người 3 | 26 đến 40 | Kết quả RQ1 đến RQ4, so sánh tài liệu, hạn chế, kết luận | 15 | 12 phút | Chương 4, Chương 5, Chương 6 |

Thời lượng trên giả định buổi trình bày 30 phút, tức khoảng 45 giây mỗi slide. Nếu hội đồng chỉ cho 20 phút, chuyển slide 8, 12, 15, 29, 31 và 37 ra sau slide cảm ơn để làm slide dự phòng.

Tiêu đề slide viết bằng tiếng Anh cho khớp đồ án. Cột "Đặt lên slide" và "Ý phải nói" ghi bằng tiếng Việt để nhóm dễ làm; khi đưa lên slide thì dịch sang tiếng Anh.

## Quy tắc chung

Mỗi slide chỉ mang một thông điệp, và tiêu đề chính là thông điệp đó.

**Mọi hình trên slide chỉ lấy từ đồ án LaTeX:** Hình 3.1 đến 3.3, Hình 4.1 đến 4.7 và logo trường ở bìa (`graphics/Image/logo.jpg`). Không vẽ hình mới, không lấy ảnh từ mạng. Ảnh trong `graphics/chapter1/` và `graphics/chapter2/` là ảnh mẫu của template, không có trong đồ án nên không dùng.

- **Nội dung:** tối đa một hình hoặc một bảng rút gọn trên một slide. Phần giải thích để vào lời nói.
- **Hình Chương 4:** lấy từ thư mục `graphics/chapter4/` của repo. File PDF là hình vector, chèn vẫn nét.
- **Hình 3.1, 3.2, 3.3:** vẽ bằng TikZ nên không có file ảnh riêng. Chụp từ `main.pdf` ở mức phóng to 300%, không vẽ lại. Hình 3.2 ở trang 32, Hình 3.3 ở trang 50 (số trang in ở chân trang). Không dùng hình ConceptDraw của bài báo IEEE: hai hình đó chưa sửa và khác chữ với đồ án.
- **Bảng:** chỉ giữ các dòng được nêu trong hướng dẫn, không dán nguyên bảng của đồ án.
- **Số liệu:** chép đúng số và đúng nhãn cấu hình trong `main.pdf`. Macro-F1 luôn kèm tên bộ phân loại nếu so sánh RF và MLP.
- **Công thức:** chỉ dùng ở slide 20, 22 và 25. Trích nguồn theo dạng đã dùng trong đồ án, ví dụ [22, Cor. 3.6, eq. (3.2)]. Số tài liệu lấy theo danh mục của `main.pdf`.
- **Chuyển người:** người trước kết thúc bằng một câu dẫn sang phần sau. Câu dẫn đã ghi ở slide 13 và slide 25.

### Những câu không được nói

Các cách nói sau vượt quá những gì đồ án đã chứng minh, nên cả 3 người phải tránh.

| Không nói | Nói thay bằng |
| --- | --- |
| Dữ liệu sinh cải thiện IDS | Khi gộp được dữ liệu thật, dữ liệu sinh gần như không thêm gì. Giá trị của nó nằm ở nơi không gộp được và ở gateway thiếu lớp |
| Nhóm đề xuất thuật toán mới | Đồ án không nhận mới về thuật toán. Đóng góp là phép đánh giá có đo đạc, kế toán DP phân tán chính xác qua SecAgg+ thật, và hướng dẫn cấu hình theo yêu cầu |
| "ε = 5" đứng một mình | ε = 5 theo gói tin, δ = 10^-5, khi mọi gateway trung thực; còn 14.2 nếu chỉ một gateway trung thực |
| Dữ liệu sinh giống dữ liệu thật | Dữ liệu sinh vẫn dễ phân biệt với dữ liệu thật: C2ST AUC từ 0.9995 trở lên ở mọi bộ sinh |
| SecAgg bảo vệ dữ liệu được công bố | SecAgg+ chỉ che bảng của từng gateway trước server. Nó không giới hạn điều tổng hợp tiết lộ, nên AUC tấn công vẫn là 0.573 |
| FedDP-Marginal tốt hơn mô hình sâu nói chung | Kết quả so một CVAE với một bộ sinh marginal trên một bộ dữ liệu |
| Các bài đã công bố bị thổi số | Các bài đó khác tác vụ, đầu vào và cách chia, nên điểm không so trực tiếp được |
| Đã đo trên gateway thật | Liên kết 5 gateway được mô phỏng trên một máy. Thời gian là thời gian tính toán, chưa đo độ trễ mạng |

## Người 1: slide 1 đến 13

Người 1 phải làm hội đồng thấy vì sao các gateway cần hợp tác mà không chia sẻ gói tin thô, và vì sao dữ liệu đáng tin.

| Slide | Tiêu đề | Đặt lên slide | Nguồn trong đồ án | Ý phải nói |
| --- | --- | --- | --- | --- |
| 1 | A Privacy-Preserving Data Generation Framework in Federated Learning for Enhanced IoT System Attack Detection | Tên đề tài đã đăng ký, 5 thành viên, TS. Nguyễn Anh Nhật, ThS. Lưu Minh Trí, mã nhóm | Bìa | Giới thiệu nhóm và người trình bày từng phần |
| 2 | Outline | Năm phần: Problem, Related work, Data, Method, Results; ghi tên người nói mỗi phần | Mục lục | Nói trước kết luận: dữ liệu sinh có ích nhất khi không thể gộp dữ liệu thật |
| 3 | MQTT gateways see attacks that few sites observe alone | Chỉ dùng chữ: MQTT là giao thức publish-subscribe; mục tiêu DoS/DDoS | Mục 1.1 | Mỗi nơi chỉ thấy một phần tấn công, nên IDS cần dữ liệu từ nhiều nơi |
| 4 | Keeping data local does not remove the privacy risk | FL giữ dữ liệu tại chỗ nhưng vẫn gửi cập nhật; gradient có thể lộ dữ liệu [7] | Mục 1.1, 1.2 | Chỉ gửi trọng số thay dữ liệu thô chưa phải bảo vệ đầy đủ |
| 5 | Privacy, rare classes and edge cost pull against each other | Chỉ dùng chữ, ba ý: ε, độ hữu ích cho IDS, chi phí tại biên | Mục 1.2 | Siết ε làm tăng nhiễu và làm mất tương quan của lớp hiếm |
| 6 | Four objectives | O1 kiến trúc liên kết, O2 FedDP-Marginal, O3 CVAE cơ sở, O4 đánh giá và hướng dẫn cấu hình | Mục 1.3.1 | Mỗi mục tiêu một dòng |
| 7 | Four research questions | RQ1 độ hữu ích, RQ2 so hai bộ sinh, RQ3 chi phí và đơn vị bảo vệ, RQ4 cấu hình theo yêu cầu | Mục 1.3.2 | Phần kết quả sẽ trả lời đúng theo thứ tự này |
| 8 | Two families of private generators | Bên trái: GAN, VAE với DP trên gradient. Bên phải: bộ sinh marginal, FLAIM [36], CaPS [37] | Mục 2.1 | Marginal liên kết đã có, nhưng chủ yếu đánh giá trên bảng dữ liệu tổng quát, không đo IDS |
| 9 | What the reviewed work leaves open | Ba khoảng trống; bản rút gọn Bảng 2.1 | Mục 2.1, Bảng 2.1 | Luôn nói kèm "theo hiểu biết của nhóm, từ một tìm kiếm không hệ thống" |
| 10 | Contribution: a measured evaluation, not a new algorithm | G1 bộ sinh marginal cho MQTT, G2 DP phân tán qua SecAgg+ thật, G3 đánh giá năm chiều và hướng dẫn cấu hình | Mục 2.3, Mục 6.1 | Nói rõ đồ án không nhận mới về thuật toán |
| 11 | 39 million packets, four attack classes under 2% | Bảng 6 lớp: NORMAL 63.99%, BCF 31.49%, DELAYED 1.54%, SYN 1.54%, INVALID 0.74%, WILL 0.69%; tổng 39,000,601 | Bảng 3.7 | Mỗi dòng là một gói tin. DoS và DDoS cùng họ được gộp một lớp |
| 12 | Traffic extracted with the authors' export settings | Normal có 49 PCAP, trích bằng TShark với thiết lập của tác giả; 411/411 file khớp; khớp 47/48 capture; 0.042% dòng khác; bỏ định danh; D = 59 cột | Mục 3.2.1, 3.2.3, Bảng 3.8, 3.9 | Bỏ IP nguồn, thời gian tuyệt đối và chỉ số stream để mô hình không học vẹt |
| 13 | Split by capture, locked test set, five leakage checks | Train 88,500, val 12,000, test 30,000 (5,000 mỗi lớp); mất cân bằng 60:1; C1 đến C5, chỉ BCF bị gắn cờ | Bảng 3.10, 4.1, Mục 3.2.4 | 8/11 lớp con chỉ có một capture nên chia theo khối. Câu chuyển: "Dữ liệu đã sẵn sàng, tiếp theo là cách các gateway hợp tác" |

## Người 2: slide 14 đến 25

Người 2 phải giải thích được vì sao ba lần gửi bảng đếm có thể chia nhiễu cho các gateway, còn DP-SGD thì không.

| Slide | Tiêu đề | Đặt lên slide | Nguồn trong đồ án | Ý phải nói |
| --- | --- | --- | --- | --- |
| 14 | Five gateways, one server, one downstream detector | Hình kiến trúc hai nhánh sinh | Hình 3.2, Mục 3.1.2 | Dữ liệu sinh được tạo ở server, không tạo ở gateway |
| 15 | Gateways hold skewed class shares | Hình phân chia non-IID; Dirichlet α = 0.5; 3,666 đến 33,618 dòng ở seed 0 | Hình 4.1, Mục 4.2.1 | Client 1 không có dòng SYN_DoS nào, đây là tình huống liên kết cần giải quyết |
| 16 | Honest-but-curious server, four trust settings | Cơ bản, h gateway trung thực, ngưỡng t, Local DP | Mục 3.1.3 | Gateway ác ý, poisoning và Byzantine nằm ngoài phạm vi |
| 17 | Secure aggregation and DP answer different threats | Hai cột: mối đe dọa, bảo đảm, điều không làm được | Bảng 3.3 | SecAgg+ che từng gateway; DP giới hạn điều đầu ra tiết lộ. Hai cơ chế không thay thế nhau |
| 18 | Two generator routes under one federation | FedDP-Marginal gửi bảng đếm trong 3 lần; CVAE gửi trọng số qua 30 vòng, 2 epoch cục bộ (mặc định) | Bảng 3.2 | Cùng cách chia dữ liệu và cùng quy trình đánh giá |
| 19 | Three noisy releases replace many training rounds | Hình giao thức ba lần gửi; d = 37 thuộc tính; 64 bin mịn; 666 cặp; phân ngân sách ω mặc định (0.3, 0.1, 0.6) | Hình 3.3, Mục 3.3.2 | Lần 1 là một chiều theo lớp, lần 2 là cặp gộp mọi lớp, lần 3 là cạnh cây theo lớp. Thiết lập chọn cuối cùng theo từng ε ở Bảng 4.3 |
| 20 | One Chow-Liu tree, sampled class by class | Công thức (3.4) [10, Def. 1], [10, Def. 2] và (3.7) [10, eq. (1)] | Mục 3.3.2 | Cây dựng từ bảng đã có nhiễu, là hậu xử lý nên không tốn thêm ngân sách. Gộp mọi lớp để tăng tỉ lệ tín hiệu trên nhiễu |
| 21 | Integer noise split across gateways sums exactly | Mỗi gateway thêm 1/K phương sai Skellam [22]; cộng modulo 2^32 qua SecAgg+ [18, Sec. 3.1] | Mục 3.3.2, 3.3.3 | Chỉ hợp lệ vì mỗi lần gửi là một tổng. DP-SGD nhiều epoch không chia nhiễu kiểu này được |
| 22 | Accounting: Rényi bound, composition, conversion | (3.10) [22, Cor. 3.6, eq. (3.2)]; cộng RDP [42, Prop. 1]; (3.11) [66, Th. 21] | Mục 3.3.3 | Với h gateway trung thực, ε tính lại từ phương sai còn lại h/K của μ. Ngưỡng t nghiệm đúng mục tiêu khi có ít nhất t gateway trung thực |
| 23 | A privacy claim needs its unit and its perimeter | Gói tin, TCP stream (m = 1, 2, 4), capture (m = 25, 50, 100); ngoài ε: nhãn, số dòng mỗi lớp, kích thước client, thống kê chuẩn hóa, chọn siêu tham số | Mục 3.1.3, 3.3.3 | ε không kèm đơn vị thì không nói được cả phiên tấn công có được che hay không |
| 24 | Federated CVAE as the deep baseline | B3 không bảo vệ, M2 SecAgg+, M1 DP-SGD, M3 cả hai; ε lấy client xấu nhất, công thức (3.14) | Mục 3.3.4, Bảng 3.14, Mục 5.5 | CVAE là tiền đề ban đầu của nghiên cứu và là mốc so sánh. Không có nó thì lợi thế của nhánh marginal không có điểm so |
| 25 | Same test set, same decision rule for every comparison | TRTR, TSTR, TAug, TAugR, tăng cường cục bộ; Macro-F1 (3.22); quy tắc (3.23) | Bảng 3.16, Mục 3.3.6, 3.3.7 | Có hiệu ứng khi CI 95% không chứa 0 và chênh lệch lớn hơn độ lệch chuẩn theo seed. 3 seed, 1,000 lần bootstrap. Câu chuyển: "Với quy tắc này, kết quả trả lời bốn câu hỏi như sau" |

## Người 3: slide 26 đến 40

Người 3 phải nói rõ cả kết quả tốt lẫn kết quả âm: bộ sinh marginal dẫn trước CVAE, nhưng dữ liệu sinh không giúp gì khi đã gộp được dữ liệu thật.

| Slide | Tiêu đề | Đặt lên slide | Nguồn trong đồ án | Ý phải nói |
| --- | --- | --- | --- | --- |
| 26 | RQ1: Synthetic-only detectors reach 0.366 to 0.433 | Biểu đồ TSTR theo ε; mốc RF dữ liệu thật 0.448, SMOTE 0.505 | Hình 4.3, Bảng 4.2, 4.4 | Bằng 82% đến 97% RF trên dữ liệu thật, mà mốc đó cần gộp dữ liệu. Sổ chạy có 1,237 dòng, 431 cấu hình; chạy lại khớp 53/53 dòng |
| 27 | RQ1: With pooled real data, synthetic rows add almost nothing | RF: 2/13 bộ sinh đạt, lớn nhất +0.0012, SMOTE +0.0575. MLP: 9/13, lớn nhất +0.0378, SMOTE +0.1339 | Bảng 4.5, Hình 4.2 | CVAE thua class weights và SMOTE cả 6/6 so sánh. Nói thẳng đây là kết quả âm |
| 28 | RQ1: A gateway lacking some classes gains about 0.04 | Macro-F1 từ 0.384 lên 0.423, 0.426, 0.427; 11, 13, 13 trên 15 mô hình client tăng | Bảng 4.6 | Đây là vai trò hữu ích nhất của dữ liệu sinh. Mức giảm tối đa 0.005 |
| 29 | RQ1: Training the detector directly is a real alternative | DP-FedSGD 0.350, 0.369, 0.389; FedDP-Marginal (MLP) 0.337, 0.425, 0.433; kết luận: không khác, thua, thua | Bảng 4.7 | 0.337 là MLP, còn 0.366 là RF. Lộ trình trực tiếp cần khoảng 7.7 GB (ước tính), so với 0.48 đến 0.53 MB |
| 30 | RQ2: At equal budget, the marginal route leads by 0.092 to 0.191 | Sáu dòng của bảng hiệu FedDP-Marginal trừ CVAE | Bảng 4.8 | Cả 12/12 so sánh đều "better" dưới cả hai bootstrap. Recall lớp hiếm hơn +0.049 đến +0.169 |
| 31 | RQ2: H1 supported, H2 not supported | H1: INVALID +0.139, WILL +0.222. H2: BCF +0.138, SYN +0.312, nghiêng về FedDP-Marginal | Hình 4.4, Bảng 4.9, 5.1 | So theo ước lượng điểm và độ lệch giữa các seed, không dùng bootstrap cho từng lớp |
| 32 | Why the marginal route withstands DP better | Ba lần gửi có độ nhạy giới hạn, so với rất nhiều bước gradient; chia nhiễu qua tổng; đường cong phẳng dần từ ε = 5 đến 10 | Mục 4.4 | Đây là giải thích phù hợp kết quả, chưa được tách riêng bằng thí nghiệm |
| 33 | RQ3: At most 1.33 MB per run against 8.4 to 191 MB | Biểu đồ macro-F1 theo lưu lượng; SecAgg+ tốn 1.02 đến 1.12 lần thời gian, 1.39 đến 1.62 lần byte | Hình 4.5, Bảng 4.11 | Byte đo trên lưới Flower. Thời gian là thời gian tính toán, chưa có độ trễ mạng |
| 34 | RQ3: The guarantee depends on the unit and on honest gateways | Stream mất 0.03 đến 0.05; capture chỉ còn 0.091 đến 0.177; với một gateway trung thực, ε = 1, 5, 10 thành 2.4, 14.2, 33.1 | Bảng 4.12, 4.13, Hình 4.6 | Bảo vệ cả capture không dùng được trên dữ liệu này. Ngưỡng t nhỏ hơn gần như không mất độ hữu ích, chỉ đúng với K = 5 |
| 35 | RQ3: The attack on released tables sees the effect of DP | AUC 0.573 không DP; 0.539, 0.525, 0.515 khi ε = 10, 5, 1; kiểm chứng dương 0.835 | Hình 4.7, Bảng 4.14 | Rò rỉ tuyệt đối nhỏ: 1.91% TPR tại 1% FPR. Tấn công trên CVAE không phát hiện gì, kể cả B3 không bảo vệ |
| 36 | RQ4: No single configuration fits every deployment | 11 yêu cầu cho ra 8 cấu hình; 17/18 cấu hình Pareto là FedDP-Marginal; chọn 4 đến 5 dòng tiêu biểu | Bảng 3.6, 4.17, công thức (3.1) | Lựa chọn phụ thuộc vào niềm tin nhiều hơn độ hữu ích. Dòng capture-privacy 0.177 không phải bộ phát hiện dùng được |
| 37 | Published scores answer other questions | Macro-F1 cùng RF từ 0.448 lên 0.941 chỉ do đổi cách chia và cột định danh; ba nghiên cứu đọc được toàn văn | Bảng 4.18, 4.20 | Các bài [2], [78], [79] khác tác vụ, đầu vào và cách chia. Không kết luận điểm của họ bị thổi |
| 38 | Limitations | Một bộ dữ liệu; gói tin độc lập; 3 seed; mô phỏng trên một máy; ε không tính bước chọn siêu tham số; chưa chạy FLAIM, AIM | Mục 5.6 | Tự nêu hạn chế trước khi hội đồng hỏi |
| 39 | Conclusions and future work | Ba kết luận của Mục 6.1; ba hướng tiếp: so với FLAIM, AIM, mô hình hóa theo phiên, đo trên gateway thật | Mục 6.1, 6.2 | Kết bằng ý: cấu hình phải chọn theo yêu cầu, không có cấu hình tốt nhất chung |
| 40 | Thank you | Tên đề tài, lời cảm ơn, Q&A | Bìa | Khi hỏi đáp: Người 1 nhận câu về dữ liệu, Người 2 về phương pháp, Người 3 về kết quả |

## Việc cần xong trước buổi bảo vệ

Hai việc đầu cần chốt trước khi làm slide, vì chúng quyết định người nói và độ dài.

- [ ] Chọn 3 người trình bày trong 5 thành viên ở bìa đồ án và điền tên vào bảng phân công
- [ ] Hỏi thời lượng hội đồng cho phép; nếu dưới 30 phút thì chuyển 6 slide dự phòng
- [ ] Hỏi khoa có mẫu slide bắt buộc hay không
- [ ] Bổ sung mã nhóm IAP491_G.. và mã đồ án cho slide 1
- [ ] Đối chiếu từng con số trên slide với `main.pdf`
- [ ] Mỗi người đọc mục "Những câu không được nói" và phần của hai người còn lại
- [ ] Tập nói đủ giờ ít nhất hai lần, có cả câu chuyển người
- [ ] Xuất thêm một bản PDF để dự phòng khi máy trình chiếu lỗi font
