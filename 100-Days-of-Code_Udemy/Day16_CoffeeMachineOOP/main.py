from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if drink != None:
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
