import time
import datetime as dt
import turtle

t1 = turtle.Turtle()
# create a turtle to create rectangle box
t2 = turtle.Turtle()
# create a turtle to display time
s = turtle.Screen()
# set background color of the screen
s.bgcolor("white")
# obtain current hour, minute and second
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(5)
t1.color('black')
t1.penup()
# set the position of turtle
t1.goto(-30, 0)
t1.pendown()
# create rectangular box
for i in range(2):
    t1.hideturtle()
    t1.forward(300)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
while True:
    t2.hideturtle()
    t2.clear()
    # display the time
    t2.write(str(hr).zfill(2)
            + ":" + str(min).zfill(2) + ":"
            + str(sec).zfill(2),
            font=("Arial Narrow", 50, "bold"))
    time.sleep(1)
    sec += 1
    if sec == 60:
        sec = 0
        min += 1
        if min == 60:
            min = 0
            hr += 1
        if hr == 13:
            hr = 1