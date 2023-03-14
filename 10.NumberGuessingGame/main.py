# Number Guessing Game Objectives:

from art import logo
import random


def game(number_of_attempts, correct_number):
    guessed = False
    while number_of_attempts > 0 and not guessed:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        number_of_attempts -= 1
        if user_number < correct_number:
            print("Too low.")
        elif user_number > correct_number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {correct_number}.")
            guessed = True

        if number_of_attempts == 0:
            print("You've run out of guesses, you lose.")
        elif user_number != correct_number:
            print("Guess again.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_level == 'easy':
    attempts = 10
else:
    attempts = 5

drawn_number = random.randint(1, 100)
game(attempts, drawn_number)
