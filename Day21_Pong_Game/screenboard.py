from turtle import Turtle


class ScreenLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")

    def draw_lines(self):
        self.goto(x=0, y=280)
        self.forward(20)
