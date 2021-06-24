from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle((-370, 0))
paddle2 = Paddle((370, 0))
ball = Ball()

game_on = True

screen.listen()

screen.onkey(fun=paddle2.move_up, key="Up")
screen.onkey(fun=paddle2.move_down, key="Down")
screen.onkey(fun=paddle.move_up, key="w")
screen.onkey(fun=paddle.move_down, key="s")


while game_on:
    time.sleep(0.1)
    screen.update()

    ball.move()

    # Detect screen's edges
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.yball_pos *= -1

    # Detect paddless
    if paddle.distance(ball) <= 24 or paddle2.distance(ball) <= 24:
        ball.xball_pos *= -1

screen.exitonclick()
