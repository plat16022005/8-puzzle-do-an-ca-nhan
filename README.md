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
      Đây là thuật toán tìm theo chiều rộng vận hành theo quy luật FIFO (First in first out)
      + Ưu điểm:
        - Tìm được đường đi tối ưu trong môi trường ma trận không có trong số, mỗi bước đi đều tốn chi phí như nhau
        - Ít khi nào rơi vào vòng lặp
      + Nhược điểm:
        - Tốn RAM vì phải lưu trữ toàn bộ cây tìm kiếm.
        - Tốc độ có thể chậm nếu không được cắt tỉa tốt
    * Uniform Cost Search (UCS):
      Đây là một thuật toán tìm kiếm theo chi phí tối ưu trên ma trận có trọng số, miễn chi phí không âm.
      + Ưu điểm:
        - Có thể tìm đường đi tối ưu.
        - Xét được chi phí trạng thái.
      + Nhược điểm:
        - Chậm hơn BFS nếu xét trong một ma trận có chi phí đồng đều, mỗi bước đi đều tốn chi phí như nhau
        - Nếu trong môi trường có trọng số thì có thể sẽ tiêu tốn RAM hơn BFS
    * Depth-First Search (DFS):
      Đây là thuật toán tìm theo chiều sâu vận hành theo quy luật LIFO (Last in first out)
      + Ưu điểm:
        - Mức độ tiêu tốn RAM sẽ ít vì chỉ lưu trữ đường đi đến đích
        - Do việc đi sâu một cách liều lĩnh nên thời gian tính toán có thể nhanh hơn.
      + Nhược điểm:
        - Không tìm ra được đường đi tối ưu
        - Dễ rơi vào vòng lặp
    * Iterative Deepening Depth-First Search (IDDFS):
      Đây là thuật toán kết hợp được ưu điểm của BFS và DFS. IDDFS thực hiện DFS có giới hạn độ sâu (depth-limited DFS) lặp đi lặp lại với độ sâu tăng dần
      + Ưu điểm:
        - Có thể tìm ra được đường đi tối ưu hơn DFS
        - Mức độ tiêu tốn RAM thấp hơn BFS
        - Tốc độ tính toán khá nhanh hơn BFS
      + Nhược điểm:
        - Tuy tìm ra được đường đi nhưng về tối ưu sẽ kém hơn BFS
        - Tốc độ tính toán chậm hơn DFS do phải lập đi lập lại nhiều lần với độ sâu tăng dần cho tới khi tìm được độ sâu chứa lời giải
* **Tìm kiếm có thông tin (Informed Search):**
    * Greedy Best-First Search (dựa trên heuristic):
      Greedy Best-First Search (Greedy) là một thuật toán tìm kiếm có định hướng (informed search), sử dụng hàm heuristic (ước lượng) để dẫn đường đến lời giải nhanh nhất có thể, mà không quan tâm đến chi phí thực tế đã đi qua. Ưu tiên trạng thái "gần goal" nhất theo ước lượng (không xét chi phí đã đi)
      + Ưu điểm:
        - Tốc độ tính toán nhanh
        - Có thể tìm được lời giải tốt nếu có một Heuristic hợp lí
      + Nhược điểm:
        - Không tìm được đường đi tối ưu do nó chỉ quan tâm đến chi phí trước mắt nên có thể dễ dàng bị đánh lừa
        - Có thể đưa ra lời giải kém nếu Heutistic không tốt
    * A* Search (kết hợp chi phí đường đi và heuristic):
      A* là một trong những thuật toán tìm kiếm thông minh nhất và phổ biến nhất hiện nay, sử dụng hàm heuristic (ước lượng) để đưa ra lời giải tốt nhất có thể, quan tâm đến chi phí đã đi qua. Nên có thể "đi vòng" nếu đường đi không hợp lí.
      + Ưu điểm:
        - Tìm ra được đường đi tối ưu hơn nhiều so với Greedy nếu dùng chung một Heuristic
        - Không dễ dàng bị đánh lừa do xét thêm chi phí đã đi
      + Nhược điểm:
        - Tiêu tốn RAM hơn nhiều so với Greedy
        - Tốc độ tính toán trung bình, chậm hơn so với Greedy
    * Iterative Deepening A* (IDA*):
      Là thuật toán kết hợp được những ưu điểm của Greedy và A*, và nguyên lí hoạt động cũng tương tự IDDFS:
      + Ưu điểm:
        - Tốc độ tính toán nhanh
        - Tìm ra được đường đi tối ưu
        - Tiêu tốn RAM ít hơn A*
      + Nhược điểm:
        - Tuy nói tốc độ tính toán nhanh nhưng vẫn chậm hơn Greedy
        - Khả năng tiêu tốn RAM vẫn sẽ nhiều hơn Greedy
