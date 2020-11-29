import turtle


pen = turtle.Pen()
pen.speed(2.5)
length = 200

pen.forward(length)
pen.left(90)
pen.forward(length)
pen.left(90)
pen.forward(length)
pen.left(90)
pen.forward(length)
pen.left(90)

pen.penup()
pen.goto(50, 120)
pen.pendown()
pen.circle(20)
pen.penup()
pen.goto(50, 140)
pen.pendown()
pen.dot(20, "black")

pen.penup()
pen.goto(150, 120)
pen.pendown()
pen.circle(20)
pen.penup()
pen.goto(150, 140)
pen.pendown()
pen.dot(20, "black")

pen.penup()
pen.goto(80, 60)
pen.pensize(20)
pen.down()
pen.forward(40)

pen.penup()
pen.pensize(1)
pen.goto(50, 200)
pen.right(90)
pen.down()
pen.forward(40)

pen.penup()
pen.goto(100, 200)
pen.down()
pen.forward(25)

pen.penup()
pen.goto(150, 200)
pen.down()
pen.forward(40)

pen.hideturtle()
turtle.done()
