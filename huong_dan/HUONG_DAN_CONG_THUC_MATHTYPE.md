# Hướng dẫn gõ công thức bằng MathType rồi đưa vào LaTeX

Yêu cầu của giảng viên: **gõ công thức trực tiếp trong MathType, rồi copy mã LaTeX do MathType sinh ra vào bài.** Bài có **9 công thức đánh số**, nằm ở `Chapter3.tex` (1–8) và `Chapter4.tex` (9).

Quy trình gồm 3 bước:
1. Gõ từng công thức trong MathType theo mục 3. Mẫu cần đạt nằm ở dòng `% Mẫu` trong file [MATHTYPE_DAN_VAO.txt](MATHTYPE_DAN_VAO.txt) và trong `main.pdf` hiện tại.
2. Ctrl+A → Ctrl+C trong MathType, rồi dán vào **đúng ô** (giữa hai dòng `BAT DAU` và `KET THUC`) của file [MATHTYPE_DAN_VAO.txt](MATHTYPE_DAN_VAO.txt). Không cần xoá `\[ \]`.
3. Chạy `python scripts/insert_mathtype.py` (hoặc nhắn Claude đưa vào giúp). Script thay công thức trong `.tex`, giữ nguyên `\label` và số thứ tự, rồi build lại trên Overleaf.

Công thức **nằm trong dòng chữ** (ví dụ $\varepsilon$, $K = 5$, $\mu_r = \Delta_{2,r}^2/(2 s_r \kappa)$) không đánh số và vẫn giữ dạng LaTeX. Nếu giảng viên yêu cầu cả phần này cũng phải làm bằng MathType, hãy báo lại.

## 1. Cài đặt MathType một lần (MathType 7, Windows)

1. Mở **Preferences → Cut and Copy Preferences…**
2. Chọn **MathML or TeX**, trong danh sách chọn **LaTeX 2.09 and later**.
3. **Bỏ chọn** *Include translator name in translation* và *Include MathType data in translation*. Nếu quên bỏ chọn cũng không sao, vì script tự lọc các dòng `%MathType...`.
4. Bấm OK. Từ giờ Ctrl+C trong MathType sẽ copy ra mã LaTeX dạng `\[ ... \]`.

## 2. Phím tắt và bảng mẫu (template) hay dùng

