# Số liệu và toạ độ để vẽ Hình 3 và Hình 4 bằng ConceptDraw

Tự sinh bởi `scripts/make_paper_figures.py` từ `results/scorecard.json` và `results/summary.csv` của dự án; **không sửa tay**. Chạy lại script nếu kết quả thay đổi.

Toạ độ tính bằng **mm từ góc trên bên trái trang**, trục Y hướng **xuống**. Nếu ConceptDraw của nhóm đo Y từ dưới lên, dùng Y' = (chiều cao trang) − Y. X, Y là **tâm** của hình (pin), không phải góc.

Ảnh tham chiếu cùng khung: `huong_dan/tham_chieu/fig3_tstr_vs_eps_reference.png` và `huong_dan/tham_chieu/fig4_utility_vs_traffic_reference.png` (600 dpi, đúng kích thước trang ở dưới).

## Hình 3: `fig3_tstr_vs_eps` (TSTR macro-F1 theo ε)

- Trang: **88 × 60 mm**. Khung đồ thị: x từ 14 đến 86 mm, y từ 3 (trên) đến 48 mm (dưới).
- **Khung đồ thị** (hình chữ nhật không nền, viền đen 0.2 mm): tâm (50.0, 25.5) mm, rộng 72 mm, cao 45 mm. Nhãn trục x căn giữa tại X = 50.0 mm, Y ≈ 57 mm; nhãn trục y xoay 90°, tâm tại X ≈ 3 mm, Y = 25.5 mm.
- Trục y: 0.05–0.55; trục x là 4 hạng mục ε cách đều nhau.

**Vạch chia trục**

| Trục | Giá trị / nhãn | X (mm) | Y (mm) |
|---|---|---|---|
| x | 1 | 21.6 | 48.0 |
| x | 5 | 40.5 | 48.0 |
| x | 10 | 59.5 | 48.0 |
| x | ∞ | 78.4 | 48.0 |
| y | 0.1 | 14.0 | 43.5 |
| y | 0.2 | 14.0 | 34.5 |
| y | 0.3 | 14.0 | 25.5 |
| y | 0.4 | 14.0 | 16.5 |
| y | 0.5 | 14.0 | 7.5 |

