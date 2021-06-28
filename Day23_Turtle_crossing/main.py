from hashlib import new
from turtle import Screen, Turtle
from playertur import PlayerTur
from cars import Car
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
# screen.tracer(0)


tim = PlayerTur()
car = Car()
screen.onkey(fun=tim.move_up, key="Up")
screen.onkey(fun=tim.move_down, key="Down")
screen.onkey(fun=tim.move_left, key="Left")
screen.onkey(fun=tim.move_right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
