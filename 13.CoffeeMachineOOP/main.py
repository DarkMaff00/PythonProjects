from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_working = True
menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

while is_working:
    prompt = input(f"what would tou like? ({menu.get_items()}): ").lower()
    if prompt == "off":
        is_working = False
    elif prompt == "report":
        machine.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(prompt)
        if machine.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                machine.make_coffee(coffee)
