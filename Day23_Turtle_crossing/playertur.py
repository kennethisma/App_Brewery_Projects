from turtle import Turtle, xcor


class PlayerTur(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.hideturtle()
        self.penup()
        self.seth(90)
        self.goto(x=0, y=-280)
        self.showturtle()

    def move_up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)
        if self.heading() != 90:
            self.seth(90)

    def move_down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)
        if self.heading() != 90:
            self.seth(90)

    def move_left(self):
        self.seth(180)
        xcor = self.xcor() - 20
        self.goto(xcor, self.ycor())

    def move_right(self):
        self.seth(0)
        xcor = self.xcor() + 20
        self.goto(xcor, self.ycor())
