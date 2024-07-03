from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
cashier = MoneyMachine()


def create_coffee():
    print(f"Here you can create {menu.get_items()}")

    recipe = input("Please choose a recipe: ")
    drink = menu.find_drink(order_name=recipe)

    if not drink:
        print(f"Sorry {recipe} is not a valid recipe!")

    is_craftable = machine.is_resource_sufficient(drink=drink)

    if not is_craftable:
        print(f"Sorry, there's not enough materials to make {drink}")

    purchased = cashier.make_payment(cost=drink.cost)

    if not purchased:
        print(f"Sorry {drink} is not enough money!")

    machine.make_coffee(drink)


def start_machine():
    keep_ongoing = True

    while keep_ongoing:
        print("Welcome to your coffee machine!")

        option = int(input("""
            What would you like to do?
        
                1. Craft a coffee
                2. Check the current inventory
                3. Exit the machine
        
        """))

        match option:
            case 1:
                create_coffee()
            case 2:
                machine.report()
            case 3:
                keep_ongoing = False
            case _:
                print(f"Sorry {option} is not a valid option!")


start_machine()
