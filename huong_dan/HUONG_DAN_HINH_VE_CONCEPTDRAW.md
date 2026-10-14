# Hướng dẫn vẽ hình bằng ConceptDraw cho bài báo IEEE

Bài báo có 4 hình:
- **Hình 1 và Hình 2** là sơ đồ, vẽ bằng ConceptDraw theo mô tả ở các mục bên dưới.
- **Hình 3 và Hình 4** là biểu đồ số liệu, **vẽ bằng Python** (quyết định ngày 14/10/2026, sau khi bản vẽ tay bị sai số liệu). Font Times New Roman, chữ ≥ 8 pt, số liệu đọc thẳng từ `results/`. Không cần vẽ tay; nếu kết quả thay đổi, chạy lại:

  ```
  python scripts/make_paper_figures.py --results ../results
  ```

Khi chưa có file, LaTeX hiện một khung giữ chỗ **đúng kích thước cuối cùng**, nên số trang khi build vẫn chính xác. Lệnh `\cdfigure` trong `main.tex` tự lấy file `.pdf` hoặc `.png` ngay khi file được đặt vào thư mục.

Tên file và kích thước dưới đây khớp với các file `.tex` hiện tại (từ commit `73eee4c`):

| Hình | File | Kích thước khi in | Môi trường trong LaTeX | Vị trí |
|---|---|---|---|---|
| Fig. 1 | `graphics/paper/fig1_architecture.pdf` | **182 × 60 mm** (rộng cả trang) | `figure*`, `\textwidth` | `Chapter3.tex`, III-A |
| Fig. 2 | `graphics/paper/Fig2.pdf` | **182 × 60 mm** (rộng cả trang); nên thu về **88 × 47 mm**, xem mục kiểm tra | `figure*`, `\textwidth` | `Chapter3.tex`, III-B |
| Fig. 3 | `graphics/paper/Fig3_python.pdf` (Python, không vẽ tay) | **88 × 60 mm** (1 cột) | `figure`, `\columnwidth` | `Chapter5.tex`, V-B |
| Fig. 4 | `graphics/paper/Fig4_python.pdf` (Python, không vẽ tay) | **88 × 70 mm** (1 cột) | `figure`, `\columnwidth` | `Chapter5.tex`, V-D |

Nếu bản vẽ Fig. 1–2 cao hơn chiều cao ghi ở bảng, hãy sửa tham số thứ ba của `\cdfigure` cho khớp, rồi build lại để kiểm tra giới hạn 10 trang.

## Kết quả kiểm tra ngày 14/10/2026 (commit `73eee4c`): việc cần sửa

Phương pháp kiểm tra: xem từng file PDF, rồi đọc toạ độ vector và cỡ chữ ngay trong file. Bản build lúc đó (`main.log`) dài **đúng 10 trang**, tức đang chạm giới hạn.

### Fig. 3 và Fig. 4: **đã xử lý**

Bản vẽ tay bằng ConceptDraw lệch số liệu tới khoảng 0.02 macro-F1, vạch trục không đều, trục log bị méo; Fig. 3 thiếu marker và thanh sai số. Ngày 14/10/2026 cả hai hình được thay bằng bản vẽ bằng Python từ `results/`, lưu thành `graphics/paper/Fig3_python.pdf` và `Fig4_python.pdf`. Hai file cũ `Fig3.pdf`, `Fig4.pdf` đã bị xoá khỏi repo, và bảng toạ độ để vẽ tay (`SO_LIEU_HINH_3_4.md`) cũng đã bỏ. Chú giải dùng "client-side DP" thay cho "local DP", khớp với bài.

### Fig. 1: sửa trình bày (kích thước và vị trí đã ổn)

Kiểm tra lại bản ngày 14/10/2026 sau commit `ce2dc3e`: font đã đổi hết sang Times (xong), nhưng **vẫn còn nhãn 6–7 pt**.

| Chữ | Hiện tại | Sửa thành |
|---|---|---|
| Chữ trong các ô (Gateway 1, 1. Local Count Tables, …) | Times 8 pt | đã đạt |
| "Raw traffic stays local on edge gateways" | Times **6 pt** | **8 pt**, nghiêng |
| "3 table releases", "30 training rounds" | Times **7 pt** | **8 pt** |
| "synthetic data", "TSTR / TAug" (nếu còn) | Times **6–7 pt** | **8 pt** |

- Thêm **mũi tên nét đứt** từ khối server quay về khối gateway, chạy dọc mép dưới, kèm nhãn 8 pt "cut points, T* (route 1) / global weights (route 2)".
- Ô "2. DP Noise Share": ghi thêm "(Skellam)".
- Giữa Gateway 2 và Gateway K = 5: thay dấu "|" bằng "⋮".
- Giữ khổ trang 182 × 60 mm, rồi xuất lại đè lên `graphics/paper/fig1_architecture.pdf`.

