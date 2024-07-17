# Stock Trading Alerts

This project is designed to monitor the stock price of a specific company and send alerts when there is a significant
change. The project integrates with various APIs to fetch stock data, retrieve news articles, and send SMS notifications

## Overview

This project consists of three main steps:

Stock Price Monitoring: Using the Alpha Vantage API to check if the stock price has increased or decreased by 5% between
yesterday and the day before yesterday.
News Retrieval: Using the News API to fetch the first three news articles related to the company when a significant
price change is detected.
SMS Notifications: Using the Twilio API to send an SMS message with the percentage change and news articles to your
phone number.

## Set up

1. Get the needed API Keys:

    - Sign up for an API key at Alpha Vantage.
    - Sign up for an API key at News API.
    - Sign up for an API key at Twilio.

2. Create a .env file in the project directory and add your API keys and phone number:

```env
STOCK_API_KEY="STOCK_API_KEY"
NEWS_API_KEY="NEWS_API_KEY"
```

## Usage

Run the script to monitor the stock price and send alerts:

```bash
python main.py
```

The script performs the following steps:

Fetches the stock price data for the specified stock symbol using the Alpha Vantage API.
Checks if the price has changed by 5% between yesterday and the day before yesterday.
If a significant change is detected, fetches the top 3 news articles related to the company using the News API.
Sends an SMS message with the percentage change and news articles using the Twilio API.