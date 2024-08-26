# Morse Code Translator

## Description

The Morse Code Translator is a Python application that converts regular text into Morse code. It leverages
the `MorseHandler` class to handle Morse code logic and the `Translator` class to manage the translation process.

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Input the text:**

   When prompted, enter the text you want to translate to Morse code.

3. **View the Morse code:**

   The translated Morse code will be displayed on the console.

## Code Explanation

### `MorseHandler.py`

This module is expected to contain the `MorseHandler` class, which handles the logic for translating characters or
strings into Morse code.

### `Translator.py`

This module contains the `Translator` class, which utilizes the `MorseHandler` to convert normal text into Morse code.
The `Translator` class likely serves as an interface to manage the translation process.

### `main.py`

This is the entry point for the application. It initializes the `MorseHandler` and `Translator` objects, takes user
input, and outputs the Morse code translation.

## Features

- **Text-to-Morse Conversion:** Converts regular text into Morse code using a simple command-line interface.
- **Modular Design:** The application is designed with separate modules for handling Morse code logic and managing the
  translation process.
