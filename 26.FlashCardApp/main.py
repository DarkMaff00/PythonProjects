from tkinter import *
import pandas as pd
import random

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- PICK WORD ------------------------------- #
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pd.read_csv("./data/french_words.csv")

translation = data.to_dict(orient="records")
current_card = {}


def pick_word():
    global current_card, timer
    root.after_cancel(timer)
    current_card = random.choice(translation)
    card.itemconfig(title, text="French", fill="black")
    card.itemconfig(word, text=f"{current_card['French']}", fill="black")
    card.itemconfig(card_image, image=front_image)
    timer = root.after(3000, flip_card)


# ---------------------------- DELETE WORDS THAT YOU KNOW ------------------------------- #

def delete_word():
    try:
        pick_word()
        translation.remove(current_card)
    except (IndexError, ValueError):
        card.itemconfig(title, text="No more cards in this deck", fill="black")
        card.itemconfig(word, text="Reload the app", fill="black")


def save_words():
    new_words = pd.DataFrame(translation)
    new_words.to_csv('./data/words_to_learn.csv', index=False)


# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    card.itemconfig(card_image, image=back_image)
    card.itemconfig(title, text="English", fill="white")
    card.itemconfig(word, text=f"{current_card['English']}", fill="white")


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = root.after(3000, flip_card)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="./images/card_back.png")
front_image = PhotoImage(file="./images/card_front.png")
card_image = card.create_image(400, 263, image=front_image)
title = card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

red_image = PhotoImage(file="./images/wrong.png")
red_button = Button(image=red_image, highlightthickness=0, bd=0, command=pick_word)
red_button.grid(column=0, row=1)

green_image = PhotoImage(file="./images/right.png")
green_button = Button(image=green_image, highlightthickness=0, bd=0, command=delete_word)
green_button.grid(column=1, row=1)

pick_word()

root.mainloop()

save_words()
