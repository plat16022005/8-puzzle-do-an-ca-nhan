from collections import deque
import copy
from queue import PriorityQueue
import random
import math

Moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def Find_Empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return None

def Check(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def Chinh_Sua_Ma_Tran(board, x, y, new_x, new_y):
    # Tạo bản sao sâu của board để không thay đổi board gốc
    new_board = copy.deepcopy(board)
    new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
    return new_board

def BFS(start, goal):
    visited = set()
    queue = deque()

    queue.append((start, [start]))
    
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        visited.add(tuple(tuple(row) for row in current))
        
        x, y = Find_Empty(current)
        
        for dx, dy in Moves:
            new_x, new_y = x + dx, y + dy
            if Check(new_x, new_y):
                new_state = Chinh_Sua_Ma_Tran(current, x, y, new_x, new_y)

                tuple_state = tuple(tuple(row) for row in new_state)
                
                if tuple_state not in visited:
                    new_path = path + [new_state]
                    queue.append((new_state, new_path))
                    visited.add(tuple_state)
    return None
def Uniform_Cost_Search(start, goal):
    visited = set()
    open = PriorityQueue()
    open.put((0, start, [start]))
    while open:
        cost, current, path = open.get()
        if str(current) not in visited:
            visited.add(tuple(tuple(row) for row in current))
            if current == goal:
                return path
            X, Y = Find_Empty(current)
            for dx, dy in Moves:
                new_x, new_y = X + dx, Y + dy
                if Check(new_x, new_y):
                    new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                    tuple_state = tuple(tuple(row) for row in new_state)
                    if tuple_state not in visited:
                        open.put(cost + 1, new_state, path + [new_state])
    return None
def DFS(start, goal):
    visited = set()
    open = []
    open.append((start, [start]))
    while open:
        current, path = open.pop()
        if current == goal:
            return path
        X, Y = Find_Empty(current)
        for dx, dy in Moves:
            new_x, new_y = X + dx, Y + dy
            if Check(new_x, new_y):
                new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                tuple_state = tuple(tuple(row) for row in new_state)
                if tuple_state not in visited:
                    open.append((new_state, path + [new_state]))
                    visited.add(tuple_state)
    return None
def depth_bounded_search(start, goal, depth_bound, visited):
    if start == goal:
        return [start]
    
    if depth_bound > 0:
        X, Y = Find_Empty(start)
        for dx, dy in Moves:
            new_x, new_y = X + dx, Y + dy
            if Check(new_x, new_y):
                new_state = Chinh_Sua_Ma_Tran(start, X, Y, new_x, new_y)
                state_tuple = tuple(tuple(row) for row in new_state)
                if state_tuple not in visited:
                    visited.add(state_tuple)
                    solution = depth_bounded_search(new_state, goal, depth_bound - 1, visited)
                    if solution is not None:
                        return [start] + solution
    return None
                
def Iterative_Deepening_DFS(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        solution = depth_bounded_search(start, goal, depth, visited)
        if solution is not None:
            return solution
    return None
def Greedy_Search(start, goal):
    visited = set()
    open = PriorityQueue()
    open.put((Manhattan_Heuristic(start, goal), start, [start]))
    while open:
        cost, current, path = open.get()
        if str(current) not in visited:
            visited.add(tuple(tuple(row) for row in current))
            if current == goal:
                return path
            X, Y = Find_Empty(current)
            for dx, dy in Moves:
                new_x, new_y = X + dx, Y + dy
                if Check(new_x, new_y):
                    new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                    tuple_state = tuple(tuple(row) for row in new_state)
                    if tuple_state not in visited:
                        open.put((Manhattan_Heuristic(current,goal), new_state, path + [new_state]))
    return None
def A_Star_Search(start, goal):
    visited = set()
    open = PriorityQueue()
    open.put((Manhattan_Heuristic(start, goal), start, [start]))
    while open:
        cost, current, path = open.get()
        if str(current) not in visited:
            visited.add(tuple(tuple(row) for row in current))
            if current == goal:
                return path
            X, Y = Find_Empty(current)
            for dx, dy in Moves:
                new_x, new_y = X + dx, Y + dy
                if Check(new_x, new_y):
                    new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                    tuple_state = tuple(tuple(row) for row in new_state)
                    if tuple_state not in visited:
                        open.put((cost+1+Manhattan_Heuristic(current,goal), new_state, path + [new_state]))
    return None
def Manhattan_Heuristic(current, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if current[i][j] != 0:
                goal_x, goal_y = Find_X(current[i][j], goal)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance
def Find_X(x, goal):
    for i in range(3):
        for j in range(3):
            if x == goal[i][j]:
                return i, j
    return None
def IDA_limit(Start, Goal, limit):
    qp = PriorityQueue()
    qp.put( (0,0,Start,[]) )
    
    visited = set()
    
    while not qp.empty():
        f_n,chiphi,current, path = qp.get()
        if current == Goal:
            path = path + [Goal]
            return path
        
        x,y = Find_Empty(current)
        
        for dx,dy in Moves:
            new_X = x + dx
            new_Y = y + dy
            
            if(Check(new_X,new_Y)):
                new_matran = Chinh_Sua_Ma_Tran(current, x, y, new_X, new_Y)
                if str(new_matran) not in visited:
                    visited.add(str(new_matran))
                    f_new = chiphi + Manhattan_Heuristic(new_matran, Goal)
                    if f_new <= limit:
                        qp.put((f_new,chiphi+1,new_matran,path+[current]))
    return None

def IDA(Start,goal,limit):
    check = None
    while check == None:
        limit = limit + limit/2
        check = IDA_limit(Start, goal ,limit)
    return check
def Simple_Hill_Climbing(start, goal):
    current = start
    path = [current]

    while True:
        neighbors = []
        X, Y = Find_Empty(current)
        for dx, dy in Moves:
            new_x, new_y = X + dx, Y + dy
            if Check(new_x, new_y):
                new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                neighbors.append(new_state)

        if not neighbors:
            break

        next_state = min(neighbors, key=lambda s: Manhattan_Heuristic(s, goal))

        if Manhattan_Heuristic(next_state, goal) >= Manhattan_Heuristic(current, goal):
            break

        current = next_state
        path.append(current)

    return path
def Stochastic_Hill_Climbing(start, goal):
    current = start
    path = [current]

    while True:
        neighbors = []
        X, Y = Find_Empty(current)
        for dx, dy in Moves:
            new_x, new_y = X + dx, Y + dy
            if Check(new_x, new_y):
                new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                neighbors.append(new_state)

        if not neighbors:
            break

        next_state = random.choice(neighbors)

        if Manhattan_Heuristic(next_state, goal) >= Manhattan_Heuristic(current, goal):
            break

        current = next_state
        path.append(current)

    return path
def Steepest_Ascent_Hill_Climbing(start, goal):
    current = start
    path = [current]

    while True:
        neighbors = []
        X, Y = Find_Empty(current)
        for dx, dy in Moves:
            new_x, new_y = X + dx, Y + dy
            if Check(new_x, new_y):
                new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                neighbors.append(new_state)

        if not neighbors:
            break

        next_state = max(neighbors, key=lambda s: -Manhattan_Heuristic(s, goal))

        if Manhattan_Heuristic(next_state, goal) >= Manhattan_Heuristic(current, goal):
            break

        current = next_state
        path.append(current)

    return path
def Simulated_Annealing(start, goal, temperature=1000, cooling_rate=0.99):
    current = start
    path = [current]

    while temperature > 1:
        if current == goal:
            break

        neighbors = []
        X, Y = Find_Empty(current)
        for dx, dy in Moves:
            new_x, new_y = X + dx, Y + dy
            if Check(new_x, new_y):
                new_state = Chinh_Sua_Ma_Tran(current, X, Y, new_x, new_y)
                neighbors.append(new_state)

        if not neighbors:
            break

        next_state = random.choice(neighbors)
        current_cost = Manhattan_Heuristic(current, goal)
        next_cost = Manhattan_Heuristic(next_state, goal)

        if next_cost < current_cost:
            current = next_state
            path.append(current)
        else:
            delta = current_cost - next_cost
            acceptance_probability = math.exp(delta / temperature)
            if random.random() < acceptance_probability:
                current = next_state
                path.append(current)

        temperature *= cooling_rate

    return path
def Beam_Search(Start, Goal, beam_width=3):
    current_level = [(Start, [])]
    visited = set()

    while current_level:
        next_level_candidates = PriorityQueue()

        for state, path in current_level:
            if state == Goal:
                return path + [Goal]

            x, y = Find_Empty(state)

            for dx, dy in Moves:
                nx, ny = x + dx, y + dy
                if Check(nx, ny):
                    new_state = Chinh_Sua_Ma_Tran(state, x, y, nx, ny)
                    if str(new_state) not in visited:
                        visited.add(str(new_state))
                        next_level_candidates.put((Manhattan_Heuristic(new_state, Goal), new_state, path + [state]))

        current_level = []
        for _ in range(min(beam_width, next_level_candidates.qsize())):
            _, new_state, new_path = next_level_candidates.get()
            current_level.append((new_state, new_path))

    return []

def Genetic_Algorithm(start, goal, population_size=10, generations=1000):
    def fitness(individual):
        return Manhattan_Heuristic(individual, goal)

    def crossover(parent1, parent2):
        flat1 = sum(parent1, [])
        flat2 = sum(parent2, [])

        index = random.randint(1, 7)
        child_flat = flat1[:index]

        for num in flat2:
            if num not in child_flat:
                child_flat.append(num)

        child = [child_flat[i*3:(i+1)*3] for i in range(3)]
        return child

    def mutate(individual):
        x, y = Find_Empty(individual)
        dx, dy = random.choice(Moves)
        new_x, new_y = x + dx, y + dy
        if Check(new_x, new_y):
            return Chinh_Sua_Ma_Tran(individual, x, y, new_x, new_y)
        return individual

    def shuffle_state(state, moves=30):
        shuffled = copy.deepcopy(state)
        for _ in range(moves):
            x, y = Find_Empty(shuffled)
            dx, dy = random.choice(Moves)
            new_x, new_y = x + dx, y + dy
            if Check(new_x, new_y):
                shuffled = Chinh_Sua_Ma_Tran(shuffled, x, y, new_x, new_y)
        return shuffled

    population = [shuffle_state(start) for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=fitness)
        if fitness(population[0]) == 0:
            return population[0]

        next_generation = population[:population_size // 2]

        while len(next_generation) < population_size:
            parent1 = random.choice(next_generation[:population_size // 4])
            parent2 = random.choice(next_generation[:population_size // 4])
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)

        population = next_generation

    return None
def And_Or_Search(current_state, goal_state, path = [], visited = set(), depth = 0, max_depth = 30):    
    if depth > max_depth:
        return (False, [])
    # Kiểm tra trạng thái hiện tại
    if current_state == goal_state:
        return (True, path)
    
    # Đánh dấu trạng thái đã thăm
    state_tuple = tuple(map(tuple, current_state))
    if state_tuple in visited:
        return (False, [])
    visited.add(state_tuple)
    
    # Tìm vị trí ô trống
    x, y = next((i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0)
    
    # Thử các hướng đi có thể (OR nodes)
    for dx, dy, move in [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Tạo trạng thái mới
            new_state = [row[:] for row in current_state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            
            # Đệ quy tìm kiếm (AND - phải tìm được đường đi từ trạng thái này)
            solved, new_path = And_Or_Search(new_state, goal_state, path + [move], visited.copy())
            
            if solved:
                return (True, new_path)
    
    return (False, [])
def Belief_State_Search(initial_belief, goal_state):
    """
    Thuật toán tìm kiếm trong môi trường niềm tin (belief state) cho bài toán 8-puzzle
    Giả định: Chỉ quan sát được vị trí của ô trống và 1 số khác (ví dụ số 1)
    """
    
    visited = set()  # Lưu các belief state đã thăm
    queue = deque()
    queue.append((initial_belief, []))  # (belief state, path)
    
    while queue:
        current_belief, path = queue.popleft()
        
        # Kiểm tra nếu tất cả các trạng thái trong belief đều là goal
        if all(state == goal_state for state in current_belief.possible_states):
            return path
        
        # Tạo key để kiểm tra belief state đã thăm
        belief_key = frozenset(tuple(tuple(row) for row in state) for state in current_belief.possible_states)
        if belief_key in visited:
            continue
        visited.add(belief_key)
        
        # Thử các action có thể
        for action in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            # Tạo belief state mới sau action
            new_belief = current_belief.update(action, get_observation_after_action(action))
            
            if new_belief.possible_states:  # Nếu action hợp lệ
                queue.append((new_belief, path + [action]))
    
    return None  # Không tìm thấy giải pháp

class BeliefState8Puzzle:
    def __init__(self, possible_states):
        self.possible_states = possible_states  # Danh sách các trạng thái có thể
        
    def update(self, action, observation):
        """Cập nhật belief state sau khi thực hiện action và nhận observation"""
        new_states = []
        for state in self.possible_states:
            new_state = self.apply_action(state, action)
            if new_state and self.observation_match(new_state, observation):
                new_states.append(new_state)
        return BeliefState8Puzzle(new_states)
    
    def apply_action(self, state, action):
        """Áp dụng action lên một trạng thái cụ thể"""
        x, y = self.find_blank(state)
        new_state = [row[:] for row in state]
        
        if action == 'UP' and x > 0:
            new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
            return new_state
        elif action == 'DOWN' and x < 2:
            new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
            return new_state
        elif action == 'LEFT' and y > 0:
            new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
            return new_state
        elif action == 'RIGHT' and y < 2:
            new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
            return new_state
        return None
    
    def observation_match(self, state, observation):
        """Kiểm tra trạng thái có phù hợp với observation không"""
        # Giả sử observation là vị trí của số 1 và ô trống
        (obs_1_x, obs_1_y), (obs_blank_x, obs_blank_y) = observation
        state_1_pos = self.find_number(state, 1)
        state_blank_pos = self.find_blank(state)
        return state_1_pos == (obs_1_x, obs_1_y) and state_blank_pos == (obs_blank_x, obs_blank_y)
    
    def find_blank(self, state):
        """Tìm vị trí ô trống (0)"""
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return (-1, -1)
    
    def find_number(self, state, num):
        """Tìm vị trí của một số cụ thể"""
        for i in range(3):
            for j in range(3):
                if state[i][j] == num:
                    return (i, j)
        return (-1, -1)
def get_observation_after_action(action):
    """Hàm giả lập sensor - trả về observation sau khi thực hiện action"""
    # Trong thực tế, đây sẽ là thông tin từ sensor
    # Ở đây giả sử observation là vị trí của số 1 và ô trống
    # (Cần được triển khai cụ thể tùy bài toán)
    pass

def generate_all_possible_states(observation):
    """Tạo tất cả các trạng thái có thể phù hợp với observation ban đầu"""
    # Triển khai hàm này dựa trên observation đầu vào
    pass