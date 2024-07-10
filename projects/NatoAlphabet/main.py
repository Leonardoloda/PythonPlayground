import pandas

alphabet = pandas.read_csv("files/nato_phonetic_alphabet.csv")

user_input = input("Enter a word: ")

# Version 1

convert_letter = lambda letter: alphabet[alphabet.letter == letter.upper()].values[0][1]

translated = [convert_letter(letter) for letter in user_input]
response = " ".join(translated)

print(f"Here's your word translated: {response}")

# Version 2

nato_alphabet = {letter: code for (_, letter, code) in alphabet.itertuples()}

converted = [nato_alphabet[letter.upper()] for letter in user_input]
converted_response = " ".join(converted)

print(f"Here's version 1 result: {converted_response}")

# Version 3

nato_alphabet = {row.letter: row.code for (_, row) in alphabet.iterrows()}

converted = [nato_alphabet[letter.upper()] for letter in user_input]
converted_response = " ".join(converted)

print(f"Here's version 1 result: {converted_response}")
