import turtle


pen = turtle.Pen()
pen.speed(0)
pen.shape("turtle")
turtle.bgcolor('black')
for j in range(36):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.left(10)
    pen.fillcolor('orange')
    for i in range(5):
        pen.forward(20)
        pen.stamp()
    pen.forward(30)
    pen.fillcolor('yellow')
    pen.begin_fill()
    for i in range(2):
        pen.forward(100)
        pen.right(30)
        pen.forward(100)
        pen.right(150)
    pen.end_fill()
pen.hideturtle()
turtle.done()
