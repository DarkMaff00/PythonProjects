MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    total = (quarter * 0.25) + (dime * 0.1) + (nickle * 0.05) + (penny * 0.01)
    return total


def check_money(coffee_cost, user_money):
    if coffee_cost > user_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += coffee_cost
        print(f"Here is ${round(user_money - coffee_cost, 2)} in change.")
        return True


def remove_ingredients(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]


def produce_coffee(coffee_name):
    coffee = MENU[coffee_name]
    enough_resources = check_resources(coffee['ingredients'])
    if enough_resources:
        provided_money = process_coins()
        enough_money = check_money(coffee['cost'], provided_money)
        if enough_money:
            remove_ingredients(coffee['ingredients'])
            print(f"Here is your {prompt} ☕. Enjoy!")
            return coffee['cost']


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


stop_machine = False

while not stop_machine:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "report":
        print_report()
    elif prompt == "off":
        stop_machine = True
    else:
        produce_coffee(prompt)
