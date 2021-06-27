from turtle import Turtle, left
from ball import Ball


class ScreenLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=300)
        self.seth(270)
        self.pensize(5)
        self.pendown()
        self.draw_line()
        self.hideturtle()

    def draw_line(self):
        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.clear()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.score}", align="left",
                   font=("calibri", 35, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def win(self):
        return self.score == 10

    def end_game(self):

        self.write(arg=f"{self.score}", align="left",
                   font=("calibri", 35, "bold"))
