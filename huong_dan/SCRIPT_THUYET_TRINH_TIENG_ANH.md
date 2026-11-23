# Script thuyết trình bài báo IEEE bằng tiếng Anh (dưới 15 phút)

Cập nhật: 2026-11-24

File này là lời nói tiếng Anh cho bộ 20 slide trong `HUONG_DAN_LAM_SLIDE.md`, đi đúng thứ tự Mục I đến Mục VI của bài báo "Privacy-Preserving Federated Synthetic Data Generation for Intrusion Detection in MQTT-Based IoT Gateways". Một người trình bày cả bộ. Mọi con số lấy từ `chapters/main/*.tex` trên nhánh IEEE.

## Cách dùng file này

Mỗi slide có ba phần. Phần "Trên slide" nhắc nhanh slide đang hiện gì, để lời nói khớp với hình. Phần "Lời nói" là đoạn tiếng Anh để nói lên, và chỉ phần này được tính giờ. Phần "Hiểu để nói" giải thích bằng tiếng Việt: vì sao câu tiếng Anh nói như vậy, từng ký hiệu trong công thức nghĩa là gì, con số đến từ đâu, và nếu bị hỏi thì trả lời từ chỗ nào. Phần này không đọc lên.

Nên học theo thứ tự: đọc "Hiểu để nói" của một slide cho hiểu, rồi mới tập nói "Lời nói" của slide đó. Khi đã hiểu, câu tiếng Anh dễ nhớ hơn nhiều so với học thuộc lòng.

Số trong file ghi theo kiểu của bài báo (dấu chấm thập phân, dấu phẩy hàng nghìn: 0.448, 88,500) để khớp với slide. Cuối file có phần câu hỏi dự kiến (Q1 đến Q14), bảng những câu không được nói và danh sách việc cần kiểm tra trước khi lên trình bày.

## Thời lượng

Tính ở tốc độ 125 từ mỗi phút, tốc độ vừa phải cho một bài kỹ thuật nói bằng tiếng Anh. Cột "Số từ khi nói" đếm số như lúc đọc lên: "0.448" là bốn từ ("point four four eight"), không phải một. Các slide kết quả nhiều số nên tốn giờ hơn số chữ trông thấy. Cột "Giây" đã làm tròn đến 5 giây.

| Slide | Mục trong bài báo | Số từ khi nói | Giây |
| --- | --- | --- | --- |
| 1 | I. Introduction | 51 | 25 |
| 2 | I. Introduction | 88 | 40 |
| 3 | I. Introduction | 70 | 35 |
| 4 | II. Related Work | 75 | 35 |
| 5 | II. Related Work | 67 | 30 |
| 6 | II. Related Work | 74 | 35 |
| 7 | III. System Model and Methodology | 79 | 40 |
| 8 | III. System Model and Methodology | 118 | 55 |
| 9 | III. System Model and Methodology | 83 | 40 |
| 10 | III. System Model and Methodology | 91 | 45 |
| 11 | IV. Experimental Setup | 76 | 35 |
| 12 | IV. Experimental Setup | 77 | 35 |
| 13 | V. Results and Discussion | 89 | 45 |
| 14 | V. Results and Discussion | 88 | 40 |
| 15 | V. Results and Discussion | 92 | 45 |
| 16 | V. Results and Discussion | 87 | 40 |
| 17 | V. Results and Discussion | 98 | 45 |
| 18 | V. Results and Discussion | 84 | 40 |
| 19 | V. Results and Discussion | 75 | 35 |
| 20 | VI. Conclusion | 94 | 45 |
| Tổng | | 1,656 | khoảng 13 phút 15 giây |

Ở 125 từ mỗi phút, cả bài mất khoảng 13 phút 15 giây; cộng chừng 15 giây chuyển slide là khoảng 13 phút 30 giây. Nói chậm hơn, ở 120 từ mỗi phút, thì khoảng 13 phút 50 giây, tức khoảng 14 phút 05 giây kể cả chuyển slide. Vẫn dưới 15 phút, còn gần một phút dự phòng cho lúc ngập ngừng hay chỉ vào hình.

Khi tập, bấm giờ thật. Nếu lần tập đầu quá 14 phút, bỏ các câu trong bảng dưới trước, rồi mới tính chuyện nói nhanh hơn. Đừng nói nhanh để kịp giờ: người nghe sẽ bỏ lỡ con số.

| Slide | Câu có thể bỏ | Tiết kiệm |
| --- | --- | --- |
| 5 | "SMOTE needs the minority records pooled." | khoảng 3 giây |
| 7 | "Both generators use this architecture." | khoảng 3 giây |
| 14 | ", and it needs 2,593 rounds and about 7.7 gigabytes" (câu kết thúc ở "loses at 5 and 10.") | khoảng 6 giây |
| 18 | "Table VI applies it to eleven scenarios." | khoảng 3 giây |
| 19 | "Synthetic packets also remain easy to tell from real ones." | khoảng 5 giây |

Bỏ hết năm chỗ này tiết kiệm khoảng 20 giây. Ngược lại, nếu tập thấy còn dư giờ, phần "Hiểu để nói" của slide 8, 10, 12 và 20 có ghi câu nào có thể nói thêm.

## Đọc đúng các từ khó

Phiên âm IPA theo giọng Mỹ. Cột cuối chỉ là cách đọc gần đúng để nhớ.

| Từ | IPA | Đọc gần giống |
| --- | --- | --- |
| MQTT | /ˌɛm kjuː tiː ˈtiː/ | em-kiu-ti-ti |
| epsilon (ε) | /ˈɛpsəlɑːn/ | ép-xơ-lan |
| delta (δ) | /ˈdɛltə/ | đeo-tơ |
| mu (μ) | /mjuː/ | miu |
| Skellam | /ˈskɛləm/ | xkê-lầm |
| Poisson | /ˈpwɑːsɑːn/ | poa-xan |
| Rényi | /ˈreɪnji/ | rây-nhi |
| Dirichlet | /ˌdɪrɪˈkleɪ/ | đi-ri-clây |
| Chow-Liu | /tʃaʊ ljuː/ | chao-liu |
| Pareto | /pəˈreɪtoʊ/ | pơ-rây-tâu |
| quantile | /ˈkwɑːntaɪl/ | quan-tai-ồ |
| synthetic | /sɪnˈθɛtɪk/ | xin-the-tíc |
| aggregation | /ˌæɡrɪˈɡeɪʃən/ | ắc-gri-gây-shần |
| autoencoder | /ˌɔːtoʊɪnˈkoʊdər/ | o-tâu-in-câu-đơ |
| inference | /ˈɪnfərəns/ | in-phơ-rần-x |
| curious | /ˈkjʊriəs/ | kiu-ri-ợt |
| SMOTE | /smoʊt/ | xmâut |
| PCAP | /ˈpiːkæp/ | pi-cáp |
| CVAE | /ˌsiː viː eɪ ˈiː/ | xi-vi-ây-i |
| SecAgg+ | /ˈsɛk æɡ plʌs/ | xéc-ác pờ-lớt |
| FedAvg | đọc là "Fed-Average" | phét-a-vờ-rịt |
| macro-F1 | /ˈmækroʊ ɛf ˈwʌn/ | méc-crâu ép-oăn |
| bootstrap | /ˈbuːtstræp/ | bút-xtrép |

## Đọc số và tên cấu hình

| Viết | Đọc |
| --- | --- |
| 0.448 | "zero point four four eight" |
| 0.48 to 0.53 MB | "zero point four eight to zero point five three megabytes" |
| 13.6 to 72.4 | "thirteen point six to seventy-two point four" |
| 1.39 times | "one point three nine times" |
| ε = 1, 5, 10 | "epsilon one, five and ten" |
| δ = 10^-5 | "delta ten to the minus five" |
| 2^32 | "two to the thirty-two" |
| 39,000,601 | "about thirty-nine million" (slide ghi số đủ) |
| 88,500 | "eighty-eight thousand five hundred" |
| 2,593 | "two thousand five hundred ninety-three" |
| 60:1 | "sixty to one" |
| RQ1 | "R-Q-one" |
| B1a | "B-one-A" |
| MGr-eps5 | "M-G-R at epsilon five" |
| MGs-t3-eps1 | "M-G-S, T-three, epsilon one" |
| MGr-t2-eps5 | "M-G-R, T-two, epsilon five" |

## Tên cấu hình trong bài

Bảng này dùng cho cả bài. Khi gặp một tên lạ trên slide, quay lại đây.

| Tên | Nghĩa |
| --- | --- |
| B0 | RF trên dữ liệu thật gộp, mất cân bằng (TRTR) |
| B1a | Như B0, thêm class weights |
| B1b | Như B0, thêm SMOTE |
| B3 | CVAE liên kết, không bảo vệ, FedAvg 30 vòng |
| M1-eps{1,5,10} | CVAE và DP-SGD tại mỗi gateway (client-side DP) |
| M2 | CVAE và SecAgg+ |
| M3-eps5 | CVAE, DP-SGD và SecAgg+ |
| M1o, M3o | M1, M3 tinh chỉnh lại theo từng ε ở quy mô liên kết đầy đủ, 15 đến 50 vòng |
| MGp-nodp | FedDP-Marginal không nhiễu, cộng bảng bằng vòng Flower thường |
| MGs-nodp | Như trên, nhưng cộng qua SecAgg+ |
| MGs-eps{1,5,10} | Nhiễu Skellam chia qua các gateway, cộng qua SecAgg+ |
| MGr-eps{1,5,10} | MGs thêm hậu xử lý, không tốn thêm ε |
| MGl-eps{1,5,10} | Mỗi gateway thêm đủ nhiễu (client-side DP), cộng thường |
| MGd | Ablation: nhiễu Gauss chia qua gateway, tổng an toàn mô phỏng trong một tiến trình |
| MGb | Ablation: mạng Bayes bậc hai thay cho cây |
| FedMLP | IDS dạng MLP huấn luyện trực tiếp bằng FL, không dùng dữ liệu sinh |
| Hậu tố -t2, -t3 | Mỗi gateway thêm 1/t phần nhiễu; ε giữ đúng khi có ít nhất t gateway trung thực |
| Hậu tố -strm1, -cap50 | Bảo vệ cả một TCP stream (tối đa m = 1 gói) hoặc cả một capture (tối đa m = 50 gói) |
| MG-eps1, MG-eps5, MG-eps10 | Tên chung của cấu hình chính: MGs-eps1, MGr-eps5, MGs-eps10 |

---

## I. Introduction

### Slide 1. Privacy-Preserving Federated Synthetic Data Generation for Intrusion Detection in MQTT-Based IoT Gateways (25 giây)

Trên slide: tên bài, 8 tác giả, Faculty of Information Assurance, FPT University. Không có logo.

#### Lời nói

> Good morning. My name is [your name], and I will present our paper on privacy-preserving federated synthetic data generation for intrusion detection in MQTT-based IoT gateways. Our main finding: synthetic traffic is useful where raw traffic must stay on the gateway, and adds almost nothing when real data can be pooled.

#### Hiểu để nói

Thay `[your name]` bằng tên người trình bày.

Câu kết luận được nói ngay từ slide đầu để người nghe biết cả bài đi về đâu. Câu này có hai vế và phải nói đủ cả hai. Vế một: dữ liệu sinh có ích khi lưu lượng thô không được rời gateway. Vế hai: khi đã gộp được dữ liệu thật về một chỗ thì dữ liệu sinh gần như không thêm gì. Đây cũng là lý do tên bài hiện tại không còn chữ "Enhanced" của bản cũ: người hướng dẫn nhận xét tên cũ hứa quá mức.

Tách tên bài ra cho dễ nhớ:

| Cụm từ | Nghĩa trong bài |
| --- | --- |
| Privacy-Preserving | Bảo vệ quyền riêng tư của từng gói tin trong dữ liệu huấn luyện |
| Federated | Nhiều gateway cùng làm; gói thô nằm lại ở gateway, chỉ gửi đi thứ đã được bảo vệ |
| Synthetic Data Generation | Sinh ra gói tin giả nhưng mang thống kê của gói thật |
| Intrusion Detection | IDS: bộ phân loại đoán một gói là bình thường hay thuộc họ tấn công nào |
| MQTT-Based IoT Gateways | Bối cảnh: các gateway IoT có lưu lượng MQTT đi qua |

