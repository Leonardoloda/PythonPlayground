from service import random_word
from constants import TITLE, HANGMAN, DEFEAT, VICTORY
from replit import clear

lives = 6
player_name = ""
answer = list(random_word)

guessed_letters = ["_"] * len(answer)
failed_letters = []

def find_all(str, char):
    indexes = []
    for i in range(len(str)):
      if i == char:
        indexes.append(i)

def print_word(word):
    print(" ".join(word))

def print_hangman(lives):
    print(HANGMAN[6 - lives])
  
    print_word(guessed_letters)

    print(f'''
      These letters are no in the word:
      {" ".join(failed_letters)}
    ''')

def mark_answer(letter):
    for i in range(len(answer)):
        if letter == answer[i]:
            guessed_letters[i] = letter
    
def guess_letter():
    global lives
    letter = input("Guess a letter: ").lower()
    if letter in answer:
      mark_answer(letter)    
    else:
      lives -= 1
      failed_letters.append(letter)
      
def clear_screen():
    clear()

def is_victorious():
  return "".join(answer) == "".join(guessed_letters)
  
def welcome():
  global player_name
  
  print(f'''
    {TITLE}

    Welcome to Hangman!
  ''')
  player_name = input("What is your name? ")
  
if not player_name:
  welcome()

while lives > 0 and not(is_victorious()):
  clear_screen()
  
  print_hangman(lives)
  guess_letter()
  
if lives == 0:
  clear_screen()
  print(f'''
    {DEFEAT}

    The word was {"".join(answer)}
  ''')
  

if is_victorious():
  print(VICTORY)