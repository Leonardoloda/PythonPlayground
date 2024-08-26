from MorseHandler import MorseHandler
from Translator import Translator

morse_handler = MorseHandler()
translator = Translator(language_handler=morse_handler)

normal_text = input("Enter your text: ")

morse_text = translator.translate("Leo")

print(f"The result is {morse_text}")
