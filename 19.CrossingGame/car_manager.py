from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
HEADING = 180


class CarManager:

    def __init__(self):
        self.cars = []
        self.pace = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.penup()
        car.setposition(310, random.randint(-250, 250))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(HEADING)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.pace)

    def speed_up(self):
        self.pace += MOVE_INCREMENT

    def crash(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
