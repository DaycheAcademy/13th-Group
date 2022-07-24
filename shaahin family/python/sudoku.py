import turtle
from random import randint


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
            grid_copy[r][c] = 0
            final_list[r][c] = 1
    # gridCopy = copy.deepcopy(grid)


if __name__ == '__main__':
    print(turtle.screensize())
    turtle.hideturtle()
    turtle.speed(0)
    turtle.title("sudoku")
    turtle.bgcolor("pink")

    top_x = -150
    top_y = 150

    grid = [[0 for j in range(i, i + 9, 1)]for i in range(1, 81, 9)]
    grid_copy = [[0 for t in range(i, i + 9, 1)]for i in range(1, 81, 9)]
    final_list = [[0 for b in range(i, i + 9, 1)]for i in range(1, 81, 9)]
    check_while = 0
    count_valid_value = 0
    count_not_valid_value = 0

    draw_grid()
    fill_grid_list(grid)

    while check_while == 0:
        check_while = 1
        for i in range(0, 9):
            for t in range(0, 9):
                if grid_copy[i][t] == 0:
                    val = turtle.textinput('', 'input value for ({},{})'.format(i, t))
                    if val.isdigit() and int(val) in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                        f_value = int(val)
                        write_text(f_value, top_x + t * 35 + 9, top_y - i * 35 - 35 + 8, 15, 'purple')
                        grid_copy[i][t] = f_value

        for i in grid_copy:
            if 0 in i:
                check_while = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if final_list[i][j] == 1 and grid_copy[i][j] == grid[i][j]:
                final_list[i][j] = grid_copy[i][j]
                write_text(grid_copy[i][j], top_x + j * 35 + 9, top_y - i * 35 - 35 + 8, 15, 'green')
                count_valid_value += 1
            elif final_list[i][j] == 1:
                final_list[i][j] = 0
                count_not_valid_value += 1
                write_text(grid_copy[i][j] if grid_copy[i][j] > 0 else '', top_x + j * 35 + 9, top_y - i * 35 - 35 + 8, 15, 'red')

    write_text(f'Number of wrong numbers: {count_not_valid_value}', -125, -200, 15, 'red')
    write_text(f'Number of correct numbers: {count_valid_value}', -125, -250, 15, 'green')

    turtle.done()
