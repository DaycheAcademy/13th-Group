import turtle
from random import randint

top_x = -150
top_y = 150

turtle.hideturtle()
turtle.speed(0)
turtle.title("sudoku")
turtle.bgcolor("orange")

grid = [[0 for j in range(i, i + 9, 1)]for i in range(1, 81, 9)]
grid_copy = [[0 for t in range(i, i + 9, 1)]for i in range(1, 81, 9)]


def fill_grid_list(grid_list):
    start = randint(1, 9)
    for i in range(0, 9):
        for j in range(0, 9):
            if j == 0 and i in (1, 2, 4, 5, 7, 8):
                start = (grid_list[2][i - 1])
            elif j == 0 and i in (3, 6):
                start = (grid_list[1][i - 3])
            if start >= 9:
                start = 1
            else:
                start += 1
            grid_list[j][i] = start
    return fill_grid(grid_list)     # [['' if i == 0 else i for i in j]for j in grid]


def draw_grid():
    init = 35
    for i in range(10):
        if i in (0, 9):
            turtle.pensize(9)
        elif i in (3, 6):
            turtle.pensize(3)
        else:
            turtle.pensize(1)
        turtle.up()
        turtle.goto(top_x, top_y - i * init)
        turtle.down()
        turtle.goto(top_x+9*init, top_y - i * init)
    for i in range(10):
        if i in (0, 9):
            turtle.pensize(9)
        elif i in (3, 6):
            turtle.pensize(3)
        else:
            turtle.pensize(1)
        turtle.up()
        turtle.goto(top_x + i * init, top_y)
        turtle.down()
        turtle.goto(top_x + i * init, top_y - 9 * init)


def write_text(msg, x, y, size, color='black'):
    turtle.up()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(msg, align="left", font=('Arial', size, 'normal'))


def fill_grid(fill_list):
    global grid_copy
    for r in range(0, 9):
        for c in range(0, 9):
            if randint(0, 1):
                write_text(fill_list[r][c], top_x + c * 35 + 9, top_y - r * 35 - 35 + 8, 15)
                grid_copy[r][c] = fill_list[r][c]
                continue
            grid_copy[r][c] = ''
    # gridCopy = copy.deepcopy(grid)


draw_grid()
fill_grid_list(grid)


while True:
    for i in range(0, 9):
        for t in range(0, 9):
            if grid_copy[i][t] == '':
                val = turtle.textinput('', 'input value for ({},{})'.format(i, t))
                if val.isdigit() and val in range(1, 10):
                    write_text(val, top_x + t * 35 + 9, top_y - i * 35 - 35 + 8, 15, 'red')
                    grid_copy[i][t] = val
            else:
                continue


turtle.done()
