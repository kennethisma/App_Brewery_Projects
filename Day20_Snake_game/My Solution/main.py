
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoarde
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("Black")
screen.title("Welcome to the Snake game")
screen.listen()


snake = Snake()
food = Food()
score_board = ScoreBoarde()
game_on = True
score = 0
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.rand_location()
        score_board.add_point()
        snake.add_tale()

    # Detect collision with wall
    if snake.touch_wall():
        score_board.end_game()
        game_on = False
    # Detect collision with tail
    elif snake.collision_tail():
        score_board.end_game()
        game_on = False

    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_right, key="Right")
    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_down, key="Down")

screen.exitonclick()
