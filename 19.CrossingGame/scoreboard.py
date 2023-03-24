from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.setposition(-240, 260)
        self.hideturtle()
        self.print_level()

    def print_level(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.print_level()

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=FONT)