* **Tìm kiếm Cục bộ (Local Search):**
    * Simple Hill Climbing
      Hill Climbing là một thuật toán tối ưu hóa địa phương (local search) được dùng để tìm lời giải gần đúng bằng cách leo dần lên đỉnh của “ngọn đồi” heuristic — tức là trạng thái có giá trị đánh giá (heuristic) tốt hơn.
      + Ưu điểm:
        - Dễ cài đặt
        - Tiết kiệm RAM
        - Nhanh trong không gian nhỏ
      + Nhược điểm:
        - Rất dễ dàng rơi vào kẹt cục bộ
        - Rất khó tìm ra lời giải
        - Không quay về trạng thái cũ để thử hướng khác.
    * Steepest Ascent Hill Climbing:
      Steepest Ascent Hill Climbing là một biến thể nâng cấp của Simple Hill Climbing, trong đó ta không chọn hàng xóm tốt đầu tiên, mà xét tất cả hàng xóm, rồi chọn hàng xóm tốt nhất (tức là có giá trị heuristic nhỏ nhất).
      + Ưu điểm:
        - Khắc phục được lỗi dễ dàng rơi vào cục bộ của Simple
        - Dễ cài đặt
        - Tiết kiệm RAM
        - Nhanh trong không gian nhỏ
      + Nhược điểm:
        - Vẫn có xác suất cao rơi vào kẹt cục bộ
        - Rất khó tìm ra lời giải
        - Không quay về trạng thái cũ để thử hướng khác.
    * Stochastic Hill Climbing:
      Stochastic Hill Climbing là một biến thể của Hill Climbing, trong đó không chọn hàng xóm tốt nhất một cách chắc chắn, mà chọn ngẫu nhiên một trong các hàng xóm tốt hơn hiện tại.
      + Ưu điểm:
        - Khắc phục được lỗi dễ dàng rơi vào cục bộ của Simple
        - Dễ cài đặt
        - Tiết kiệm RAM
        - Nhanh trong không gian nhỏ
      + Nhược điểm:
        - Vẫn có xác suất cao rơi vào kẹt cục bộ tuy cao hơn Steepest nhưng vẫn sẽ nhỏ hơn Simple
        - Rất khó tìm ra lời giải
        - Không quay về trạng thái cũ để thử hướng khác.
    * Simulated Annealing:
      Simulated Annealing (SA) là một thuật toán tối ưu hóa ngẫu nhiên, lấy cảm hứng từ quá trình làm nguội chậm của kim loại trong vật lý — quá trình kết tinh giúp kim loại đạt trạng thái năng lượng tối thiểu. SA giống như một biến thể của hill climbing, nhưng cho phép chấp nhận cả những bước đi "tồi hơn" (heuristic cao hơn) với một xác suất giảm dần theo thời gian. Mức nhiệt độ càng giảm thì sẽ càng "khó tín" trong việc lựa chon đường đi
      + Ưu điểm:
        - Có khả năng thoát local optimum
        - Khả năng tìm ra lời giải cao hơn nhiều so với Simple, Steepest, Stochastic
      + Nhược điểm:
        - Cần phải thiết lập nhiều tham số
        - Vẫn có khả năng cao không tìm ra lời giải và nếu có thì lời giải thường kém tiêu tốn rất nhiều bước đi
    * Genetic Algorithm:
      Genetic Algorithm là một thuật toán tối ưu hóa dựa trên nguyên lý tiến hóa sinh học — chọn lọc tự nhiên và di truyền. GA được dùng để tìm lời giải gần tối ưu cho các bài toán phức tạp mà không thể giải triệt để trong thời gian hợp lý. Qua các bước lặp gọi là thế hệ (generations), các cá thể được chọn lọc, lai ghép (crossover), đột biến (mutation) để tạo ra quần thể mới có chất lượng cao hơn.
      + Ưu điểm:
        - Tìm lời giải gần tối ưu trong không gian lớn
        - Dễ dàng áp dụng cho các bài toán phức tạp
      + Nhược điểm:
        - Khó để cài đặt code, cần rất nhiều tham số
        - Không tìm được đường đi tối ưu
        - Có thể mất nhiều thời gian và tài nguyên
    * Beam Search
      Beam Search là một thuật toán tìm kiếm mở rộng từ Best-First Search, kết hợp giữa hiệu quả của tìm kiếm có định hướng và giới hạn bộ nhớ. Beam Search chỉ giữ lại một số lượng giới hạn k trạng thái tốt nhất tại mỗi bước (gọi là beam width), giúp giảm đáng kể độ phức tạp tính toán và bộ nhớ. Khắc phục rất tốt các nhược điểm của những thuật toán trong nhóm Local Search
      + Ưu điểm:
        - Tốc độ nhanh
        - Dễ mở rộng
        - Tiết kiệm RAM do chỉ dữ lại 3 nhóm tốt nhất
      + Nhược điểm:
        - Vẫn có xác suất không tìm thấy lời giải nếu Beam_Width thấp
        - Có thể bỏ sót trạng thái tốt do beam width nhỏ
