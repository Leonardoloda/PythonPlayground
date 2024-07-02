from math import floor

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

COINS = {
    "dollar": 1,
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
    "dollar": 1
}


def welcome_screen():
    """Shows a welcome screen."""
    print("Welcome to Coffee Machine!")


def menu():
    """Displays the menu."""
    print("""
        Welcome to your coffee machine, please choose what you wanna do
    
            1. Create a new order
            2. Visualize inventory
            3. Exit the program
        
    """)

    return input("Enter your option: ")


def show_inventory(inventory):
    """Displays the inventory."""

    print(f"""
        Currently the coffee machine has the next amount of resources:
        
        1. Water: {inventory["water"]}
        2. Milk: {inventory["milk"]}
        3. Coffee: {inventory["coffee"]}
        
        Thanks for checking
    """)


def check_availability(ingredients, resources):
    """Check if the coffee machine has the needed amount of resources to make the recipe"""
    if ingredients["water"] >= resources["water"]:
        return False
    elif ingredients["milk"] >= resources["milk"]:
        return False
    elif ingredients["coffee"] >= resources["coffee"]:
        return False

    return True


def get_desired_order(order):
    match order:
        case "1":
            return "espresso"
        case "2":
            return "latte"
        case "3":
            return "cappuccino"


def prepare_coffee(inventory, menu, order):
    """Prepares the coffee based on the user selection. 1 for espresso, 2 for latte, 3 for cappuccino"""
    recipe = get_desired_order(order)

    creatable = check_availability(ingredients=menu[recipe]["ingredients"], resources=inventory)

    if not creatable:
        print("Sorry, there's no enough ingredients to process your order ")
        return None

    adjust_inventory(inventory, water=menu[recipe]["ingredients"]["water"],
                     milk=menu[recipe]["ingredients"]["milk"],
                     coffee=menu[recipe]["ingredients"]["coffee"])

    return recipe


def adjust_inventory(inventory, water=None, milk=None, coffee=None):
    if water:
        inventory["water"] -= water

    if milk:
        inventory["milk"] -= milk

    if coffee:
        inventory["coffee"] -= coffee


def calculate_budget(menu, order):
    recipe = get_desired_order(order)

    print(f"Your {recipe} will be ${menu[recipe]['cost']}")

    budget = {}

    for key in COINS:
        coins_amount = input(f"How many {key} would you like?: ")
        budget[key] = int(coins_amount)

        total = get_budget_total(budget)

        if total >= menu[recipe]["cost"]:
            print("That's enough money")
            break

    change = total - menu[recipe]["cost"]

    print(f"Your change is ${change:.2f}")

    if change == 0:
        print("There's no change needed")
        return True
    elif change < 0:
        print("That's not enough money, here's your refund")
        return False
    elif change > 0:
        give_change(change)
        return True


def give_change(desired_amount):
    print("About to give money, prepare yourself")

    while desired_amount > 0:
        for key in COINS:
            print("remaining", desired_amount)
            if desired_amount % COINS[key] == 0:
                number_coins = desired_amount / COINS[key]
                print(f"Here you go, {number_coins} {key}s")

                return number_coins
            else:
                number_coins = floor(desired_amount / COINS[key])
                print(f"Here you go, {number_coins} {key}s")
                desired_amount -= floor(desired_amount / COINS[key]) * COINS[key]


def get_budget_total(budget):
    """Returns the calculated total budget"""
    total = 0

    for key in budget:
        total += budget[key] * COINS[key]

    return total


def create_order():
    """Creates a new order."""
    print("""
        1. espresso
        2. latte
        3. cappuccino
    """)

    order = input("What would you like to order? ")
    affordable = calculate_budget(menu=MENU, order=order)

    if not affordable:
        print("That's not enough money")
        return None

    coffee = prepare_coffee(menu=MENU, inventory=resources, order=order)

    if coffee:
        print(f"Here's your coffee f{coffee}")
    else:
        print("Sorry, no coffee is available")


def main():
    welcome_screen()

    keep_operating = True

    while keep_operating:
        option = menu()

        match option:
            case "1":
                create_order()
            case "2":
                show_inventory(resources)
            case "3":
                keep_operating = False
            case _:
                print(f"Sorry {option}, isn't a valid option")

    print("Thank you for using Coffee Machine!")


main()
