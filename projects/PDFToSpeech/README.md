### README for PDF-to-Speech Application

# PDF-to-Speech Application

## Description

The PDF-to-Speech Application is a Python-based tool that reads the contents of a PDF file and converts it into speech.
It uses OpenAI's text-to-speech (TTS) API to generate speech from the text extracted from the PDF.

## Requirements

Make sure to install the python-dotenv library to load environment variables from a .env file. Add your OpenAI API key
in the .env file.

### Install dotenv:

```bash
pip install python-dotenv
```

### Set up .env file:

Create a .env file in the root directory and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. **PDF File Location:**

   Ensure the PDF file is located in the `assets` folder with the name `offer.pdf` or modify the file path in the code
   to match your PDF's location.

2. **Run the Application:**

   After running the application, the text from the PDF will be extracted and converted into speech, which will be saved
   as `speech.mp3` in the current directory.

3. **Listen to the Speech:**

   Open the `speech.mp3` file with any media player to listen to the generated speech.

## Contributing

Feel free to create a PR if you'd like to contribute!

## License

Free to use.
