from Constants import MORSE_CODE_DICT

from LanguageHandler import LanguageHandler


class MorseHandler(LanguageHandler):

    def translate(self, text: str) -> str:
        translated = ""

        for letter in text:

            letter = letter.upper()

            if letter in MORSE_CODE_DICT:
                translated += MORSE_CODE_DICT[letter]
                translated += " "

        return translated;