---

### Slide 2. Rare attacks are scattered, and each protection answers a different threat (40 giây)

Trên slide: MQTT và DoS/DDoS [1]; FL giữ dữ liệu tại chỗ [2] nhưng gradient có thể lộ dữ liệu [3]; lớp hiếm phân tán non-IID; SecAgg+ che từng gateway [5], [6]; DP giới hạn điều đầu ra tiết lộ [7].

#### Lời nói

> MQTT brokers can be flooded with denial-of-service attacks, and the labeled traffic an IDS needs sits on gateways that cannot pool it. Federated learning keeps data local, yet two problems remain. Rare attacks are scattered: one gateway holds a few packets of a rare attack, another none. And model updates can still leak training records. Secure aggregation hides each gateway's update from the server; differential privacy limits what the result reveals about one record. Our starting point: a count table is a sum, exactly what secure aggregation computes.

#### Hiểu để nói

MQTT chạy theo kiểu publish-subscribe. Thiết bị IoT gửi (publish) message lên broker theo một topic, thiết bị khác đăng ký (subscribe) topic đó để nhận. Broker là điểm trung tâm, nên khi attacker flood broker bằng kết nối hoặc message giả thì mọi thiết bị phía sau đều bị ảnh hưởng. Bộ dữ liệu có năm họ tấn công kiểu này, mỗi họ có bản DoS (từ một nguồn) và bản DDoS (từ nhiều nguồn).

Gateway là máy đứng giữa thiết bị IoT và mạng, nên nó thấy lưu lượng MQTT đi qua. Mỗi gateway chỉ thấy phần của mình. Vì lý do bảo mật hay quy định, các gateway không gửi gói thô về một chỗ.

Federated learning (FL) chạy theo vòng. Server gửi mô hình xuống, mỗi gateway huấn luyện trên gói tin của mình, gửi phần cập nhật lên, server lấy trung bình (FedAvg) rồi gửi mô hình mới xuống. Gói thô không rời gateway. Nhưng phần cập nhật được tính từ chính các gói đó, nên vẫn có thể dựng lại một phần dữ liệu huấn luyện từ gradient. Bài trích nghiên cứu của Zhu và cộng sự (2019) cho ý này.

Non-IID nghĩa là dữ liệu ở các gateway không cùng phân phối. Ví dụ trong bài: lớp WILL chỉ có 1,000 gói trong tập train. Sau khi chia cho 5 gateway theo Dirichlet (slide 7), có gateway gần như không có gói WILL nào. IDS chỉ học trên dữ liệu của gateway đó sẽ không bao giờ đoán ra WILL.

Hai lớp bảo vệ trả lời hai câu hỏi khác nhau, nên không thay thế được nhau:

| Lớp bảo vệ | Câu hỏi nó trả lời | Điều nó không làm |
| --- | --- | --- |
| SecAgg+ | Server có thấy bảng hay cập nhật của từng gateway không? Không, server chỉ thấy tổng | Không giới hạn điều mà tổng, mô hình hay dữ liệu sinh tiết lộ |
| DP | Kết quả cuối tiết lộ được bao nhiêu về một gói tin? Bị chặn bởi ε | Không che bảng của từng gateway trước server, trừ khi mỗi gateway tự thêm đủ nhiễu |

Câu cuối của slide dẫn sang phương pháp. Bảng đếm (count table) đếm số gói rơi vào mỗi ô. Ví dụ bảng của cột message type theo lớp: mỗi ô là số gói có một giá trị message type và một nhãn lớp. Cộng bảng của 5 gateway lại thì ra đúng bảng của toàn bộ dữ liệu. SecAgg chỉ tính được tổng, nên bảng đếm khớp với SecAgg một cách tự nhiên. Mô hình sâu thì phải gửi cả bộ trọng số qua nhiều vòng (slide 5).

---

### Slide 3. Four research questions, no new synthesis algorithm (35 giây)

Trên slide: RQ1 đến RQ4, mỗi câu một dòng; ba đóng góp: giao thức ba lần gửi, so sánh có kiểm soát, hướng dẫn cấu hình.

#### Lời nói

> We ask four questions. RQ1: how useful are federated synthetic data when raw traffic cannot be pooled, and when it can? RQ2: at equal privacy budgets, how does a marginal generator compare with a CVAE trained with DP-SGD? RQ3: what does each protection cost and protect? RQ4: which configuration fits a deployment? We claim no new synthesis algorithm; we contribute a three-release protocol, a controlled comparison, and a configuration guide.

#### Hiểu để nói

| RQ | Hỏi bằng lời thường | Trả lời ở slide |
| --- | --- | --- |
| RQ1 | Dữ liệu sinh còn giữ được bao nhiêu độ hữu ích cho IDS khi không gộp được dữ liệu thật? Khi gộp được rồi thì có thêm gì không? | 13, 14 |
| RQ2 | Cùng một ngân sách riêng tư (ε, δ), bộ sinh dựa trên bảng đếm (FedDP-Marginal) so với CVAE huấn luyện bằng DP-SGD thế nào, về macro-F1, recall lớp hiếm và lượng dữ liệu truyền? | 15 |
| RQ3 | Mỗi lớp bảo vệ (DP, SecAgg+, cả hai) tốn gì và che được gì, khi đổi đơn vị bảo vệ (gói, TCP stream, capture) và số gateway trung thực? | 16, 17 |
| RQ4 | Một triển khai cụ thể nên chọn cấu hình nào theo yêu cầu về tin cậy, riêng tư và băng thông? | 18 |

"Utility" (độ hữu ích) trong bài luôn là macro-F1 của IDS trên tập test thật (macro-F1 giải thích ở slide 12).

CVAE là conditional variational autoencoder. Một mạng nén gói tin thành một vector ẩn z, một mạng khác dựng lại gói tin từ z. Chữ "conditional" nghĩa là nhãn lớp được đưa vào cả hai mạng, nên khi sinh ta chọn được lớp muốn sinh. DP-SGD là cách huấn luyện mạng nơ-ron có DP (công thức (8), slide 10).

Câu "We do not claim a new synthesis algorithm" bắt buộc phải nói. FedDP-Marginal dựa trên cây Chow-Liu (1968) và phương pháp MST; FLAIM và CaPS đã đưa họ marginal lên dữ liệu phân tán. Ba đóng góp của bài:

1. Giao thức ba lần gửi cho gateway IoT-MQTT. Mỗi gateway thêm một phần nhiễu Skellam số nguyên vào bảng đếm, rồi các bảng được cộng qua SecAgg+ của Flower. ε được tính chính xác và báo cho mọi số gateway trung thực. Có thêm tùy chọn ngưỡng gateway trung thực, client-side DP, và bảo vệ theo stream hay capture.
2. So sánh có kiểm soát với một CVAE liên kết: cùng phân vùng, cùng ngân sách, cùng SecAgg+, cùng cách đánh giá. Nhờ vậy tách riêng được chi phí của DP, chi phí của SecAgg+ và ảnh hưởng của họ bộ sinh.
3. Hướng dẫn chọn cấu hình theo yêu cầu triển khai: lọc cấu hình theo tin cậy, ngân sách, băng thông và loại tấn công ưu tiên, rồi chọn trên Pareto front.

---

## II. Related Work

### Slide 4. Privacy protection in FL: DP, secure aggregation, and both (35 giây)

Trên slide: DP [7], client-side DP, DP-SGD [12], RDP [21]; SecAgg [5], SecAgg+ [6]; DP phân tán [16], [17].

#### Lời nói

> Of the privacy techniques used in this field, multi-party computation, trusted hardware and blockchain are heavy for small gateways, so we use differential privacy and secure aggregation. Differential privacy adds calibrated noise so the output barely depends on any one record; in client-side DP, each gateway adds enough noise for its own release to be private. Distributed DP combines both: each gateway adds a share of the noise, and only the noisy sum is revealed.

#### Hiểu để nói

Khảo sát của Vyas và cộng sự (2024) chia kỹ thuật bảo vệ riêng tư cho FL trong IDS IoT thành năm họ: DP, mã hóa đồng cấu (homomorphic encryption), tính toán đa bên an toàn (MPC), vùng thực thi tin cậy trên chip (TEE) và blockchain. Bài nói ba họ cuối cần tính toán nặng, phần cứng đặc biệt hoặc chi phí đồng thuận, không hợp với gateway nhỏ. Bài không đánh giá mã hóa đồng cấu. Nếu bị hỏi, nói thật như vậy.

Định nghĩa DP, để hiểu chứ không cần nói. Một thuật toán M là (ε, δ)-DP nếu với hai tập dữ liệu D và D' chỉ khác nhau một gói tin, và với mọi tập kết quả S:

```
P[ M(D) ∈ S ]  ≤  e^ε · P[ M(D') ∈ S ]  +  δ
```

| Ký hiệu | Nghĩa |
| --- | --- |
| M | Thuật toán công bố. Ở FedDP-Marginal là cả ba lần gửi bảng đếm có nhiễu |
| D, D' | Hai tập train giống hệt nhau, chỉ khác một gói tin |
| S | Một tập kết quả bất kỳ mà attacker quan tâm |
| e^ε | Hệ số tối đa mà xác suất được phép thay đổi khi thêm hay bớt một gói. ε càng nhỏ thì kết quả trên D và D' càng khó phân biệt |
| δ | Xác suất nhỏ mà bảo đảm được phép không giữ. Bài dùng δ = 10^-5 |

Nói gọn: nhìn vào kết quả, attacker khó đoán một gói cụ thể có nằm trong tập huấn luyện hay không.

Ba cách đặt nhiễu:

| Mô hình | Nhiễu thêm ở đâu | Đổi lại |
| --- | --- | --- |
| Central DP | Một bên tin cậy giữ toàn bộ dữ liệu, thêm nhiễu một lần vào kết quả | Ít nhiễu nhất, nhưng phải tin bên giữ dữ liệu |
| Local DP cổ điển | Từng bản ghi bị làm nhiễu trước khi rời chủ | Không cần tin ai, nhưng nhiễu lớn hơn nhiều |
| Client-side DP (bài dùng) | Mỗi gateway thêm đủ nhiễu để phần nó gửi đi tự thỏa DP | Không cần tin server hay gateway khác; mức nhiễu ở giữa hai cách trên |

Luôn nói "client-side DP", không gọi MGl là "local DP".

RDP (Rényi DP) là một thước đo mất mát riêng tư có ưu điểm là cộng dồn dễ qua nhiều lần công bố, rồi cuối cùng đổi về (ε, δ). Chi tiết ở slide 9.

SecAgg (Bonawitz và cộng sự, 2017) chạy thế này. Mỗi cặp gateway thỏa thuận một mặt nạ ngẫu nhiên chung. Gateway này cộng mặt nạ vào vector của mình, gateway kia trừ đi. Từng vector gửi lên trông như số ngẫu nhiên, nhưng khi server cộng tất cả lại thì các mặt nạ triệt tiêu, chỉ còn tổng thật. Secret sharing giúp khôi phục mặt nạ nếu có gateway rớt giữa chừng. SecAgg+ (Bell và cộng sự, 2020) chỉ ghép mỗi gateway với một số hàng xóm theo một đồ thị ngẫu nhiên thưa, nên chi phí tăng chậm theo số client (polylog). SecAgg không thêm nhiễu, nên nó không cho bảo đảm DP nào.

DP phân tán (distributed DP) ghép hai thứ: mỗi gateway thêm một phần nhiễu, SecAgg chỉ lộ tổng, và tổng mang đủ nhiễu. Vì SecAgg làm trên số nguyên modulo 2^b, nhiễu phải là số nguyên: Kairouz (2021) dùng discrete Gaussian, Agarwal (2021) dùng Skellam. Cả hai áp cho huấn luyện FL nhiều vòng. Bảng đếm, mỗi bảng chỉ là một tổng, khớp với cách này đơn giản hơn.

---

### Slide 5. Synthetic data for IDS, and the marginal alternative (30 giây)

