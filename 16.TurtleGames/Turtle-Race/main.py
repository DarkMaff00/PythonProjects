from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

turtle_space = 0
for color in colors:
    runner = Turtle(shape="turtle")
    runner.color(color)
    runner.penup()
    runner.goto(x=-230, y=-100 + turtle_space)
    turtle_space += 40
    turtles.append(runner)

if user_bet:
    is_race_on = True

while is_race_on:
    for runner in turtles:
        if runner.xcor() > 230:
            is_race_on = False
            winning_color = runner.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        runner.forward(rand_distance)

screen.exitonclick()
