# Họ và tên: Phạm Lê Anh Tuấn
# Mã số sinh viên: 23110356
# Đồ án cá nhân: Khám Phá giải thuật 8-Puzzle với các thuật toán tìm kiếm trong Trí Tuệ Nhân Tạo

Dự án này cung cấp một nền tảng tương tác để tìm hiểu và trực quan hóa cách các thuật toán Trí tuệ Nhân tạo giải quyết bài toán 8-puzzle cổ điển. Sử dụng thư viện Pygame để xây dựng giao diện đồ họa, ứng dụng cho phép người dùng khám phá sự hoạt động của nhiều phương pháp tìm kiếm và học máy khác nhau.

## Tổng quan Dự án

Mục tiêu chính của dự án là minh họa quá trình giải 8-puzzle, từ các chiến lược tìm kiếm cơ bản đến những kỹ thuật nâng cao hơn. Giao diện trực quan giúp người dùng dễ dàng thiết lập bài toán, chọn thuật toán giải và quan sát từng bước di chuyển của các viên gạch trong quá trình tìm kiếm lời giải.

## Các Tính năng Nổi bật

* **Thiết lập Puzzle Linh hoạt:** Bắt đầu với một cấu hình puzzle được định sẵn, ngẫu nhiên hoặc tự do nhập trạng thái ban đầu mong muốn.
* **Bộ Sưu Tập Thuật Toán Đa dạng:** Tích hợp nhiều thuật toán giải quyết vấn đề từ các lĩnh vực khác nhau của AI.
* **Trực quan hóa Quá trình Giải:** Theo dõi từng bước di chuyển của puzzle khi thuật toán tìm kiếm được thực thi (đối với các thuật toán tìm đường đi trạng thái).
* **Kiểm soát Trực quan:** Điều chỉnh tốc độ hiển thị các bước giải và xem lại từng bước nếu cần ('-', '+', '<-', '->').
* **Hiển thị Trạng thái Rõ ràng:** Nhận thông báo về tình trạng hiện tại của bộ giải (SOLVING, DONE, NO SOLUTION).
* **Hỗ trợ các Kỹ thuật AI Đặc biệt:** Bao gồm khả năng khám phá các thuật toán ít truyền thống hơn như tìm kiếm trên trạng thái niềm tin, xử lý ràng buộc và học tăng cường cơ bản.

## Các Phương Pháp Giải Được Hỗ Trợ

Dự án cài đặt và triển khai các thuật toán sau để giải bài toán 8-puzzle:

* **Tìm kiếm không có thông tin (Uninformed Search):**
    * Breadth-First Search (BFS):
    * Uniform Cost Search (UCS):
    * Depth-First Search (DFS)
    * Iterative Deepening Depth-First Search (IDDFS)
* **Tìm kiếm có thông tin (Informed Search):**
    * Greedy Best-First Search (dựa trên heuristic)
    * A\* Search (kết hợp chi phí đường đi và heuristic)
    * Iterative Deepening A\* (IDA\*)
* **Tìm kiếm Cục bộ (Local Search):**
    * Simple Hill Climbing
    * Steepest Ascent Hill Climbing
    * Stochastic Hill Climbing
    * Simulated Annealing
    * Genetic Algorithm
    * Beam Search
* **Tìm kiếm trong môi trường phức tạp:**
    * AND-OR Tree Search
    * Belief State Search (Tìm kiếm trong môi trường niềm tin)
    * Partially Observable (Nhìn thấy một phần)
* **Tìm kiếm trong môi trường có ràng buộc:**
    * Backtracking Search
* **Reforcement Learning:**
    * Q-Learning (một dạng Học tăng cường)

## Hàm Heuristic

**Khoảng cách Manhattan (`Manhattan_Heuristic`):** Tính tổng khoảng cách di chuyển theo chiều ngang và dọc từ vị trí hiện tại của mỗi viên gạch đến vị trí đích của nó. Đây là heuristic phổ biến và hiệu quả cho 8-puzzle.

## Cấu trúc Dự án

Dự án được tổ chức gọn gàng thành các tệp Python chính:
* AI.py       # Chứa cài đặt các thuật toán AI và các hàm hỗ trợ cho 8-puzzle.
* UI.py       # Xây dựng giao diện đồ họa bằng Pygame và xử lý tương tác người dùng.
* README.md   # File mô tả dự án.
## Yêu cầu Hệ thống

Để chạy ứng dụng này, bạn cần có:

* Phiên bản Python 3.x (khuyến nghị 3.6 trở lên).
* Thư viện Pygame.
* Thư viện NumPy (được sử dụng bởi `AI.py`).

## Hướng dẫn Cài đặt

1.  Tải về mã nguồn của dự án.
2.  Mở cửa sổ Terminal hoặc Command Prompt.
3.  Điều hướng đến thư mục chứa mã nguồn đã tải về.
4.  Cài đặt các thư viện cần thiết: pygame, numpy,...

## Cách Chạy Ứng dụng

Từ thư mục gốc của dự án trong Terminal hoặc Command Prompt, chạy lệnh sau:

```bash
python UI.py
