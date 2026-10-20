# Trả lời nhận xét của thầy Nguyễn Anh Nhật ("Review of PP-FedData")

Cập nhật: 20/10/2026, nhánh `IEEE`. Mỗi dòng cho biết **đã sửa gì và ở đâu** trong bài; nếu không sửa thì nêu **lý do**. Số liệu đều đọc từ `results/` của dự án hoặc từ hai phân tích trong `analysis/`, **sau vòng R** (dữ liệu Normal trích xuất lại theo đúng thiết lập của tác giả bộ dữ liệu trên Kaggle, toàn bộ thí nghiệm chạy lại ngày 16–17/10/2026). Số của bản 14/10 không còn dùng.

Ký hiệu trạng thái: ✅ đã sửa · 💬 giải thích, không sửa · ⏳ chưa làm (cần thí nghiệm hoặc quyết định của nhóm).

## 1. Vấn đề chính (logic và tính đúng)

| Ý | Trạng thái | Đã làm / giải thích | Vị trí |
|---|---|---|---|
| 1.1 So sánh RQ2 không cùng mô hình tin cậy | ✅ | Bảng IV thêm 3 hàng MGl (client-side DP, cùng mô hình tin cậy với CVAE) và cột ghi rõ cs/dist. Áp **luật (9)** đầy đủ, bootstrap cả theo dòng lẫn theo stream (`analysis/rule9_rq2.py`, CVAE tốt nhất trên validation: M1-eps1, M3o-eps5, M1o-eps10): MGl − CVAE = +0.092 [0.088, 0.095], +0.143 [0.139, 0.147], +0.131 [0.127, 0.135] ở ε = 1, 5, 10, đều lớn hơn độ lệch seed, nên MGl **tốt hơn ở cả ba mức ε**; recall lớp hiếm cũng tốt hơn (+0.049, +0.147, +0.131). MG phân tán tốt hơn CVAE +0.16 đến +0.19. (Bản 14/10 trên dữ liệu cũ cho kết quả hoà ở ε = 1; với dữ liệu vòng R kết luận này không còn đúng.) Abstract, RQ2 và Kết luận đã viết lại tương ứng. | Abstract, V-B, Bảng IV, VI |
| 1.2 Chia noise với DP-SGD mâu thuẫn [16], [17] | ✅ + ⏳ | Đã sửa câu cho đúng phạm vi: [16], [17] cộng noise **một lần mỗi vòng** vào tổng các update đã cắt (kiểu DP-FedSGD), nên chia được; còn CVAE của nhóm chạy **DP-SGD mức bản ghi với nhiều bước cục bộ** (Opacus), noise nằm trong quá trình tối ưu của từng gateway nên không chia được. Biến thể DP-FedSGD cho CVAE đã viết nhưng **chưa chạy**, vì sau khi chuyển sang FedDP-Marginal làm bộ sinh chính, CVAE chỉ còn là baseline (`SPEC_DEVIATIONS` O2.1). Đã ghi vào Limitations và Future work. Đối thủ trực tiếp hơn đã được chạy: **bộ phân loại huấn luyện bằng FL với noise phân tán** (DP-FedSGD, noise chia cho các gateway như FedDP-Marginal, `SPEC_DEVIATIONS` R.7), xem 1.3. | III-C, V-A, V-E, VI |
| 1.3 So với bộ phân loại FedAvg chưa hợp lý | ✅ | FedMLP đã có trong Bảng III. Đã so trong cùng điều kiện DP: FedMLP với DP-SGD tại mỗi gateway đạt 0.245 / 0.276 / 0.290 ở ε = 1 / 5 / 10 (MGl: 0.267 / 0.397 / 0.406). Với noise chia cho các gateway (DP-FedSGD, tinh chỉnh theo từng ε) đạt 0.350 / 0.369 / 0.389; so với FedDP-Marginal cùng bộ phân loại MLP (0.337 / 0.425 / 0.433), luật (9) cho **hoà ở ε = 1, thua 0.057 và 0.043 ở ε = 5 và 10**. Cách huấn luyện trực tiếp cần 2.593 vòng, khoảng 7,7 GB, và khi chỉ còn một gateway trung thực thì ε tăng lên 3.1 / 58.6 / 142 (FedDP-Marginal: 2.4 / 14.2 / 33.1). Kết luận RQ1 sửa cho nhất quán: dữ liệu sinh hữu ích nhất khi có DP; không có DP thì huấn luyện trực tiếp bằng FedAvg là phương án rẻ hơn nếu không cần dữ liệu chia sẻ. | V-A, Bảng III |
| 1.4 Mâu thuẫn trong cách chia dữ liệu | ✅ | Ghi rõ đây là **ngoại lệ** cho 8 trong 10 lớp con tấn công (chỉ có một capture), nêu rủi ro rò rỉ theo thời gian dù đã có buffer 1.000 dòng, và kết quả kiểm tra độ nhạy (đổi nhóm test hai lần: giữ 8/10 kết luận). | IV-A |
| 1.5 Tiền xử lý tập trung | ✅ | Thêm một gạch đầu dòng vào Limitations: cách làm khi triển khai thật (dải giá trị công khai, giao thức bảo mật, hoặc công bố có DP trước Release 1, tốn một phần ngân sách). | IV-A, V-E |
| 1.6 Bảng VI không khớp luật năm bước | 💬 + ✅ | Bảng VI đã thay bằng kết quả `recommend` của vòng R và **khớp với luật như đã cài đặt** (`recommend.py`). Bài mô tả lại bước (iv)–(v) cho đúng code: Pareto front tính trên utility, ε, việc dùng SecAgg+ và chi phí; rồi chọn cấu hình có chỉ số ưu tiên cao nhất, các cấu hình trong độ lệch seed được báo là hoà. (a) ε là bảo đảm theo giả định tin cậy của kịch bản: khi gateway có thể thông đồng thì lấy ε với một gateway trung thực, nên *consortium* chọn MGr-t2-eps5 (7.63); khi gateway được tin, cấu hình ngưỡng tính theo **ε mục tiêu** (MGs-t3-eps5 tính là 5, không phải 3.72). (b) Hai lựa chọn có hoà, bài ghi rõ: *lab* hoà MGp-nodp với MGs-nodp; *cloud-aggregator* hoà MGd-eps5 (tổng bảo mật **mô phỏng trong tiến trình**) với MGs-t3-eps5 (0.420, chạy qua SecAgg+ thật của Flower). (c) *capture-privacy*: m = 50 là **giới hạn số gói lấy từ mỗi capture**, nên ε vẫn bảo vệ trọn cả capture; vì utility quá thấp (0.177), bảng ghi chú † "đạt về hình thức, không thực tế". ⏳ Nếu thầy muốn tính ε của cấu hình t theo trường hợp mọi gateway trung thực, cần đổi luật, chạy lại `recommend` và ghi vào `SPEC_DEVIATIONS`. | V-D, Bảng VI |
| 1.7 Tính bất biến khi đổi cách chia dữ liệu | ✅ | Ghi rõ đây là **hệ quả của thiết kế**. Các lần chạy với α và K khác nhau chỉ dùng **1 seed**: α = 0.1 và α = 10 cho kết quả giống hệt nhau (0.398, MGs ở ε = 5), đúng như dự đoán; K = 10 và 20 cho 0.400 và 0.415, khác nhau do lần rút noise và bộ phân loại được chọn trên validation. | V-C |
| 1.8 MIA thiếu khoảng tin cậy | ✅ | Tính lại điểm tấn công từng bản ghi (4 cấu hình của vòng R × 3 seed: MGs-nodp, MGs-eps1, MGr-eps5, MGs-eps10, khớp `results/mia_marginal.json`), rồi bootstrap 1000 lần, lấy lại bản ghi trong từng nhóm lớp × thành viên, ghép cặp giữa các cấu hình (`analysis/mia_bootstrap.py`). AUC: không DP 0.573 [0.568, 0.578]; ε = 1, 5, 10: 0.515 [0.510, 0.520], 0.525 [0.519, 0.530], 0.539 [0.534, 0.544]. Mức giảm so với không DP: 0.059 [0.052, 0.065], 0.048 [0.042, 0.055], 0.034 [0.029, 0.040]. Cả ba khoảng đều không chứa 0 và lớn hơn độ lệch seed lớn nhất (0.0040), nên **đạt luật (9)**. TPR@1% FPR: 1.91% [1.85, 2.00] không DP so với 1.14–1.39% có DP. Đối chứng dương của tấn công: AUC 0.835 trên bảng không noise của 500 bản ghi. Kết luận dùng số trung bình mới (0.573 → 0.515–0.539). | V-C, VI |

