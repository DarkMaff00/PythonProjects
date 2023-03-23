from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)
        self.setposition(x, 0)

    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)

