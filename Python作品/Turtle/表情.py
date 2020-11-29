import turtle


pen = turtle.Pen()
pen.speed(2.5)
length = 200

password = turtle.textinput("密码", "请输入密码：")
if password == "happy":

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
    pen.down()
    pen.right(90)
    pen.circle(20,180)
    pen.hideturtle()
elif password == "sad":

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
    pen.goto(120, 60)
    pen.down()
    pen.left(90)
    pen.circle(20,180)
    pen.hideturtle()
else:
    turtle.write("输入错误")
turtle.done()
