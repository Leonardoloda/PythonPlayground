from random import choice

from replit import clear

from art import logo, vs
from game_data import data


def welcome_screen():
    print(logo)


def pick_contestant(available):
    contestant = choice(available)

    available.remove(contestant)

    return contestant


def show_vs(main, opponent):
    print(
        f"Compare A: {main['name']}, a {main['description']}, from {main['country']}"
    )
    print(vs)
    print(
        f"Compare B: {opponent['name']}, a {opponent['description']}, from {opponent['country']} \n"
    )


def show_score(score):
    print(f"Score: {score} \n")


def get_winner(main, opponent):
    if main['follower_count'] > opponent['follower_count']:
        return "A"
    else:
        return "B"


def get_result(main, opponent):
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    winner = get_winner(main, opponent)

    if answer == winner:
        return True
    else:
        return False


def start_game():
    clear()
    welcome_screen()

    main = pick_contestant(data)
    score = 0

    is_victory = True

    while is_victory == True and len(data) > 0:
        show_score(score)
        opponent = pick_contestant(data)

        show_vs(main=main, opponent=opponent)

        is_victory = get_result(main, opponent)

        if is_victory == True:
            clear()
            score += 1

    print(f"Your final score was {score}")

    if is_victory == True:
        print("Congratulations, you've won the game")

    if is_victory == True and len(data) == 0:
        print("Congratulations, you've won the game, you're la reata")

    if is_victory == False:
        print("You've lost the game")

        restart = input(
            "Do you wanna star a new game? Type 'y' for yes or 'n' for no: ")

        if restart == "y":
            start_game()


start_game()
