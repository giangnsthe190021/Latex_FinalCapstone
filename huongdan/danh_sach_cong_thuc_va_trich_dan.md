# Danh sách công thức và trích dẫn trong đồ án (nhánh `main`)

Cập nhật: 2026-11-10 (lần 5: thêm trích dẫn Macro-F1, thay Hình 3.2 và 3.3 bằng hình ConceptDraw của bài báo IEEE). Đối chiếu với bản PDF 146 trang build từ mã nguồn hiện tại.

File này liệt kê **mọi công thức** trong đồ án, công thức nào đã cite đúng chuẩn IEEE, cite ở đâu, căn cứ vào đâu, và những gì còn lại.

> Số trích dẫn [n] trong file này là số trong bản PDF hiện tại. Khi thêm nguồn mới, số của các nguồn đứng sau sẽ tăng lên; LaTeX tự đánh lại số.

---

## 1. Chuẩn cite áp dụng

Với công thức lấy từ tài liệu khác, IEEE cho phép ghi **vị trí chính xác (pinpoint)** trong ngoặc vuông:

| Loại | Cách ghi trong PDF | Cách viết trong LaTeX |
|---|---|---|
| Phương trình | `[22, eq. (3.2)]` | `\cite[eq.~(3.2)]{agarwal2021}` |
| Định lý | `[66, Th. 21]` | `\cite[Th.~21]{balle2020}` |
| Định nghĩa / Bổ đề / Mệnh đề / Hệ quả | `[10, Def. 1]`, `[53, Lemma 1.7]`, `[53, Prop. 1.6]` | `\cite[Def.~1]{chow1968}` |
| Thuật toán / Cấu trúc | `[4, Algorithm 1]`, `[61, Construction A]` | `\cite[Algorithm~1]{mcmahan2017}` |
| Mục / Phụ lục / Trang | `[44, Sec. 3]`, `[11, App. E.1]`, `[74, p. 39]` | `\cite[Sec.~3]{hsu2019}` |

**Quy tắc bắt buộc:** chỉ ghi pinpoint khi **đã đọc đúng nhãn đó trong bài gốc**. Không đoán số, không lấy số từ bài khác trích lại. Nếu nguồn không đánh số công thức thì cite theo mục (Sec.) hoặc trang (p.); cite không pinpoint vẫn hợp lệ khi nguồn chỉ có một trang hoặc không có nhãn nào. Công thức do nhóm tự đặt hoặc tự suy ra thì **không** cite.

---

## 2. Tổng quan

Đồ án có **23 công thức đánh số**, tất cả nằm trong Chương 3: (3.1) đến (3.23). Chương 1, 2, 4, 5, 6 và phụ lục không có công thức đánh số.

| Trạng thái | Số lượng | Công thức |
|---|---|---|
| Đã cite đúng chuẩn (pinpoint đã đọc trong bài gốc) | 19 | 3.2, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.15, 3.16, 3.17, 3.18, 3.20, 3.21, 3.22, 3.23 |
| Nhóm tự đặt / tự suy ra, không cần cite | 4 | 3.1, 3.3, 3.14, 3.19 |

4 công thức viết trong dòng (không đánh số) đều đã xử lý xong (Mục 5).

**Mọi công thức lấy từ tài liệu khác đều đã có pinpoint. Không còn gì bắt buộc phải bổ sung.**

---

## 3. Bảng đầy đủ 23 công thức

Cột "Dòng" là dòng trong `chapters/main/Chapter3.tex` (bấm để mở trên GitHub). Cột "Trang" là trang trong `main.pdf`.

