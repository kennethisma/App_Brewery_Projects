from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_car()
        self.speed = 0.1

    def create_car(self):
        for _ in range(15):
            car = Turtle("square")
            car.color(self.random_colors())
            car.speed("slowest")
            car.hideturtle()
            car.shapesize(stretch_wid=1, stretch_len=2.5)
            car.penup()
            car.goto(x=random.randint(-420, 420), y=random.randint(-230, 230))
            car.showturtle()
            self.cars.append(car)

    def move(self):
        for item in self.cars:
            xcor = item.xcor() - 5
            item.goto(xcor, item.ycor())

    def random_colors(self):
        R = random.random()
        G = random.random()
        B = random.random()
        return (R, G, B)

    def detect_edge(self):
        for item in self.cars:
            if item.xcor() < -420:
                item.goto(x=420,
                          y=random.randint(-230, 230))

    def increase_speed(self):
        self.speed *= 0.9

    def cars_next_level(self):
        for item in self.cars:
            item.goto(x=random.randint(-420, 420),
                      y=random.randint(-230, 230))
