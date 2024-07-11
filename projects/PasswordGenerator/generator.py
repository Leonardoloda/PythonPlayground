from random import choice


class Generator:

    def __init__(self):
        self.LOWERCASE_LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        self.UPPERCASE_LETTERS = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.NUMBERS = [str(i) for i in range(10)]
        self.SYMBOLS = [chr(i) for i in range(ord('!'), ord('.') + 1)]

    def get_random_lowercase(self):
        return choice(self.LOWERCASE_LETTERS)

    def get_random_uppercase(self):
        return choice(self.UPPERCASE_LETTERS)

    def get_random_symbol(self):
        return choice(self.SYMBOLS)

    def get_random_number(self):
        return str(choice(self.NUMBERS))

    def generate_password(self, n_lowercase_letters=8, n_uppercase_letters=1, n_numbers=4, n_symbols=1):
        password = ""
        password_len = n_lowercase_letters + n_uppercase_letters + n_numbers + n_symbols

        password_generators = [self.get_random_lowercase, self.get_random_uppercase, self.get_random_symbol,
                               self.get_random_number]

        lower_counter = 0
        upper_counter = 0
        numbers_counter = 0
        symbols_counter = 0

        for i in range(1, password_len + 1):
            generator = choice(password_generators)

            new_character = generator()

            if new_character in self.UPPERCASE_LETTERS:
                upper_counter += 1
            elif new_character in self.LOWERCASE_LETTERS:
                lower_counter += 1
            elif new_character in self.NUMBERS:
                numbers_counter += 1
            elif new_character in self.SYMBOLS:
                symbols_counter += 1

            if new_character in self.LOWERCASE_LETTERS and lower_counter >= n_lowercase_letters:
                password_generators.remove(self.get_random_lowercase)

            if new_character in self.UPPERCASE_LETTERS and upper_counter >= n_uppercase_letters:
                password_generators.remove(self.get_random_uppercase)

            if new_character in self.NUMBERS and numbers_counter >= n_numbers:
                password_generators.remove(self.get_random_number)

            if new_character in self.SYMBOLS and symbols_counter >= n_symbols:
                password_generators.remove(self.get_random_symbol)

            password += new_character

        return password
