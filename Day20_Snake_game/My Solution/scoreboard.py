from turtle import Turtle, position


class ScoreBoarde(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(x=-270, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-270, y=270)
        self.write(arg=f"Score = {self.score}", align="Left",
                   font=("Arial", 15, "normal"))
        self.goto(x=0, y=270)
        self.write(arg=f"High score = {self.high_score}", align="Center",
                   font=("Arial", 15, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_score()

    def end_game(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", align="center",
                   font=("Arial", 15, "normal"))

    # def add_high_score(self):
    #     self.high_score = self.score
    #     self.clear()
    #     self.update_score()

    def add_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()