* **Tìm kiếm trong môi trường phức tạp:**
    * AND-OR Tree Search
      AND-OR Tree Search là một thuật toán mở rộng từ tìm kiếm cây thông thường, được thiết kế để giải quyết các bài toán có tính phân nhánh quyết định phức tạp, nơi một hành động có thể dẫn đến nhiều kết quả (OR), và một số mục tiêu chỉ đạt được nếu tất cả điều kiện con đều đạt (AND). Trong đồ án thì node Or đại diện cho số trường hợp có thể đi của Empty, node And thì sẽ đại diện cho cách giải của từng trường hợp, cách giải thường dùng là BFS và in ra trong Terminal
      + Ưu điểm:
        - Giải được các bài toán với hành động không chắc chắn
        - Tìm được kế hoạch có điều kiện
        - Áp dụng được trong hệ chuyên gia, lập kế hoạch AI
      + Nhược điểm:
        - Không phù hợp cho bài toán có môi trường xác định
        - Độ phức tạp cao hơn nhiều so với các nhóm thuật toán khác
        - Đòi hỏi biểu diễn rõ cây AND/OR và trạng thái không chắc chắn
    * Belief State Search (Tìm kiếm trong môi trường niềm tin):
      Belief State Search là một kỹ thuật tìm kiếm trong môi trường không hoàn toàn xác định (partially observable environment), nơi tác nhân không biết chính xác mình đang ở đâu, mà chỉ có một tập hợp các trạng thái có thể. Trong bài đồ án này, thuật toán sẽ đưa random trạng thái bắt đầu và từ trạng thái đó đưa ra lời giải dựa trên thuật toán BFS
      + Ưu điểm:
        - Hoạt động tốt trong môi trường không chắc chắn
        - Cho phép tác nhân ra quyết định khi không có đủ thông tin
        - Cơ sở lý thuyết vững chắc trong AI hiện đại
      + Nhược điểm:
        - Không gian belief state rất lớn
        - Khó xác định trạng thái đích chính xác
        - Cần tính toán phức tạp với nhiều phép hợp và cập nhật
    * Partially Observable (Nhìn thấy một phần):
      Một môi trường Partially Observable (PO) là môi trường mà tác nhân không thể quan sát hoàn toàn trạng thái hiện tại của thế giới. Tác nhân chỉ có thông tin một phần, thông qua các quan sát mơ hồ hoặc giới hạn, dẫn đến sự không chắc chắn về trạng thái thực tế. Trong đồ án này thì sẽ liệt kê ra các bảng random giống với Belief State Search nhưng khác biệt ở bản random này là tác nhân nhìn thấy một phần là [1,2,3]
      + Ưu điểm:
        - Hoạt động tốt trong môi trường không chắc chắn
        - Cho phép tác nhân ra quyết định khi không có đủ thông tin
        - Cơ sở lý thuyết vững chắc trong AI hiện đại
      + Nhược điểm:
        - Không gian rất lớn
        - Khó xác định trạng thái đích chính xác
        - Cần tính toán phức tạp với nhiều phép hợp và cập nhật
