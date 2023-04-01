import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

correct_world = False

while not correct_world:
    word = input("Enter a word: ").upper()
    try:
        translation = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        correct_world = True
        print(translation)
