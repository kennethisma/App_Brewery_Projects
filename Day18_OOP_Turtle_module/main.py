###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
from turtle import Turtle, Screen
import random


TURTLE_SIZE = 20
screen = Screen()
screen.colormode(255)
tim = Turtle()

colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178,

                                                                                                                                                                                                         149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def dots_in_row():
    for item in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)


tim.penup()
tim.hideturtle()
tim.goto(-300, -250)  # Move the turtle in the lower left corner

column = -200

tim.showturtle()

for row in range(10):
    dots_in_row()
    tim.setx(-300)  # Sets the x coordinate of the turtle
    tim.sety(column)  # Sets the y coordinate of the turtle
    column += 50

screen.exitonclick()
