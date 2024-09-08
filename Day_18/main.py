import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_tuple = (r, g, b)
    return rgb_tuple


timmy.speed("fastest")
timmy.color(random_color())
timmy.circle(100)

screen = turtle.Screen()
screen.exitonclick()