Trên slide: bên trái SMOTE [22], GAN và VAE [8], [9], [10], [11]; bên phải PrivBayes [13], MST [14], AIM [15], FLAIM [18], CaPS [19].

#### Lời nói

> For synthetic attack traffic, studies use SMOTE, GANs or variational autoencoders. SMOTE needs the minority records pooled. Federated generators exchange full models over many rounds, and the closest studies apply no secure aggregation to generator updates. Marginal methods such as PrivBayes, MST and AIM sample records from noisy low-order count tables. FLAIM and CaPS bring them to distributed data, but were tested mainly on general tabular benchmarks.

#### Hiểu để nói

| Phương pháp | Làm gì |
| --- | --- |
| SMOTE | Tạo gói mới nằm giữa hai gói thiểu số gần nhau (nội suy). Cần các gói thiểu số ở cùng một chỗ, nên không dùng được khi gateway chỉ có vài gói hoặc không có gói nào. Trong bài, B1b (RF và SMOTE trên dữ liệu gộp) chỉ là mốc tham chiếu |
| GAN | Hai mạng thi nhau: mạng sinh tạo gói giả, mạng phân biệt đoán thật hay giả. Hay gặp mode collapse (chỉ sinh ra vài kiểu mẫu) và huấn luyện không ổn định |
| VAE | Họ của CVAE (slide 3) |
| PrivBayes | Dựng mạng Bayes từ các marginal bậc thấp có nhiễu |
| MST | Đo marginal hai chiều có nhiễu theo cây khung lớn nhất, rồi hậu xử lý bằng mô hình đồ thị. FedDP-Marginal gần MST nhất |
| AIM | Chọn marginal nào để đo một cách thích nghi, lặp nhiều lần |
| FLAIM | AIM cho các client liên kết, dùng zero-concentrated DP, có so với một biến thể MPC |
| CaPS | Chọn và đo marginal bên trong MPC ("DP-in-MPC") |

Marginal là bảng đếm theo một hay vài cột. "Low-order" (bậc thấp) nghĩa là một hoặc hai cột, không phải cả 37 cột cùng lúc.

Ba nghiên cứu sinh dữ liệu cho IDS gần nhất:

| Nghiên cứu | Làm gì | Thiếu gì so với bài |
| --- | --- | --- |
| Hamouda 2024 | GAN có điều kiện huấn luyện liên kết trên Edge-IIoTset | DP chỉ áp cho bộ phân loại, không cho bộ sinh |
| Yao 2024 | Secret sharing cho chiều server gửi mẫu xuống | Gradient chiều lên chỉ dùng DP Gauss |
| Shettar 2026 | F1 96.8% với aggregator trung tâm, DP ở ε = 4.8 | Không có secure aggregation cho cập nhật của bộ sinh |

Không so 96.8% của Shettar với macro-F1 6 lớp của bài: khác bộ dữ liệu, khác bài toán, khác metric.

FLAIM có dùng dữ liệu IDS cũ của DARPA, nhưng đo lỗi workload và negative log-likelihood, không đo khả năng phát hiện lớp hiếm. Đó là chỗ trống mà slide 6 nói tới.

Điểm yếu của họ marginal, nói khi bị hỏi: chỉ nắm phụ thuộc bậc thấp, phải rời rạc hóa cột liên tục thành bin, và ô thưa có tín hiệu nhỏ so với nhiễu.

---

### Slide 6. No prior study combines these on IoT-MQTT traffic (35 giây)

Trên slide: Table I rút gọn ([9], [10], [11], FLAIM, CaPS, PP-FedData) và ba khoảng trống (i), (ii), (iii).

#### Lời nói

> Table I compares the closest work. From a non-systematic search, and to the best of our knowledge, no prior study has evaluated a federated marginal generator on IoT-MQTT traffic for rare-class detection, compared it with a federated deep generator under identical conditions, or combined distributed discrete DP with a working secure aggregation and reported the guarantee for every number of honest gateways. Each part is known; we add the combination and the controlled comparison.

#### Hiểu để nói

Đọc Table I:

| Cột | Nghĩa |
| --- | --- |
| FL | Có huấn luyện liên kết |
| IoT | Dùng dữ liệu IoT |
| Syn. | Có sinh dữ liệu |
| DP | Có DP |
| SA | Có secure aggregation hoặc MPC |
| Marg. | Sinh dữ liệu dựa trên marginal có DP |
| D-DP | DP phân tán (nhiễu chia qua các client) |
| IDS | Có đánh giá phát hiện xâm nhập ở hạ nguồn |

Dấu ✓ là có, ✗ là không, ○ là một phần (Hamouda có DP nhưng ở bộ phân loại; Yao có secret sharing nhưng chỉ ở chiều xuống).

Câu "From a non-systematic search, and to the best of our knowledge" bắt buộc phải nói. Nhóm không tra cứu theo quy trình hệ thống (có giao thức tìm kiếm và tiêu chí chọn bài), nên không được khẳng định tuyệt đối là chưa ai làm. Không dùng chữ "first" hay "novel".

Ba khoảng trống nói bằng lời thường:

| Khoảng trống | Nghĩa |
| --- | --- |
| (i) | Chưa ai đo một bộ sinh marginal liên kết trên lưu lượng IoT-MQTT bằng khả năng phát hiện lớp hiếm của IDS. FLAIM và CaPS đo trên bảng dữ liệu tổng quát |
| (ii) | Chưa ai so bộ sinh marginal liên kết với một bộ sinh sâu liên kết trong cùng điều kiện: cùng phân vùng, cùng ngân sách, cùng secure aggregation |
| (iii) | Chưa ai ghép DP phân tán số nguyên với một bản secure aggregation chạy thật và báo ε theo số client trung thực |

Hàng PP-FedData có dấu ✓ ở mọi cột, nhưng đó là nhờ ghép các phần đã có. Câu cuối của lời nói nói đúng điều này.

---

## III. System Model and Methodology

### Slide 7. Gateways keep raw traffic, the server sees only protected releases (40 giây)

Trên slide: Fig. 1; K = 5 gateway; chia non-IID Dirichlet α_dir = 0.5 [23]; server honest-but-curious.

#### Lời nói

> Figure 1 shows the system. Five gateways keep their MQTT packets. A server rebuilds a generator from the protected releases and samples synthetic packets; an IDS is trained on them and tested on real traffic. Both generators use this architecture. Each class is split across the gateways with Dirichlet shares, alpha 0.5, so some gateways get almost no packets of a rare class. The server is honest-but-curious, and labels, class quotas and preprocessing statistics are treated as public.

#### Hiểu để nói

Fig. 1 có ba bên: các gateway giữ gói tin, server tổng hợp, và IDS ở hạ nguồn. Hai nhánh sinh dùng chung kiến trúc này: FedDP-Marginal gửi bảng đếm ba lần, CVAE gửi trọng số qua hàng chục vòng FedAvg. Chung kiến trúc thì so sánh mới công bằng.

Công thức (1), chia non-IID theo cách của Hsu và cộng sự:

```
p_c = (p_{c,1}, ..., p_{c,K})  ~  Dir(α_dir · 1_K)
```

| Ký hiệu | Nghĩa |
| --- | --- |
| c | Một lớp, từ 1 đến C = 6 |
| K | Số gateway, K = 5 |
| p_{c,k} | Tỉ lệ gói của lớp c đi về gateway k. Năm tỉ lệ cộng lại bằng 1 |
| Dir(...) | Phân phối Dirichlet: rút ngẫu nhiên một bộ K tỉ lệ có tổng bằng 1 |
| 1_K | Vector gồm K số 1: trước khi rút, không gateway nào được ưu tiên |
| α_dir | Độ đều. α nhỏ (0.5) cho tỉ lệ lệch: vài gateway nhận phần lớn, số khác gần như không có gì. α lớn cho tỉ lệ gần đều |

Sau khi rút p_c, mỗi gói của lớp c đi về gateway k với xác suất p_{c,k}. Phân vùng được rút một lần cho mỗi seed và dùng chung cho mọi cấu hình.

Một điểm đáng nhớ: với FedDP-Marginal, tổng các bảng không nhiễu không phụ thuộc cách chia gói, và tổng nhiễu không phụ thuộc K khi t = K. Bài có chạy thử một seed MGs ở ε = 5: α_dir = 0.1 và 10 cho cùng 0.398; 10 và 20 gateway cho 0.400 và 0.415.

Honest-but-curious: server chạy đúng giao thức nhưng tò mò, xem xét mọi thứ nó nhận được. Gateway cũng chạy đúng giao thức. Poisoning (gửi dữ liệu độc để làm hỏng mô hình) và Byzantine (hành xử tùy ý) nằm ngoài phạm vi. Nếu bị hỏi về poisoning, nói thẳng là ngoài phạm vi.

Thông tin coi là công khai, nằm ngoài ε: nhãn lớp, quota lớp, số mẫu của mỗi gateway và thống kê tiền xử lý. Đây là một giới hạn, sẽ nhắc lại ở slide 19.

---

### Slide 8. Three noisy releases build one Chow-Liu tree (55 giây)

Trên slide: Fig. 2 ở nửa trên; công thức (2) và (3) ở nửa dưới; d = 37 thuộc tính, 64 bin mịn, 666 cặp.

#### Lời nói

> FedDP-Marginal models 37 attributes per packet, and Figure 2 shows its three releases. In Release 1, each gateway counts every attribute per class on 64 fine bins; from the noisy sum, the server places coarse bins at the quantiles. In Release 2, gateways count all 666 attribute pairs, pooled over classes. The server estimates each pair's mutual information and builds one Chow-Liu tree, the tree with the largest total, Equation 2. Pooling is deliberate: a split by class would cut the signal per cell about six times, with the same noise. In Release 3, gateways count the root and every tree edge per class, and the server samples each class from root to leaves, Equation 3.

#### Hiểu để nói

Đây là slide khó nhất. Hiểu được slide này thì phần còn lại của Mục III dễ hơn nhiều.

37 thuộc tính khác với 59 cột. 59 là số đặc trưng sau one-hot, dùng cho CVAE và IDS. 37 là thuộc tính gốc, dùng cho bảng đếm:

| Loại | Số lượng | Cách đếm |
| --- | --- | --- |
| Số (numeric) | 13 | Đã chuẩn hóa và cắt ở ±5, chia 64 bin đều trên đoạn [-5, 5] (bin mịn) |
| Nhị phân (binary) | 19 | 7 cờ giao thức và 12 cờ thiếu giá trị |
| Phân loại (categorical) | 5 | Message type, hai trường QoS, requested QoS, protocol |

Release 1: 37 bảng, mỗi bảng là một thuộc tính theo lớp, trên bin mịn. Server cộng xong có histogram nhiễu của từng cột số. Từ đó server đặt B_coarse bin thô tại các phân vị (quantile), nghĩa là mỗi bin thô chứa xấp xỉ cùng số gói. Server gửi cut point (ranh giới bin thô) về các gateway. Đặt bin từ histogram đã có nhiễu là hậu xử lý, không tốn thêm ε.

Release 2: C(37, 2) = 37 × 36 / 2 = 666 cặp thuộc tính. Mỗi bảng đếm số gói có giá trị a ở cột i và giá trị b ở cột j, trên bin thô, gộp mọi lớp lại.

Mutual information (MI) đo hai cột phụ thuộc nhau đến đâu:

```
Î(X_i; X_j) = Σ_{a,b}  p̂(a,b) · log[ p̂(a,b) / ( p̂(a) · p̂(b) ) ]
```

| Ký hiệu | Nghĩa |
| --- | --- |
| X_i, X_j | Hai thuộc tính |
| a, b | Một giá trị (một bin) của X_i và của X_j |
| p̂(a,b) | Tỉ lệ gói có cùng lúc X_i = a và X_j = b, lấy từ bảng cặp có nhiễu (số âm cắt về 0, rồi làm trơn) |
| p̂(a), p̂(b) | Tỉ lệ riêng của từng cột |
| log[...] | Bằng 0 khi p̂(a,b) = p̂(a)·p̂(b), tức hai cột độc lập ở ô đó |

Hai cột độc lập thì MI = 0. Biết cột này càng đoán được cột kia thì MI càng lớn.

