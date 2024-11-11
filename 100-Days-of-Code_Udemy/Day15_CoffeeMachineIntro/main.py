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


MONEY = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

MACHINE_PROFIT = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_report():
    """Prints report of available resources and profit in machine."""
    for item in resources:
        unit = "ml"
        if item == "coffee":
            unit = "g"
        print(f"{item.title()}: {resources[item]}{unit}")
    print(f"Money: ${MACHINE_PROFIT}")


def check_resources(requested_drink):
    """Checks if resources available for requested drink"""
    enough = True
    for res, val in requested_drink["ingredients"].items():
        if resources[res] < val:
            enough = False
            print(f"Sorry there is not enough {res}.")
    return enough


def process_coins():
    """Processes amount of money entered by user"""
    user_money = 0
    print("Please insert coins.")
    for coin, value in MONEY.items():
        user_money += int(input(f"How many {coin}?: ")) * value
    print("")
    return user_money


def make_drink(drink, money_in):
    """Deducts used resources from available in machine, adds profit and provides drink."""
    global MACHINE_PROFIT
    MACHINE_PROFIT += drink["cost"]
    change = round(money_in - drink["cost"], 2)
    if change != 0:
        print(f"Here is ${change} dollars in change.")
    for res, val in drink["ingredients"].items():
        resources[res] -= val


def coffee_machine(request):
    print("")
    """Runs the coffee machine. If entered drink not in Menu, exits."""
    if request in MENU:
        drink = MENU[request]
        if check_resources(drink):
            inserted_money = process_coins()
            if inserted_money < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                print("")
            else:
                make_drink(drink, inserted_money)
                print(f"Here is your {request} ☕. Enjoy!")
                print("")
    else:
        print("Sorry, that drink is not available on this machine.")
        print("")


machine_on = True
while machine_on:
    user_input = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        get_report()
    else:
        coffee_machine(user_input)