### Fig. 2: sửa trình bày

> **Ảnh minh hoạ để vẽ theo:** [`minh_hoa/fig2_mot_cot_88x47mm.png`](minh_hoa/fig2_mot_cot_88x47mm.png) (kèm bản PDF), khổ đúng 88 × 47 mm, font Times New Roman, mọi chữ 8 pt. Ảnh này được sinh bởi `scripts/make_fig2_mockup.py` và chỉ để tham khảo: hình trong bài vẫn phải vẽ bằng ConceptDraw. Có thể đặt ảnh làm nền (layer khoá), vẽ đè lên, rồi xoá nền trước khi xuất.

- Tăng các nhãn **7 pt** lên **8 pt**. Bản `ccaaa4a` còn 8 nhãn 7 pt: "uint32" (×3, trên mũi tên từ gateway sang SecAgg+), "lift" (×3, trên mũi tên từ SecAgg+ sang server), "coarse cut points", "tree T\*".
- "tree T" và "Chow–Liu tree T" đã sửa thành **T\*** (commit `e8090d9`).
- ~~Thêm "+ share ξₖ" vào ba ô Release~~: **đã xong** (commit `5bb51e8`, `ccaaa4a`), khớp với caption "count tables plus Skellam noise shares".
- **Nên làm:** phần vẽ chỉ rộng khoảng **105 mm** mà đang chiếm cả khổ 182 mm, hai bên để trắng. Nếu vẽ lại gọn **88 × 47 mm** theo mẫu ở mục Fig. 2 bên dưới, hình nằm vừa một cột và bài ngắn đi khoảng 0.2 trang (đang đúng 10 trang). Khi đó, trong `Chapter3.tex` đổi `figure*` thành `figure` và `\textwidth` thành `\columnwidth`, với chiều cao `1.85in`.

## Quy ước chung (Hình 1 và Hình 2)

- **Khổ trang:** trong ConceptDraw (File → Document Properties / Page Setup), đặt khổ đúng kích thước ở bảng trên, lề 0. Vẽ ở tỉ lệ 1:1 để cỡ chữ khi in đúng như thiết kế.
- **Font:** Times New Roman (khớp với chữ IEEE). Template hội nghị IEEE yêu cầu chữ trong hình khoảng 8–12 pt, nên **mọi chữ ≥ 8 pt**: tiêu đề nhóm in đậm 8–9 pt, chữ thường 8 pt, chú thích nhỏ in nghiêng 8 pt.
- **Màu:** dùng bảng dưới đây. In đen trắng vẫn phân biệt được nhờ viền và kiểu nét.

  | Thành phần | Nền | Viền / chữ tiêu đề |
  |---|---|---|
  | Gateway (client) | `#DCE9F7` | `#1F4E79` |
  | FedDP-Marginal (route 1) | `#E8F0FB` | `#2E75B6` |
  | Federated CVAE (route 2) | `#FCEBDD` | `#C55A11` |
  | SecAgg+ | `#D9F0EC` | `#11736B` |
  | Server | `#F8DEDA` | `#9C2B1F` (viền **nét đứt**: "honest-but-curious") |
  | IDS / đánh giá | `#E9E1F3` | `#5B3A8C` |

- **Mũi tên:** nét 0.75 pt, màu đen hoặc màu của route. Dữ liệu gửi lên dùng **nét liền**; thông tin server gửi ngược xuống gateway dùng **nét đứt**.
- **Hộp:** chữ nhật bo góc 1.5 mm, viền 0.75 pt.
- **Xuất file:** File → Export → **PDF** (vector, khuyến nghị). Nếu chỉ xuất được ảnh thì dùng PNG **600 dpi**. Đặt tên và để đúng đường dẫn ở bảng trên. Không để khoảng trắng thừa quanh hình.
- **Không** ghi số hình hay tiêu đề "Fig. 1" lên hình, vì LaTeX tự thêm caption.
- Bản TikZ cũ của hai sơ đồ này vẫn còn trong git (commit `0628d91`, file `chapters/main/Chapter3.tex`, khoảng dòng 179–286 và 714–742) và có thể dùng làm hình tham khảo.

## Fig. 1: mẫu bố cục một cột ban đầu (chỉ để tham khảo)

> Bản nhóm đã vẽ dùng **bố cục ngang 182 × 60 mm** (`figure*`), và bố cục này được giữ nguyên. Các điểm cần sửa nằm ở mục *Kết quả kiểm tra* phía trên. Mẫu 88 × 60 mm dưới đây chỉ dùng nếu sau này cần thu Fig. 1 về một cột.

