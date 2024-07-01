# Functions can receive arguments
def greet(pronoun, person):
  print(f"Hello {pronoun} {person}")


# Arguments are based on the position of the argument
greet("Sir", "Leo")

# You can also use keyword arguments
greet(person = "Leo", pronoun = "Sir")

from math import floor

MIN_CODE = 97
MAX_CODE = 122
LETTERS = 25

TITLE = '''
   _____ _____ _____  _    _ ______ _____  
  / ____|_   _|  __ \| |  | |  ____|  __ \ 
 | |      | | | |__) | |__| | |__  | |__) |
 | |      | | |  ___/|  __  |  __| |  _  / 
 | |____ _| |_| |    | |  | | |____| | \ \ 
  \_____|_____|_|    |_|  |_|______|_|  \_\

'''

def encrypt(message, shift):
  encrypted_message = ""
  message = message.lower()

  print("shift", shift)

  for letter in message:
    if not letter.isalpha():
      encrypted_message += letter
      continue

    encrypted_message += chr((ord(letter) + shift - 97) % 26 + 97)

  return encrypted_message

def decrypt(message, shift):
  decrypted_message = ""

  for letter in message:
    if not letter.isalpha():
      decrypted_message += letter
      continue
      
    decrypted_message += chr((ord(letter) - shift - 97) % 26 + 97)

  return decrypted_message

print(TITLE)
print("Welcome to Caesar Cipher")

keep_ciphering = True

while keep_ciphering == True:
  print("Would you like to encrypt or decrypt a message?")
  choice = input("Type 'e' for encrypt or 'd' for decrypt: ")

  if choice == "e":
    message = input("Enter the message you would like to encrypt: ")
    shift = int(input("Enter the shift: "))
    print(f"Your encrypted message is: {encrypt(message, shift)}\n")
  elif choice == "d":
    message = input("Enter the message you would like to decrypt: ")
    shift = int(input("Enter the shift: "))
    print(f"Your decrypted message is: {decrypt(message, shift)}\n")
  else:
    print("Invalid choice")


  print("Would you like to keep ciphering?")
  continue_ciphering = input("Type 'y' for yes or 'n' for no: ")
  if continue_ciphering == "n":
    keep_ciphering = False