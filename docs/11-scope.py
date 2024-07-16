# python creates a scope for each function
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function {enemies}")


# global variables can only be changed with the global keyword
def increase_global_enemies():
    # This is highly not recommended
    global enemies
    enemies *= 0
    print(f"enemies inside function: {enemies}")


# Instead use function returns
def increase_enemy_number(enemies):
    return enemies + 1


enemies = increase_enemy_number(enemies)

increase_global_enemies()
print(f"enemies increase from inside the function {enemies}")


def print_global_enemies():
    print(f"Global enemies {enemies}")


print_global_enemies()

# However there's no block scope, just scope for functions
game_level = 3
enemies = []

if game_level < 5:
    new_enemy = "Zombie"

print(new_enemy)

# Number guessing game

from random import randint

UPPER_LIMIT = 100
TITLE = '''
███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████  ██    ██ ███████ ███████ ███████ ███████ ██████  
████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██       ██    ██ ██      ██      ██      ██      ██   ██ 
██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██   ███ ██    ██ █████   ███████ ███████ █████   ██████  
██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██    ██ ██    ██ ██           ██      ██ ██      ██   ██ 
██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████   ██████  ███████ ███████ ███████ ███████ ██   ██ 
'''


def generate_random_number(limit):
    return randint(0, limit)


def welcome_screen():
    print(TITLE)
    print("Welcome to number guessing game")
    print("I'm thinking of a number between 0 and 100")
    print("Your job is to guess the number")


def difficulty_selection():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if choice == "easy":
        return 10
    elif choice == "hard":
        return 5
    else:
        print("You're not funny bro")
        return 1


def start_game():
    welcome_screen()

    attempts = difficulty_selection()
    number = generate_random_number(limit=UPPER_LIMIT)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess == number:
            print("You've guessed the number, you win")
            break
        elif guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")

        attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose")

    if input("Do you wanna start a new game?") == "yes":
        start_game()


start_game()
