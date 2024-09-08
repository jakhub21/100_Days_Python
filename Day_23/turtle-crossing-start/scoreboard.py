from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def win(self):
        self.level += 1
        self.update()

    def lose(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

