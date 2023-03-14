print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? PLN"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = (tip_percentage / 100) + 1
payment = (total_bill / number_of_people) * tip_percentage
print(f"Each person should pay: PLN{'{:.2f}'.format(payment)}")
