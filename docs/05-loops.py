# Loops

anime = [
    "Attack on Titan", "One Piece", "Naruto", "Demon Slayer",
    "My Hero Academia"
]

# You can iterate through lists using for loops

p = ""

for item in anime:
    print(item)

# You can also iterate through a range
for number in range(1, 10):
    print(number)

ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

print("Printing ordinals and index: ")

# You can also use enumerate to have a tracking index, if you don't assing an index, starts from 0
for index, ordinal in enumerate(ordinals):
    print(f"{index + 1}. {ordinal}")

# Same thing can be done with the start argument
for index, ordinal in enumerate(ordinals, start=1):
    print(f"{index}. {ordinal}")

# It can be done with any type, strings
word = "abcdefghijklmnopqrst"

for index, letter in enumerate(word, start=1):
    print(f"{index}. {letter}")

person = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 30,
}

# or dicts
for index, key in enumerate(person, start=1):
    print(f"{index}. {key} is {person[key]}")

# Password generator

import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z"
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to your password generator")

n_letters = int(input("How many letters would you like in your password? "))
n_numbers = int(input("How many numbers would you like in your password? "))
n_symbols = int(input("How many symbols would you like in your password? "))

password = ""
password_len = n_letters + n_numbers + n_symbols


def get_random_letter():
    return random.choice(letters)


def get_random_symbol():
    return random.choice(symbols)


def get_random_number():
    return str(random.choice(numbers))


password_generators = [get_random_letter, get_random_symbol, get_random_number]

letters_counter = 0
numbers_counter = 0
symbols_counter = 0

for i in range(1, password_len + 1):
    generator = random.choice(password_generators)

    new_character = generator()

    if new_character in letters:
        letters_counter += 1
    elif new_character in numbers:
        numbers_counter += 1
    elif new_character in symbols:
        symbols_counter += 1

    if new_character in letters and letters_counter >= n_letters:
        password_generators.remove(get_random_letter)

    if new_character in numbers and numbers_counter >= n_numbers:
        password_generators.remove(get_random_number)

    if new_character in symbols and symbols_counter >= n_symbols:
        password_generators.remove(get_random_symbol)

    password += new_character

print(password)
