import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")


def draw_state(state_name):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    state = data[data.state == state_name]
    x_cor = int(state.x)
    y_cor = int(state.y)
    pen.setposition(x_cor, y_cor)
    pen.write(state_name, align="center", font=("Arial", 8, "normal"))


def check_state(state_name):
    if state_name in data.state.to_list():
        return True


screen = turtle.Screen()
screen.setup(width=730, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
score = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f" {score}/50 Guess the State",
                                    prompt="What's another state's name ?").title()

    if answer_state == "Exit":
        states_to_learn = data.state[~data.state.isin(guessed_states)]
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if check_state(answer_state) and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        draw_state(answer_state)
        score += 1

    if score == 50:
        game_is_on = False

