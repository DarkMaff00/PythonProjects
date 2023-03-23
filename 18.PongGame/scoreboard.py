from turtle import Turtle

FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.print_score()

    def print_score(self):
        self.goto(100, 200)
        self.write(f"P1:{self.p1_score}", align="center", font=FONT)
        self.goto(-100, 200)
        self.write(f"P2:{self.p2_score}", align="center", font=FONT)

    def update_score(self, player):
        if player == "p1":
            self.p1_score += 1
        elif player == "p2":
            self.p2_score += 1
        self.clear()
        self.print_score()

    def end_game(self, player):
        self.goto(0, 0)
        self.write(f"{player} won!", align="center", font=FONT)