## 2. Vấn đề vừa phải

| Nhận xét | Trạng thái | Đã làm / giải thích |
|---|---|---|
| MB trong Abstract (27–68) khác RQ2 (27–44) | ✅ | Thống nhất 13.6–72.4 MB ở cả Abstract và RQ2 (ba cấu hình CVAE có DP tốt nhất của vòng R: M1-eps1 16.9, M3o-eps5 13.6, M1o-eps10 72.4 MB). |
| MB/vòng của CVAE khác nhau | ✅ | Do kích thước mạng khác nhau: (256, 128) cho B3/M2; (128, 64) cho M1/M3; width 64–128, latent 16 cho M1o/M3o tái tinh chỉnh. Đã ghi trong III-D. |
| 0.174/0.129 = 1.35 chứ không phải 1.34 | 💬 + ✅ | Số của vòng R là 0.158 / 0.114 MB = **1.39×** (thời gian 21.6 / 20.4 s = 1.06×). Bài ghi rõ phép so là MGs-nodp (qua SecAgg+) với MGp-nodp (Flower thường). |
| Chọn bin ngược trực giác (32 bin ở ε = 1) | ✅ | Sau vòng R, tìm kiếm trên validation chọn 16 bin ở ε = 1 và 5, 8 bin ở ε = 10, nên không còn điểm ngược trực giác; câu giải thích cũ đã bỏ. |
| δ = 10⁻⁵ chỉ dưới 1/N một chút | 💬 + ⏳ | Đã thừa nhận trong IV-B: δ < 1/n ≈ 1.13 × 10⁻⁵ nhưng không nhỏ hơn nhiều. Giảm δ phải hiệu chỉnh lại noise và chạy lại toàn bộ thí nghiệm. |
| "Local DP" gây hiểu nhầm | ✅ | Đổi thành **client-side DP** (mỗi gateway tự đảm bảo DP cho bản công bố của mình), định nghĩa ở II-A, dùng thống nhất trong toàn bài, bảng và hình. |
| "eleven DoS/DDoS sub-classes" | ✅ | Sửa thành "eight of the ten attack sub-classes". |
| "plain decoder" gây hiểu nhầm | ✅ | Ghi rõ: bản DP dùng plain decoder; B3/M2 (không DP) dùng residual-noise decoder (với plain decoder B3 đạt 0.407 thay vì 0.413), có chú thích ở Bảng IV. |
| Bảng I quá thô | ✅ | Thêm ký hiệu ○ "một phần" cho Hamouda (DP áp lên bộ phân loại) và Yao (chỉ chia sẻ bí mật ở chiều xuống). |
| Tiêu đề nói quá | ✅ | Đổi theo gợi ý của thầy: "Privacy-Preserving Federated Synthetic Data Generation for Intrusion Detection in MQTT-Based IoT Gateways". |
| Trục ε của Hình 3 cách đều | ✅ | Caption ghi rõ đây là trục phân loại. Hình 3–4 vẽ lại bằng Python từ `results/`. |

