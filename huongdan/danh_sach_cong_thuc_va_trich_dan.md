# Danh sách công thức và trích dẫn trong đồ án (nhánh `main`)

Cập nhật: 2026-11-10. Đối chiếu với bản PDF 145 trang build từ mã nguồn hiện tại.

File này liệt kê **mọi công thức** trong đồ án, công thức nào đã cite đúng chuẩn IEEE, công thức nào còn thiếu, thiếu vì sao, và **nhóm cần gửi gì** để hoàn thiện.

---

## 1. Chuẩn cite áp dụng

Với công thức lấy từ tài liệu khác, IEEE cho phép ghi **vị trí chính xác (pinpoint)** trong ngoặc vuông:

| Loại | Cách ghi trong PDF | Cách viết trong LaTeX |
|---|---|---|
| Phương trình | `[22, eq. (3.2)]` | `\cite[eq.~(3.2)]{agarwal2021}` |
| Định lý | `[64, Th. 21]` | `\cite[Th.~21]{balle2020}` |
| Bổ đề / Mệnh đề / Hệ quả | `[53, Lemma 1.7]`, `[53, Prop. 1.6]` | `\cite[Lemma~1.7]{bun2016}` |
| Thuật toán | `[4, Algorithm 1]` | `\cite[Algorithm~1]{mcmahan2017}` |
| Mục / Phụ lục / Trang | `[11, App. E.1]`, `[73, Sec. 7.10]`, `[73, p. 244]` | `\cite[Sec.~7.10]{hastie2009}` |

**Quy tắc bắt buộc:** chỉ ghi pinpoint khi **đã đọc đúng nhãn đó trong bài gốc**. Không đoán số, không lấy số từ bài khác trích lại. Nếu nguồn không đánh số công thức thì cite không pinpoint vẫn hợp lệ.

---

## 2. Tổng quan

Đồ án có **23 công thức đánh số**, tất cả nằm trong Chương 3: (3.1) đến (3.23). Chương 1, 2, 4, 5, 6 và phụ lục không có công thức đánh số.

| Trạng thái | Số lượng | Công thức |
|---|---|---|
| Đã cite đúng chuẩn (có pinpoint đã đọc) | 8 | 3.5, 3.8, 3.9, 3.10, 3.11, 3.13, 3.16, 3.17 |
| Chuẩn một phần | 1 | 3.15 |
| Có cite nhưng thiếu pinpoint | 7 | 3.2, 3.4, 3.6, 3.7, 3.12, 3.18, 3.21 |
| Có cite, pinpoint không bắt buộc | 2 | 3.20, 3.23 |
| Chưa có cite (tùy chọn) | 1 | 3.22 |
| Nhóm tự đặt / tự suy ra, không cần cite | 4 | 3.1, 3.3, 3.14, 3.19 |

Ngoài ra có **4 công thức viết trong dòng** (không đánh số) chưa có nguồn, xem Mục 5.

---

## 3. Bảng đầy đủ 23 công thức

Cột "Dòng" là dòng trong `chapters/main/Chapter3.tex`. Cột "Trang" là trang trong `main.pdf`.

