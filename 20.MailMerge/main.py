
PLACEHOLDER = "[name]"

names = []
with open("./Input/Names/invited_names.txt") as data:
    lines = data.readlines()
    for line in lines:
        names.append(line.strip())

with open("./Input/Letters/starting_letter.txt") as template:
    letter_template = template.read()
    for name in names:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
            new_letter.write(letter_template.replace(PLACEHOLDER, name))
