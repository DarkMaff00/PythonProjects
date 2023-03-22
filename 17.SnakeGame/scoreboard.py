from turtle import Turtle

FONT = ("Arial", 14, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.print_score()

    def print_score(self):
        self.write(f"Score:  {self.score}", align="center", font=FONT)

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align="center", font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.print_score()
