
from turtle import Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("Black")
screen.title("Welcome to the Snake game")
screen.listen()


snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_right, key="Right")
    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_down, key="Down")
