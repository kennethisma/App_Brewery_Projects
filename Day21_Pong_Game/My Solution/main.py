from turtle import Screen, left, right
from paddle import Paddle
from ball import Ball
from screenboard import ScreenLine, ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle((370, 0))
paddle2 = Paddle((-370, 0))
ball = Ball()
line_scr = ScreenLine()
right_score = ScoreBoard((40, 250))
left_score = ScoreBoard((-60, 250))
game_on = True

screen.listen()

screen.onkey(fun=paddle.move_up, key="Up")
screen.onkey(fun=paddle.move_down, key="Down")
screen.onkey(fun=paddle2.move_up, key="w")
screen.onkey(fun=paddle2.move_down, key="s")


while game_on:
    time.sleep(0.1)
    screen.update()

    ball.move()

    # Detect screen's edges
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.yball_pos *= -1

    # Detect paddless
    if ball.distance(paddle) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.xball_pos *= -1
        ball.xball_pos *= 1.1

    # Detecting score
    if ball.xcor() > 410:
        left_score.add_score()
        screen.ontimer(fun=ball.home(), t=1000)
        ball.random_position()
    elif ball.xcor() < -410:
        right_score.add_score()
        screen.ontimer(fun=ball.home(), t=1000)
        ball.random_position()

    if left_score.win() or right_score.win():
        game_on = False

screen.exitonclick()
