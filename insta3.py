import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(100)
pen.width(2)
pen.hideturtle()

h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    pen.pencolor(c)

    for _ in range(12):
        pen.forward(i * 0.10)
        pen.left(150)

    pen.left(5)
    h += 0.01

turtle.done()