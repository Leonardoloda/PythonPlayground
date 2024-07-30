## Instagram Follower Bot

This project uses Selenium to create a bot that logs into Instagram and follows each account that follows a specified account.

## Table of Contents

Overview
Setup
Usage
Features
Contributing

## Overview

The Instagram Follower Bot allows you to:

- Automatically log into Instagram.
- Follow each account that follows a specified account.

## Setup

1. Create a .env file in the project directory and add your Instagram credentials:

```env
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
INSTAGRAM_URL="https://www.instagram.com/"
INSTAGRAM_PROFILE=target_account_username
```

## Usage

Run the script to start the bot:

```bash
python main.py
```

## How It Works

1. Set Up WebDriver:
   - Sets up Selenium WebDriver for Chrome and navigates to Instagram's login page.
2. Log Into Instagram:
   - Uses Selenium to enter your Instagram credentials and log into your account.
3. Follow Followers:
   - Navigates to the target account's followers list.
   - Iterates through the list and follows each account.

## Features

- **Automated Instagram Login:** Uses Selenium to log into Instagram.
- **Automated Following:** Follows each account that follows a specified account.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.
