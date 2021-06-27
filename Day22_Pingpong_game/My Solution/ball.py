from turtle import Turtle
import random

POSITIONS = [10, -10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # Random start position of ball.
        self.yball_pos = POSITIONS[0]
        self.xball_pos = POSITIONS[1]
        self.random_position()

    def move(self):
        new_y = self.ycor() + self.yball_pos
        new_x = self.xcor() + self.xball_pos
        self.goto(new_x, new_y)

    def random_position(self):
        self.yball_pos = random.choice(POSITIONS)
        self.xball_pos = random.choice(POSITIONS)