Bố cục gồm 4 dải dọc, đi từ trái sang phải. Toạ độ tính theo mm từ góc trên bên trái và chỉ là gợi ý.

```
x:  0        20 22                    48 50  56 58                      88
   +----------+ +----------------------+ +----+ +------------------------+
   | EDGE     | | Route 1 (xanh)       | | S  | | HONEST-BUT-CURIOUS     |
   | GATEWAYS | | FedDP-Marginal       | | e  | | SERVER (viền đứt đỏ)   |
   |  (K = 5) | | count tables         |=| c  |=| ① Aggregate → tables,  |
   | [GW 1]   | | + Skellam share ξk   | | A  | |    Chow–Liu tree T*    |
   | [GW 2]   | | 3 releases           | | g  | | ② Sample synthetic     |
   |   ⋮      | +----------------------+ | g  | |    packets per class   |
   | [GW 5]   | +----------------------+ | +  | +-----------+------------+
   |          | | Route 2 (cam)        | |    |             ↓ synthetic
   | raw pkts | | Federated CVAE       |=|sum |=  FedAvg →  +------------------------+
   | stay     | | local training       | |only| | DOWNSTREAM IDS (RF/MLP) |
   | local    | | + DP-SGD, 30 rounds  | |    | | TSTR · TAug · local aug.|
   +----------+ +----------------------+ +----+ | → locked real test set  |
                                                 +------------------------+
   ◄- - - - - - - - - - cut points, tree T* / global model (nét đứt) - - - - - -
```

Chi tiết từng khối:

1. **Edge gateways** (x 0–20 mm, cao cả hình)
   - Tiêu đề: "Edge gateways (K = 5)".
   - Bên trong là 3 hộp nhỏ "GW 1", "GW 2", "GW 5", giữa GW 2 và GW 5 có dấu "⋮".
   - Mỗi hộp có một biểu tượng router nhỏ (thư viện *Network* của ConceptDraw) kèm chữ "local MQTT packets $\mathcal{D}_k$".
   - Chú thích nghiêng ở đáy: "raw packets never leave".
2. **Route 1, FedDP-Marginal** (x 22–48, nửa trên, màu xanh)
   - Tiêu đề: "Route 1: FedDP-Marginal (main)".
   - 2 dòng nội dung: "count tables + Skellam noise share ξ_k" và "3 releases (Fig. 2)".
3. **Route 2, Federated CVAE** (x 22–48, nửa dưới, màu cam)
   - Tiêu đề: "Route 2: Federated CVAE (baseline)".
   - 2 dòng nội dung: "local training + DP-SGD (clip, noise)" và "30 FedAvg rounds".
4. **SecAgg+** (x 50–56, một thanh dọc nối cả hai route, màu teal)
   - Chữ xoay 90°: "SecAgg+ — server sees only the sum".
   - Mũi tên của cả hai route đi xuyên qua thanh này để vào server.
5. **Server** (x 58–88, nửa trên, viền đỏ nét đứt)
   - Tiêu đề: "Honest-but-curious server".
   - 2 hộp con nối với nhau bằng mũi tên:
     - ① "Aggregate: noisy tables → tree T* / global CVAE";
     - ② "Sample synthetic packets per class".
6. **Downstream IDS** (x 58–88, nửa dưới, màu tím)
   - Hộp: "Downstream IDS (RF / MLP)".
   - Hai dòng nhỏ: "TSTR · TAug · local augmentation" và "evaluated on locked real test set".
   - Mũi tên từ server ② xuống hộp này, nhãn "synthetic data".
7. **Mũi tên ngược** (nét đứt, chạy dọc mép dưới hoặc mép trên, từ server về gateways)
   - Nhãn: "cut points, T* (route 1) / global weights (route 2)".
8. **Hai nhãn mô hình đe doạ** (tuỳ chọn, chữ đỏ 8 pt), mỗi nhãn kèm một biểu tượng:
   - cạnh server, biểu tượng con mắt: "curious server";
   - cạnh hộp ②, biểu tượng khiên: "DP: ε bounds what the release reveals about one packet".

## Fig. 2: mẫu bố cục một cột 88 × 47 mm (khuyến nghị khi vẽ lại `Fig2`)

> Bản hiện tại rộng 182 mm (`figure*`). Nếu vẽ lại theo mẫu dưới đây, xuất đè lên `graphics/paper/Fig2.pdf`. Sau đó, trong `Chapter3.tex` đổi `figure*` thành `figure` và `\textwidth` thành `\columnwidth`, với chiều cao `1.85in`.

Lưới 3 hàng (Release 1, 2, 3) × 3 cột (Gateways → SecAgg+ → Server).

