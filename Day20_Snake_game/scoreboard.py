from turtle import Turtle


class ScoreBoarde(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.clear()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(x=-20, y=270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score = {self.score}", align="center",
                   font=("Arial", 20, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_score()
