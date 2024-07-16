# Conditionals
'''
  if condition:
    do this
  else:
    do this
'''
'''
height = int(input("What's your height? "))

MINIMUM_HEIGHT = 160

if height >= MINIMUM_HEIGHT:
  print("You can ride the rollercoaster!")

  bill = 0

  age = int(input("What's your age? "))

  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bil = 7
    print("Please pay $7.")
  else:
    bill = 12
    print("Please pay $12.")

  photo = input("Do you want a photo taken? Y or N. ")

  if photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else: 
  print("You can't ride the rollercoaster!")
'''

# Comparison Operators

# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to
# and
# or

# Treasure island game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


def start_game():
    direction = input(
        "You're at a cross road. Where do you want to go? Type 'left' or 'right'\n"
    )

    if direction == "right":
        print("Game over")
        return

    action = input(
        "You come to a lake. There is an island in the middle of the lake. Do you want to 'wait' for a boat or 'swim' across?"
    )

    if action == "swim":
        print("Game over")
        return

    door = input(
        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n"
    )

    if door == "red" or door == "blue":
        print("Game over")
        return

    print("You win!")


start_game()