**Đường tham chiếu** (đường ngang 0.3 mm, màu xám #595959, kéo hết chiều rộng khung đồ thị; kiểu nét ở cột bên)

| Đường | Giá trị | Y (mm) | Kiểu nét | Nhãn (đặt sát trên đường, căn trái tại X = 15 mm) |
|---|---|---|---|---|
| B0 | 0.447 | 12.3 | gạch (dashed) | pooled real data (B0) |
| B1b | 0.504 | 7.1 | chấm (dotted) | pooled real data + SMOTE (B1b) |

**Điểm và thanh sai số** (X, Y là tâm marker; thanh sai số dọc từ Y trên đến Y dưới, có gạch ngang ở hai đầu rộng 1.4 mm; các điểm cùng chuỗi nối bằng đường liền 0.4 mm)

| Chuỗi | ε | Cấu hình | macro-F1 | std | X (mm) | Y (mm) | Y trên (mm) | Y dưới (mm) | Màu | Marker |
|---|---|---|---|---|---|---|---|---|---|---|
| FedDP-Marginal, distributed DP | 1 | MGr-eps1 | 0.389 | 0.010 | 20.1 | 17.5 | 16.6 | 18.3 | #1F77B4 | tròn |
| FedDP-Marginal, distributed DP | 5 | MGs-eps5 | 0.408 | 0.003 | 39.0 | 15.7 | 15.5 | 16.0 | #1F77B4 | tròn |
| FedDP-Marginal, distributed DP | 10 | MGs-eps10 | 0.429 | 0.008 | 58.0 | 13.9 | 13.2 | 14.6 | #1F77B4 | tròn |
| FedDP-Marginal, distributed DP | ∞ | MGs-nodp | 0.444 | 0.017 | 76.9 | 12.5 | 11.0 | 14.1 | #1F77B4 | tròn |
| FedDP-Marginal, client-side DP | 1 | MGl-eps1 | 0.253 | 0.029 | 21.6 | 29.8 | 27.2 | 32.3 | #2CA02C | vuông |
| FedDP-Marginal, client-side DP | 5 | MGl-eps5 | 0.374 | 0.010 | 40.5 | 18.8 | 17.9 | 19.8 | #2CA02C | vuông |
| FedDP-Marginal, client-side DP | 10 | MGl-eps10 | 0.413 | 0.007 | 59.5 | 15.3 | 14.6 | 16.0 | #2CA02C | vuông |
| Federated CVAE (best config.) | 1 | M1-eps1 | 0.227 | 0.030 | 23.1 | 32.1 | 29.3 | 34.8 | #D62728 | tam giác |
| Federated CVAE (best config.) | 5 | M1o-eps5 (plain) | 0.287 | 0.027 | 42.0 | 26.7 | 24.3 | 29.1 | #D62728 | tam giác |
| Federated CVAE (best config.) | 10 | M1o-eps10 | 0.289 | 0.040 | 61.0 | 26.5 | 22.9 | 30.1 | #D62728 | tam giác |
| Federated CVAE (best config.) | ∞ | B3 | 0.420 | 0.014 | 79.9 | 14.7 | 13.4 | 16.0 | #D62728 | tam giác |

**Chú giải (legend):** góc dưới bên phải trong khung đồ thị, không viền, 3 dòng theo thứ tự trên, mỗi dòng gồm một đoạn thẳng có marker giữa và tên chuỗi (8 pt). Xem vị trí trong ảnh tham chiếu.

## Hình 4: `fig4_utility_vs_traffic` (macro-F1 theo tổng lưu lượng, trục x logarit)

- Trang: **88 × 70 mm**. Khung đồ thị: x từ 14 đến 86 mm, y từ 15 đến 58 mm. Chú giải nằm phía trên khung (y khoảng 1–14 mm).
- **Khung đồ thị** (hình chữ nhật không nền, viền đen 0.2 mm): tâm (50.0, 36.5) mm, rộng 72 mm, cao 43 mm. Nhãn trục x căn giữa tại X = 50.0 mm, Y ≈ 67 mm; nhãn trục y xoay 90°, tâm tại X ≈ 3 mm, Y = 36.5 mm.
- Trục x **logarit** từ 0.25 đến 400 MB; trục y 0.1–0.5. Mọi vị trí dưới đây đã được quy đổi sẵn sang mm, nên chỉ cần đặt hình đúng toạ độ.

**Vạch chia trục** (vạch chính có nhãn; vạch phụ của trục x ngắn hơn, không nhãn)

| Trục | Giá trị | Nhãn | X (mm) | Y (mm) |
|---|---|---|---|---|
| x chính | 1 | 10^0 | 27.5 | 58.0 |
| x chính | 10 | 10^1 | 50.0 | 58.0 |
| x chính | 100 | 10^2 | 72.5 | 58.0 |
| x phụ | 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 2, 3, 4, 5, 6, 7, 8, 9, 20, 30, 40, 50, 60, 70, 80, 90, 200, 300, 400 | – | 15.8, 18.6, 20.8, 22.5, 24.0, 25.4, 26.5, 34.3, 38.3, 41.1, 43.2, 45.0, 46.5, 47.8, 49.0, 56.8, 60.7, 63.5, 65.7, 67.5, 69.0, 70.3, 71.4, 79.2, 83.2, 86.0 | 58.0 |
| y | 0.1 | 0.1 | 14.0 | 58.0 |
| y | 0.2 | 0.2 | 14.0 | 47.2 |
| y | 0.3 | 0.3 | 14.0 | 36.5 |
| y | 0.4 | 0.4 | 14.0 | 25.7 |
| y | 0.5 | 0.5 | 14.0 | 15.0 |

**Điểm** (X, Y là tâm marker, cỡ marker 1.8 mm; *tô đặc* = nằm trên mặt Pareto, còn lại chỉ có viền)

| Cấu hình | Nhóm (chú giải) | MB/lượt | macro-F1 | X (mm) | Y (mm) | Tô đặc | Màu | Marker |
|---|---|---|---|---|---|---|---|---|
| M1o-eps5 | Federated CVAE | 26.78 | 0.271 | 59.6 | 39.6 | không | #D62728 | tam giác |
| M1o-eps5 (plain) | Federated CVAE | 26.78 | 0.287 | 59.6 | 37.9 | không | #D62728 | tam giác |
| M1o-eps10 | Federated CVAE | 41.87 | 0.289 | 64.0 | 37.7 | không | #D62728 | tam giác |
| M1o-eps10 (plain) | Federated CVAE | 41.87 | 0.271 | 64.0 | 39.6 | không | #D62728 | tam giác |
| M1o-eps1 | Federated CVAE | 41.87 | 0.182 | 64.0 | 49.2 | không | #D62728 | tam giác |
| M1o-eps1 (plain) | Federated CVAE | 41.87 | 0.195 | 64.0 | 47.7 | không | #D62728 | tam giác |
| M3o-eps5 | Federated CVAE | 43.46 | 0.261 | 64.3 | 40.7 | không | #D62728 | tam giác |
| M3o-eps5 (plain) | Federated CVAE | 43.46 | 0.272 | 64.3 | 39.5 | không | #D62728 | tam giác |
| M1-eps1 | Federated CVAE | 43.73 | 0.227 | 64.4 | 44.3 | không | #D62728 | tam giác |
| M1-eps5 | Federated CVAE | 43.73 | 0.258 | 64.4 | 41.1 | không | #D62728 | tam giác |
| M1-eps10 | Federated CVAE | 43.73 | 0.243 | 64.4 | 42.6 | không | #D62728 | tam giác |
| M3o-eps10 | Federated CVAE | 64.78 | 0.261 | 68.2 | 40.7 | không | #D62728 | tam giác |
| M3o-eps10 (plain) | Federated CVAE | 64.78 | 0.263 | 68.2 | 40.4 | không | #D62728 | tam giác |
| M3o-eps1 | Federated CVAE | 64.79 | 0.170 | 68.2 | 50.4 | không | #D62728 | tam giác |
| M3o-eps1 (plain) | Federated CVAE | 64.79 | 0.184 | 68.2 | 48.9 | không | #D62728 | tam giác |
| M3-eps5 | Federated CVAE | 67.58 | 0.256 | 68.6 | 41.3 | không | #D62728 | tam giác |
| B3 | Federated CVAE | 126.68 | 0.420 | 74.8 | 23.6 | có | #D62728 | tam giác |
| M2 | Federated CVAE | 192.00 | 0.417 | 78.8 | 24.0 | không | #D62728 | tam giác |
| MGs-t3-eps5 | MG, distributed DP | 0.44 | 0.408 | 19.6 | 24.9 | không | #1F77B4 | tròn |
| MGs-t2-eps5 | MG, distributed DP | 0.45 | 0.396 | 19.7 | 26.2 | không | #1F77B4 | tròn |
| MGs-strm2-eps5 | MG, distributed DP | 0.45 | 0.371 | 19.7 | 28.8 | không | #1F77B4 | tròn |
| MGs-eps5 | MG, distributed DP | 0.45 | 0.408 | 19.7 | 24.9 | có | #1F77B4 | tròn |
| MGs-strm1-eps10 | MG, distributed DP | 0.47 | 0.409 | 20.1 | 24.8 | không | #1F77B4 | tròn |
| MGr-eps10 | MG, distributed DP | 0.47 | 0.433 | 20.2 | 22.2 | không | #1F77B4 | tròn |
| MGs-eps10 | MG, distributed DP | 0.47 | 0.429 | 20.2 | 22.7 | có | #1F77B4 | tròn |
| MGs-cap25-eps5 | MG, distributed DP | 0.47 | 0.203 | 20.3 | 46.9 | không | #1F77B4 | tròn |
| MGs-t2-eps10 | MG, distributed DP | 0.48 | 0.418 | 20.3 | 23.8 | không | #1F77B4 | tròn |
| MGs-t3-eps10 | MG, distributed DP | 0.48 | 0.428 | 20.3 | 22.8 | không | #1F77B4 | tròn |
| MGr-strm1-eps1 | MG, distributed DP | 0.59 | 0.353 | 22.3 | 30.8 | không | #1F77B4 | tròn |
| MGr-eps1 | MG, distributed DP | 0.60 | 0.389 | 22.6 | 26.9 | có | #1F77B4 | tròn |
| MGs-eps1 | MG, distributed DP | 0.60 | 0.342 | 22.6 | 32.0 | không | #1F77B4 | tròn |
| MGr-t3-eps1 | MG, distributed DP | 0.61 | 0.392 | 22.7 | 26.6 | không | #1F77B4 | tròn |
| MGr-t2-eps1 | MG, distributed DP | 0.62 | 0.341 | 22.9 | 32.1 | không | #1F77B4 | tròn |
| MGs-cap25-eps10 | MG, distributed DP | 0.68 | 0.195 | 23.8 | 47.7 | không | #1F77B4 | tròn |
| MGd-eps5 | MG, distributed DP | 0.83 | 0.417 | 25.7 | 23.9 | có | #1F77B4 | tròn |
| MGd-eps10 | MG, distributed DP | 0.92 | 0.427 | 26.7 | 22.8 | có | #1F77B4 | tròn |
| MGb-eps10 | MG, distributed DP | 1.16 | 0.433 | 29.0 | 22.2 | có | #1F77B4 | tròn |
| MGd-eps1 | MG, distributed DP | 1.32 | 0.349 | 30.2 | 31.2 | có | #1F77B4 | tròn |
| MGr-cap25-eps1 | MG, distributed DP | 2.30 | 0.154 | 35.6 | 52.2 | không | #1F77B4 | tròn |
| MGl-eps5 | MG, client-side DP | 0.83 | 0.374 | 25.7 | 28.5 | không | #2CA02C | vuông |
| MGl-eps10 | MG, client-side DP | 0.93 | 0.413 | 26.8 | 24.3 | có | #2CA02C | vuông |
| MGl-eps1 | MG, client-side DP | 1.56 | 0.253 | 31.9 | 41.6 | không | #2CA02C | vuông |
| MGp-nodp | MG, no DP | 0.39 | 0.444 | 18.3 | 21.0 | có | #9467BD | thoi |
| MGs-nodp | MG, no DP | 0.52 | 0.444 | 21.2 | 21.0 | không | #9467BD | thoi |

**Nhãn điểm** (chữ 8 pt, màu xám đậm; đường dẫn mảnh 0.2 mm màu xám nối tâm chữ tới tâm marker)

| Nhãn | Tâm chữ X (mm) | Tâm chữ Y (mm) | Đầu đường dẫn tại marker X, Y (mm) |
|---|---|---|---|
| MGs-eps10 | 38.9 | 19.1 | 20.2, 22.7 |
| MGs-eps5 | 38.9 | 25.2 | 19.7, 24.9 |
| MGr-eps1 | 38.9 | 31.1 | 22.6, 26.9 |
| B3 | 63.5 | 19.1 | 74.8, 23.6 |
| M2 | 80.6 | 28.8 | 78.8, 24.0 |
| M1-eps1 | 76.4 | 43.0 | 64.4, 44.3 |

**Chú giải (legend):** phía trên khung đồ thị, 2 cột, không viền: (cột 1) MG, distributed DP · MG, client-side DP · MG, no DP; (cột 2) Federated CVAE · filled: Pareto front (một chấm tròn đặc màu xám). Marker trong chú giải chỉ vẽ viền.