| Số | Trang | Dòng | Nội dung | Cite hiện tại | Trạng thái |
|---|---|---|---|---|---|
| (3.1) | 38 | [438](../chapters/main/Chapter3.tex#L438) | Bộ yêu cầu triển khai R | không | Nhóm tự đặt, không cần cite |
| (3.2) | 47 | [663](../chapters/main/Chapter3.tex#L663) | Phân hoạch Dirichlet theo lớp | [44] Hsu 2019 | **Thiếu pinpoint** |
| (3.3) | 49 | [714](../chapters/main/Chapter3.tex#L714) | Tổng các bảng đếm qua SecAgg⁺ bằng bảng tập trung | [18] Bell 2020 (cho SecAgg⁺) | Phép cộng tự suy ra, không cần pinpoint |
| (3.4) | 51 | [783](../chapters/main/Chapter3.tex#L783) | Cây Chow–Liu và thông tin tương hỗ | [10] Chow–Liu 1968, [61] Kruskal 1956 | **Thiếu pinpoint** |
| (3.5) | 51 | [788](../chapters/main/Chapter3.tex#L788) | p̂: cắt ở 0, làm trơn Laplace, chuẩn hoá | [40, eq. (2)] MST | Đã sửa 2026-11-10, chuẩn |
| (3.6) | 52 | [799](../chapters/main/Chapter3.tex#L799) | Hiệu chỉnh Miller–Madow cho MI | [62] Miller 1955 | **Thiếu pinpoint** |
| (3.7) | 52 | [807](../chapters/main/Chapter3.tex#L807) | Phân tích phân phối theo cây | [10] Chow–Liu 1968 | **Thiếu pinpoint** |
| (3.8) | 54 | [834](../chapters/main/Chapter3.tex#L834) | Gộp theo trọng số nghịch đảo phương sai | [11, App. E.1] Private-PGM | Đã sửa 2026-11-10, chuẩn |
| (3.9) | 56 | [881](../chapters/main/Chapter3.tex#L881) | ρ của zCDP và chuyển sang (ε, δ) | [53, Prop. 1.3], [53, Prop. 1.6], [53, Lemma 1.7] | Chuẩn |
| (3.10) | 57 | [891](../chapters/main/Chapter3.tex#L891) | Cận RDP của cơ chế Skellam | [22, Corollary 3.6, eq. (3.2)] | Chuẩn |
| (3.11) | 57 | [896](../chapters/main/Chapter3.tex#L896) | Chuyển RDP sang (ε, δ) | [64, Th. 21]; cộng dồn RDP [42, Proposition 1] | Chuẩn |
| (3.12) | 58 | [917](../chapters/main/Chapter3.tex#L917) | Độ nhạy theo nhóm Δ_group = m·Δ | [51] Dwork–Roth 2014 | **Thiếu pinpoint** |
| (3.13) | 58 | [924](../chapters/main/Chapter3.tex#L924) | ρ_group = ℓ²ρ | [53, Prop. 1.9] | Chuẩn |
| (3.14) | 59 | [942](../chapters/main/Chapter3.tex#L942) | ε hiệu dụng = max theo client | không (quy ước của nhóm) | Đã sửa 2026-11-10, không cần cite |
| (3.15) | 61 | [966](../chapters/main/Chapter3.tex#L966) | Hàm mất mát CVAE | [67, eq. (3)]; [41] Sohn 2015; [68] Higgins 2017 | **Chuẩn một phần**: Sohn, Higgins thiếu pinpoint |
| (3.16) | 61 | [980](../chapters/main/Chapter3.tex#L980) | FedAvg | [4, Algorithm 1] | Chuẩn |
| (3.17) | 62 | [992](../chapters/main/Chapter3.tex#L992) | Kẹp gradient và thêm nhiễu DP-SGD | [43, Algorithm 1] | Chuẩn |
| (3.18) | 62 | [1004](../chapters/main/Chapter3.tex#L1004) | Tổng modulo 2³² của SecAgg⁺ | [18] Bell 2020 | **Thiếu pinpoint** |
| (3.19) | 62 | [1009](../chapters/main/Chapter3.tex#L1009) | Cận chống tràn số modulo | không | Nhóm tự suy ra, không cần cite |
| (3.20) | 65 | [1059](../chapters/main/Chapter3.tex#L1059) | Hệ số Jaccard | [72] Jaccard 1912 | Pinpoint không bắt buộc |
| (3.21) | 65 | [1091](../chapters/main/Chapter3.tex#L1091) | Quy tắc lọc một độ lệch chuẩn | [73] Hastie ESL 2009 | **Thiếu pinpoint** |
| (3.22) | 68 | [1140](../chapters/main/Chapter3.tex#L1140) | F1 theo lớp và Macro-F1 | không | Tùy chọn (chỉ số chuẩn) |
| (3.23) | 70 | [1177](../chapters/main/Chapter3.tex#L1177) | Quy tắc quyết định thống kê | [74] Efron–Tibshirani 1993 (cho bootstrap, đoạn sau) | Quy tắc tự đặt; pinpoint bootstrap không bắt buộc |

---

## 4. Những gì nhóm cần gửi để cite chuẩn

Sắp xếp theo mức ưu tiên. Mỗi mục ghi: thiếu gì, vì sao thiếu, cần gửi gì.

### Ưu tiên cao (công thức lõi của phương pháp)

**(3.4) và (3.7): Chow–Liu 1968 [10]**
- *Vì sao thiếu:* bản gốc (IEEE Trans. Inf. Theory, 1968) phải trả phí, Claude không đọc được.
- *Cần gửi:* file PDF bài báo, **hoặc** số phương trình nơi bài định nghĩa (a) tổng thông tin tương hỗ trên cây và (b) phân tích phân phối theo cây.
- *Sẽ ghi thành ví dụ:* `[10, eq. (k)]`.

**(3.6): Miller 1955 [62]**
- *Vì sao thiếu:* chương sách cũ, không tìm được bản đọc. Thêm nữa, bài gốc hiệu chỉnh độ lệch cho **entropy**; dạng cho thông tin tương hỗ (MI) trong đồ án là suy ra từ đó.
- *Cần gửi một trong hai:* (a) PDF bài Miller kèm số trang của công thức hiệu chỉnh; hoặc (b) một nguồn khác **có sẵn dạng cho MI** (ví dụ một bài tổng quan về ước lượng MI) kèm số phương trình. Nếu chọn (b), Claude sẽ thêm nguồn vào `reference.bib` và ghi rõ "dạng cho MI suy ra từ [62]".

**(3.12): Dwork–Roth 2014 [51]**
- *Vì sao thiếu:* chưa mở sách để đọc số định lý về quyền riêng tư theo nhóm (group privacy).
- *Cần gửi:* số định lý hoặc mục. Sách có bản PDF miễn phí trên trang của tác giả, **Claude có thể tự đọc nếu nhóm đồng ý**.

**(3.18): Bell et al. 2020 [18]**
- *Vì sao thiếu:* chưa đọc bài.
- *Cần gửi:* số định nghĩa hoặc mục mô tả tổng modulo của SecAgg⁺. Bài có bản miễn phí (IACR ePrint 2020/704), **Claude có thể tự đọc nếu nhóm đồng ý**.

### Ưu tiên trung bình

**(3.2): Hsu et al. 2019 [44]**
- *Vì sao thiếu:* trong bài, công thức Dirichlet **không đánh số**.
- *Cần gửi:* số mục (Sec.) hoặc số trang nơi bài mô tả cách chia dữ liệu bằng Dir(α). Bài có trên arXiv (1909.06335), **Claude có thể tự đọc nếu nhóm đồng ý**.
- *Sẽ ghi thành ví dụ:* `[44, Sec. k]`.

**(3.15): Sohn 2015 [41] và Higgins 2017 [68]**
- *Vì sao thiếu:* Claude không đọc được bản gốc. Phần chính của công thức đã có pinpoint `[67, eq. (3)]` (Kingma–Welling).
- *Cần gửi:* PDF hoặc số phương trình của (a) hàm mục tiêu CVAE trong Sohn 2015 và (b) hàm mục tiêu có trọng số β trong Higgins 2017.

**(3.21): Hastie, Tibshirani, Friedman 2009 [73]**
- *Vì sao thiếu:* chưa đọc sách.
- *Cần gửi:* số mục và số trang nói về "one-standard-error rule" (bản in lần 2). Sách có bản PDF miễn phí, **Claude có thể tự đọc nếu nhóm đồng ý**.

### Không bắt buộc (làm nếu còn thời gian)

- **(3.20) Jaccard 1912 [72]:** bài năm 1912 có thể chỉ mô tả bằng lời. Cite không pinpoint vẫn hợp lệ. Nếu có PDF, gửi số trang.
- **(3.23) Efron–Tibshirani 1993 [74]:** nếu muốn, gửi số chương hoặc mục về khoảng tin cậy percentile.
- **(3.22) Macro-F1:** chỉ số chuẩn, không bắt buộc cite. Nếu muốn, gửi một nguồn (ví dụ bài tổng quan về các chỉ số đánh giá phân loại) kèm số phương trình hoặc bảng; Claude sẽ thêm vào `reference.bib`.

---

## 5. Công thức viết trong dòng (không đánh số) chưa có nguồn

| Dòng | Công thức | Tình trạng | Cần gì |
|---|---|---|---|
| [825](../chapters/main/Chapter3.tex#L825) | σ_r = Δ_{2,r} / √(2ω_r ρ) (độ lệch chuẩn nhiễu Gauss theo zCDP) | Chưa cite | **Claude tự bổ sung được** `[53, Prop. 1.6]` (nhãn đã đọc), chỉ cần nhóm đồng ý |
| [923](../chapters/main/Chapter3.tex#L923) | Cận nhóm ℓ·e^{(ℓ−1)ε}·δ cho (ε, δ)-DP | Chưa cite | Một nguồn có phát biểu cận này, kèm số bổ đề hoặc định lý |
| [803](../chapters/main/Chapter3.tex#L803) | MI chuẩn hoá I / √(H(X_i)·H(X_j)) | Chưa cite, chưa có trong `reference.bib` | Một nguồn định nghĩa MI chuẩn hoá dạng căn bậc hai, kèm số phương trình |
| [851](../chapters/main/Chapter3.tex#L851) | "by the Skellam tail bound" (xác suất vượt ngưỡng < 10⁻⁹) | Chưa cite | Một nguồn có cận đuôi của phân phối Skellam, **hoặc** xác nhận nhóm tự tính để Claude ghi rõ là tự suy ra |

---

## 6. Đã sửa ngày 2026-11-10

| Công thức | Trước | Sau | Lý do |
|---|---|---|---|
| (3.5) | "Following the post-processing of McKenna et al. [40]" | Ghi rõ cắt ở 0 và làm trơn Laplace là lựa chọn của nhóm; MST khớp mô hình đồ thị bằng bình phương tối thiểu `[40, eq. (2)]` | Bài MST không có bước cắt ở 0 và làm trơn; code `src/ppfeddata/models/marginal.py` cho thấy đây là cách nhóm tự cài đặt |
| (3.8) | "Following McKenna et al. [40]" | Cách gộp mà Private-PGM dùng để ước lượng tổng số bản ghi `[11, App. E.1]` | Bài MST không có gộp theo nghịch đảo phương sai; Private-PGM có, ở Phụ lục E.1 |
| (3.14) | "worst client [66]" | "By the convention of this study, ... worst client" | Mironov 2019 [66] nói về RDP của sampled Gaussian, không nói về việc lấy client tệ nhất |

---

## 7. Mẫu gửi thông tin cho Claude

Mỗi nguồn, nhóm gửi theo mẫu dưới đây (hoặc gửi thẳng file PDF):

```
Công thức: (3.x)
Nguồn: <tên bài / sách, năm>
Nhãn đọc được trong bài: <eq. (k) | Th. k | Lemma k | Sec. k | p. k>
Ảnh chụp hoặc đoạn trích chứa nhãn đó: <đính kèm>
```

Khi nhận được, Claude sẽ:
1. Kiểm tra nhãn khớp với nội dung công thức trong đồ án.
2. Sửa `\cite{...}` thành `\cite[nhãn]{...}` trong `Chapter3.tex`, thêm nguồn mới vào `references/reference.bib` nếu cần.
3. Build lại `main.pdf`, kiểm tra không có lỗi và không có trích dẫn bị thiếu.
4. Cập nhật file này.
