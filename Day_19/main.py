from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
y_value = -125
race = False
all_turtle = []

for i in colors:
    tim = Turtle(shape="turtle")
    tim.color(i)
    tim.penup()
    tim.goto(x=-230, y=y_value)
    all_turtle.append(tim)
    y_value += 50

if bet:
    race = True


while race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race = False
            winning = turtle.pencolor()
            if winning == bet:
                print(f"You have won! The {winning} turtle is the winner")
            else:
                print(f"You have lost! The {winning} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
