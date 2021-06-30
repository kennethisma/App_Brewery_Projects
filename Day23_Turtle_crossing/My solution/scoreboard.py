from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-350, y=250)
        self.refresh_score()

    def refresh_score(self):
        self.write(arg=f"Level {self.score}",
                   align="Left", font=("Arial", 15, "normal"))

    def next_level(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game over",
                   align="Center", font=("Arial", 20, "normal"))
