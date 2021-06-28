from turtle import Turtle, position
import random
YPOSITION = random.randint(-250, 250)
R = random.random()
G = random.random()
B = random.random()
COLORS = (R, G, B)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS)
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.goto(x=420, y=YPOSITION)
        self.showturtle()

    def move(self):
        xcor = self.xcor() - 5
        self.goto(xcor, self.ycor())

    def randompos(self):
        self.goto(self.xcor(), YPOSITION)
