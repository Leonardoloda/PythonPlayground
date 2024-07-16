# Dictionaries
# A key value data structure
# Dictionaries are unordered

dict = {
    "key": "value",
    "second_key": "second_value",
}

print("Dict values", dict)
print("Values can be obtained with key", dict["key"])

# Can't access with the property
# print(dict.key) Wont work

nested = {
    "nest": {
        "nest": "1"
    }
}

print("Can be neste dictionaries", nested)

# You can add keys to a dictionary
nested["second_key"] = "second_value"

print(nested)

empty_dictionary = {}

print("Can also create empty dictionaries", empty_dictionary)

dictionary_with_keys = {
    "key": "value",
    "key2": "value2"
}

dictionary_with_keys = {}

print("Dictionary can be emptied", dictionary_with_keys)

dictionary_long = {
    "key": "value",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
    "key6": "value6",
    "key7": "value7",
    "key8": "value8",
    "key9": "value9",
    "key10": "value10",
    "key11": "value11",
    "key12": "value12",
    "key13": "value13",
    "key14": "value14",
    "key15": "value15",
    "key16": "value16",
    "key17": "value17",
    "key18": "value18",
    "key19": "value19",
    "key20": "value20",
    "key21": "value21",
    "key22": "value22",
    "key23": "value23",
    "key24": "value24",
}

# you can iterate with a for loop
for key in dictionary_long:
    print(key, dictionary_long[key])

# any type can be assigned as a value
dict_with_list = {
    "cities": ["Paris", "London", "Berlin"]
}

print(dict_with_list)

# Bidding application
from replit import clear

players = []
winner = {}

print("Welcome to your new bidding application")

has_more_players = True

while has_more_players == True:
    name = input("What's your name? ")
    bid = int(input("What's your bid? "))

    players.append({
        "name": name,
        "bid": bid
    })

    clear()

    has_more_players = input("Are there more players?") == "yes"


def bidding_winner(players):
    highest_bid = 0

    for player in players:
        if player["bid"] > highest_bid:
            highest_bid = player["bid"]
            winner = player["name"]

    return {"player": winner, "bid": highest_bid}


winner = bidding_winner(players)

print(f"Congratulations the winner is {winner}")
