from turtle import Turtle


class Snake:
    def __init__(self):
        self.squares = []
        self.square_width = 0
        for _ in range(3):
            square = Turtle(shape="square")
            square.color("White")
            square.penup()
            square.goto(x=self.square_width, y=0)
            self.square_width -= 20  # Decreases the x coordinates
            self.squares.append(square)

    def move(self):
        # Animate the snake
        for squ in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[squ - 1].xcor()
            new_y = self.squares[squ - 1].ycor()
            self.squares[squ].goto(new_x, new_y)
        self.squares[0].forward(20)

    def turn_up(self):
        self.squares[0].setheading(90)

    def turn_right(self):
        self.squares[0].setheading(0)

    def turn_left(self):
        self.squares[0].setheading(180)

    def turn_down(self):
        self.squares[0].setheading(270)
