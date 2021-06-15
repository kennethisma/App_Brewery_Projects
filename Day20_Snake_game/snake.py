from turtle import Turtle, distance, xcor

# Constants
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        square_start_position = 0
        for _ in range(3):
            square = Turtle(shape="square")
            square.color("White")
            square.penup()
            square.goto(x=square_start_position, y=0)
            square_start_position -= 20  # Decreases the x coordinates
            self.squares.append(square)

    def move(self):
        # Animate the snake
        for squ in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[squ - 1].xcor()
            new_y = self.squares[squ - 1].ycor()
            self.squares[squ].goto(new_x, new_y)
        self.head.forward(20)

    def add_tale(self):
        x_pos = self.squares[2].xcor()
        y_pos = self.squares[2].ycor()
        tale = Turtle(shape="square")
        tale.color("White")
        tale.penup()
        tale.goto(x_pos, y_pos)
        self.squares.append(tale)

    def touch_wall(self):
        x_cor = self.head.xcor()
        y_cor = self.head.ycor()

        if x_cor > 300 or x_cor < -300:
            return True
        elif y_cor > 300 or y_cor < -300:
            return True
        else:
            return False

    def collision(self):
        collision = False
        for item in range(2, len(self.squares)):
            t_x = self.squares[item].xcor()
            t_y = self.squares[item].ycor()
            if self.head.distance(t_x, t_y) < 20:
                collision = True
        return collision

    def turn_up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def turn_right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def turn_left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def turn_down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