| Cần gõ | Cách làm trong MathType |
|---|---|
| Chỉ số dưới $x_k$ / mũ $x^2$ / cả hai $\Delta_{2,r}^2$ | **Ctrl+L** / **Ctrl+H** / **Ctrl+J** |
| Phân số $\frac{a}{b}$ | **Ctrl+F** |
| Căn $\sqrt{T}$ | **Ctrl+R** |
| Ngoặc tròn co giãn $\left( \right)$ | **Ctrl+9**; ngoặc vuông: **Ctrl+[** |
| Chữ Hy Lạp | **Ctrl+G**, rồi gõ chữ Latin tương ứng: a→α, d→δ, D→Δ, e→ε, k→κ, l→λ, m→μ, s→σ, x→ξ |
| Chữ đứng (Dir, ln, min, max, arg max, mod, CI, sd) | Chọn kiểu **Function**: **Ctrl+Shift+F**; quay lại kiểu thường: **Ctrl+Shift+=** |
| Chữ thường trong công thức ("and") | Kiểu **Text**: **Ctrl+Shift+E** |
| Chữ đậm ($\mathbf{p}$, $\mathbf{1}$, $\mathbf{x}$, $\mathbf{I}$) | Kiểu **Vector-Matrix**: **Ctrl+Shift+B** |
| Tổng $\sum$, tích $\prod$ có cận dưới/trên | Thanh **Summation templates** / **Product templates** (dòng template trên toolbar), chọn mẫu có cận dưới (và cận trên nếu cần) |
| min, arg max có biến **bên dưới** | Gõ chữ ở kiểu Function, rồi dùng mẫu **Underscript** (thanh *Underscript and overscript templates*) |
| Mũ "hat" $\hat{P}$, ngã $\tilde{g}$, gạch trên $\bar{\Delta}$ | Bảng **Embellishments** (dấu trên chữ) trên toolbar |
| $\sim$, $\le$, $>$, $\in$, $\notin$, $\mid$ | Bảng **Relational symbols** và **Set theory symbols** |
| Chuẩn $\lVert g \rVert$ | Bảng **Fence templates**, chọn mẫu ngoặc hai gạch đứng |
| Dấu sao $T^\star$ | Ctrl+H rồi **Edit → Insert Symbol**, tìm *star operator* (⋆) |
| Chữ hoa thư pháp $\mathcal{K}$, $\mathcal{N}$ | **Edit → Insert Symbol**, chọn chữ hoa kiểu script/calligraphic |
| Khoảng trống lớn (giữa hai vế ở (4) và (9)) | Bảng **Spaces and ellipses** (em space) |

Nếu một ký hiệu khó gõ, hãy gõ gần đúng rồi cứ dán vào ô. Khi đưa vào bài, Claude sẽ so với `% Mẫu` và báo chỗ lệch, ví dụ chữ thư pháp bị xuất thành ký tự lạ.

## 3. Ghi chú cho từng công thức

Gõ **cả dấu phẩy hoặc dấu chấm cuối công thức** đúng như Mẫu, vì câu văn của bài tiếp tục ngay sau công thức.

| Số | Label | Ý chính | Lưu ý khi gõ |
|---|---|---|---|
| (1) | `eq:dirichlet` | $\mathbf{p}_c = (p_{c,1}, \dots, p_{c,K}) \sim \mathrm{Dir}(\alpha_{\mathrm{dir}} \mathbf{1}_K)$, | **p** và **1** đậm (Ctrl+Shift+B); "Dir" và chỉ số "dir" ở kiểu Function; "…" lấy từ bảng Spaces and ellipses |
| (2) | `eq:chow_liu` | $T^\star = \arg\max_T \sum_{(i,j) \in T} \hat{I}(X_i; X_j)$, | "arg max" kiểu Function, T đặt bên dưới (Underscript); tổng dùng mẫu có cận dưới |
| (3) | `eq:tree_factorization` | $\hat{P}(\mathbf{x} \mid y = c) = \hat{P}(x_r \mid y = c) \prod_{(u,v) \in T^\star} \hat{P}(x_v \mid x_u, y = c)$, | **x** đậm; dấu "∣" lấy từ Relational symbols; tích dùng mẫu có cận dưới |
| (4) | `eq:sensitivity` | $\Delta_{1,r} = m\,T_r, \qquad \Delta_{2,r} = m\sqrt{T_r}$. | Thêm khoảng trống lớn giữa hai vế |
| (5) | `eq:skellam_rdp` | Cận RDP của Skellam | **Hai dòng:** gõ dòng 1 đến hết phân số đầu, nhấn **Enter**, gõ dòng 2 bắt đầu bằng "+ min(…)". Sau đó **Format → Align at =** để dòng 2 lùi vào thẳng vế phải. Công thức một dòng sẽ tràn cột. |
| (6) | `eq:rdp_conversion` | $\varepsilon = \min_\lambda [\dots]$, | "min" kiểu Function, λ bên dưới; ngoặc vuông co giãn (Ctrl+[); hai phân số; "ln" kiểu Function |
| (7) | `eq:secagg` | $S = \sum_{k \in \mathcal{K}} (\mathbf{x}_k + \boldsymbol{\xi}_k) \bmod 2^{32}$, | 𝒦 chữ thư pháp; **x** và **ξ** đậm; "mod" kiểu Function |
| (8) | `eq:dpsgd` | $\tilde{g} = \frac{1}{B}(\sum \dots + \mathcal{N}(0, \sigma_k^2 C^2 \mathbf{I}))$, | 𝒩 chữ thư pháp; **I** đậm; "max" kiểu Function; chuẩn ‖g_i‖₂ dùng Fence template |
| (9) | `eq:decision_rule` | $0 \notin \mathrm{CI}_{95\%}(\bar{\Delta})$ and $\lvert\bar{\Delta}\rvert > \max(\mathrm{sd}_A, \mathrm{sd}_B)$, | "CI", "sd", "max" kiểu Function; "and" kiểu **Text** (Ctrl+Shift+E), hai bên có khoảng trống lớn |

## 4. Đưa vào bài

Trong thư mục `Latex_FinalCapstone`:

```
python scripts/insert_mathtype.py --dry-run
```

Lệnh này chỉ in ra công thức nào sẽ được thay, chưa ghi gì. Nếu không có dòng `LỖI`, chạy tiếp:

```
python scripts/insert_mathtype.py
```

Script sẽ:
- bỏ `\[ \]` (hoặc `$$ $$`) và các dòng `%MathType...`;
- đổi `\epsilon` thành `\varepsilon` cho thống nhất với chữ trong bài;
- thay **thân** công thức có `\label` tương ứng, giữ `\begin{equation}`, `\label{...}` và `\end{equation}`, và thêm dòng chú thích `% typed in MathType`;
- **bỏ qua** các ô còn trống, nên có thể làm dần từng công thức;
- **báo LỖI** và không thay nếu mã dán vào bị lệch ngoặc `{ }` hoặc còn sót `\[`, `\]`, `$`. Khi đó thường là do copy thiếu, chỉ cần copy lại từ MathType.

Có thể chạy lại script bao nhiêu lần cũng được: lần sau sẽ thay đè lần trước.

> **Trước lần chạy đầu tiên**, hãy commit bản bài báo hiện tại, hoặc copy `Chapter3.tex` và `Chapter4.tex` ra chỗ khác, để còn đường quay lại. **Đừng** dùng `git checkout -- <file>` khi bản viết lại chưa được commit: lệnh đó đưa file về commit cũ (bản 27 trang) và làm mất phần viết lại.

Sau khi chạy xong: đóng gói lại zip hoặc upload hai file `Chapter3.tex` và `Chapter4.tex` lên Overleaf, rồi Recompile.

## 5. Kiểm tra trên Overleaf

- [ ] Đủ 9 số (1)–(9), đúng thứ tự, và các `\eqref{...}` trong bài không ra `??`.
- [ ] Không có cảnh báo **Overfull \hbox** ở dòng công thức. Nếu có, công thức đang tràn cột: tách dòng trong MathType (Enter + Align at =), copy và chạy lại script.
- [ ] Ký hiệu khớp với chữ trong bài: $\varepsilon$ (epsilon cong), $\Delta_{1,r}$, $\Delta_{2,r}$, $\mu_r$, $T^\star$, $\mathcal{K}$, $\mathcal{N}$.
- [ ] Mã MathType dùng `{\rm ...}`, `{\bf ...}`, `\begin{array}`: các lệnh này biên dịch được với `IEEEtran.cls` và `amsmath` đã khai báo trong `main.tex`.

Nguồn của từng công thức (để trả lời hội đồng):
- (1) Hsu et al. 2019.
- (2)–(3) Chow & Liu 1968.
- (4)–(5) Agarwal et al. 2021, Cor. 3.6, và hàm `skellam_rdp` trong `src/ppfeddata/models/marginal.py`.
- (6) hàm `rdp_to_eps` trong cùng file, theo cách đổi của Opacus.
- (7) `src/ppfeddata/fl/mg_app.py`.
- (8) Abadi et al. 2016.
- (9) luật quyết định trong `docs/PP-FedData_Implementation_Spec.md`.
