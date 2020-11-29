import turtle
pen = turtle.Pen()

pen.pensize(3)
pen.speed(0)
pen.hideturtle()
turtle.colormode(255)

pen.dot(400, (0, 255, 255))
pen.dot(380, (255, 255, 255))
pen.dot(320, (222, 171, 82))
pen.dot(300, (0, 0, 0))

def draw_hexagon(fillcolor, y, side_length):
    pen.fillcolor(fillcolor)
    pen.penup()
    pen.goto(0, y)
    pen.pendown()
    pen.begin_fill()
    pen.setheading(30)
    for i in range(6):
        pen.forward(side_length)
        pen.left(360/6)
    pen.end_fill()

draw_hexagon((255, 215, 0), -140, 140)
draw_hexagon((0, 0, 0), -130, 130)

def draw_pentagram(fillcolor, y, side_length):
    pen.fillcolor(fillcolor)
    pen.penup()
    pen.goto(0, y)
    pen.pendown()
    pen.begin_fill()
    pen.setheading(-72)
    for i in range(5):
        pen.forward(side_length)
        pen.left(72)
        pen.forward(side_length)
        pen.right(144)
    pen.end_fill()

draw_pentagram((255, 205, 62), 120, 80)
draw_pentagram((255, 215, 0), 90, 60)
turtle.done()
