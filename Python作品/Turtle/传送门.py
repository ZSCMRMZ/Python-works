import turtle


pen = turtle.Pen()
pen.speed(0)
for i in range(20, 170):
    if (i < 50):
        pen.pencolor('red')
    elif (i < 80):
        pen.pencolor('white')
    elif (i < 110):
        pen.pencolor('green')
    elif (i < 140):
        pen.pencolor('white')
    else:
        pen.pencolor('blue')
    pen.forward(i)
    pen.left(90)
    print('循环变量i:', i)
pen.hideturtle()
turtle.done()
