import pygame
import random
import AI

pygame.init()
pygame.font.init()

pygame.display.set_caption("8-puzzle")
screen = pygame.display.set_mode((1200, 800))

running = True
solving = False
inputting = False
pressed = False
selected = False
done = False
speed = 500
begin_base = [
    [2,6,5],
    [0,8,7],
    [4,3,1]
]
begin = begin_base
puzzle_input = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
puzzle_input_check = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
result = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]
algorithm = {'Breadth-first search': False,
             'Uniform Cost Search': False,
             'AND-OR graph search': False,
             'Depth-First Search': False,
             'Greedy Search': False, 
             'Iterative Deepening DFS': False,
             'A* Search': False,
             'IDA* Search': False,
             'Simple Hill Climbing': False,
             'Stochastic Hill Climbing': False,
             'Steepest Ascent Hill Climbing': False,
             'Simulated Annealing': False,
             'Beam Search': False,
             'Genetic Algorithm': False}
blocks = []
block_width = 100
block_height = 100
spacing = 20
text_box_algorithm = ''
def create_blocks():
    new_blocks = []
    for i in range(9):
        if i <= 4:
            x = 950
            y = 50 + i * (block_height + spacing)
        else:
            x = 1070
            y = 50 + (i - 5) * (block_height + spacing)
        
        value = i
        label = '' if i == 0 else str(i)
        rect = pygame.Rect(x, y, block_width, block_height)
        new_blocks.append((rect, value))
    return new_blocks
blocks = create_blocks()  # khởi tạo ban đầu
index = 0

def button(x, y, width, height, text, color, text_color):
    nut = pygame.draw.rect(screen, color, (x, y, width, height), 0, 5)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return nut
def draw_box_with_text(x, y, width, height, text, color, text_color):
    box = pygame.draw.rect(screen, color, (x, y, width, height), 0, 5)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return box
def draw_puzzle(puzzle, pos):
    font = pygame.font.Font(None, 72)
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                text_surface = font.render(str(puzzle[i][j]), True, 'black')
                text_rect = text_surface.get_rect(center=(pos[0] + j * 100 + 50, pos[1] + i * 100 + 50))
                pygame.draw.rect(screen, 'white', (pos[0] + j * 100, pos[1] + i * 100, 100, 100))
                pygame.draw.rect(screen, 'black', (pos[0] + j * 100, pos[1] + i * 100, 100, 100), 2)
                screen.blit(text_surface, text_rect)

def is_solvable(puzzle):
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def random_puzzle():
    while True:
        puzzle = [i for i in range(9)]
        random.shuffle(puzzle)
        puzzle = [puzzle[i:i + 3] for i in range(0, 9, 3)]
        if is_solvable(puzzle):
            return puzzle
def add_number_to_input(puzzle_input, number):
    for i in range(3):
        for j in range(3):
            if puzzle_input_check[i][j] == 0:
                puzzle_input[i][j] = number
                puzzle_input_check[i][j] = 1
                return True
    return False
def reset_input():
    global puzzle_input, puzzle_input_check, blocks
    puzzle_input = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    puzzle_input_check = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    blocks = create_blocks()