Cây Chow-Liu, công thức (2):

```
T* = argmax_T  Σ_{(i,j) ∈ T}  Î(X_i; X_j)
```

| Ký hiệu | Nghĩa |
| --- | --- |
| T | Một cây nối cả 37 thuộc tính bằng 36 cạnh, không có vòng |
| (i, j) ∈ T | Một cạnh của cây |
| argmax_T | Chọn cây có tổng MI lớn nhất |

Cách tìm: sắp 666 cặp theo MI giảm dần, lấy lần lượt từng cặp, bỏ cặp nào tạo vòng (thuật toán Kruskal). Chow và Liu (1968) chỉ ra rằng cây có tổng MI lớn nhất cho phân phối xấp xỉ sát nhất trong các phân phối có dạng cây.

Vì sao gộp lớp ở Release 2: độ nhạy không đổi dù chia hay gộp (một gói vẫn chạm đúng một ô mỗi bảng), nhưng chia theo 6 lớp làm mỗi ô có ít gói hơn khoảng 6 lần trong khi nhiễu giữ nguyên. Tín hiệu nhỏ so với nhiễu thì MI ước lượng sai, và cây sai. Thông tin riêng của từng lớp vào ở Release 3.

Release 3: bảng (root, y) và bảng (parent, child, y) cho 36 cạnh, tổng cộng 37 bảng, trên bin thô. Root là thuộc tính gốc của cây, y là nhãn lớp.

Lấy mẫu, công thức (3):

```
P̂(x | c) = P̂(x_r | c) · Π_{(u,v) ∈ T*}  P̂(x_v | x_u, c)
```

| Ký hiệu | Nghĩa |
| --- | --- |
| x | Một gói gồm 37 thuộc tính |
| c | Lớp cần sinh |
| r | Thuộc tính gốc |
| (u, v) | Một cạnh, hướng từ gốc ra: u là cha, v là con |
| P̂(x_v \| x_u, c) | Tỉ lệ lấy từ bảng (u, v, y) tại hàng có giá trị cha x_u và lớp c |

Lấy mẫu từng bước: với lớp c, rút giá trị root theo bảng (root, y = c). Đi xuống từng cạnh, rút giá trị con theo hàng của giá trị cha vừa rút. Đi hết cây là có một gói 37 thuộc tính trên bin thô. Cột số được tinh chỉnh từ bin thô về bin mịn nhờ histogram của lớp đó ở Release 1, rồi rút đều trong bin mịn. Cuối cùng đảo tiền xử lý để ra 59 đặc trưng cho IDS.

Lời nói không nhắc MGr để đủ giờ. Nếu còn dư giờ, thêm câu "The refined variant, MGr, fuses the noisy estimates as post-processing, at no extra privacy cost." Nếu bị hỏi vì sao cấu hình chính ở ε = 5 là MGr-eps5, trả lời từ đoạn dưới.

MGr làm bốn việc: gộp mọi ước lượng nhiễu độc lập của cùng một marginal (từ Release 1 và từ các bảng cạnh chạm vào thuộc tính đó) theo trọng số nghịch đảo phương sai, tức ước lượng ít nhiễu được tin nhiều hơn; cắt số âm; khớp bảng cạnh với marginal đã gộp bằng IPF (iterative proportional fitting); và có thể đổi gốc sang thuộc tính có tổng MI lớn nhất. Vì chỉ biến đổi thứ đã công bố, MGr không tốn thêm ngân sách. Đây là tính chất post-processing của DP: xử lý gì trên kết quả DP mà không đụng lại dữ liệu thô thì kết quả vẫn DP với cùng ε.

---

### Slide 9. Exact accounting: sensitivity, Rényi bound, conversion (40 giây)

Trên slide: công thức (4), (5) [17, Cor. 3.6], (6) [24].

#### Lời nói

> The accounting is exact. One packet adds one count to one cell of every table, so a release of M tables has L1 sensitivity M and L2 sensitivity root M, Equation 4, times m for a unit of up to m packets. Each cell gets Skellam noise: an integer with mean zero that stays Skellam when summed. Equation 5 is its Rényi DP bound; the releases add up, and Equation 6 converts the total to epsilon, with delta ten to the minus five.

#### Hiểu để nói

Hai tập dữ liệu là láng giềng (neighbors) nếu chỉ khác nhau đúng một gói tin. ε nói về cặp láng giềng này.

Độ nhạy (sensitivity): khi thêm hoặc bớt một gói, kết quả thay đổi tối đa bao nhiêu. Nhiễu phải đủ lớn để che được mức thay đổi đó. Một gói rơi vào đúng một ô của mỗi bảng. Release r có M_r bảng (37, 666 và 37 cho ba lần gửi), nên thêm một gói làm M_r ô, mỗi ô tăng 1.

Công thức (4):

```
Δ_{1,r} = m · M_r          Δ_{2,r} = m · √M_r
```

| Ký hiệu | Nghĩa |
| --- | --- |
| Δ_{1,r} | Độ nhạy chuẩn L1: tổng giá trị tuyệt đối thay đổi. M_r ô, mỗi ô đổi 1, nên bằng M_r |
| Δ_{2,r} | Độ nhạy chuẩn L2: căn của tổng bình phương thay đổi, √(M_r × 1²) = √M_r |
| m | Số gói tối đa của một đơn vị (TCP stream hay capture) mà gateway được dùng. Mặc định đơn vị là một gói, m = 1 |

Ví dụ với m = 1: Release 2 có Δ_1 = 666 và Δ_2 = √666 ≈ 25.8; Release 1 và 3 có Δ_1 = 37 và Δ_2 = √37 ≈ 6.1. Bảo vệ một đơn vị gồm m gói thì mỗi bảng có thể đổi tới m, nên nhân cả hai với m. Mỗi đơn vị được gán cho đúng một gateway.

Skellam: Sk(μ) = Pois(μ/2) − Pois(μ/2). Poisson là phân phối của số đếm (0, 1, 2, ...), có trung bình bằng phương sai. Lấy hiệu hai số Poisson độc lập cùng tham số μ/2 thì được một số nguyên (có thể âm), trung bình 0, phương sai μ/2 + μ/2 = μ. Điểm mấu chốt: cộng các Skellam độc lập lại vẫn ra Skellam, và phương sai cộng dồn. Năm gateway, mỗi gateway thêm Sk(μ/5), tổng là Sk(μ). Đó là lý do chia nhiễu được (slide 10).

Ghi chú ký hiệu: Agarwal viết Skellam đối xứng là Sk_{μ,μ} với phương sai 2μ; bài viết lại theo phương sai cho gọn. Nếu ai đối chiếu với bài gốc thấy lệch hệ số 2 thì đây là lý do.

Công thức (5), bound RDP của Agarwal và cộng sự [Cor. 3.6]:

```
ε_r(λ) ≤ λ·Δ_{2,r}² / (2μ_r)
         + min( ((2λ − 1)·Δ_{2,r}² + 6·Δ_{1,r}) / (4μ_r²) ,  3·Δ_{1,r} / (2μ_r) )
```

| Ký hiệu | Nghĩa |
| --- | --- |
| λ | Bậc Rényi, số nguyên lớn hơn 1. Mỗi λ cho một cách đo; cuối cùng chọn λ tốt nhất |
| μ_r | Phương sai nhiễu mỗi ô ở release r |
| λ·Δ_2² / (2μ_r) | Phần chính, giống hệt cơ chế Gauss liên tục |
| min(...) | Phần phạt thêm vì nhiễu là số nguyên; μ_r càng lớn thì phần này càng nhỏ |

Nhìn nhanh: nhiễu lớn (μ_r lớn) thì ε_r nhỏ; độ nhạy lớn thì ε_r lớn.

Ba release cộng lại: RDP ở cùng bậc λ cộng thẳng, ε_1(λ) + ε_2(λ) + ε_3(λ).

Công thức (6), đổi về (ε, δ):

```
ε = min_λ [ Σ_{r=1..3} ε_r(λ)  −  (ln δ + ln λ) / (λ − 1)  +  ln((λ − 1) / λ) ]
```

Σ ε_r(λ) là tổng RDP. Hai số hạng sau là chi phí đổi từ RDP sang (ε, δ) với δ cho trước. min_λ nghĩa là thử mọi λ trong {2, ..., 63} ∪ {64, 72, ..., 1024} rồi lấy giá trị nhỏ nhất. Đây là công thức mà accountant của Opacus dùng.

Chia ngân sách cho ba release: μ_r = Δ_{2,r}² / (2 · s_r · κ).

| Ký hiệu | Nghĩa |
| --- | --- |
| s = (s_1, s_2, s_3) | Phần ngân sách cho từng release, cộng lại bằng 1. s_r lớn thì μ_r nhỏ, release đó ít nhiễu |
| κ | Hệ số chung, tìm bằng chia đôi (bisection) sao cho công thức (6) ra đúng ε mục tiêu |

Thiết lập được chọn trên validation:

| ε | Số bin thô | Chia ngân sách s |
| --- | --- | --- |
| 1 | 16 | (0.3, 0.1, 0.6) |
| 5 | 16 | (0.15, 0.05, 0.8) |
| 10 | 8 | (0.5, 0.1, 0.4) |

Việc chọn này nằm ngoài ε (giới hạn, slide 19).

δ = 10^-5 nhỏ hơn 1/n ≈ 1.13 × 10^-5 với n = 88,500 gói train, nhưng không nhỏ hơn nhiều. Bài tự nêu điều này; nếu bị hỏi thì thừa nhận (Q13).

---

### Slide 10. Integer noise is split across gateways; the CVAE baseline cannot do this (45 giây)

Trên slide: mỗi gateway thêm Sk(μ/t); công thức (7) trên Z_(2^32); MGl thêm đủ μ; CVAE: B3, M1, M2, M3, 30 vòng, 2 epoch cục bộ.

#### Lời nói

> Each gateway adds only a share of the noise, Skellam with variance mu over t. With t equal to five, the sum carries the full noise when all five gateways are honest. Flower's SecAgg+ sums the integer tables modulo two to the thirty-two, Equation 7. The split is valid because each release is one sum. In the client-side variant, MGl, every gateway adds the full noise. The CVAE baseline is different: DP-SGD adds noise at every local step inside each gateway, so even with SecAgg+, the CVAE has client-side DP only.

#### Hiểu để nói

Chia nhiễu: gateway k thêm ξ_k ~ Sk(μ_r / t) vào mỗi ô.

| Ký hiệu | Nghĩa |
| --- | --- |
| t | Số phần nhiễu. Mặc định t = K = 5 (MGs, MGr) |
| h | Số gateway thực sự thêm phần nhiễu của mình (gateway trung thực) |

Tổng nhiễu có phương sai h · μ_r / t. Khi h = t = 5 thì đủ μ_r. Nếu chỉ có h = 1 thì còn μ_r / 5, ε yếu đi. Bài tính lại ε cho mọi h, ví dụ ε = 5 thành 14.2 khi chỉ một gateway trung thực (slide 17).

Ngưỡng t < K (hậu tố -t2, -t3): mỗi gateway thêm μ_r / t, nên chỉ cần t gateway trung thực là đủ μ_r. Khi cả 5 trung thực thì tổng là 5μ_r / t, nhiều hơn mức cần. Vì vậy ε thực tế nhỏ hơn mục tiêu (MGr-t3-eps5: 3.72 khi cả 5 trung thực), đổi lại có thêm nhiễu.

MGl (client-side DP): mỗi gateway thêm đủ μ_r. Phần nó gửi đi tự thỏa DP, không cần tin server hay gateway khác. Tổng mang 5μ_r, gấp 5 lần mức cần, nên ở ε nhỏ MGl thua MG khá xa (0.267 so với 0.366 ở ε = 1).

Công thức (7):

```
S = Σ_{k ∈ K} ( x_k + ξ_k )  mod 2^32
```

| Ký hiệu | Nghĩa |
| --- | --- |
| x_k | Các số đếm của gateway k |
| ξ_k | Nhiễu số nguyên của gateway k |
| mod 2^32 | SecAgg+ làm trên số nguyên không dấu 32 bit: vượt quá 2^32 thì quay vòng về 0 |