## 3. Ký hiệu

| Nhận xét | Trạng thái | Đã làm |
|---|---|---|
| C: số lớp / ngưỡng cắt gradient | ✅ | Ngưỡng cắt đổi thành **G** ở (8). |
| D: dữ liệu / số đặc trưng | ✅ | Dữ liệu là $\mathcal{D}_k$ (chữ thư pháp, đã có từ trước); số đặc trưng đổi thành **p** (p = 59 sau vòng R). |
| T: số bảng / cây T\*; Fig. 2 ghi "tree T" | ✅ | Số bảng đổi thành **M_r** ở (4); Fig. 2 đã sửa thành T\* (commit `e8090d9`). |
| B: batch / B_fine / B0 | ✅ | Batch đổi thành **b** ở (8). |
| K: tập / số gateway | 💬 | Bài đã dùng $\mathcal{K}$ (chữ thư pháp) cho tập, kể cả ở (7), và K cho số lượng. |
| N: 88.500 / N(0, I) | ✅ | Số mẫu đổi thành **n**. |
| (3) giả định cạnh có hướng | ✅ | Ghi rõ "every edge (u, v) of T\* is oriented away from r". Đồng thời viết gọn điều kiện thành "c" để (3) vừa một cột. |
| (5) cách tham số hoá Skellam | ✅ | Thêm ghi chú: Agarwal et al. viết Sk_{μ,μ} có phương sai 2μ; (5) là bound của họ viết lại theo phương sai. |
| MGd, MGb, MGp chưa định nghĩa; tiêu đề Bảng V; chú thích Bảng IV | ✅ | Định nghĩa trong chú thích Bảng III và caption Hình 4; tiêu đề Bảng V sửa thành "at ε = 5, With the Non-Private References"; thêm chú thích viết tắt cho Bảng IV. |

