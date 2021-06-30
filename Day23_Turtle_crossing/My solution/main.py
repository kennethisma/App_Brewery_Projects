from turtle import Screen
from playertur import PlayerTur
from cars import Car
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Welcome to turtle crossing game")
screen.listen()
screen.tracer(0)

tim = PlayerTur()
car = Car()
scoreboard = Scoreboard()


screen.onkey(fun=tim.move_up, key="Up")

game_on = True
while game_on:
    time.sleep(car.speed)
    screen.update()

    car.move()

    car.detect_edge()

    # Detect collision
    for rectangle in car.cars:
        if tim.distance(rectangle) < 28 and rectangle.xcor() >= 0:
            scoreboard.game_over()
            game_on = False

    # Detect when turtle touches the up edge
    if tim.ycor() > 280:
        car.cars_next_level()  # Start again with random position
        tim.home()
        car.increase_speed()
        scoreboard.next_level()
        time.sleep(0.5)


screen.exitonclick()
