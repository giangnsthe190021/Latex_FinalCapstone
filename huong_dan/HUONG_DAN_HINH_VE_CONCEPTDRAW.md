# Hướng dẫn vẽ hình bằng ConceptDraw cho bài báo IEEE

Bài báo có 4 hình, **cả 4 đều vẽ bằng ConceptDraw**:
- **Hình 1 và Hình 2** là sơ đồ: vẽ theo mô tả ở các mục bên dưới.
- **Hình 3 và Hình 4** là biểu đồ số liệu: vẽ đè lên ảnh tham chiếu theo bảng toạ độ đã sinh sẵn (mục *Fig. 3 và Fig. 4*), để số liệu khớp đúng với `results/`.

Khi chưa có file, LaTeX hiện một khung giữ chỗ **đúng kích thước cuối cùng**, nên số trang khi build vẫn chính xác. Lệnh `\cdfigure` trong `main.tex` tự lấy file `.pdf` hoặc `.png` ngay khi file được đặt vào thư mục.

| Hình | File cần xuất | Kích thước khi in | Vị trí trong bài |
|---|---|---|---|
| Fig. 1 | `graphics/paper/fig1_architecture.pdf` | rộng **88 mm** (1 cột) × cao **60 mm** | `Chapter3.tex`, mục III-A |
| Fig. 2 | `graphics/paper/fig2_three_releases.pdf` | rộng **88 mm** × cao **47 mm** | `Chapter3.tex`, mục III-B |
| Fig. 3 | `graphics/paper/fig3_tstr_vs_eps.pdf` | rộng **88 mm** × cao **60 mm** | `Chapter5.tex`, mục V-B |
| Fig. 4 | `graphics/paper/fig4_utility_vs_traffic.pdf` | rộng **88 mm** × cao **70 mm** | `Chapter5.tex`, mục V-D |

Nếu bản vẽ cao hơn chiều cao ghi ở bảng, hãy sửa tham số thứ ba của `\cdfigure` cho khớp, rồi build lại để kiểm tra giới hạn 10 trang.

## Quy ước chung (cả 4 hình)

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

## Fig. 1: Kiến trúc PP-FedData (`fig1_architecture`, 88 × 60 mm)

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

## Fig. 2: Giao thức ba lượt công bố (`fig2_three_releases`, 88 × 47 mm)

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

## Fig. 3 và Fig. 4: biểu đồ số liệu

Hai biểu đồ này chứa số liệu kết quả, nên **không được ước lượng bằng mắt**. Mọi vị trí lấy từ hai nguồn sau:
- **[SO_LIEU_HINH_3_4.md](SO_LIEU_HINH_3_4.md):** số liệu cùng toạ độ (mm) của từng điểm, thanh sai số, vạch chia trục, đường tham chiếu và nhãn. File này tự sinh từ `results/scorecard.json` và `results/summary.csv`, nên không sửa tay.
- **Ảnh tham chiếu** `tham_chieu/fig3_tstr_vs_eps_reference.png` và `tham_chieu/fig4_utility_vs_traffic_reference.png` (600 dpi). Trang và khung đồ thị của ảnh có **đúng kích thước** như trong bảng toạ độ, nên đặt ảnh làm nền là các điểm trùng khớp.

Nếu kết quả thay đổi, chạy lại lệnh sau để có bảng và ảnh mới:

```
python scripts/make_paper_figures.py --results ../results
```

### Quy trình vẽ đè (khuyến nghị)