Nhiễu có thể âm. Trong số học modulo, −3 được lưu thành 2^32 − 3. Server lấy lại số âm bằng quy tắc: mục nào S ≥ 2^31 thì đổi thành S − 2^32. Số đếm tối đa là 88,500 và nhiễu nhỏ so với 2^31 (khoảng 2.1 tỷ), nên không có tràn số: tổng sau khi đổi đúng bằng tổng nhiễu thật. Vì thế SecAgg+ không thêm sai số làm tròn và cũng không được tính công vào ε.

Ví dụ minh họa với số tự đặt, không phải kết quả của bài. Ở một ô của Release 1, năm gateway đếm được 40, 15, 0, 7, 0 gói và thêm nhiễu −2, +1, +3, 0, −1. Server chỉ thấy tổng 63 (62 gói thật cộng nhiễu +1), không biết gateway nào đóng góp bao nhiêu. Từng giá trị gửi lên đã bị mặt nạ SecAgg che.

CVAE baseline. Lời nói chỉ giữ ý chính là CVAE chỉ có client-side DP. Nếu còn dư giờ, thêm trước câu cuối: "The CVAE baseline trains with FedAvg for 30 rounds, with DP-SGD in M1, SecAgg+ in M2, and both in M3."

| Tên | Bảo vệ |
| --- | --- |
| B3 | Không bảo vệ, FedAvg 30 vòng, mỗi vòng 2 epoch cục bộ |
| M1 | DP-SGD tại mỗi gateway (Opacus 1.6.0) |
| M2 | SecAgg+: 5 share, ngưỡng khôi phục 3, clipping range 16, 2^22 mức lượng tử hóa |
| M3 | M1 và M2 cùng lúc |
| M1o, M3o | M1, M3 tinh chỉnh lại theo từng ε ở quy mô liên kết đầy đủ, 15 đến 50 vòng |

Công thức (8), DP-SGD:

```
g̃ = (1/b) · ( Σ_{i=1..b} g_i / max(1, ‖g_i‖_2 / G)  +  N(0, σ_k² G² I) )
```

| Ký hiệu | Nghĩa |
| --- | --- |
| g_i | Gradient của mẫu (gói) i trong minibatch |
| b | Kích thước minibatch |
| G | Ngưỡng cắt: gradient dài hơn G bị thu về độ dài G |
| max(1, ‖g_i‖ / G) | Phép cắt; gradient ngắn hơn G giữ nguyên |
| N(0, σ_k² G² I) | Nhiễu Gauss; σ_k (noise multiplier) chỉnh riêng cho gateway k |

Nhiễu được cộng ở mọi bước cục bộ, bên trong quá trình tối ưu của từng gateway, nên mỗi gateway phải tự thêm đủ nhiễu: đó là client-side DP. ε của cả liên kết là của gateway tệ nhất, max_k ε_k. SecAgg+ chỉ che trọng số trước server, không làm nhiễu nhỏ đi.

Nếu bị hỏi "sao không dùng nhiễu phân tán cho CVAE": có cách DP-FedSGD (mỗi vòng, mỗi gateway gửi một cập nhật đã cắt, nhiễu được cộng vào tổng). Nhóm đã cài một biến thể CVAE như vậy nhưng chưa chạy. Nói thật như vậy, và nói đây là hướng tiếp theo.

Vì sao CVAE vẫn có trong bài: CVAE là thiết kế ban đầu. Utility dưới DP vẫn thấp kể cả sau khi tinh chỉnh lại theo từng ε ở quy mô đầy đủ (M1o, M3o), nên FedDP-Marginal thành bộ sinh chính và CVAE giữ vai trò baseline.

---

## IV. Experimental Setup

### Slide 11. 39 million packets, six classes, 60:1 training imbalance (35 giây)

Trên slide: Table II rút gọn (số gói thô, tỉ lệ, train 88,500, val 12,000, test 30,000).

#### Lời nói

> The data are the DoS/DDoS-MQTT-IoT dataset, about 39 million packets. We exported the normal traffic from PCAP with the authors' export settings, which reproduce their attack rows exactly in 47 of 48 captures. Merging the DoS and DDoS variants of each family gives six classes. Training has 88,500 packets with a 60 to 1 imbalance; validation and test are balanced. No single column exceeds 0.9 macro-F1, so there is no shortcut feature.

#### Hiểu để nói

Table II:

| Lớp | Tên đầy đủ | Gói thô | Tỉ lệ | Train | Val | Test |
| --- | --- | --- | --- | --- | --- | --- |
| NORMAL | Lưu lượng bình thường | 24,955,877 | 63.99% | 60,000 | 2,000 | 5,000 |
| BCF | Basic connect flooding | 12,280,874 | 31.49% | 20,000 | 2,000 | 5,000 |
| DELAYED | Delayed connect flooding | 601,542 | 1.54% | 3,000 | 2,000 | 5,000 |
| SYN | SYN TCP flooding | 601,439 | 1.54% | 3,000 | 2,000 | 5,000 |
| INVALID | Invalid subscription flooding | 290,340 | 0.74% | 1,500 | 2,000 | 5,000 |
| WILL | Connect flooding with WILL payload | 270,529 | 0.69% | 1,000 | 2,000 | 5,000 |
| Tổng | | 39,000,601 | 100% | 88,500 | 12,000 | 30,000 |

Bộ dữ liệu có 39,000,601 gói, mỗi gói 33 cột. Hàng tấn công là file CSV của tác giả. Normal chỉ có dạng PCAP, nên nhóm xuất bằng TShark ra cùng các cột với thiết lập xuất của tác giả (two-pass dissection, chỉ lấy gói gửi tới broker). Kiểm chứng: thiết lập này tái tạo đúng hàng tấn công của tác giả ở 47 trên 48 capture. Khi nói, dùng "exported with the authors' export settings". Không nói nhóm "filtered" dữ liệu.

Vì sao gộp DoS và DDoS: tách 11 lớp con ở mức gói khó. RF trên dữ liệu thật chỉ được macro-F1 0.336 trên 11 lớp con, và hai lớp con của BCF gần như đoán mò (0.59 cho 2 lớp). Lý do dễ hiểu: DoS và DDoS khác nhau ở số nguồn tấn công, mà một gói đơn lẻ không cho thấy điều đó. Gộp lại thì IDS phát hiện họ tấn công.

60:1 là 60,000 gói NORMAL so với 1,000 gói WILL trong tập train. Tập train giữ thứ hạng của dữ liệu thô (lớp lớn vẫn lớn). Val và test cân bằng (2,000 và 5,000 mỗi lớp) để metric không bị lớp lớn chi phối. Bốn lớp hiếm: DELAYED, SYN, INVALID, WILL.

Chia train, val, test theo nhóm capture. Normal có 49 nhóm capture, và cả nhóm đi về cùng một tập. 8 trên 10 lớp con tấn công chỉ có một file capture, nên val và test là các khối liên tiếp trong file đó, cách nhau 1,000 hàng đệm, và các TCP stream vắt qua ranh giới bị bỏ. Các khối gần nhau vẫn có thể chung bối cảnh thời gian, nên rò rỉ giảm chứ không loại hẳn. Chạy lại với hai lựa chọn nhóm test khác giữ được 8 trên 10 kết luận. Tập test (11 nhóm capture, 20,485 TCP stream) chỉ dùng một lần cho đánh giá cuối.

Tiền xử lý: bỏ định danh và metadata capture (frame number, timestamp tuyệt đối và tương đối, địa chỉ nguồn, chuỗi info) để tránh rò rỉ; lấy log cho cột số có độ lệch (skewness) trên 2; chuẩn hóa; cắt ở ±5σ; one-hot cho cột phân loại. Kết quả là p = 59 đặc trưng. Thống kê tiền xử lý tính trên tập train gộp, nằm ngoài ε (giới hạn, slide 19).

Không có đặc trưng "đường tắt" (shortcut): không cột đơn nào đạt macro-F1 trên 0.9; riêng các cờ thiếu giá trị chỉ được 0.18 (đoán mò là 0.17); chia ngẫu nhiên theo hàng chỉ hơn chia theo nhóm capture 0.009.

---

### Slide 12. Every comparison uses one test set and one decision rule (35 giây)

Trên slide: Table III rút gọn; TRTR, TSTR, TAug, tăng cường cục bộ; công thức (9); 3 seed; 1,000 lần bootstrap.

#### Lời nói

> Every comparison uses one real test set. TRTR trains the IDS on pooled real data, our references B0, B1a and B1b. TSTR trains it on synthetic data only, which is what a federation gets when raw data stay local. The main metric is macro-F1 over six classes, with three seeds. A is better than B only if the 95% bootstrap interval of the difference excludes zero and the difference exceeds the seed standard deviation, Equation 9.

#### Hiểu để nói

Bốn cách đánh giá:

| Tên | Viết đầy đủ | Làm gì |
| --- | --- | --- |
| TRTR | Train on real, test on real | Train IDS trên dữ liệu thật gộp: B0, B1a, B1b. Cần gộp gói thô, nên liên kết không có. Chỉ là mốc tham chiếu |
| TSTR | Train on synthetic, test on real | Train chỉ trên 5,000 dòng sinh mỗi lớp. Đo thứ mà liên kết nhận được khi không gộp được dữ liệu thô |
| TAug | Training augmentation | Thêm dòng sinh vào dữ liệu thật gộp đến khi mỗi lớp có ít nhất 20,000 dòng |
| Local augmentation | | Mỗi gateway train IDS trên dữ liệu của nó, bù dòng sinh cho lớp nào có dưới 5,000 dòng. 5 gateway × 3 seed = 15 mô hình |

IDS là RF 200 cây hoặc MLP với hai lớp ẩn (128, 64). Mỗi cách đánh giá báo bộ phân loại có macro-F1 trên validation cao hơn.

Metric. F1 của một lớp = 2PR / (P + R). P (precision): trong các gói IDS đoán là lớp đó, bao nhiêu phần đoán đúng. R (recall): trong các gói thật của lớp đó, IDS bắt được bao nhiêu phần. Macro-F1 là trung bình cộng F1 của 6 lớp, mỗi lớp nặng như nhau, nên lớp hiếm có tiếng nói ngang lớp lớn. Binary F1 chỉ phân biệt normal với attack. Rare-class recall là trung bình recall của 4 lớp hiếm.

Fidelity (dữ liệu sinh giống thật đến đâu) đo bằng Wasserstein-1, Jensen-Shannon, khoảng cách tương quan, và C2ST: train một bộ phân loại để phân biệt dòng sinh với dòng thật; AUC 0.5 là không phân biệt được, 1.0 là phân biệt hoàn toàn.

Privacy đo bằng ε hình thức (được tính lại độc lập) và ba tấn công suy luận thành viên (MIA), tức đoán một gói có nằm trong tập huấn luyện hay không: tấn công trên dữ liệu sinh, tấn công có quyền truy cập mô hình công bố (hiệu chỉnh bằng một mô hình tham chiếu), và tấn công trên bảng công bố của FedDP-Marginal. Mỗi tấn công phải thắng một positive control, tức một trường hợp chắc chắn có rò rỉ. Không thắng ở đó thì kết quả "gần 0.5" không nói lên gì.

Công thức (9), quy tắc kết luận:

```
0 ∉ CI_95%(Δ̄)    và    |Δ̄| > max(sd_A, sd_B)
```

| Ký hiệu | Nghĩa |
| --- | --- |
| Δ̄ | Chênh lệch macro-F1 trung bình giữa A và B qua 3 seed |
| CI_95%(Δ̄) | Khoảng tin cậy 95%, từ bootstrap ghép cặp 1,000 lần trên các hàng test (phân tầng theo lớp, giống nhau cho mọi run) |
| 0 ∉ CI | Khoảng không chứa 0: chênh lệch không phải do may rủi khi lấy mẫu test |
| sd_A, sd_B | Độ lệch chuẩn theo seed của A và của B |
| \|Δ̄\| > max(sd) | Chênh lệch lớn hơn mức dao động giữa các seed |

Cả hai điều kiện đúng mới nói "better" hay "worse". Nếu không thì nói "no effect". Bài không báo p-value.