def reset(box_status, box_thuattoan):
    box_status = draw_box_with_text(400, 20, 400, 50, 'STATUS', 'black', 'white')
    box_thuattoan = draw_box_with_text(400, 100, 400, 50, 'Algorithm', 'black', 'white')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inputting == False:
                if btn_random.collidepoint(event.pos) and solving == False:
                    begin = random_puzzle()
                elif btn_input.collidepoint(event.pos) and solving == False:
                    inputting = True
                    reset_input()
                elif btn_cong.collidepoint(event.pos):
                    if speed > 0:
                        speed -= 100
                elif btn_tru.collidepoint(event.pos):
                        speed += 100
                elif btn_BFS.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Breadth-first search'
                    selected = True
                elif btn_UCS.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Uniform Cost Search'
                    selected = True
                elif btn_Greedy.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Greedy Search'
                    selected = True
                # elif btn_AND_OR.collidepoint(event.pos) and solving == False:
                #     text_box_algorithm = 'AND-OR graph search'
                #     selected = True
                elif btn_DFS.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Depth-First Search'
                    selected = True
                elif btn_IDDFS.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Iterative Deepening DFS'
                    selected = True
                elif btn_A_Star.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'A* Search'
                    selected = True
                elif btn_IDA_Star.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'IDA* Search'
                    selected = True
                elif btn_SimpleHC.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Simple Hill Climbing'
                    selected = True
                elif btn_StochasticHC.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Stochastic Hill Climbing'
                    selected = True
                elif btn_Steepest.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Steepest Ascent Hill Climbing'
                    selected = True
                elif btn_Simulated.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Simulated Annealing'
                    selected = True
                elif btn_Beam.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Beam Search'
                    selected = True
                elif btn_GA.collidepoint(event.pos) and solving == False:
                    text_box_algorithm = 'Genetic Algorithm'
                    selected = True
                elif btn_solve.collidepoint(event.pos) and solving == False:
                    if selected == True:
                        algorithm[f'{text_box_algorithm}'] = True
                        solving = True
                        if text_box_algorithm == 'Breadth-first search':
                            path = AI.BFS(begin, result)
                        elif text_box_algorithm == 'Uniform Cost Search':
                            path = AI.Uniform_Cost_Search(begin, result)
                        # elif text_box_algorithm == 'AND-OR graph search':
                        #     problem = AI.Problem(begin, result)
                        #     path = AI.AND_OR_Graph_Search(problem)
                        elif text_box_algorithm == 'Depth-First Search':
                            path = AI.DFS(begin, result)
                        elif text_box_algorithm == 'Iterative Deepening DFS':
                            path = AI.Iterative_Deepening_DFS(begin, result, 50)
                        elif text_box_algorithm == 'Greedy Search':
                            path = AI.Greedy_Search(begin, result)
                        elif text_box_algorithm == 'A* Search':
                            path = AI.A_Star_Search(begin, result)
                        elif text_box_algorithm == 'IDA* Search':
                            path = AI.IDA(begin, result, 50)
                        elif text_box_algorithm == 'Simple Hill Climbing':
                            path = AI.Simple_Hill_Climbing(begin, result)
                        elif text_box_algorithm == 'Stochastic Hill Climbing':
                            path = AI.Stochastic_Hill_Climbing(begin, result)
                        elif text_box_algorithm == 'Steepest Ascent Hill Climbing':
                            path = AI.Steepest_Ascent_Hill_Climbing(begin, result)
                        elif text_box_algorithm == 'Simulated Annealing':
                            path = AI.Simulated_Annealing(begin, result)
                        elif text_box_algorithm == 'Beam Search':
                            path = AI.Beam_Search(begin, result, 50)
                        elif text_box_algorithm == 'Genetic Algorithm':
                            path = AI.Genetic_Algorithm(begin, result, 50)
                elif btn_next.collidepoint(event.pos) and solving == True:
                    if index < len(path):
                        index += 1
                elif btn_prev.collidepoint(event.pos) and solving == True:
                    if index > 1:
                        index -= 1
                elif btn_reset.collidepoint(event.pos):
                    reset(box_status, box_thuattoan)
                    index = 0
                    solving = False
                    current = []
                    path = []
                    text_box_algorithm = ''
                    done = False
                    algorithm = {'Breadth-first search': False,
                                 'Uniform Cost Search': False,
                                 'AND-OR graph search': False,
                                 'Depth-First Search': False,
                                 'Iterative Deepening DFS': False,
                                 'Greedy Search': False,
                                 'A* Search': False,
                                 'IDA* Search': False,
                                 'Simple Hill Climbing': False,
                                 'Stochastic Hill Climbing': False,
                                 'Steepest Ascent Hill Climbing': False,
                                 'Simulated Annealing': False,
                                 'Beam Search': False,
                                 'Genetic Algorithm': False}
                    selected = False
                    speed = 500
            else:  # inputting == True
                if btn_back.collidepoint(event.pos):
                    inputting = False
                elif btn_ok.collidepoint(event.pos):
                    begin = puzzle_input
                    inputting = False
                elif btn_reset_input.collidepoint(event.pos):
                    reset_input()
                for block in blocks:
                    rect, value = block
                    if rect.collidepoint(event.pos):
                        if add_number_to_input(puzzle_input, value):
                            blocks.remove(block)  # xoá khối vừa nhấn
                        break

    # Fill the screen with white color
    screen.fill('lightgrey')
    if inputting == False:
        font_title = pygame.font.Font(pygame.font.match_font('comicsansms'), 48)
        text_title = font_title.render('8-PUZZLE', True, 'gold')
        text_rect_title = text_title.get_rect(center=(250, 200))

        border_font = pygame.font.Font(pygame.font.match_font('comicsansms'), 48)
        border_text = border_font.render('8-PUZZLE', True, 'black')
        border_rect = border_text.get_rect(center=(247, 198))
        screen.blit(border_text, border_rect)

        screen.blit(text_title, text_rect_title)
        
        khung = pygame.draw.rect(screen, 'darkgrey', (175, 250, 300, 300), 0, 5)
        border_khung = pygame.draw.rect(screen, 'black', (175, 250, 300, 300), 2, 5)
        
        btn_random = button(20, 600, 125, 50, 'RANDOM', 'red', 'white')
        btn_input = button(185, 600, 125, 50, 'INPUT', 'orange', 'white')
        btn_solve = button(350, 600, 125, 50, 'SOLVE', 'green', 'white')
        btn_reset = button(185, 700, 125, 50, 'RESET', 'blue', 'white')
        btn_next = button(350, 700, 125, 50, '->', 'blue', 'white')
        btn_prev = button(20, 700, 125, 50, '<-', 'blue', 'white')
        btn_tru = button(25, 50, 50, 50, '-', 'black', 'white')
        btn_cong = button(225, 50, 50, 50, '+', 'black', 'white') 
        
        btn_BFS = button(550, 250, 125, 50, 'BFS', 'green', 'white')
        btn_UCS = button(700, 250, 125, 50, 'UCS', 'green', 'white')
        btn_DFS = button(850, 250, 125, 50, 'DFS', 'green', 'white')
        btn_IDDFS = button(1000, 250, 125, 50, 'IDDFS', 'green', 'white')
        btn_Greedy = button(550, 350, 125, 50, 'Greedy', 'green', 'white')
        btn_A_Star = button(700, 350, 125, 50, 'A*', 'green', 'white')
        btn_IDA_Star = button(850, 350, 125, 50, 'IDA*', 'green', 'white')
        btn_SimpleHC = button(1000, 350, 125, 50, 'Sim HC', 'green', 'white')
        btn_StochasticHC = button(550, 450, 125, 50, 'Stoc HC', 'green', 'white')
        btn_Steepest = button(700, 450, 125, 50, 'Steep HC', 'green', 'white')
        btn_Simulated = button(850, 450, 125, 50, 'Simulated', 'green', 'white')
        btn_Beam = button(1000, 450, 125, 50, 'Beam', 'green', 'white')
        btn_GA = button(550, 550, 125, 50, 'GA', 'green', 'white')
        # btn_AND_OR = button(850, 250, 125, 50, 'AND-OR', 'green', 'white')
        
        box_status = draw_box_with_text(400, 20, 400, 50, 'STATUS', 'black', 'white')
        box_thuattoan = draw_box_with_text(400, 100, 400, 50, text_box_algorithm, 'black', 'white')
        box_step = draw_box_with_text(40, 250, 100, 50, str(index), 'black', 'white')
        box_speed = draw_box_with_text(100, 50, 100, 50, str(speed), 'black', 'white')
        if solving == True and done == False:
            if algorithm[f'{text_box_algorithm}'] == True:
                if path != None:
                    if index < len(path):
                        box_status = draw_box_with_text(400, 20, 400, 50, 'SOLVING...', 'black', 'white')
                        box_thuattoan = draw_box_with_text(400, 100, 400, 50, f'{text_box_algorithm}', 'black', 'white')
                        current = path[index]
                        index += 1
                        box_step = draw_box_with_text(40, 250, 100, 50, str(index), 'black', 'white')
                        draw_puzzle(current, (175, 250))
                        pygame.time.delay(speed)  # Delay to see the solving process
                    else:
                        done = True
                else:
                    box_status = draw_box_with_text(400, 20, 400, 50, 'NO SOLUTION!', 'black', 'white')
                    box_thuattoan = draw_box_with_text(400, 100, 400, 50, f'{text_box_algorithm}', 'black', 'white')
                    solving = False
        elif solving == True and done == True:
            box_status = draw_box_with_text(400, 20, 400, 50, 'DONE!', 'black', 'white')
            box_thuattoan = draw_box_with_text(400, 100, 400, 50, f'{text_box_algorithm}', 'black', 'white')
            current = path[index-1]
            draw_puzzle(current, (175, 250))
        else:
            draw_puzzle(begin, (175, 250))
        draw_box_with_text(500, 250, 5, 500, '', 'black', 'white')
    else:
        font_input = pygame.font.Font(pygame.font.match_font('comicsansms'), 36)
        text_input = font_input.render('INPUT PUZZLE:', True, 'black')
        text_rect_input = text_input.get_rect(center=(250, 200))

        font_result = pygame.font.Font(pygame.font.match_font('comicsansms'), 36)
        text_result = font_result.render('RESULT:', True, 'black')
        text_rect_result = text_result.get_rect(center=(650, 200))

        border_font_input = pygame.font.Font(pygame.font.match_font('comicsansms'), 36)
        border_text_input = border_font_input.render('INPUT PUZZLE:', True, 'white')
        border_rect_input = border_text_input.get_rect(center=(247, 198))
        
        border_font_result = pygame.font.Font(pygame.font.match_font('comicsansms'), 36)
        border_text_result = border_font_result.render('RESULT:', True, 'white')
        border_rect_result = border_text_result.get_rect(center=(647, 198))
        
        font_den = pygame.font.Font(None, 56)
        text_den = font_den.render('->', True, 'black')
        text_rect_den = text_den.get_rect(center=(450, 350))
        
        font_select = pygame.font.Font(pygame.font.match_font('comicsansms'), 36)
        text_select = font_select.render('SELECT...', True, 'black')
        text_rect_select = text_select.get_rect(center=(1050, 700))
        
        border_font_select = pygame.font.Font(pygame.font.match_font('comicsansms'), 36)
        border_text_select = border_font_select.render('SELECT...', True, 'white')
        border_rect_select = border_text_select.get_rect(center=(1047, 698))
        
        screen.blit(border_text_input, border_rect_input)
        screen.blit(text_input, text_rect_input)
        screen.blit(border_text_result, border_rect_result)
        screen.blit(text_result, text_rect_result)
        screen.blit(text_den, text_rect_den)

        khung_input = pygame.draw.rect(screen, 'darkgrey', (100, 250, 300, 300), 0, 5)
        border_input = pygame.draw.rect(screen, 'black', (100, 250, 300, 300), 2, 5)
        khung_result = pygame.draw.rect(screen, 'darkgrey', (500, 250, 300, 300), 0, 5)
        border_result = pygame.draw.rect(screen, 'black', (500, 250, 300, 300), 2, 5)
        
        btn_back = button(20, 600, 125, 50, 'BACK', 'red', 'white')
        btn_ok = button(185, 600, 125, 50, 'OK', 'green', 'white')
        btn_reset_input = button(350, 600, 125, 50, 'RESET', 'blue', 'white')
        
        draw_puzzle(puzzle_input, (100, 250))
        draw_puzzle(result, (500, 250))
        
        frame_chua_khoi = pygame.draw.rect(screen, 'darkgrey', (900, 0, 300, 800), 0, 5)
        border_frame_chua_khoi = pygame.draw.rect(screen, 'black', (900, 0, 300, 800), 2, 5)
        screen.blit(border_text_select, border_rect_select)
        screen.blit(text_select, text_rect_select)
        
        # Create an array of blocks from 0 to 8, split into left and right columns
        # Vẽ từng block hiện có
        font_block = pygame.font.Font(None, 36)
        for rect, value in blocks:
            label = '' if value == 0 else str(value)
            pygame.draw.rect(screen, 'white', rect, 0, 5)
            pygame.draw.rect(screen, 'black', rect, 2, 5)
            text_surface = font_block.render(label, True, 'black')
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

    pygame.display.flip()
pygame.quit()