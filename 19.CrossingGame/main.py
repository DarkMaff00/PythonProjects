import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
generate_car = 0
while game_is_on:
    generate_car += 1
    time.sleep(0.1)
    screen.update()

    if generate_car == 5:
        cars.generate_car()
        generate_car = 0
    cars.move()

    if player.finish():
        scoreboard.level_up()
        cars.speed_up()

    if cars.crash(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
