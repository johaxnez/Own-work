from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 10
        self.update_score()

    def write_score(self):
        self.update_score()

    def point(self):
        self.score += 10
        self.update_score()

    def life_lost(self):
        self.lives -= 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.score, align="center", font=("Courier", 30, "normal"))
        self.goto(-150, 130)
        self.write(f"lives left: {self.lives}", align="center", font=("Courier", 20, "normal"))

