import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

PLAYER1_X = 350
PLAYER2_X = -350
SCORE_LIMIT = 5

screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player1 = Paddle(PLAYER1_X)
player2 = Paddle(PLAYER2_X)
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

game_is_on = True
speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(player1) < 50 and ball.xcor() > 325 or ball.distance(player2) < 50 and ball.xcor() < -325:
        ball.paddle_bounce()
        speed *= 0.9

    if ball.xcor() > 390:
        ball.next_round()
        scoreboard.update_score("p2")
        speed = 0.1

    if ball.xcor() < -390:
        ball.next_round()
        scoreboard.update_score("p1")
        speed = 0.1

    if scoreboard.p2_score == SCORE_LIMIT:
        game_is_on = False
        scoreboard.end_game("p2")

    if scoreboard.p1_score == SCORE_LIMIT:
        game_is_on = False
        scoreboard.end_game("p1")

screen.exitonclick()
