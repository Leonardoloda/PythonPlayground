import random

def clear():
    print("")

# How much risk the house takes
HOUSE_TOLERANCE = 5

title = """
 #####  #        ##    ####  #    #      #   ##    ####  #    # 
 #    # #       #  #  #    # #   #       #  #  #  #    # #   #  
 #####  #      #    # #      ####        # #    # #      ####   
 #    # #      ###### #      #  #        # ###### #      #  #   
 #    # #      #    # #    # #   #  #    # #    # #    # #   #  
 #####  ###### #    #  ####  #    #  ####  #    #  ####  #    # 
"""

cards = [{
    "display": """
     ___  
    |A  | 
    |   | 
    |  A| 
     ‾‾‾  """,
    "value": 11
}, {
    "display": """
   ___  
  |2  | 
  |   | 
  |  2| 
   ‾‾‾  """,
    "value": 2
}, {
    "display": """
   ___  
  |3  | 
  |   | 
  |  3| 
   ‾‾‾  """,
    "value": 3
}, {
    "display": """
   ___  
  |4  | 
  |   | 
  |  4| 
   ‾‾‾  """,
    "value": 4
}, {
    "display": """
   ___  
  |5  | 
  |   | 
  |  5| 
   ‾‾‾  """,
    "value": 5
}, {
    "display": """
   ___  
  |6  | 
  |   | 
  |  6| 
   ‾‾‾  """,
    "value": 6
}, {
    "display": """
   ___  
  |7  | 
  |   | 
  |  7| 
   ‾‾‾  """,
    "value": 7
}, {
    "display": """
   ___  
  |8  | 
  |   | 
  |  8| 
   ‾‾‾  """,
    "value": 8
}, {
    "display": """
   ___  
  |9  | 
  |   | 
  |  9| 
   ‾‾‾  """,
    "value": 9
}, {
    "display": """
   ___  
  |10 | 
  |   | 
  | 10| 
   ‾‾‾  """,
    "value": 10
}, {
    "display": """
   ___  
  |J  | 
  |   | 
  |  J| 
   ‾‾‾  """,
    "value": 10
}, {
    "display": """
   ___  
  |Q  | 
  |   | 
  |  Q| 
   ‾‾‾  """,
    "value": 10
}, {
    "display": """
   ___  
  |K  | 
  |   | 
  |  K| 
   ‾‾‾  """,
    "value": 10
}]

print(title)
print("Welcome to blackjack")


def create_players(player_number):
    players = {}

    for i in range(player_number):
        name = input("What's the name of player " + str(i + 1) + "? ")

        players[name] = {
            "hand": [],
        }

    # Add the house as a player
    players["House"] = {
        "hand": [],
    }

    return players


def deal(players):
    for player in players:
        players[player]["hand"].append(random.choice(cards))
        players[player]["hand"].append(random.choice(cards))

    return players


def show_cards(player):
    cards = []

    for card in player["hand"]:
        cards.append(card['display'])

    print(" ".join(cards))


def show_table(players):
    print("Time to reveal all the player's cards")

    for player in players:
        print(f"Player {player} has the next cards: \n")
        show_cards(players[player])
        print("\n")


def request_cards(player):
    wants_more_cards = True

    while wants_more_cards == True:
        show_cards(player)
        player_choice = input("\nWould you like another card? ")
        clear()

        wants_more_cards = player_choice == 'y'

        if wants_more_cards == False:
            clear()
            return

        player["hand"].append(random.choice(cards))
        print("You've been dealt another card")

        if check_score(player) > 21:
            print("You've gone over the limit, skipping to next player \n")
            return

    clear()


def deel_house(house):
    print(f"The house is playing")

    while check_score(house) < 21 - HOUSE_TOLERANCE:
        house["hand"].append(random.choice(cards))

        print("The house has been dealt a card")
        show_cards(house)

        if check_score(house) > 21:
            print("The house has gone over the limit \n")

    print("The house has stopped playing \n")


def ask_table(players):
    for player in players:
        if player == "House":
            deel_house(players[player])
        else:
            print(f"Now is your turn {player}, these are your cards \n")
            request_cards(players[player])


def check_score(player):
    score = 0
    for card in player["hand"]:
        score += card["value"]

        if card["value"] == 11 and (score > 21 or score + card["value"] > 21):
            score -= 10

    return score


def check_winner(players):
    highest_score = 0
    winners = []
    highest = []

    for player in players:
        current_player = players[player]

        if check_score(current_player) > 21:
            print(f"{player} has gone over the limit")
        elif check_score(current_player) == 21:
            winners.append(player)
        elif check_score(current_player) > highest_score:
            highest_score = check_score(current_player)
            highest = [player]
        elif check_score(current_player) == highest_score:
            highest.append(player)

    if len(winners) > 0:
        print(f"{' '.join(winners)} have won the game")
    elif len(highest) > 1:
        print("No one has a 21, looking for the highest scores")
        print(f"The winners are {', '.join(highest)}")
    elif len(highest) == 1:
        print(f"{highest[0]} has won the game")


clear()


def play_game():
    player_number = int(input("How many players are there? "))
    players = create_players(player_number)

    deal(players)

    ask_table(players)
    show_table(players)
    check_winner(players)


keep_playing_game = True

while keep_playing_game == True:
    play_game()

    keep_playing_game = input("Would you like to keep playing? ") == "y"
