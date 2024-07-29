# SpeedTest and Twitter Bot

This project uses Selenium to create a bot that checks your internet connection speed using Speedtest and tweets a
complaint to your ISP if the speed is below a certain threshold.

## Table of Contents

1. [Overview](#overview)
2. [Setup](#setup)
3. [Usage](#usage)
4. [How it works](#how-it-works)
5. [Contributing](#contributing)

## Overview

The SpeedTest and Twitter Bot allows you to:

- Automatically check your internet connection speed.
- Tweet a complaint to your ISP if the speed is below a specified threshold.
-

## Setup

1. Set up a Twitter account to get your credentials. Add your credentials to the .env
   file.
2. Create a .env file in the project directory and add your environment variables:

```env
TWITTER_USERNAME="..."
TWITTER_PASSWORD="..."
TWITTER_EMAIL="..."
```

## Usage

Run the script to start the bot:

```bash
python main.py
```

## How It Works

1. **Set Up WebDriver:** sets up Selenium WebDriver for Chrome and opens the Speedtest website.
2. **Perform Speed Test:** uses Selenium to interact with the Speedtest website and retrieve the download and upload
   speeds.
3. **Check Speed and Creates Tweet:** Compares the speeds with the specified thresholds. If the speeds are below the
   thresholds, uses Twitter to post a tweet a complaint to your ISP.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

