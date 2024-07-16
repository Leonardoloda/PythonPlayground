import random

randomInt = random.randrange(0, 10)

print(randomInt)

# YOu can import modules from other files

# If it was in another file
# from module import MODULE_VALUE

MODULE_VALUE = 2.973

print(MODULE_VALUE)

randomFloat = random.random() * 5

print("Float", randomFloat)

# Arrays work pretty much the same
cities = ["London", "Paris", "Berlin"]

print("First city", cities[0])

# However you can use negative indexes to start from the last element
print("Last city", cities[-1])

# You can't add elements out of bounds
# cities[3] = "Madrid"

# You can add elements to the end of the array
cities.append("Madrid")

print("Cities with a new city", cities)

# You can extend list with new arrays
new_cities = ["Moscow", "Rome"]
cities.extend(new_cities)

print(cities)

fruits = [
    "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
    "Pears"
]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

options = ['rock', 'paper', 'scissors']

print("Welcome to rock paper scissors")

player_input = input(
    "Choose rock, paper or scissors: Enter a number from 0 to 2\n")

player_choice = options[int(player_input)]
computer_choice = random.choice(options)

print(f"You chose {player_choice}")
print(f"Computer chose {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win")
else:
    print("You lose")