Bootstrap theo stream: các gói trong cùng một TCP stream giống nhau, nên bootstrap theo hàng có thể cho khoảng hẹp hơn thực tế. Mỗi kết luận được lặp lại với bootstrap rút cả stream. Lời nói bỏ ý này để đủ giờ; nếu còn dư giờ, thêm câu "Every verdict is repeated with a bootstrap over whole TCP streams." Nếu bị hỏi về tương quan giữa các gói trong một stream, trả lời bằng ý này.

Seed {0, 1, 2} điều khiển phân vùng, khởi tạo và lấy mẫu.

---

## V. Results and Discussion

### Slide 13. RQ1: With pooled real data, synthetic rows add almost nothing (45 giây)

Trên slide: mốc thật B0 0.448, B1a 0.496, B1b 0.505; không DP: MG 0.459, CVAE 0.413; TAug với RF: 2/13, tối đa +0.001, SMOTE +0.057.

#### Lời nói

> RQ1 first, and the first answer is negative. With all real data pooled, a random forest reaches 0.448 macro-F1, and SMOTE raises it to 0.505. Trained only on synthetic data without DP, the IDS reaches 0.459 with FedDP-Marginal and 0.413 with the CVAE. But adding synthetic rows to pooled real data does not help: with the random forest, 2 of 13 generators improve, by at most 0.001, against 0.057 for SMOTE.

#### Hiểu để nói

| Cấu hình | Macro-F1 | Ghi chú |
| --- | --- | --- |
| B0 | 0.448 | RF trên dữ liệu thật mất cân bằng; rare recall 0.285 |
| B1a | 0.496 | Thêm class weights |
| B1b | 0.505 | Thêm SMOTE |
| MGs-nodp (TSTR) | 0.459 ± 0.007 | FedDP-Marginal không DP |
| B3 (TSTR) | 0.413 ± 0.005 | CVAE không DP |

Dấu ± là độ lệch chuẩn theo seed.

TSTR ngang mốc B0 nhưng dưới B1a và B1b. Nghĩa là một phần giá trị của dữ liệu sinh đến từ việc tập sinh cân bằng lớp (5,000 dòng mỗi lớp).

Phát hiện tấn công ở mức gói khó ngay cả với dữ liệu thật: mốc tốt nhất chỉ khoảng 0.5. Nếu bị hỏi vì sao macro-F1 thấp, xem Q1.

TAug chi tiết hơn: với RF, 2 trên 13 cấu hình bộ sinh hơn B0 theo quy tắc (9), tối đa +0.001, trong khi SMOTE +0.057. Với MLP, 9 trên 13 hơn, tối đa +0.038, SMOTE +0.134. Recall lớp hiếm thay đổi tối đa 0.007 với mọi bộ sinh, so với +0.070 đến +0.096 cho class weights và SMOTE.

Nói thẳng đây là kết quả âm, không né. Mọi mốc dữ liệu thật đều cần gộp gói thô, thứ mà liên kết không có. Slide sau cho thấy dữ liệu sinh có ích ở đâu.

---

### Slide 14. RQ1: The value appears where traffic must stay local (40 giây)

Trên slide: tăng cường cục bộ 0.384 lên 0.423, 0.426, 0.427; 11, 13, 13 trên 15; FedMLP DP-FedSGD 0.350, 0.369, 0.389 so với MG (MLP) 0.337, 0.425, 0.433.

#### Lời nói

> The picture changes when the comparison is the gateway itself. A gateway's own IDS reaches 0.384. Topping up its missing classes with FedDP-Marginal data raises this to 0.423 to 0.427, with a raw gain in 11 to 13 of 15 gateway-seed pairs. A detector trained directly by federated learning with shared noise ties with FedDP-Marginal at epsilon 1 and loses at 5 and 10, and it needs 2,593 rounds and about 7.7 gigabytes.

#### Hiểu để nói

Local augmentation: IDS riêng của gateway, chỉ học trên dữ liệu non-IID của nó, đạt 0.384 ± 0.055. Bù các lớp thiếu bằng dữ liệu FedDP-Marginal được 0.423, 0.426, 0.427 ở ε = 1, 5, 10 (tăng +0.039, +0.042, +0.043). Có 11, 13, 13 trên 15 cặp gateway-seed được lợi, nhiều nhất +0.139; các cặp còn lại mất tối đa 0.005. Số 11, 13, 13 là chênh lệch thô, chưa qua công thức (9), nên lời nói dùng chữ "a raw gain" và gộp thành "11 to 13 of 15". Slide ghi đủ ba số.

Vì sao có ích: gateway không có gói WILL thì IDS của nó không bao giờ đoán ra WILL. Dữ liệu sinh lấp đúng chỗ trống đó.

FedMLP là IDS dạng MLP huấn luyện trực tiếp bằng FL, không dùng dữ liệu sinh:

| FedMLP | ε = 1 | ε = 5 | ε = 10 | So với |
| --- | --- | --- | --- | --- |
| Không bảo vệ | 0.425 | | | Nằm giữa CVAE (0.413) và MG (0.459) |
| DP-SGD tại mỗi gateway | 0.245 | 0.276 | 0.290 | MGl: 0.267, 0.397, 0.406 |
| DP-FedSGD (nhiễu chia, chỉnh theo ε) | 0.350 | 0.369 | 0.389 | MG cùng MLP: 0.337, 0.425, 0.433 |

Theo quy tắc (9), FedMLP với nhiễu chia không khác MG ở ε = 1 và thua 0.057 và 0.043 ở ε = 5 và 10. FedMLP cần 2,593 vòng và khoảng 7.7 GB, so với 3 lần gửi khoảng 0.5 MB. Khi chỉ một gateway trung thực, ε của FedMLP yếu đi thành 3.1, 58.6, 142, còn của MG là 2.4, 14.2, 33.1.

Số dễ nhầm: 0.366 ở slide 15 là bộ phân loại được chọn trong Table IV; 0.337 là MG khi so cùng MLP với FedMLP.

Câu trả lời RQ1 trong bài, nhớ để trả lời khi bị hỏi: dữ liệu sinh liên kết có ích khi gói thô không gộp được, để train một IDS dùng chung (nhất là dưới DP) hoặc để lấp các lớp mà gateway không thấy. Không có DP thì train IDS trực tiếp bằng FL là lựa chọn rẻ hơn khi không cần dữ liệu chia sẻ được. Dữ liệu sinh không cải thiện IDS khi dữ liệu thật đã gộp.

---

### Slide 15. RQ2: FedDP-Marginal leads the CVAE at every budget (45 giây)

Trên slide: Fig. 3; MG 0.366, 0.425, 0.433; CVAE 0.176, 0.254, 0.275; MGl 0.267, 0.397, 0.406; 0.48 đến 0.53 MB so với 13.6 đến 72.4 MB.

#### Lời nói

> RQ2 compares the generators at equal budgets, in Figure 3. With noise shared across honest gateways, FedDP-Marginal reaches 0.366 to 0.433 from epsilon 1 to 10; the best CVAE reaches 0.176 to 0.275. The CVAE adds its noise at each gateway, so the fair pair is MGl, our client-side variant. MGl is still better than the CVAE at every budget, by 0.092 to 0.143. FedDP-Marginal also sends over 96 percent less data per run.

#### Hiểu để nói

Table IV rút gọn:

| ε | Cấu hình | Macro-F1 | Rare recall | MB/run |
| --- | --- | --- | --- | --- |
| 1 | M1-eps1 (CVAE, client-side) | 0.176 ± 0.008 | 0.068 | 16.9 |
| 1 | MGl-eps1 (MG, client-side) | 0.267 ± 0.021 | 0.117 | 1.13* |
| 1 | MGs-eps1 (MG, phân tán) | 0.366 ± 0.018 | 0.231 | 0.53 |
| 5 | M3o-eps5 (CVAE, client-side) | 0.254 ± 0.013 | 0.132 | 13.6 |
| 5 | MGl-eps5 (MG, client-side) | 0.397 ± 0.006 | 0.279 | 1.05* |
| 5 | MGr-eps5 (MG, phân tán) | 0.425 ± 0.004 | 0.301 | 0.51 |
| 10 | M1o-eps10 (CVAE, client-side) | 0.275 ± 0.015 | 0.146 | 72.4 |
| 10 | MGl-eps10 (MG, client-side) | 0.406 ± 0.015 | 0.277 | 0.94* |
| 10 | MGs-eps10 (MG, phân tán) | 0.433 ± 0.004 | 0.301 | 0.48 |

Dấu * là số ước tính: MGl được cộng trong một tiến trình, nên byte của nó dùng số byte mỗi giá trị đo được ở M2.

Cấu hình chính MG-eps1, MG-eps5, MG-eps10 là MGs-eps1, MGr-eps5, MGs-eps10, chọn trên validation. Vì vậy ở ε = 5 là bản có hậu xử lý, còn ε = 1 và 10 thì không. CVAE tốt nhất ở mỗi ε cũng chọn trên validation, gồm cả các bản tinh chỉnh lại.

Recall lớp hiếm của MG gấp 2.1 đến 3.4 lần CVAE.

So công bằng là so cùng mô hình tin cậy (client-side): MGl hơn CVAE 0.092 [0.088, 0.095], 0.143 và 0.131; recall lớp hiếm cũng hơn; đúng với cả bootstrap theo hàng và theo stream. Lời nói gộp thành "by 0.092 to 0.143" vì khoảng này chứa cả ba số; slide ghi đủ 0.092, 0.143, 0.131. MG nhiễu chia hơn CVAE 0.16 đến 0.19, nhưng đó là khi MG được chia nhiễu qua các gateway trung thực, không phải cùng điều kiện. Không nói "MG hơn CVAE 0.16 đến 0.19 trong cùng điều kiện".

Lượng truyền: MG cần 3 vòng × 0.16 đến 0.18 MB; CVAE cần 15 đến 50 vòng × 0.56 đến 1.45 MB. Tổng mỗi run là 0.48 đến 0.53 MB so với 13.6 đến 72.4 MB, giảm hơn 96% ở mỗi ε.

Đọc Fig. 3: trục ε rời rạc (khoảng cách đều, không theo tỉ lệ); thanh dọc là một độ lệch chuẩn theo seed; đường đứt là RF trên dữ liệu thật gộp.

Chi phí DP của từng nhánh, so với chính nó khi không DP, theo quy tắc (9): MG mất 0.076 (RF) và 0.122 (MLP) ở ε = 1; 0.017 và 0.033 ở ε = 5; ở ε = 10 MLP mất 0.026, còn RF lại tăng 0.012. CVAE: 11 trên 12 so sánh tệ hơn, mất tới 58% macro-F1. Không DP, MG cũng hơn CVAE (RF +0.044, MLP +0.046). Nhiễu client-side làm MG tốn nhất ở ngân sách nhỏ, vì tổng mang gấp K lần phương sai.

Fidelity: ở ε = 5 và 10, khoảng cách Wasserstein của MG là 0.037 và 0.049, của M1 là 0.194 và 0.176; ở ε = 1 hai bên gần nhau (0.194 và 0.235). C2ST AUC 0.9995 đến 1.0000 với mọi bộ sinh, có DP hay không: dữ liệu sinh hữu ích cho IDS không có nghĩa là trông giống thật.

---

### Slide 16. RQ3: SecAgg+ is cheap, and DP measurably reduces table leakage (40 giây)

Trên slide: SecAgg+ với MG 1.39 lần byte, 1.06 lần thời gian; AUC 0.573 không DP; 0.515, 0.525, 0.539 ở ε = 1, 5, 10; kiểm chứng dương 0.835.

#### Lời nói

> Now RQ3. For FedDP-Marginal, SecAgg+ costs 1.39 times the bytes and no utility, because the secure sum equals the exact sum. A membership inference attack on the released tables passes its positive control at 0.835 AUC. Its AUC is 0.573 without DP and 0.515 to 0.539 with DP. The drops pass our rule, but the leakage is small. SecAgg+ alone does not change it: it hides each gateway's tables, not their sum.

#### Hiểu để nói

