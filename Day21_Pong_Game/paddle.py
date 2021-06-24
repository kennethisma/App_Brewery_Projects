from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(coordinates)
        self.movement = 20

    def move_up(self):
        up_y = self.ycor() + self.movement
        self.goto(self.xcor(), up_y)

        # Limits in the edges screen for paddle.
        if self.ycor() > 255 or self.ycor() < -255:
            up_y = self.ycor() - self.movement
            self.goto(self.xcor(), up_y)

    def move_down(self):
        down_y = self.ycor() - self.movement
        self.goto(self.xcor(), down_y)

        if self.ycor() > 255 or self.ycor() < -255:
            down_y = self.ycor() + self.movement
