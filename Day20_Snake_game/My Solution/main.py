
from turtle import Screen, update
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


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Storing high score in high_score.txt
    with open("high_score.txt", mode="w") as score_file:
        score_file.write(str(score_board.high_score))

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.rand_location()
        score_board.add_point()
        snake.add_tale()

    # Detect collision with wall and  Detect collision with tail
    if snake.touch_wall() or snake.collision_tail():
        score_board.add_high_score()
        score_board.reset_score()
        snake.delete_tail()
        snake.start_again()

    screen.onkey(fun=snake.turn_up, key="Up")
    screen.onkey(fun=snake.turn_right, key="Right")
    screen.onkey(fun=snake.turn_left, key="Left")
    screen.onkey(fun=snake.turn_down, key="Down")


screen.exitonclick()
