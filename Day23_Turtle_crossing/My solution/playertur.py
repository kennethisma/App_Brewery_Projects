from turtle import Turtle, xcor

START_POSITION = (0, -280)


class PlayerTur(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.hideturtle()
        self.penup()
        self.seth(90)
        self.goto(START_POSITION)
        self.showturtle()

    def move_up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def home(self):
        self.goto(START_POSITION)