```
x:  0                      34 37        51 54                         88
   +------------------------+ +----------+ +---------------------------+
R1 | Release 1              |→|          |→| noisy histograms →        |
   | 1-way counts per class | |          | | coarse cut points         |
   | 37 tables, 64 fine bins| | SecAgg+  | +---------------------------+
   +------------------------+ | over     |   ┆ broadcast cut points (nét đứt về trái)
   +------------------------+ | Z_2^32   | +---------------------------+
R2 | Release 2              |→| (uint32  |→| noisy mutual information →|
   | 2-way counts, 666 pairs| |  masked  | | Chow–Liu tree T*          |
   | coarse, pooled classes | |  sums)   | +---------------------------+
   +------------------------+ |          |   ┆ broadcast T* (nét đứt về trái)
   +------------------------+ | exact    | +---------------------------+
R3 | Release 3              |→| integer  |→| class-conditional tables →|
   | (root,y), (parent,     | | sum,     | | sample along T*           |
   |  child,y): 37 tables   | | no error | +---------------------------+
   +------------------------+ +----------+
```

Chi tiết từng khối:

- **Cột trái** (x 0–34 mm), 3 hộp màu xanh của gateway:
  - Tiêu đề cột: "Gateways k = 1…K: counts + noise share ξ_k".
  - Mỗi hộp có dòng đầu in đậm "Release r", sau đó là 2 dòng như ở sơ đồ.
- **Cột giữa** (x 37–51 mm), một hộp teal cao hết 3 hàng:
  - Chữ: "SecAgg+ over ℤ_{2^32}", "uint32 masked sums", "exact integer sum".
  - Mỗi hàng có mũi tên liền từ hộp trái vào cột giữa (nhãn nhỏ "uint32") và từ cột giữa sang hộp phải (nhãn "lift").
- **Cột phải** (x 54–88 mm), 3 hộp màu đỏ nhạt của server:
  - Tiêu đề cột: "Server (post-processing, no extra ε)".
- **Mũi tên nét đứt:** từ hộp phải của R1 vòng về hộp trái của R2, nhãn "cut points"; từ hộp phải của R2 vòng về hộp trái của R3, nhãn "T*".
- **Chú thích ngân sách** (tuỳ chọn), dòng chữ nhỏ ở đáy hình: "budget split s = (s₁, s₂, s₃) over the three releases; Skellam RDP composed over releases".

## Fig. 3 và Fig. 4: biểu đồ số liệu (Python)

Hai hình do `scripts/make_paper_figures.py` vẽ, đọc `results/scorecard.json` và `results/summary.csv`:

- khổ 88 × 60 mm (Fig. 3) và 88 × 70 mm (Fig. 4), vừa một cột IEEE;
- font Times New Roman cho cả chữ và ký hiệu toán (ε, δ), nhúng trong PDF, không có font Type 3;
- mọi chữ ≥ 8 pt; nhóm số liệu phân biệt bằng cả màu lẫn hình dạng marker, nên in đen trắng vẫn đọc được.

Script ghi ra `graphics/paper/Fig3_python.pdf` và `Fig4_python.pdf`, và `Chapter5.tex` gọi đúng hai tên này (có đuôi `.pdf`). Vì vậy file `Fig3.pdf`, `Fig4.pdf` hay `.png` vẽ tay còn sót trên máy hoặc trên Overleaf **không còn được dùng**. `.gitignore` chặn hai tên cũ, nên cũng không commit nhầm lại được. **Không vẽ lại Hình 3–4 bằng ConceptDraw**; nếu `results/` thay đổi, chỉ cần chạy lại:

```
python scripts/make_paper_figures.py --results ../results
```

## Kiểm tra trước khi nộp

- [ ] Đủ 4 file trong `graphics/paper/`, đúng tên mà `.tex` đang dùng: `fig1_architecture`, `Fig2` (`.pdf` hoặc `.png`, vẽ bằng ConceptDraw), `Fig3_python.pdf`, `Fig4_python.pdf` (Python).
- [ ] Đã xử lý hết các mục trong *Kết quả kiểm tra ngày 14/10/2026*.
- [ ] Build trên Overleaf: không còn khung giữ chỗ nào, tổng số trang vẫn ≤ 10.
- [ ] Chữ trong hình **≥ 8 pt** khi in, thuật ngữ khớp với bài: FedDP-Marginal, SecAgg+, Skellam, Chow–Liu, TSTR, TAug.
- [ ] Hình 1–2 không chứa số liệu kết quả. Hình 3–4 là bản Python mới nhất (chạy lại script nếu `results/` thay đổi).
- [ ] In thử đen trắng: các nhóm vẫn phân biệt được nhờ hình dạng marker và kiểu nét.