* **Tìm kiếm trong môi trường có ràng buộc:**
    * Backtracking Search
      Backtracking Search là một thuật toán tìm kiếm tổng quát theo chiều sâu (depth-first), được dùng để giải quyết các bài toán ràng buộc (constraint problems) bằng cách thử và loại bỏ (try & backtrack) các giá trị không hợp lệ. Nó khám phá từng khả năng, và nếu một lựa chọn dẫn đến bế tắc, thuật toán quay lui (backtrack) để thử một lựa chọn khác.
      + Ưu điểm:
        - Dễ triển khai, trực quan
        - Giải được bài toán không gian lớn
        - Cho lời giải chính xác
      + Nhược điểm:
        - Hiệu suất thấp nếu không có tối ưu hóa
        - Có thể mất rất nhiều thời gian với không gian lớn
        - Không tận dụng thông tin trước đó
    * Forward Checking:
      Forward Checking là một kỹ thuật hỗ trợ cho Backtracking Search dùng trong các bài toán ràng buộc (CSP — Constraint Satisfaction Problem). Nó giúp phát hiện sớm mâu thuẫn bằng cách: Khi gán giá trị cho một biến, loại bỏ các giá trị không hợp lệ trong các biến chưa gán.
      + Ưu điểm:
        - Phát hiện xung đột sớm hơn Backtracking thông thường
        - Tránh nhiều nhánh không cần thiết
        - Giúp giảm số lần quay lui
      + Nhược điểm:
        - Không giải quyết tất cả mâu thuẫn phức tạp
        - Không lan truyền ràng buộc sâu
        - Chi phí tính toán tăng theo mỗi lần gán
    * AC-3:
      AC-3 là một thuật toán dùng để duy trì tính nhất quán của các ràng buộc nhị phân trong bài toán ràng buộc (CSP). Mục tiêu: Đảm bảo rằng mọi giá trị trong miền của một biến đều thỏa mãn ít nhất một giá trị hợp lệ ở biến liên quan.
      + Ưu điểm:
        - Phát hiện mâu thuẫn ngay từ đầu
        - Giảm đáng kể miền giá trị
        - Có thể dùng trước hoặc trong khi tìm kiếm (backtracking)
      + Nhược điểm:
        - Chỉ áp dụng với ràng buộc nhị phân
        - Không giải được tất cả bài toán CSP
* **Reforcement Learning:**
    * Q-Learning (một dạng Học tăng cường)
      Q-Learning là một thuật toán Học Tăng Cường (Reinforcement Learning) giúp tác nhân (agent) học cách hành động tối ưu trong một môi trường thông qua thử và sai (trial-and-error) mà không cần mô hình của môi trường. Mục tiêu: Học một chính sách hành động tối ưu (optimal policy) bằng cách ước lượng giá trị Q của từng hành động tại mỗi trạng thái.
      + Ưu điểm:
        - Không cần biết mô hình môi trường
        - Dễ mở rộng sang bài toán phức tạp
        - Học dần qua thử nghiệm
        - Đơn giản hơn nhiều so với các thuật toán cùng nhóm
        - Có thể áp dụng vào môi trường biến thiên trạng thái liên tục
      + Nhược điểm:
        - Q-Table lớn với không gian trạng thái lớn, khó có thể triển khai trong không gian có nhiều trạng thái và nhiều hành động
        - Cần nhiều vòng lặp để hội tụ
        - Thời gian học khá lâu

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
