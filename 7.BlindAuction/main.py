from art import logo
from replit import clear


is_more_people = True
bids = {}

print(logo)


def who_won(prices):
    winning_bid = 0
    winner = ""
    for bidder in prices:
        if prices[bidder] > winning_bid:
            winning_bid = prices[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${winning_bid}")


while is_more_people:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    result = input("Are there any other bidders? Type 'yes or no'.\n")
    if result == "yes":
        clear()
    else:
        is_more_people = False
        who_won(bids)
