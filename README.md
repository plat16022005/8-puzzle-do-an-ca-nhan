# Họ và tên: Phạm Lê Anh Tuấn
# Mã số sinh viên: 23110356
# Đồ án cá nhân: Khám Phá giải thuật 8-Puzzle với các thuật toán tìm kiếm trong Trí Tuệ Nhân Tạo

# 1. Mục tiêu:
Dự án này cung cấp một nền tảng tương tác để tìm hiểu và trực quan hóa cách các thuật toán Trí tuệ Nhân tạo giải quyết bài toán 8-puzzle cổ điển. Sử dụng thư viện Pygame để xây dựng giao diện đồ họa, ứng dụng cho phép người dùng khám phá sự hoạt động của nhiều phương pháp tìm kiếm và học máy khác nhau.

## Tổng quan Dự án

Mục tiêu chính của dự án là minh họa quá trình giải 8-puzzle, từ các chiến lược tìm kiếm cơ bản đến những kỹ thuật nâng cao hơn. Giao diện trực quan giúp người dùng dễ dàng thiết lập bài toán, chọn thuật toán giải và quan sát từng bước di chuyển của các viên gạch trong quá trình tìm kiếm lời giải.

# 2. Nội dung:
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
   
   Các thành phần chính:
   - Initial State: Trạng thái bắt đầu (vd: cấu hình ban đầu của 8-puzzle)
   - Actions: Tập các hành động hợp lệ (vd: di chuyển ô trống lên, xuống, trái, phải)
   - Transition Model: Mô tả kết quả của mỗi hành động (trạng thái mới sau khi thực hiện hành động)
   - Goal Test: Kiểm tra xem trạng thái hiện tại có phải là mục tiêu hay không
   - Path Cost: Tổng chi phí của đường đi (thường là số bước đi trong bài toán không có trọng số)
   
   Solution: Solution (lời giải) là dãy hành động (action sequence) đưa trạng thái ban đầu đến trạng thái mục tiêu. Mỗi bước tương ứng với một hành động di chuyển ô trống.

   So Sánh hiệu suất:
   * BFS:
     - Số bước trung bình: 20
     - Số node sinh ra: 30,000+
     - Bộ nhớ sử dụng: Cao
       
       ![2025-05-18 11-24-52](https://github.com/user-attachments/assets/d2ef13ca-5bfd-4c8a-b876-1ad1daed9bec)

   * DFS:
     - Số bước: Có thể bị lặp, không xác định
     - Số node sinh ra: 1000+
     - Bộ nhớ sử dụng: Thấp

      ![2025-05-18 11-35-55](https://github.com/user-attachments/assets/32a9e5eb-59ec-46ec-8c0c-4ce763b88cdb)

   * UCS:
     - Số bước trung bình: 20
     - Số node sinh ra: 5,000–20,000
     - Bộ nhớ sử dụng: Cao

      ![2025-05-18 11-34-42](https://github.com/user-attachments/assets/4ab5dedf-48f2-4f4b-b389-d17eb8d0f361)

   * IDDFS:
     - Số bước trung bình: 20
     - Số node sinh ra: Có thể cao hơn DFS
     - Bộ nhớ sử dụng: Thấp

      ![2025-05-18 11-37-02](https://github.com/user-attachments/assets/e6948393-ddd3-4b67-82ef-ec089368dc2a)

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
   
   Các thành phần chính
   - Initial State: Trạng thái bắt đầu (vd: cấu hình ban đầu của 8‑puzzle).
   - Actions: Tập các hành động hợp lệ (di chuyển ô trống lên, xuống, trái, phải).
   - Transition Model: Kết quả của mỗi hành động (bàn cờ mới sau khi di chuyển).
   - Goal Test: Kiểm tra trạng thái hiện tại có phải trạng thái mục tiêu không.
   - Path Cost: Tổng chi phí đường đi (với 8‑puzzle không trọng số → số bước).

   Solution: Solution (lời giải) là chuỗi hành động đưa trạng thái ban đầu đến mục tiêu. Trong 8‑puzzle, mỗi phần tử trong chuỗi là một bước di chuyển ô trống.

   So sánh hiệu suất:
   * A*
     - Số bước trung bình: ~ 20
     - Số node: 1 000 – 10 000
     - Tiêu tốn bộ nhớ: Cao

       ![2025-05-18 11-39-21](https://github.com/user-attachments/assets/b52f440a-7123-401f-9723-1d137098ace0)

   * Greedy:
     - Số bước trung bình: 25 – 40
     - Số node: 500 – 5 000
     - Tiêu tốn bộ nhớ: Thấp

       ![2025-05-18 11-38-22](https://github.com/user-attachments/assets/b8a7c078-1323-4ee7-a74e-b4c44c0eacae)

   * IDA*:
     - Số bước trung bình: ~ 20
     - Số node: 80 000 – 150 000
     - Tiêu tốn bộ nhớ: Vừa

       ![2025-05-18 11-40-27](https://github.com/user-attachments/assets/da1f7dde-f107-4854-9df9-4f8a66d31a06)

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

   Các thành phần chính:
   - Initial State: Trạng thái ban đầu (cấu hình xuất phát của 8-puzzle)
   - Actions: Tập các hành động hợp lệ (di chuyển ô trống lên, xuống, trái, phải)
   - Transition Model: Trạng thái mới sau khi thực hiện hành động
   - Goal Test: Kiểm tra trạng thái hiện tại có phải mục tiêu hay không
   - Path Cost: Thường không quan trọng bằng giá trị heuristic (h), tập trung vào việc tối ưu h(n)

   Solution: Solution là dãy hành động đưa trạng thái ban đầu đến trạng thái mục tiêu, nhưng các thuật toán này không đảm bảo tìm ra lời giải tối ưu, mà chủ yếu tìm trạng thái “tốt hơn” dần theo heuristic.

   So sánh hiệu suất:
   * Simple Hill Climbing:
   - Số bước trung bình: Không ổn định (có thể kẹt sớm)
   - Số node sinh ra: Rất ít
   - Bộ nhớ sử dụng: Thấp

     ![2025-05-18 11-40-27](https://github.com/user-attachments/assets/bcebf586-5d90-4e2b-819e-fa77cc433dab)

   * Steepest Ascent Hill Climbing:
   - Số bước trung bình: Tốt hơn simple hill climbing
   - Số node sinh ra: Ít
   - Bộ nhớ sử dụng: Thấp

     ![2025-05-18 11-45-28](https://github.com/user-attachments/assets/5e5fca56-6560-4a51-b745-1888782fe54f)

   * Stochastic Hill Climbing:
   - Số bước trung bình: Không ổn định, tùy lựa chọn ngẫu nhiên
   - Số node sinh ra: Thấp
   - Bộ nhớ sử dụng: Thấp

     ![2025-05-18 11-44-52](https://github.com/user-attachments/assets/f729a47f-4691-4014-9542-f32f499880eb)

   * Simulated Annealing:
   - Số bước trung bình: 25 – 40 (nếu cấu hình nhiệt độ tốt)
   - Số node sinh ra: Vừa
   - Bộ nhớ sử dụng: Thấp
   - Ghi chú: Có khả năng thoát khỏi local optimum nhờ chọn ngẫu nhiên có xác suất
     
      ![2025-05-18 11-45-53](https://github.com/user-attachments/assets/8d258740-55bd-4f5d-89f3-9878a0744886)

   * Beam Search:
   - Số bước trung bình: 20 – 40 (tùy beam width)
   - Số node sinh ra: Vừa – Cao
   - Bộ nhớ sử dụng: Tùy beam width (beam width càng lớn, bộ nhớ càng cao)
     
      ![2025-05-18 11-47-48](https://github.com/user-attachments/assets/47d0db15-6278-46ce-884e-371ab6120b00)

   * Genetic Algorithm:
   - Số bước trung bình: 30 – 60 (tùy cấu hình)
   - Số node sinh ra: Rất cao (quần thể lớn, nhiều thế hệ)
   - Bộ nhớ sử dụng: Cao
   - Ghi chú: Không đảm bảo tối ưu, nhạy với cấu hình (số thế hệ, mutation rate, crossover rate)

     ![2025-05-18 11-48-15](https://github.com/user-attachments/assets/5c30a277-f97b-4160-8460-bb4a752b468c)

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
   
   Các thành phần chính:
   - Initial State: Trạng thái ban đầu (trong nhiều trường hợp là tập hợp các trạng thái có thể, do không xác định rõ)
   - Actions: Tập các hành động hợp lệ (di chuyển, quan sát, chọn chiến lược...)
   - Transition Model: Không xác định hoặc xác suất (vd: hành động có thể không luôn dẫn đến cùng một trạng thái)
   - Goal Test: Kiểm tra xem trạng thái hiện tại (hoặc tập trạng thái) có đạt mục tiêu không
   - Path Cost: Có thể không xác định rõ ràng, hoặc tính theo kỳ vọng (expectation)

   Solution:
   - Lời giải không đơn thuần là dãy hành động cụ thể, mà có thể là:
     + Một kế hoạch điều kiện (contingency plan)
     + Một cây chiến lược cho mọi tình huống có thể xảy ra
     + Một chính sách hành động (policy) phù hợp với trạng thái nhận thức hiện tại
   Các thuật toán:
   * And-Or Search:
     
        ![2025-05-18 11-51-07](https://github.com/user-attachments/assets/ab2cefc6-b7f6-4ae1-b07e-9e20687301b2)

   * Belief State Search:

        ![2025-05-18 12-02-39](https://github.com/user-attachments/assets/7636af81-5d8f-4cdd-b809-ea0bc5deea0c)

   * Partially Observable:

        ![2025-05-18 12-06-25](https://github.com/user-attachments/assets/ffebe9bd-8508-4fd6-95bc-5c9868f85ae9)

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
   
   Các thành phần chính:
   - Initial State: Tập biến chưa được gán giá trị
   - Actions: Gán một giá trị hợp lệ cho một biến chưa được gán
   - Transition Model: Mỗi hành động cập nhật trạng thái bài toán (gán thêm biến)
   - Goal Test: Kiểm tra xem tất cả các biến đã được gán hợp lệ (thỏa ràng buộc)
   - Path Cost: Thường không tính đến — mục tiêu là tìm ra lời giải hợp lệ

   Solution: Lời giải là một tập gán giá trị cho tất cả các biến, sao cho tất cả ràng buộc được thỏa mãn.

   So sánh hiệu suất:
   * Backtracking Search:
   - Số bước trung bình: Tùy số biến và ràng buộc (có thể rất nhiều nếu không tối ưu)
   - Số node sinh ra: Cao nếu không có heuristic hoặc kiểm tra ràng buộc
   - Bộ nhớ sử dụng: Thấp
   - Ghi chú: Duyệt cây gán giá trị theo chiều sâu; đơn giản nhưng dễ bị quay lui nhiều
     
      ![2025-05-18 12-07-22](https://github.com/user-attachments/assets/eb464881-2838-4bb1-accc-52d135013429)

   * Forward Checking:
   - Số bước trung bình: Giảm nhiều so với backtracking cơ bản
   - Số node sinh ra: Ít hơn
   - Bộ nhớ sử dụng: Vừa
   - Ghi chú: Sau mỗi bước gán, loại trước các giá trị không còn hợp lệ cho biến chưa gán → phát hiện sớm dead-end
     
      ![2025-05-18 12-08-12](https://github.com/user-attachments/assets/4361832b-a6e2-4cb2-b39a-9cf7e31e1d32)

   * AC-3 (Arc Consistency Algorithm 3):
   - Số bước trung bình: Nhanh nếu dùng trước khi gán biến (preprocessing)
   - Số node sinh ra: Không áp dụng như trong tìm kiếm tuần tự (AC-3 hoạt động trên miền giá trị)
   - Bộ nhớ sử dụng: Vừa
   - Ghi chú: Duy trì ràng buộc nhị phân (arc-consistent) giữa các biến → giảm không gian tìm kiếm rất hiệu quả

     ![2025-05-18 12-09-29](https://github.com/user-attachments/assets/5129361e-034c-47b5-9556-5ba90cc6068c)

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
   
   Các thành phần chính:
   - Initial State: Trạng thái bắt đầu của agent (ví dụ: cấu hình ban đầu của 8-puzzle hoặc vị trí trong môi trường)
   - Actions: Tập các hành động hợp lệ tại mỗi trạng thái (vd: di chuyển lên, xuống, trái, phải)
   - Transition Model: Không cần biết trước — agent học từ tương tác với môi trường
   - Goal Test: Trạng thái mục tiêu cần đạt được (vd: 8-puzzle đúng thứ tự)
   - Path Cost / Reward: Không tính path cost mà là phần thưởng (reward) cho mỗi hành động; agent học chính sách tối đa hóa phần thưởng tổng cộng

   Solution:
   Lời giải là một chính sách hành động tối ưu (policy): tại mỗi trạng thái, chọn hành động có giá trị Q lớn nhất.
   Thuật toán cập nhật giá trị Q(s, a) qua công thức:
            Q(s, a) ← Q(s, a) + α * [r + γ * max(Q(s', a')) − Q(s, a)]
                     Trong đó:
                     + α là learning rate
                     + γ là discount factor
                     + r là phần thưởng nhận được
                     + s' là trạng thái kế tiếp sau hành động a

   So sánh hiệu suất:
   * Q-Learning:
   - Số bước trung bình: Tùy thuộc vào số tập huấn luyện và cấu hình
   - Số node sinh ra: Không đếm theo node mà theo số lần cập nhật Q
   - Bộ nhớ sử dụng: Cao (cần lưu Q-table với mọi cặp trạng thái – hành động)
   - Ghi chú: Cần nhiều vòng lặp huấn luyện để hội tụ, không phù hợp lắm cho không gian trạng thái lớn như 8-puzzle trừ khi dùng approximation (Deep Q)

     (Khá tiêu tốn thời gian, vui lòng chờ 2 phút...)
     ![q-learning (2)](https://github.com/user-attachments/assets/1bd567b4-6f9e-459e-99dd-f313f119c3ce)


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
