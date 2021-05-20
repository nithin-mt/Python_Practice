from art import logo

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


def total():
    quarter = n_quarter*0.25
    dimes = n_dimes*0.1
    nickels = n_nickels*0.05
    pennies = n_pennies*0.01
    total_amount = quarter+dimes+nickels+pennies
    return total_amount


def remaining_resources(u_choice):
    global MENU
    if u_choice == "espresso":
        resources['water'] -= MENU[u_choice]['ingredients']['water']
        resources['coffee'] -= MENU[u_choice]['ingredients']['coffee']
        print(resources)

        for i in resources:
            if resources[i] <= 0:
                return 1

    else:

        resources['water'] -= MENU[u_choice]['ingredients']['water']
        resources['milk'] -= MENU[u_choice]['ingredients']['milk']
        resources['coffee'] -= MENU[u_choice]['ingredients']['coffee']
        print(resources)

        for i in resources:
            if resources[i] <= 0:
                return 1


def change():
    global got_coffee
    got_coffee = False
    if remaining_resources(user_choice) == 1:
        print(f"No sufficient resources")

    else:
        if user_choice == "espresso":
            if total() >= 1.5:
                print(f"Here's your change : {round(total() - 1.5, 2)}")
                print("Here's your Espresso! ☕ Enjoy!")

            elif total() < 1.5:
                print(f"Sorry that's not enough money. Money refunded.")
        if user_choice == "latte":
            if total() >= 2.5:
                print(f"Here's your change : {round(total() - 2.5, 2)}")
                print("Here's your Latte! ☕ Enjoy!")

            elif total() < 2.5:
                print("Sorry that's not enough money. Money refunded.")
        if user_choice == "cappuccino":
            if total() >= 3.0:
                print(f"Here's your change : {round(total() - 3.0, 2)}")
                print("Here's your Cappuccino! ☕ Enjoy!")

            elif total() < 3.0:
                print("Sorry that's not enough money. Money refunded.")


got_coffee = False
print(logo)

while not got_coffee:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice == "off":
        got_coffee = True
    else:
        if user_choice == "report":
            print(resources)

    remaining_resources(user_choice)
    print("Please insert coins.")
    n_quarter = float(input("How many quarters> : "))
    n_dimes = float(input("How many dimes? : "))
    n_nickels = float(input("How many nickels? : "))
    n_pennies = float(input("How many pennies? : "))

    change()
