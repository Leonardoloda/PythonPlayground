# Workout Tracker

Welcome to the Workout Tracker! This project helps you log your workouts by using the Nutritionix API to parse the
workout details you provide and then adding them to your Google Sheets using Sheety's API.

## Table of contents

1. [Overview](#overview)
2. [Set up](#set-up)
3. [Usage](#usage)
4. [How it works](#how-it-works)
5. [Features](#features)
6. [Contributing](#contributing)

## Overview

The Workout Tracker allows you to:

1. Input your workout details in natural language.
2. Use the Nutritionix API to parse and get detailed information about your workout.
3. Log your workout details into Google Sheets using the Sheety API.

## Set up

1. Sign up for an API key and App ID at Nutritionix.
2. Sign up for an API token at Sheety.
3. Create a .env file in the project directory and add your API keys and tokens:
    ```env
    API_KEY=your_nutritionix_api_key
    APP_ID=your_nutritionix_app_id
    SHEETY_TOKEN=your_sheety_token
    ```

## Usage

Run the script to start logging your workouts:

```bash
python main.py
```

You will be prompted to enter the details of your workout in natural language.

## How It Works

- **Input Workout:** The script prompts you to input your workout details in natural language.
- **Parse Workout:** The script uses the Nutritionix API to parse the workout details and get information such as
  exercise name, duration,
  and calories burned.
- **Log Workout:** The script logs the parsed workout details to your Google Sheets using the Sheety API.

## Features

- **Natural Language Processing:** Input workout details in natural language and get them parsed by the Nutritionix API.
- **Google Sheets Logging:** Automatically log your workout details into Google Sheets for easy tracking and management.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.