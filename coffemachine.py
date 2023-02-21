# from menu import MENU
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. (DONE) Print report of all coffee-machine resources.


# TODO: 2. (DONE)  Check resources sufficient to make drink order.

# TODO: (DONE) 3. Make function that calculates change inserted.

# TODO: 4. (DONE)Make function to make coffee and update resources.

# TODO: 5. (DONE)Make "off-switch".

#

# PROJECT START

# Variables
money = 0
user_order = ""
change = 0
empty_machine = False
is_on = True

# Functions


def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return True
        else:
            return False

def coins_insert():
    """A function that calculates the value of USD coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    value = ((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies))
    return value


def give_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def take_order():
    user_order = input("Please select 'latte', 'cappuccino' or 'espresso': ")
    return user_order


def return_change(change):
    if drink['cost'] > change:
        print("Sorry, you have not inserted enough change. ")
        print(f"Your change is ${change}")
    else:
        print(f"Returning money. ${change}")
    change = 0
    return change

def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


#Machine starts here:

while is_on == True:
    choice = input("Please select 'latte', 'cappuccino' or 'espresso': ")
    if choice == "off":
        is_on = False
        break
    elif choice == "report":
        give_report()
    else:
        drink = MENU[choice]
        change = coins_insert()
        empty_machine = enough_resources(drink['ingredients'])
        if empty_machine is True:
            return_change(change)
        if choice == "latte" and empty_machine is False:
            if change >= MENU['latte']['cost']:
                make_drink(choice, drink['ingredients'])
                change -= MENU['latte']['cost']
                if change > MENU['latte']['cost']:
                    print(f"Your change is ${change}")
                money += float(MENU['latte']['cost'])
            else:
                change = return_change(change)
        elif choice == "espresso" and empty_machine is False:
            empty_machine = enough_resources(drink['ingredients'])
            if change >= MENU['espresso']['cost']:
                make_drink(choice, drink['ingredients'])
                change -= MENU['espresso']['cost']
                if change > MENU['espresso']['cost']:
                    print(f"Your change is ${change}.")
                money += float(MENU['espresso']['cost'])
        elif choice == "cappuccino" and empty_machine is False:
            empty_machine = enough_resources(drink['ingredients'])
            if change >= MENU['cappuccino']['cost']:
                make_drink(choice, drink['ingredients'])
                change -= MENU['cappuccino']['cost']

                if change > MENU['cappuccino']['cost']:
                    print(f"Your change is ${change}.")
                money += MENU['cappuccino']['cost']
