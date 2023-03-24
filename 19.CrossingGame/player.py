from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(UP)
        self.setposition(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.clear()
            self.setposition(STARTING_POSITION)
            return True
