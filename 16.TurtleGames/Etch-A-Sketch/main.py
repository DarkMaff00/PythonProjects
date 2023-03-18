# You can draw by pressing W - to move forward, S - backward, D - to turn right, A - turn left and C - to restart.
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forward():
    pen.forward(10)


def move_backward():
    pen.backward(10)


def move_clockwise():
    pen.right(10)


def move_anticlockwise():
    pen.left(10)


def start():
    pen.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkeypress(key="a", fun=move_anticlockwise)
screen.onkey(key="c", fun=start)

screen.exitonclick()
