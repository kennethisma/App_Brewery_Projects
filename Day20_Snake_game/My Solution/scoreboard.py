from turtle import Turtle, mode, position


class ScoreBoarde(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.stored_score()  # open the high_score.text and change the variable high_score value
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score} ", align="center",
                   font=("Arial", 15, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_score()

    def add_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()

    def stored_score(self):
        with open("high_score.txt", mode="r") as score_file2:
            news_score = score_file2.read()
            self.high_score = int(news_score)
