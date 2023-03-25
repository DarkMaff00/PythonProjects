from turtle import Turtle

FONT = ("Arial", 14, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score:  {self.score} \tHigh Score: {self.high_score}", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.sety(0)
    #     self.write("GAME OVER", align="center", font=FONT)

    def update(self):
        self.score += 1
        self.print_score()