SecAgg+ với MG: so MGs-nodp với MGp-nodp, byte mỗi vòng là 0.158 so với 0.114 MB (1.39 lần), thời gian ba vòng là 21.6 so với 20.4 giây (1.06 lần, phần lớn là thời gian khởi động simulator). Utility không đổi vì tổng an toàn bằng đúng tổng thật.

Với CVAE: SecAgg+ tốn 1.12 lần thời gian mỗi vòng và 1.52 lần byte mỗi tham số; 7 trên 8 so sánh utility không khác. DP-SGD nhân thời gian mỗi vòng lên 1.9 lần.

MIA trên bảng: attacker có một gói X và các bảng đã công bố, muốn đoán X có nằm trong tập train không. AUC 0.5 là đoán mò, 1.0 là lúc nào cũng đúng.

Positive control: chạy tấn công trên bảng không nhiễu của 500 bản ghi, một trường hợp dễ rò rỉ, được AUC 0.835. Tấn công đủ mạnh, nên các số bên dưới có ý nghĩa.

| Cấu hình | AUC (trung bình 3 seed) | Mức giảm so với không DP [CI 95%] |
| --- | --- | --- |
| Không DP | 0.573 | |
| ε = 1 | 0.515 | 0.059 [0.052, 0.065] |
| ε = 5 | 0.525 | 0.048 [0.042, 0.055] |
| ε = 10 | 0.539 | 0.034 [0.029, 0.040] |

Cả ba mức giảm qua quy tắc (9). Nhưng rò rỉ tuyệt đối nhỏ: ở mức 1% false positive, attacker nhận ra 1.9% bản ghi train khi không DP và 1.1 đến 1.4% khi có DP, so với 1% nếu đoán mò.

SecAgg+ không đổi các số này: MGp-nodp và MGs-nodp cùng 0.573. Nó che bảng của từng gateway, không che điều mà tổng tiết lộ. Không nói "SecAgg+ bảo vệ dữ liệu được công bố".

Với CVAE: tấn công trên dữ liệu sinh gần đoán mò (0.488 đến 0.494) ở mọi ε, kể cả không DP, nhưng trượt positive control (0.510), nên không dùng để kết luận được. Tấn công có quyền truy cập mô hình qua được control (0.647) nhưng không thấy rò rỉ ở mô hình liên kết (0.497 đến 0.506). Với CVAE, DP cho bảo đảm hình thức nhưng không đo được mức giảm.

---

### Slide 17. RQ3: The guarantee depends on honest gateways and on the unit (45 giây)

Trên slide: Table V rút gọn với MGr-eps5, MGr-t3-eps5, MGl-eps5, MGr-strm1-eps5, MGr-cap50-eps5.

#### Lời nói

> The guarantee also depends on trust and on the protected unit, in Table V. With the noise split over five gateways, epsilon 5 holds when all are honest, and becomes 14.2 if only one adds its share. A threshold of three keeps epsilon at most 5 with any three honest gateways; client-side noise keeps it under any trust, at a lower macro-F1. Protecting a TCP stream costs 0.03 to 0.05, since 90 percent of streams have one packet. A whole capture leaves too little data: 0.09 to 0.18.

#### Hiểu để nói

Table V rút gọn:

| Cấu hình | Bảo vệ | Macro-F1 | ε khi 5 gateway trung thực | ε khi 1 gateway trung thực |
| --- | --- | --- | --- | --- |
| MGs-nodp | Chỉ SecAgg+ | 0.459 ± 0.007 | ∞ | ∞ |
| MGl-eps5 | Client-side DP | 0.397 ± 0.006 | 5.00 | 5.00 |
| MGr-eps5 | Phân tán, t = 5 | 0.425 ± 0.004 | 5.00 | 14.2 |
| MGr-t3-eps5 | Phân tán, t = 3 | 0.420 ± 0.009 | 3.72 | 10.1 |
| MGr-t2-eps5 | Phân tán, t = 2 | 0.425 ± 0.011 | 2.94 | 7.6 |
| MGr-strm1-eps5 | Đơn vị stream, m = 1 | 0.376 ± 0.007 | 5.00 | 14.2 |
| MGr-cap50-eps5 | Đơn vị capture, m = 50 | 0.177 ± 0.020 | 5.00 | 13.0 |

Vì sao ra 14.2: chỉ một gateway thêm Sk(μ/5), tổng chỉ còn μ/5 phương sai, nhiễu ít đi nên ε lớn lên. Con số này tăng theo kích thước liên kết: 25.4 với 10 gateway, 49.9 với 20, vì mỗi phần nhiễu càng nhỏ.

Ngưỡng t = 3: ε giữ ≤ 5 với bất kỳ ba gateway trung thực nào. Khi cả 5 trung thực thì thừa nhiễu, ε thực tế là 3.72. Ngưỡng làm utility thay đổi từ −0.005 đến +0.016 qua các ngân sách.

MGl giữ 5.00 dù bao nhiêu gateway trung thực, vì mỗi gateway tự thêm đủ nhiễu. Đổi lại macro-F1 thấp hơn (0.397).

Đơn vị bảo vệ: mặc định ε bảo vệ một gói. Bảo vệ cả TCP stream (m = 1, mỗi stream chỉ dùng một gói) mất 0.03 đến 0.05 macro-F1 (MGr-strm1-eps5 là 0.376 so với 0.425), vì 90% stream vốn chỉ góp một gói. Một capture có tới 1,277 gói; chỉ bảo vệ được cả capture khi giới hạn mỗi capture còn m = 25 đến 100 gói. Bảo đảm khi đó phủ cả capture, nhưng còn quá ít dữ liệu: macro-F1 0.09 đến 0.18 (cap50 là 0.177).

Không bao giờ nói "ε = 5" một mình. Nói đủ: "epsilon 5 per packet, delta ten to the minus five, with all five gateways honest; 14.2 if only one is honest".

---

### Slide 18. RQ4: The choice depends on trust, privacy and bandwidth (40 giây)

Trên slide: Fig. 4; 3 đến 4 dòng của Table VI; 17/18 cấu hình Pareto là FedDP-Marginal.

#### Lời nói

> RQ4 turns this into a choice, since the best configurations differ more in what they protect and cost than in macro-F1. Our rule keeps valid configurations, applies the trust requirement, drops those over the limits on epsilon, bandwidth, rounds or attack AUC, keeps the Pareto front, and picks the best on the priority metric. Table VI applies it to eleven scenarios. In Figure 4, every FedDP-Marginal variant stays below 1.4 megabytes per run, and 17 of the 18 Pareto configurations are FedDP-Marginal.

#### Hiểu để nói

Năm bước của quy tắc chọn:

| Bước | Làm gì |
| --- | --- |
| (i) | Giữ cấu hình hợp lệ: bảo đảm của nó phủ mọi thứ nó công bố |
| (ii) | Áp yêu cầu tin cậy: server không tin cậy thì cần SecAgg+ hoặc client-side DP; gateway có thể thông đồng thì cần client-side DP hoặc ngưỡng t |
| (iii) | Bỏ cấu hình vượt giới hạn về ε, băng thông, số vòng hoặc MIA AUC |
| (iv) | Giữ Pareto front theo utility, ε, có dùng SecAgg+ hay không, và chi phí. Utility trong khoảng độ lệch chuẩn seed, ε trong 2%, chi phí trong 5% thì coi như bằng nhau |
| (v) | Chọn thành viên của front có metric ưu tiên cao nhất (macro-F1 hoặc rare recall); các cấu hình trong khoảng độ lệch chuẩn seed được báo là hòa |

Pareto front là tập cấu hình mà không cấu hình nào khác vừa tốt bằng ở mọi tiêu chí vừa tốt hơn hẳn ở ít nhất một tiêu chí.

ε được tính theo giả định tin cậy của từng kịch bản. Nếu gateway có thể thông đồng, dùng giá trị khi chỉ một gateway trung thực; vì vậy consortium chọn MGr-t2-eps5 (ε = 7.63) thay vì nhiễu client-side. Nếu gateway được tin, cấu hình ngưỡng tính theo mục tiêu: MGs-t3-eps5 tính là 5, không phải 3.72.

Một số dòng của Table VI:

| Kịch bản | Yêu cầu | Chọn | Macro-F1 | ε |
| --- | --- | --- | --- | --- |
| lab | Mọi bên tin cậy, không DP | MGp-nodp | 0.459 | ∞ |
| hidden-tables | Server không tin cậy, không DP | MGs-nodp | 0.459 | ∞ |
| strict-privacy | Server không tin cậy, ε ≤ 1 | MGs-t3-eps1 | 0.373 | 1 |
| consortium | Gateway có thể thông đồng, ε ≤ 10 | MGr-t2-eps5 | 0.425 | 7.63 |
| session-privacy | Đơn vị TCP stream, ε ≤ 5 | MGs-strm1-eps5 | 0.397 | 5 |

Hai lựa chọn có hòa. lab hòa giữa MGp-nodp và MGs-nodp (cùng bảng, gửi qua SecAgg+, 0.158 thay vì 0.114 MB mỗi vòng). cloud-aggregator chọn MGd-eps5 (0.426), nhưng tổng an toàn của MGd được mô phỏng trong một tiến trình; cấu hình hòa chạy qua SecAgg+ thật của Flower là MGs-t3-eps5 (0.420). capture-privacy chọn MGr-cap50-eps5, hợp lệ về hình thức nhưng không thực tế với 0.177.

Đọc Fig. 4: trục ngang là tổng lưu lượng mỗi run (thang log), trục dọc là macro-F1 TSTR; điểm tô đặc là thành viên Pareto front. Mọi biến thể MG dưới 1.4 MB mỗi run, ít nhất 6 lần ít hơn bất kỳ nhánh CVAE nào (8.4 đến 191 MB). Khoảng 8.4 đến 191 MB là mọi nhánh CVAE trong Fig. 4, khác với khoảng 13.6 đến 72.4 MB của các cấu hình CVAE chính trong Table IV.

---

### Slide 19. Discussion and limitations (35 giây)

Trên slide: vì sao marginal chịu DP tốt hơn; một bộ dữ liệu, mức gói tin; mô phỏng trên một máy; 3 seed; tiền xử lý và chọn siêu tham số ngoài ε; chưa so FLAIM, AIM, CVAE nhiễu phân tán.

#### Lời nói

> Why does the marginal route degrade less under DP? Its budget goes to three sums with known sensitivity, so each cell gets noise once. The price: only pairwise dependencies, through one tree. Our limitations: one dataset at the packet level, a federation simulated on one machine, three seeds, preprocessing and tuning outside epsilon, and no comparison with FLAIM, AIM or a CVAE with distributed noise. Synthetic packets also remain easy to tell from real ones.

#### Hiểu để nói

Vì sao nhánh marginal chịu DP tốt hơn, ba ý:

1. Ngân sách chỉ tiêu vào ba lần gửi, mỗi lần là một tổng có độ nhạy biết trước, nên mỗi ô chỉ nhận nhiễu một lần. DP-SGD cộng nhiễu ở hàng nghìn bước tối ưu.
2. Release 2 gộp lớp, giữ tín hiệu mỗi ô cao (slide 8).
3. Mỗi lần gửi là một tổng, nên khớp chính xác với nhiễu phân tán và SecAgg+. Trong cách DP-SGD dùng ở đây, nhiễu thêm ở mọi bước cục bộ và không chia qua gateway được.

Cái giá: chỉ nắm phụ thuộc theo cặp qua một cây. Ablation MGb (mạng Bayes bậc hai) không giúp gì trên dữ liệu này.

Giới hạn đầy đủ theo bài, để trả lời khi bị hỏi sâu:

