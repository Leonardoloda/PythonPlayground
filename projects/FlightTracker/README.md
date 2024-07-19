# Flight Tracker

This project tracks a list of destinations from a Google Sheet and uses the Amadeus API to get the IATA code for each
city and the price for flights to those destinations in the next 6 months. If it finds a lower price, it updates the
price and triggers two alerts: a WhatsApp alert and an email alert for clients who subscribed via a Google form.

## Overview

The Flight Price Tracker helps you:

- Track flight prices for a list of destinations.
- Get the IATA code for each destination city using the Amadeus API.
- Monitor flight prices and update the lowest price found.
- Send alerts via WhatsApp and email when a lower price is found.

## Set up

1. Get the needed API Keys:

    - Sign up for an API key at Amadeus.
    - Sign up for an API key at Sheety.
    - Sign up for an API key at Twilio.

2. Create a .env file in the project directory and add your API keys and phone number:

```env
SHEETY_TOKEN=your_sheety_token
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret

ACCOUNT_SID=your_twilio_account_sid
SECRET_KEY=your_twilio_secret_key
AUTH_TOKEN=your_twilio_auth_token

EMAIL=your_email
PASSWORD=your_email_password

FLIGHTS_SHEET=flights
USERS_SHEET=users
ORIGIN=SYD
```

## Usage

Run the script to start tracking flight prices:

```bash
python main.py
```

## How It Works

### Load Data:

Loads the list of destinations from the flights sheet and the list of users from the users sheet.

### Get IATA Codes:

Uses the Amadeus API to get the IATA code for each city that doesn't have one.

### Track Flight Prices:

Uses the Amadeus API to get available flights from the origin city to each destination.
Checks for the lowest price and updates the Google Sheet if a new lower price is found.

### Send Alerts:

Triggers WhatsApp and email alerts to the subscribed users when a new lower price is found.

## Features

- **Flight Price Tracking:** Monitor and update the lowest flight prices for a list of destinations.
- **IATA Code Retrieval:** Automatically get the IATA code for each destination city using the Amadeus API.
- **WhatsApp and Email Alerts:** Send alerts to subscribed users when a new lower price is found.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.