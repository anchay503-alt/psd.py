import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Star Spiral Animation")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

screen.tracer(0)

h = 0

for i in range(720):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.forward(i * 0.4)

    # Draw star
    for _ in range(8):
        t.forward(80)
        t.backward(80)
        t.right(45)

    t.right(8)
    h += 0.004

    if i % 5 == 0:
        screen.update()

screen.update()
turtle.done()