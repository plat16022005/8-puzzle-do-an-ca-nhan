from collections import deque
import copy
from queue import PriorityQueue

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
class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        x, y = Find_Empty(state)
        acts = []
        for dx, dy in Moves:
            new_x, new_y = x + dx, y + dy
            if Check(new_x, new_y):
                acts.append((dx, dy))
        return acts

    def results(self, state, action):
        # Giả lập môi trường không xác định: có thể thành công hoặc thất bại
        x, y = Find_Empty(state)
        dx, dy = action
        new_x, new_y = x + dx, y + dy
        if not Check(new_x, new_y):
            return [state]  # thất bại

        success = Chinh_Sua_Ma_Tran(state, x, y, new_x, new_y)
        return [success, state]  # có thể thành công hoặc không
def AND_OR_Graph_Search(problem):
    return OR_Search(problem.initial, problem, [])

def OR_Search(state, problem, path):
    if problem.goal_test(state):
        return []

    if tuple(tuple(row) for row in state) in path:
        return None  # tránh lặp

    for action in problem.actions(state):
        results = problem.results(state, action)
        plan = AND_Search(results, problem, path + [tuple(tuple(row) for row in state)])
        if plan is not None:
            return [(action, plan)]
    return None

def AND_Search(states, problem, path):
    plans = []
    for s in states:
        plan = OR_Search(s, problem, path)
        if plan is None:
            return None
        plans.append(plan)
    return plans