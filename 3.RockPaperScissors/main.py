import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
your_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 3 > your_pick >= 0:
    print(hands[your_pick])
    computer_pick = random.randint(0, 2)
    print("Computer chose:")
    print(hands[computer_pick])
    if your_pick == computer_pick:
        print("Draw")
    elif (your_pick == 0 and computer_pick == 2) or (your_pick == 1 and computer_pick == 0) or (
            your_pick == 2 and computer_pick == 1):
        print("You win!")
    else:
        print("You lose.")
else:
    print("You typed invalid number, you lose.")
