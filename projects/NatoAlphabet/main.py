import pandas

try:
    alphabet = pandas.read_csv("files/nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("ERROR: Missing config file")
    exit()

user_input = input("Enter a word: ")

'''
# Version 1
def convert_letter(letter):
    """ Gets the nato letter for any letter """
    try:
        return alphabet[alphabet.letter == letter.upper()].values[0][1]
    except IndexError:
        return letter


translated = [convert_letter(letter) for letter in user_input]
response = " ".join(translated)

print(f"Here's your word translated: {response}")
'''



# Version 2

nato_alphabet = {letter: code for (_, letter, code) in alphabet.itertuples()}

def translate_letter(letter):
    """Gets the NATO letter for the input"""
    try:
        return nato_alphabet[letter]
    except KeyError:
        return letter
    

response = [translate_letter(letter.upper()) for letter in user_input]

print(f"Here's version 1 result: {''.join(response)}")
