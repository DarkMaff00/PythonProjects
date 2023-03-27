import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
translation = [alphabet_dict[letter] for letter in word]
print(translation)
