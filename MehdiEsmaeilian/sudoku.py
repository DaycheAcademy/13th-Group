
import turtle

myTurtle = turtle.Turtle()
myTurtle.speed(0)
myTurtle.color("#000000")
myTurtle.hideturtle()
topLeft_x = -150
topLeft_y = 150

# A procedure to draw 9*9 sudoku table  using Python Turtle
intDim = 35
for row in range(0, 10):
        if row == 0 or row == 9:
            myTurtle.pensize(5)
        elif (row % 3) == 0:
            myTurtle.pensize(3)
        else:
            myTurtle.pensize(1)
        myTurtle.penup()
        myTurtle.goto(topLeft_x, topLeft_y - row * intDim)
        myTurtle.pendown()
        myTurtle.goto(topLeft_x + 9 * intDim, topLeft_y - row * intDim)

for col in range(0, 10):
        if col == 0 or col == 9:
            myTurtle.pensize(5)
        elif (col % 3) == 0:
            myTurtle.pensize(3)
        else:
            myTurtle.pensize(1)
        myTurtle.penup()
        myTurtle.goto(topLeft_x + col * intDim, topLeft_y)
        myTurtle.pendown()
        myTurtle.goto(topLeft_x + col * intDim, topLeft_y - 9 * intDim)

turtle.done()