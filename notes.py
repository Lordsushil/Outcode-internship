# Upgraded Tetris Game with Ghost Piece, Hold Feature, Grid Lines, Next Piece Preview (No external dependencies)

import turtle as t
import random
import time

# === Constants ===
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 24

grid_offset_x = -GRID_WIDTH * CELL_SIZE // 2
grid_offset_y = -GRID_HEIGHT * CELL_SIZE // 2

# === Global Variables ===
board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
score = 0
level = 1
fall_speed = 0.5
hold_piece = None
can_hold = True
game_over = False

# === Tetromino Shapes ===
SHAPES = {
    'I': [(0,0), (1,0), (-1,0), (-2,0)],
    'O': [(0,0), (0,1), (1,0), (1,1)],
    'T': [(0,0), (-1,0), (1,0), (0,1)],
    'S': [(0,0), (1,0), (0,1), (-1,1)],
    'Z': [(0,0), (-1,0), (0,1), (1,1)],
    'L': [(0,0), (-1,0), (-2,0), (0,1)],
    'J': [(0,0), (1,0), (2,0), (0,1)],
}
COLORS = {
    'I': 'cyan', 'O': 'yellow', 'T': 'purple',
    'S': 'green', 'Z': 'red', 'L': 'orange', 'J': 'blue'
}

# === Turtle Setup ===
screen = t.Screen()
screen.title("Advanced Tetris 2025")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

drawer = t.Turtle()
drawer.penup()
drawer.hideturtle()
drawer.speed(0)

score_display = t.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(150, 220)

def draw_square(x, y, color):
    px = x * CELL_SIZE + grid_offset_x
    py = y * CELL_SIZE + grid_offset_y
    drawer.goto(px, py)
    drawer.color("white", color)
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(CELL_SIZE)
        drawer.left(90)
    drawer.end_fill()

def draw_grid():
    drawer.color("gray")
    for x in range(GRID_WIDTH + 1):
        drawer.goto(grid_offset_x + x * CELL_SIZE, grid_offset_y)
        drawer.pendown()
        drawer.goto(grid_offset_x + x * CELL_SIZE, grid_offset_y + GRID_HEIGHT * CELL_SIZE)
        drawer.penup()
    for y in range(GRID_HEIGHT + 1):
        drawer.goto(grid_offset_x, grid_offset_y + y * CELL_SIZE)
        drawer.pendown()
        drawer.goto(grid_offset_x + GRID_WIDTH * CELL_SIZE, grid_offset_y + y * CELL_SIZE)
        drawer.penup()

def draw_board(current=None, ghost=None):
    drawer.clear()
    draw_grid()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if board[y][x]:
                draw_square(x, y, board[y][x])
    if ghost:
        for dx, dy in ghost['shape']:
            draw_square(ghost['x'] + dx, ghost['y'] + dy, "#222222")
    if current:
        for dx, dy in current['shape']:
            draw_square(current['x'] + dx, current['y'] + dy, COLORS[current['type']])
    draw_hold()
    draw_next()
    update_score()
    screen.update()

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}\nLevel: {level}", align="left", font=("Arial", 16, "bold"))

def valid(piece, dx=0, dy=0, rotated=False):
    shape = piece['shape']
    if rotated:
        shape = [(-y, x) for x, y in shape]
    for x, y in shape:
        nx, ny = piece['x'] + x + dx, piece['y'] + y + dy
        if nx < 0 or nx >= GRID_WIDTH or ny < 0:
            return False
        if ny < GRID_HEIGHT and board[ny][nx]:
            return False
    return True

def freeze(piece):
    for dx, dy in piece['shape']:
        x, y = piece['x'] + dx, piece['y'] + dy
        if y >= 0:
            board[y][x] = COLORS[piece['type']]

def clear_lines():
    global score
    cleared = 0
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    cleared = GRID_HEIGHT - len(new_board)
    for _ in range(cleared):
        new_board.insert(0, [0]*GRID_WIDTH)
    if cleared:
        score += cleared * 100
    return new_board

def new_piece():
    shape_type = random.choice(list(SHAPES.keys()))
    return {
        'type': shape_type,
        'shape': SHAPES[shape_type],
        'x': GRID_WIDTH // 2,
        'y': GRID_HEIGHT - 2
    }

def get_ghost(piece):
    ghost = piece.copy()
    while valid(ghost, dy=-1):
        ghost['y'] -= 1
    return ghost

def draw_hold():
    if hold_piece:
        x, y = 150, 50
        drawer.goto(x, y)
        drawer.color("white")
        drawer.write("Hold:", align="left", font=("Arial", 12))
        for dx, dy in SHAPES[hold_piece]:
            draw_square(7 + dx, 18 - dy, COLORS[hold_piece])

def draw_next():
    x, y = 150, 150
    drawer.goto(x, y)
    drawer.color("white")
    drawer.write("Next:", align="left", font=("Arial", 12))
    for dx, dy in next_piece['shape']:
        draw_square(7 + dx, 23 - dy, COLORS[next_piece['type']])

def hold():
    global hold_piece, can_hold, current_piece, next_piece
    if not can_hold:
        return
    can_hold = False
    current_type = current_piece['type']
    if not hold_piece:
        hold_piece = current_type
        current_piece = next_piece
        generate_next()
    else:
        hold_piece, current_piece = current_type, {'type': hold_piece, 'shape': SHAPES[hold_piece], 'x': GRID_WIDTH // 2, 'y': GRID_HEIGHT - 2}

def generate_next():
    global next_piece
    next_piece = new_piece()

# === Controls ===
def move_left():
    if valid(current_piece, dx=-1):
        current_piece['x'] -= 1
        draw_board(current_piece, get_ghost(current_piece))

def move_right():
    if valid(current_piece, dx=1):
        current_piece['x'] += 1
        draw_board(current_piece, get_ghost(current_piece))

def rotate():
    if valid(current_piece, rotated=True):
        current_piece['shape'] = [(-y, x) for x, y in current_piece['shape']]
        draw_board(current_piece, get_ghost(current_piece))

def drop():
    move_down(force=True)

def move_down(force=False):
    global current_piece, board, can_hold, game_over
    if valid(current_piece, dy=-1):
        current_piece['y'] -= 1
    else:
        freeze(current_piece)
        board = clear_lines()
        current_piece = next_piece
        generate_next()
        can_hold = True
        if not valid(current_piece):
            game_over = True
    draw_board(current_piece, get_ghost(current_piece))

# === Input Bindings ===
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_down, "Down")
screen.onkeypress(rotate, "Up")
screen.onkeypress(drop, "space")
screen.onkeypress(hold, "h")

# === Game Start ===
current_piece = new_piece()
next_piece = new_piece()
draw_board(current_piece, get_ghost(current_piece))

# === Game Loop ===
while not game_over:
    time.sleep(fall_speed)
    move_down()

# Show Game Over
end = t.Turtle()
end.color("red")
end.penup()
end.hideturtle()
end.goto(0, 0)
end.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
screen.mainloop()