## 4. Văn phong

| Nhận xét | Trạng thái | Đã làm / giải thích |
|---|---|---|
| Từ viết tắt chưa định nghĩa | ✅ | Định nghĩa ở lần dùng đầu trong thân bài: FedAvg, CVAE, non-IID, MPC, SMOTE, QoS, PCAP, TRTR, TSTR, TAug, RF, MLP, AUC. |
| Câu kể chuyện | ✅ | Viết lại: "Our contribution lies in combining these components…", "The federated CVAE was the initial design choice; because…". |
| Thuật ngữ không thống nhất | ✅ | Thống nhất gateway (client chỉ dùng khi nói FL chung), sub-class, một con số duy nhất cho chi phí SecAgg+ (1.39× sau vòng R). |
| Lỗi dính chữ ("thenoisy"…) | 💬 | Mã nguồn không có các lỗi này; nhiều khả năng do công cụ trích chữ từ PDF. |
| "16.9 GB RAM" | ✅ | Sửa thành 16 GB. |
| "real SecAgg+ implementation" | ✅ | Sửa thành "the SecAgg+ implementation of the Flower framework". Bài cũng ghi rõ mọi thứ chạy mô phỏng trên một máy. |

## 5. Định dạng IEEE

| Nhận xét | Trạng thái | Giải thích |
|---|---|---|
| "Fig." ở đầu câu phải viết "Figure" | 💬 | Template hội nghị IEEE quy định dùng "Fig." **kể cả ở đầu câu** ("Use the abbreviation 'Fig. 1', even at the beginning of a sentence"). Nhóm giữ nguyên theo template. |
| Độ dài (khoảng 7 trang, hội nghị giới hạn 5–6) | 💬 | Giới hạn của trường cho bài này là **10 trang** tính cả tài liệu tham khảo; bản build ngày 14/10 đúng 10 trang. Abstract đã rút còn khoảng 230 từ. |
| Tài liệu tham khảo không thống nhất | ✅ | Viết tắt tên hội nghị và tạp chí theo cùng một kiểu IEEE ("Proc. …", "Adv. Neural Inf. Process. Syst.", "IEEE Trans. …"); bỏ URL ở các mục đã có thông tin xuất bản; sửa [2] thành "B. Agüera y Arcas"; dấu của Rényi, Gascón, Rätsch, Tramèr, Gusmão đã đúng. |
| Kiểm tra phiên bản phần mềm và [11] | 💬 | Phiên bản (PyTorch 2.14, Flower 1.39, scikit-learn 1.9) lấy từ `results/repro/environment.json` của dự án. [11] (Shettar et al., IEEE Access, vol. 14, pp. 117847–117860, 2026) đã đối chiếu trên Crossref. |
| "rule (9)" → "(9)" | ✅ | Đã sửa. |
| Bảng VI ngắt dòng xấu | ✅ | Cột Scenario không còn ngắt dòng (đã kiểm tra trên bản build). |
| Email tác giả nên dùng @fpt.edu.vn | ⏳ | Nhóm quyết định. |

## 6. Việc còn lại

1. ⏳ Chạy biến thể DP-FedSGD (noise phân tán) cho CVAE, nếu thầy yêu cầu trả lời trọn ý 1.2.
2. ⏳ Quyết định có đổi cách tính ε của cấu hình ngưỡng t trong luật chọn không (1.6).
3. ⏳ δ nhỏ hơn: chỉ làm được nếu chạy lại thí nghiệm.
4. ⏳ Email tác giả; sửa Hình 1 (nhãn 6–7 pt) và Hình 2 (theo `minh_hoa/fig2_mot_cot_88x47mm.png`).
