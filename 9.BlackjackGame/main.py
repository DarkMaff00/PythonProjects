# Blackjack Project
from art import logo
import random
from replit import clear


def draw_card(deck):
    """Draws random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = random.choice(cards)
    if drawn_card == 11 and sum(deck) > 10:
        deck.append(1)
    else:
        deck.append(drawn_card)


def count_score(deck):
    """Counts score of deck and checks if there is a BlackJack."""
    score = sum(deck)
    if score == 21 and len(deck) == 2:
        return 0
    else:
        return score


def check_results(your_cards, computer_cards):
    """
    Continue game by drawing next cards or stop it.
    Checks if you already lose.
    """
    print(f"\tYour cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")
    if count_score(your_cards) < 22:
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
            draw_card(your_cards)
            check_results(your_cards, computer_cards)


def rules(user_score, computer_score):
    """Prints final result of this game."""
    if user_score == computer_score:
        print("Draw 🙃")
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif user_score == 0:
        print("Win with a Blackjack 😎")
    elif user_score > 21:
        print("You went over. You lose 😤")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")


def game():
    """Conducts the game."""
    print(logo)
    your_cards = []
    computer_cards = []
    # Draw first two cards.
    for _ in range(2):
        draw_card(your_cards)
    # Draw all cards for computer
    # If sum of cards values is less than 17, draw another one.
    while sum(computer_cards) < 17:
        draw_card(computer_cards)
    # If user or computer have Blackjack this game.
    if count_score(your_cards) != 0 and count_score(computer_cards) != 0:
        check_results(your_cards, computer_cards)
    print(f"\tYour final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    rules(count_score(your_cards), count_score(computer_cards))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    game()
