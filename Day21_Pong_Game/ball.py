from turtle import Turtle
import random

POSITIONS = [10, -10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.yball_pos = random.choice(POSITIONS)
        self.xball_pos = random.choice(POSITIONS)

    def move(self):
        new_y = self.ycor() + self.yball_pos
        new_x = self.xcor() + self.xball_pos
        self.goto(new_x, new_y)