1. **Tạo trang.** Trang mới đúng khổ (Fig. 3: 88 × 60 mm; Fig. 4: 88 × 70 mm), lề 0, đơn vị đo là mm.
2. **Đặt ảnh nền.** Tạo một layer tên `tham_chieu`, chèn ảnh PNG tham chiếu và đặt kích thước bằng đúng trang, góc trên trái ở (0, 0). Khoá layer này lại; nếu ConceptDraw có tuỳ chọn độ trong suốt thì giảm còn khoảng 40%.
3. **Vẽ trên layer mới** tên `ve`, theo thứ tự:
   1. **Khung đồ thị:** hình chữ nhật không nền, viền đen 0.2 mm, toạ độ lấy ở dòng "Khung đồ thị" trong bảng.
   2. **Lưới:**
      - Hình 3: chỉ có đường ngang tại các vạch y.
      - Hình 4: có đường ngang tại các vạch y và đường dọc tại các vạch x chính.
      - Kiểu nét: xám nhạt `#D9D9D9`, dày 0.15 mm.
   3. **Vạch chia:**
      - Đoạn thẳng dài 1.2 mm nhô ra ngoài khung: xuống dưới với trục x, sang trái với trục y.
      - Nhãn số 8 pt đặt ngay ngoài vạch.
      - Trục x của Hình 4 ghi 10⁰, 10¹, 10² (số mũ viết dạng chỉ số trên), có thêm vạch phụ ngắn 0.7 mm và không nhãn.
   4. **Đường tham chiếu (chỉ Hình 3):** B0 nét gạch, B1b nét chấm, màu xám `#595959`. Mỗi đường có nhãn 8 pt đặt sát phía trên.
   5. **Điểm:**
      - Marker cỡ 1.8 mm, viền 0.25 mm, màu và hình dạng theo bảng.
      - Hình 3: các điểm cùng chuỗi nối bằng đường liền 0.4 mm cùng màu. Thanh sai số là đoạn dọc 0.25 mm từ "Y trên" đến "Y dưới", hai đầu có gạch ngang rộng 1.4 mm.
      - Hình 4: điểm có cột "Tô đặc" = *có* thì tô đặc bằng màu của nhóm; các điểm còn lại chỉ có viền, nền trắng.
   6. **Nhãn điểm (chỉ Hình 4):** chữ 8 pt căn giữa tại toạ độ ghi trong bảng, kèm đường dẫn mảnh 0.2 mm màu xám nối tới tâm marker.
   7. **Nhãn trục:**
      - Trục y: "TSTR macro-F1 (test)", xoay 90°, căn giữa theo chiều cao khung, cách mép trái khoảng 3 mm.
      - Trục x của Hình 3: "Privacy budget ε (δ = 10⁻⁵)", trong đó ε và δ in nghiêng.
      - Trục x của Hình 4: "Total traffic per run (MB, log scale)".
      - Cả hai nhãn trục x căn giữa dưới khung, cỡ 8.5 pt.
   8. **Chú giải:** đặt đúng vị trí như ảnh tham chiếu, nội dung ghi ở cuối mỗi phần trong bảng toạ độ.
4. **Xuất file.** Ẩn hoặc xoá layer `tham_chieu`, rồi xuất PDF vector vào `graphics/paper/` với tên ở bảng đầu file.
5. **Đối chiếu.** Mở file PDF vừa xuất cạnh ảnh tham chiếu: mọi điểm, thanh sai số và nhãn phải trùng vị trí.

> Có thể dùng các mẫu biểu đồ sẵn có của ConceptDraw (nhóm *Graphs and Charts*). Tuy nhiên, Hình 4 cần **trục x logarit** và Hình 3 cần **thanh sai số**, hai thứ mà mẫu biểu đồ thường không hỗ trợ đầy đủ. Vì vậy vẽ đè theo toạ độ là cách an toàn nhất. Nếu vẫn dùng mẫu, hãy nhập số từ cột macro-F1, std và MB/lượt trong bảng, đừng đọc số từ ảnh.

## Kiểm tra trước khi nộp

- [ ] Đủ 4 file trong `graphics/paper/`: `fig1_architecture`, `fig2_three_releases`, `fig3_tstr_vs_eps`, `fig4_utility_vs_traffic` (`.pdf` hoặc `.png`).
- [ ] Build trên Overleaf: không còn khung giữ chỗ nào, tổng số trang vẫn ≤ 10.
- [ ] Chữ trong hình **≥ 8 pt** khi in, thuật ngữ khớp với bài: FedDP-Marginal, SecAgg+, Skellam, Chow–Liu, TSTR, TAug.
- [ ] Hình 1–2 không chứa số liệu kết quả. Hình 3–4 có số liệu và vị trí khớp với `SO_LIEU_HINH_3_4.md`.
- [ ] In thử đen trắng: các nhóm vẫn phân biệt được nhờ hình dạng marker và kiểu nét.
