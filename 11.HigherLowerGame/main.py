from art import logo, vs
from game_data import data
from random import choice
from replit import clear


def draw_random_account(second_account):
    """Returns random account from list and checks if it's different that second_account."""
    account = choice(data)
    if account == second_account:
        account = choice(data)
    return account


def check(answer, account_a, account_b):
    """Checks if you provided correct answer."""
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    if (a_followers > b_followers and answer == 'a') or (a_followers < b_followers and answer == 'b'):
        return True
    else:
        return False


def game():
    print(logo)
    is_correct = True
    score = 0
    account_a = choice(data)
    while is_correct:
        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(vs)
        account_b = draw_random_account(account_a)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        if check(answer, account_a, account_b):
            score += 1
            account_a = account_b
            print(f"You're right! Current score: {score}.")
        else:
            is_correct = False
            print(f"Sorry, that's wrong. Final score: {score}.")


game()
