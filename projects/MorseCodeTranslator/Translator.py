from LanguageHandler import LanguageHandler


class Translator:
    def __init__(self, language_handler: LanguageHandler):
        self._language_handler = language_handler

    def translate(self, word: str) -> str:
        return self._language_handler.translate(word)