| Giới hạn | Chi tiết |
| --- | --- |
| Một bộ dữ liệu, mức gói | Gói sinh không có ngữ cảnh stream. Một capture tấn công được công bố cả hai chiều, nên 18.1% dòng train của SYN là gói do broker gửi |
| ε mặc định bảo vệ một gói | Một nhóm capture góp tới 188 gói của một lớp hiếm, nên bound theo nhóm cho cả capture là vô nghĩa (vacuous). Nhãn, số đếm lớp, thống kê tiền xử lý và việc chọn theo validation nằm ngoài ε |
| Thống kê tiền xử lý tính tập trung | Thống kê chuẩn hóa, kiểm định skewness, khoảng cắt và danh sách category lấy từ train gộp. Triển khai thật cần khoảng cố định công khai, một giao thức an toàn, hoặc một lần công bố có DP trước Release 1 (tốn một phần ngân sách) |
| Giả định và mô phỏng | Các bên honest-but-curious. Liên kết, kể cả SecAgg+, mô phỏng bằng Flower và Ray trên một máy Windows 11 (chỉ CPU, 16 GB RAM), nên thời gian phản ánh tính toán chứ không phải độ trễ mạng |
| Thống kê và so sánh | 3 seed chỉ cho độ dao động thô; kết luận đúng cho split test này. Chưa so CVAE nhiễu phân tán, FLAIM, AIM và các bộ sinh sâu khác. Detector nhiễu chia dùng accounting Gauss và một lưới nhỏ chỉnh trên một seed |

"Synthetic packets also stay easy to tell from real ones": C2ST AUC 0.9995 đến 1.0000 (slide 15).

Tự nêu giới hạn trước khi bị hỏi, đúng như bài báo đã viết.

---

## VI. Conclusion

### Slide 20. Conclusion: useful where traffic must stay local (45 giây)

Trên slide: các kết luận chính; hướng tiếp theo; dòng "Thank you".

#### Lời nói

> To conclude: FedDP-Marginal kept 0.366 to 0.433 macro-F1 at epsilon 1 to 10, against 0.176 to 0.275 for the federated CVAE, and it still led under the CVAE's own trust model. Synthetic data did not improve an IDS whose real data could be pooled. The framework is a way to train or complete an IDS where traffic must stay local, and its rule tells a deployment which protection to choose and at what cost. Thank you; I am happy to take questions.

#### Hiểu để nói

Mọi con số ở đây đã xuất hiện ở các slide trước. "It still led under the CVAE's own trust model" nghĩa là MGl hơn CVAE ở mọi ε (slide 15).

Kết luận đầy đủ trong bài còn hai ý, dùng khi được hỏi thêm: DP làm FedDP-Marginal mất tới 0.12 macro-F1 ở ε = 1 và tối đa 0.03 ở ε = 5 và 10; DP làm AUC của tấn công trên bảng giảm từ 0.573 xuống 0.515 đến 0.539, dù rò rỉ ở cả hai trường hợp đều nhỏ. Bảo đảm là theo gói, trừ khi chọn đơn vị stream.

Lời nói không có câu về hướng tiếp theo để đủ giờ. Nếu còn dư giờ, thêm trước "Thank you": "Next, we will test other datasets and real gateways." Cũng có thể bổ sung "with under 1 megabyte per run" sau "for the federated CVAE".

Hướng tiếp theo trong bài: đánh giá trên các bộ dữ liệu IoT khác; so với FLAIM, AIM và CVAE nhiễu phân tán; ước lượng thống kê tiền xử lý và chọn siêu tham số có DP; đo các giao thức trên gateway thật qua mạng thật.

Câu chốt mang ý của cả bài: chọn lớp bảo vệ theo yêu cầu triển khai, và biết trước cái giá phải trả.

---

## Câu hỏi dự kiến (Q&A)

Mỗi câu có câu trả lời tiếng Anh ngắn (nói trong 20 đến 30 giây) và ý chính bằng tiếng Việt. Trả lời bằng số trong bài, không thêm số mới. Không biết thì nói "We did not measure that" và nói hướng sẽ làm.

### Q1. Why is macro-F1 only around 0.4 to 0.5?

Answer: Packet-level detection on this dataset is hard even with real data. A random forest on all pooled real data reaches 0.448, and 0.505 with SMOTE. A single packet carries no stream context, and the DoS and DDoS variants of one family look alike at the packet level, which is why we merged them. Our test set is class-balanced, so macro-F1 is not inflated by the majority class.

Ý chính: thấp vì bài toán khó ở mức gói, không phải vì phương pháp hỏng. Mốc dữ liệu thật cũng chỉ 0.448 đến 0.505. Test cân bằng nên không có chuyện lớp NORMAL kéo điểm lên.

### Q2. If synthetic data do not improve the IDS, why use them?

Answer: Their value is where raw traffic cannot be pooled. Without DP, an IDS trained only on synthetic data reaches 0.459, close to the imbalanced real reference of 0.448. A gateway that tops up its missing classes goes from 0.384 to between 0.423 and 0.427. When real data can be pooled, synthetic rows add almost nothing, and we say so in the paper.

Ý chính: so đúng mốc. Khi không gộp được dữ liệu, mốc so là IDS của chính gateway (0.384), không phải B1b.

### Q3. Is the comparison with the CVAE fair?

Answer: We kept the same partitions, budgets, secure aggregation and evaluation, and the CVAE was re-tuned per epsilon at full scale. The CVAE gives client-side DP, so we compare it with MGl, which has the same trust model, and MGl is still better at every budget. We implemented a CVAE with distributed noise but did not run it, so that comparison is still open.

Ý chính: cặp so công bằng là MGl và CVAE (hơn 0.092, 0.143, 0.131). Nói thật phần chưa làm.

### Q4. What does epsilon 5 mean in practice?

Answer: Epsilon 5 is per packet, with delta ten to the minus five, when all five gateways add their noise share. Adding or removing one packet changes the probability of any output by at most a factor of e to the epsilon, plus delta. If only one gateway is honest, the same run gives 14.2. The paper reports the guarantee for every number of honest gateways.

Ý chính: luôn nói kèm đơn vị (gói), δ và giả định tin cậy. Đừng tự tính e^5 ra số khi trả lời.

### Q5. Why not train the detector directly with federated learning?

Answer: We did that too. Without protection, a federated MLP reaches 0.425, and without DP it is the cheaper option when no shareable data are needed. With shared noise it reaches 0.350 to 0.389; our rule finds no difference at epsilon 1 and a loss at 5 and 10. It also needs 2,593 rounds and about 7.7 gigabytes, against three releases of about 0.5 megabytes.

Ý chính: thừa nhận FL trực tiếp rẻ hơn khi không DP. Dưới DP thì MG ngang hoặc hơn, và chỉ cần 3 lần gửi khoảng 0.5 MB thay vì 2,593 vòng khoảng 7.7 GB.

### Q6. Does SecAgg+ give privacy by itself?

Answer: No. SecAgg+ hides each gateway's tables from the server, but the sum is revealed exactly. The membership attack gives the same AUC, 0.573, with and without SecAgg+. The bound on what the sum reveals comes from DP.

Ý chính: SecAgg+ che từng phần, DP giới hạn điều tổng tiết lộ. Hai thứ trả lời hai mối đe dọa khác nhau.

### Q7. Your attacks are close to chance. Does DP do anything?

Answer: On the released tables, the attack passes its positive control at 0.835, and DP lowers its AUC from 0.573 to between 0.515 and 0.539; those drops pass our rule. The leakage is small in absolute terms: at 1 percent false positives, the attack finds 1.9 percent of training records without DP. For the CVAE, the attacks found no leakage, so there DP gives a formal guarantee without a measured reduction.

Ý chính: tách hai nhánh. Với bảng của MG có mức giảm đo được nhưng rò rỉ tuyệt đối nhỏ. Với CVAE không đo được mức giảm.

### Q8. The preprocessing statistics are computed centrally. Is that a leak?

Answer: Yes, they are outside epsilon, and we list this as a limitation. The standardization statistics, clipping range and category lists come from the pooled training split. A deployment would need fixed public ranges, a secure protocol, or a DP release of these statistics before Release 1, which would use part of the budget.

Ý chính: nhận luôn, rồi nói cách khắc phục mà bài đã ghi.

### Q9. Why only a tree? Real traffic has higher-order dependencies.

Answer: A tree captures only pairwise dependencies; that is the price of the method. We tried a second-order Bayesian network as an ablation, MGb, and it did not help on this data. Few releases with a known sensitivity keep the noise per cell low.

Ý chính: đã thử bậc hai (MGb), không giúp. Ít release thì ít nhiễu mỗi ô.

### Q10. Did you test on real gateways?

Answer: No. The federation, including SecAgg+, is simulated with Flower and Ray on one Windows machine, so the times reflect computation, not network latency. Measuring the protocols on physical gateways over a real network is future work.

Ý chính: nói thẳng là mô phỏng, nêu hướng tiếp.

### Q11. What is new here?

Answer: We do not claim a new algorithm. The contribution is the combination for IoT gateways, with integer Skellam noise shared across gateways and summed through Flower's SecAgg+, exact accounting for every number of honest gateways, a controlled comparison with a federated CVAE, and a configuration guide. Our literature search was not systematic.

Ý chính: không dùng chữ "novel" hay "first". Nhắc tìm kiếm không hệ thống.

### Q12. Could test rows leak from training rows, since some classes come from one capture?

Answer: We reduced that risk but cannot rule it out. Eight of the ten attack sub-classes come from one capture, so validation and test are contiguous blocks with 1,000-row buffers, and streams that cross a boundary are dropped. A random row split scores only 0.009 above the group split, and re-running with two other choices of test groups kept 8 of 10 verdicts.

Ý chính: đã giảm, chưa loại hẳn; có hai bằng chứng (0.009 và 8/10).

### Q13. Why delta ten to the minus five?

Answer: Delta is below one over n, which is about 1.13 times ten to the minus five for our 88,500 training packets, but not far below it. We state that in the paper as it is.

Ý chính: thừa nhận δ không nhỏ hơn 1/n nhiều. Đừng nói δ "rất nhỏ".

### Q14. Why Skellam and not Gaussian noise?

Answer: Secure aggregation works on integers modulo two to the thirty-two, so the noise must be an integer. Skellam noise is an integer, stays Skellam when summed, and has a tight Rényi bound from Agarwal and colleagues. Our Gaussian variant, MGd, was only summed in-process, not through SecAgg+.

Ý chính: SecAgg cần số nguyên; Skellam cộng lại vẫn là Skellam. MGd chỉ là ablation.

---

## Những câu không được nói

Bảng này viết bằng tiếng Anh vì lúc trình bày và trả lời câu hỏi đều nói tiếng Anh. Nó bám theo bảng "Những câu không được nói" trong `HUONG_DAN_LAM_SLIDE.md`.

| Không nói | Nói thay |
| --- | --- |
| Synthetic data improve the IDS. | Synthetic data do not improve an IDS when real data can be pooled; their value is where traffic must stay local. |
| We propose a new synthesis algorithm. | We adapt known marginal synthesis to IoT gateways and compare it under controlled conditions. |
| MG beats the CVAE by 0.16 to 0.19 under the same conditions. | Under the same trust model, MGl beats the CVAE by 0.092, 0.143 and 0.131. |
| Epsilon 5 (một mình). | Epsilon 5 per packet, delta ten to the minus five, with all five gateways honest; 14.2 with one honest gateway. |
| SecAgg+ protects the released data. | SecAgg+ hides each gateway's tables; DP bounds what the sum reveals. |
| The synthetic data look like real data. | A classifier still separates them almost perfectly: C2ST AUC 0.9995 to 1.0000. |
| FedDP-Marginal beats deep generators. | We compared one CVAE on one dataset. FLAIM, AIM and other deep generators were not compared. |
| We measured it on real gateways. | The federation, including SecAgg+, was simulated on one machine. |
| We filtered the data. | Normal traffic was exported from PCAP with the authors' export settings. |
| Local DP (cho MGl). | Client-side DP. |

---

## Việc cần kiểm tra trước khi trình bày

- [ ] Thay `[your name]` ở slide 1.
- [ ] Bấm giờ khi tập; nếu quá 14 phút thì bỏ các câu trong bảng "Câu có thể bỏ" ở đầu file.
- [ ] Đối chiếu số trên từng slide với lời nói trong file này và với `main.pdf` của nhánh IEEE.
- [ ] Tập đọc các từ trong bảng "Đọc đúng các từ khó" và các tên cấu hình, nhất là MGs-t3-eps1 và MGr-t2-eps5.
- [ ] Tập trả lời Q1 đến Q7 thành tiếng; đây là các câu dễ gặp nhất.
- [ ] Tập nói đủ giờ ít nhất hai lần, một lần có người nghe và hỏi.