| Số | Trang | Dòng | Nội dung | Cite hiện tại | Trạng thái |
|---|---|---|---|---|---|
| (3.1) | 38 | [334](../chapters/main/Chapter3.tex#L334) | Bộ yêu cầu triển khai R | không | Nhóm tự đặt, không cần cite |
| (3.2) | 47 | [559](../chapters/main/Chapter3.tex#L559) | Phân hoạch Dirichlet theo lớp | [44, Sec. 3] Hsu 2019 | Chuẩn (bài gốc không đánh số công thức nên cite theo mục) |
| (3.3) | 48 | [610](../chapters/main/Chapter3.tex#L610) | Tổng các bảng đếm qua SecAgg⁺ bằng bảng tập trung | [18] Bell 2020 (cho SecAgg⁺) | Phép cộng tự suy ra, không cần pinpoint |
| (3.4) | 51 | [657](../chapters/main/Chapter3.tex#L657) | Cây Chow–Liu và thông tin tương hỗ | [10, Def. 1], [10, Def. 2], [10, Sec. III], [10, Sec. IV]; [61, Construction A] | Chuẩn |
| (3.5) | 52 | [662](../chapters/main/Chapter3.tex#L662) | p̂: cắt ở 0, làm trơn Laplace, chuẩn hoá | [40, eq. (2)] MST | Chuẩn |
| (3.6) | 52 | [673](../chapters/main/Chapter3.tex#L673) | Hiệu chỉnh Miller–Madow cho MI | [62] Miller 1955; [63, eq. (2.12)] Treves–Panzeri 1995 | Chuẩn (dạng cho MI lấy từ Treves–Panzeri) |
| (3.7) | 53 | [681](../chapters/main/Chapter3.tex#L681) | Phân tích phân phối theo cây | [10, eq. (1)] | Chuẩn |
| (3.8) | 54 | [708](../chapters/main/Chapter3.tex#L708) | Gộp theo trọng số nghịch đảo phương sai | [11, App. E.1] Private-PGM | Chuẩn |
| (3.9) | 57 | [755](../chapters/main/Chapter3.tex#L755) | ρ của zCDP và chuyển sang (ε, δ) | [53, Prop. 1.3], [53, Prop. 1.6], [53, Lemma 1.7] | Chuẩn |
| (3.10) | 57 | [765](../chapters/main/Chapter3.tex#L765) | Cận RDP của cơ chế Skellam | [22, Corollary 3.6, eq. (3.2)] | Chuẩn |
| (3.11) | 57 | [770](../chapters/main/Chapter3.tex#L770) | Chuyển RDP sang (ε, δ) | [66, Th. 21]; cộng dồn RDP [42, Proposition 1] | Chuẩn |
| (3.12) | 58 | [791](../chapters/main/Chapter3.tex#L791) | Độ nhạy theo nhóm Δ_group = m·Δ | [51, Defs. 3.1 and 3.8], [51, Th. 2.2] | Chuẩn |
| (3.13) | 59 | [798](../chapters/main/Chapter3.tex#L798) | ρ_group = ℓ²ρ | [53, Prop. 1.9] | Chuẩn |
| (3.14) | 60 | [816](../chapters/main/Chapter3.tex#L816) | ε hiệu dụng = max theo client | không (quy ước của nhóm) | Không cần cite |
| (3.15) | 61 | [840](../chapters/main/Chapter3.tex#L840) | Hàm mất mát CVAE | [69, eq. (3)] Kingma–Welling; [41, eq. (4)] Sohn; [70, eq. (4)] Higgins | Chuẩn |
| (3.16) | 62 | [854](../chapters/main/Chapter3.tex#L854) | FedAvg | [4, Algorithm 1] | Chuẩn |
| (3.17) | 62 | [866](../chapters/main/Chapter3.tex#L866) | Kẹp gradient và thêm nhiễu DP-SGD | [43, Algorithm 1] | Chuẩn |
| (3.18) | 63 | [878](../chapters/main/Chapter3.tex#L878) | Tổng modulo 2³² của SecAgg⁺ | [18, Sec. 3.1] Bell 2020 | Chuẩn |
| (3.19) | 63 | [883](../chapters/main/Chapter3.tex#L883) | Cận chống tràn số modulo | không | Nhóm tự suy ra, không cần cite |
| (3.20) | 65 | [933](../chapters/main/Chapter3.tex#L933) | Hệ số Jaccard | [74, p. 39] Jaccard 1912 | Chuẩn (bài gốc định nghĩa ở chú thích 1, trang 39) |
| (3.21) | 67 | [965](../chapters/main/Chapter3.tex#L965) | Quy tắc lọc một độ lệch chuẩn | [75, Sec. 7.10.1] Hastie ESL | Chuẩn |
| (3.22) | 69 | [1014](../chapters/main/Chapter3.tex#L1014) | F1 theo lớp và Macro-F1 | [77, eq. (1)], [77, eq. (2)], phân biệt với [77, eq. (3)] Opitz–Burst | Chuẩn |
| (3.23) | 71 | [1051](../chapters/main/Chapter3.tex#L1051) | Quy tắc quyết định thống kê | [76, Sec. 13.3] Efron–Tibshirani (khoảng percentile, đoạn sau) | Quy tắc tự đặt; nguồn bootstrap đã có pinpoint |

**Vì sao 4 công thức (3.1), (3.3), (3.14), (3.19) không có pinpoint:** cả bốn không lấy từ tài liệu nào. (3.1) là định nghĩa của nhóm, (3.3) là phép cộng số nguyên, (3.14) là quy ước báo cáo, (3.19) là phép tính số học. Theo chuẩn IEEE, định nghĩa và suy luận của chính tác giả không cần trích dẫn; gắn đại một nguồn vào là cite sai.

---

## 4. Những gì còn lại (đều không bắt buộc)

- **Miller 1955 [62]:** vẫn cite không pinpoint vì chưa có file. Công thức (3.6) đã có căn cứ đầy đủ nhờ Treves–Panzeri eq. (2.12). Nếu nhóm có bản scan, Claude có thể thêm số trang.
- **Skellam 1946 [67]:** bài chỉ có một trang (tr. 296) và không đánh số công thức, nên cite không pinpoint là đúng.
- **Lỗi chữ trong Hình 3.3 (Fig. 2 của bài báo IEEE):** ba mũi tên ghi **"unit 32"**, đúng ra là **"uint32"** (số nguyên không dấu 32 bit, như hình TikZ cũ). Hình vẽ bằng ConceptDraw nên Claude không sửa được file PDF; nhóm cần sửa trong ConceptDraw rồi xuất lại `graphics/paper/Fig2.pdf` cho **cả hai nhánh** `main` và `IEEE`.

---

## 5. Công thức viết trong dòng (không đánh số)

| Dòng | Công thức | Tình trạng |
|---|---|---|
| [699](../chapters/main/Chapter3.tex#L699) | σ_r = Δ_{2,r} / √(2ω_r ρ) | Đã cite `[53, Proposition 1.6]` |
| [797](../chapters/main/Chapter3.tex#L797) | Cận nhóm ℓ·e^{(ℓ−1)ε}·δ cho (ε, δ)-DP | Đã cite `[51, Sec. 2.3]` (chú thích 1 của Mục 2.3) |
| [677](../chapters/main/Chapter3.tex#L677) | MI chuẩn hoá I / √(H(X_i)·H(X_j)) | Đã cite `[64, eq. (2)]` Strehl–Ghosh 2002 |
| [725](../chapters/main/Chapter3.tex#L725) | Xác suất một giá trị nhiễu vượt C_clip, khoảng 10⁻⁹ | Đã sửa: ghi rõ là xấp xỉ Gauss, không cần nguồn |

**Ghi chú về dòng 725.** Câu cũ viết "below 10⁻⁹ by the Skellam tail bound" nhưng không có nguồn: bài Skellam của Agarwal et al. [22] không có cận đuôi nào được đánh số trong các phần đã đọc. Câu mới (nhóm đồng ý ngày 2026-11-10) nói rõ ba điều:
- Chỉ một ô chứa gần đủ N bản ghi, với nhiễu lệch lên trên quá 6σ, mới có thể vượt C_clip (trường hợp xấu nhất, một phía).
- Con số khoảng 10⁻⁹ là **xấp xỉ Gauss** (một phía ở 6σ: khoảng 9,9 × 10⁻¹⁰). Xấp xỉ này chính xác vì phương sai nhiễu lớn: đuôi Skellam chỉ nặng hơn đuôi Gauss khoảng e^(54/μ) lần. Cận Chernoff chặt chẽ chỉ cho khoảng 1,5 × 10⁻⁸, nên không được viết "nhỏ hơn 10⁻⁹" như một cận.
- Xác suất này **không** được cộng vào δ.

---

## 6. Đối chiếu với ghi chú trong `README_THONG_KE.md` của nhóm

Claude đã mở từng file PDF trong thư mục `source_citation` và đọc đúng trang. Phần lớn ghi chú của nhóm khớp; hai chỗ lệch được sửa theo bài gốc:

| Nguồn | Ghi chú của nhóm | Đọc trong bài gốc | Dùng trong đồ án |
|---|---|---|---|
| Chow–Liu 1968 | (3.4): Th. 1, p. 464 | Bài **không có nhãn "Theorem 1"**. Trang 463 có Definition 1 (thông tin tương hỗ), Definition 2 (cây trọng số lớn nhất) và kết quả tối ưu phát biểu không đánh nhãn trong Mục III. Trang 464 là Mục IV (thuật toán Kruskal) | `[10, Def. 1]`, `[10, Def. 2]`, `[10, Sec. III]`, `[10, Sec. IV]` |
| Chow–Liu 1968 | (3.7): eq. 1, p. 462 | Khớp | `[10, eq. (1)]` |
| Bell 2020 | (3.18): Sec. 3 | Khớp. Mục 3.1 "An abstract summation protocol" (tr. 1256) mô tả tổng có mặt nạ; Definition 4.1 nêu đầu vào trong Z_R | `[18, Sec. 3.1]` |
| Higgins 2017 | (3.15): eq. 4, p. 5 | Khớp | `[70, eq. (4)]` |
| Efron–Tibshirani 1993 | (3.23): Sec. 13.3, p. 170 | Khớp | `[76, Sec. 13.3]` |
| Hastie 2009 | (3.21): Sec. 7.10, p. 244 | Khớp; cụ thể hơn là Mục 7.10.1, trang 244 (bản in lần 12, 2017) | `[75, Sec. 7.10.1]` |
| Jaccard 1912 | (3.20): p. 40, fn. 1 | **Trang 39**, chú thích 1 (hệ số = số loài chung / tổng số loài × 100) | `[74, p. 39]` |
| Miller 1955 | (3.6) suy ra từ pp. 95–100 | Chưa có file để kiểm tra. pp. 95–100 là số trang của cả chương | Giữ `[62]`, thêm `[63, eq. (2.12)]` Treves–Panzeri |
| Treves 1995 | không có ghi chú | eq. (2.12), tr. 403: số hạng hiệu chỉnh bậc một C₁ = (S−1)(R−1)/(2N ln 2), tính theo bit | `[63, eq. (2.12)]`, nguồn mới thêm vào `reference.bib` |

Các nhãn đã dùng từ trước cũng được kiểm tra lại bằng file của nhóm: Abadi Algorithm 1, McMahan Algorithm 1, Mironov Proposition 1, Dwork–Roth Th. 2.2, Defs. 3.1 và 3.8 đều khớp.

**Opitz–Burst 2019 [77]** (Macro-F1) không có trong thư mục của nhóm; Claude tải bản arXiv v3 và đọc trực tiếp: eq. (1) là precision, recall, F1 theo lớp (mẫu số bằng 0 thì gán 0), eq. (2) là "averaged F1" (trung bình cộng các F1 theo lớp), eq. (3) là "F1 of averages" (F1 của precision và recall trung bình). Code `src/ppfeddata/eval/utility.py` tính đúng eq. (2).

---

## 7. Hình vẽ thay bằng bản ConceptDraw (ngày 2026-11-10)

| Hình trong đồ án | Trước | Sau | File |
|---|---|---|---|
| Hình 3.2 (tr. 31), kiến trúc hệ thống với hai nhánh sinh dữ liệu | Vẽ bằng TikZ trong `Chapter3.tex` | Fig. 1 của bài báo IEEE (ConceptDraw), chú thích dài hơn theo bài báo | `graphics/paper/fig1_architecture.pdf` |
| Hình 3.3 (tr. 50), giao thức ba lần phát hành của FedDP-Marginal | Vẽ bằng TikZ trong `Chapter3.tex` | Fig. 2 của bài báo IEEE (ConceptDraw), cắt bỏ khoảng trắng hai bên khi chèn; file gốc giữ nguyên | `graphics/paper/Fig2.pdf` |

Hai file được chép nguyên từ nhánh `IEEE`, nên khi nhóm sửa hình trong ConceptDraw cần chép bản mới vào **cả hai nhánh**. Nhãn `fig:system_arch` và `fig:three_release` giữ nguyên, nên mọi chỗ dẫn "Figure 3.2", "Figure 3.3" trong đồ án vẫn đúng. Danh mục hình dùng chú thích ngắn như cũ.

---

## 8. Lịch sử sửa trích dẫn (ngày 2026-11-10)

| Vị trí | Trước | Sau | Căn cứ |
|---|---|---|---|
| (3.5) | "Following the post-processing of McKenna et al. [40]" | Cắt ở 0 và làm trơn là lựa chọn của nhóm; MST khớp mô hình đồ thị bằng bình phương tối thiểu `[40, eq. (2)]` | Bài MST không có bước cắt và làm trơn; code `src/ppfeddata/models/marginal.py` là cách nhóm tự cài đặt |
| (3.8) | "Following McKenna et al. [40]" | Cách gộp mà Private-PGM dùng để ước lượng tổng số bản ghi `[11, App. E.1]` | Bài MST không có; Private-PGM có ở Phụ lục E.1 |
| (3.14) | "worst client [Mironov 2019]" | "By the convention of this study, ... worst client" | Mironov 2019 không nói về việc lấy client tệ nhất |
| (3.2) | "label-skew model of Hsu et al. [44]" | `[44, Sec. 3]`, nói rõ đồ án dùng **dạng chuyển vị** | Hsu et al. rút tỉ lệ lớp cho từng client; code `src/ppfeddata/partition.py` rút tỉ lệ chia cho từng lớp qua K gateway |
| (3.12) | "scaled by the cap m [51]" | Giải thích vì sao nhân m; `[51, Defs. 3.1 and 3.8]`, `[51, Th. 2.2]` | Sách Dwork–Roth |
| (3.15) | Sohn, Higgins không pinpoint | `[41, eq. (4)]`, `[70, eq. (4)]` | Bài Sohn eq. (4); bài Higgins eq. (4) |
| (3.4) | `[10]`, `[61]` không pinpoint | `[10, Def. 1]`, `[10, Def. 2]`, `[10, Sec. III]`, `[10, Sec. IV]`, `[61, Construction A]` | Bài Chow–Liu tr. 463–464; bài Kruskal "Construction A" |
| (3.6) | `[62]` không pinpoint | Thêm `[63, eq. (2.12)]` Treves–Panzeri, ghi rõ đổi từ bit sang nat | Treves–Panzeri tr. 403 |
| (3.7) | `[10]` | `[10, eq. (1)]` | Chow–Liu tr. 462 |
| (3.18) | `[18]` | `[18, Sec. 3.1]` | Bell tr. 1256 |
| (3.20) | `[74]` | `[74, p. 39]` | Jaccard tr. 39, chú thích 1 |
| (3.21) | `[75]` | `[75, Sec. 7.10.1]` | ESL tr. 244 |
| (3.22) | không cite | `[77, eq. (1)]`, `[77, eq. (2)]`, nói rõ không phải `[77, eq. (3)]`; thêm `opitz2019` vào `reference.bib` | Opitz–Burst arXiv v3; code tính trung bình cộng các F1 theo lớp |
| (3.23) | `[76]` | `[76, Sec. 13.3]` | Efron–Tibshirani tr. 170 |
| Dòng 699 | không cite | `[53, Proposition 1.6]` | Bun–Steinke |
| Dòng 797 | không cite | `[51, Sec. 2.3]` | Dwork–Roth, chú thích 1 của Mục 2.3 |
| Dòng 677 | không cite | `[64, eq. (2)]`, thêm `strehl2002` vào `reference.bib` | Strehl–Ghosh eq. (2) |
| Dòng 725 | "below 10⁻⁹ by the Skellam tail bound" | Khoảng 10⁻⁹ mỗi ô theo xấp xỉ Gauss; không phải cận chặt, không cộng vào δ | Không có nguồn cho cận đuôi |

---

## 9. Mẫu gửi thông tin cho Claude (nếu bổ sung thêm)

```
Công thức: (3.x)
Nguồn: <tên bài / sách, năm>
Nhãn đọc được trong bài: <eq. (k) | Th. k | Lemma k | Sec. k | p. k>
Ảnh chụp hoặc đoạn trích chứa nhãn đó: <đính kèm>
```

Khi nhận được, Claude sẽ kiểm tra nhãn trong bài gốc, sửa `\cite[nhãn]{...}` trong `Chapter3.tex`, thêm nguồn vào `references/reference.bib` nếu cần, build lại `main.pdf` và cập nhật file này.
