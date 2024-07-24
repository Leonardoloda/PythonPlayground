# Amazon Price Tracker

This project tracks the price of a product on Amazon. It scrapes the product page for the current price and sends an
email alert if the price is lower than your target price.

## Table of Contents

1. Overview
2. Setup
3. Usage
4. Features
5. Contributing

## Overview

The Amazon Price Tracker allows you to:

- Scrape the price of a specified product from Amazon.
- Check if the current price is lower than your target price.
- Send an email alert when the price drops below your target price.

## Setup

1. Set up an email account to send notifications.
2. Create a .env file in the project directory and add your email credentials:

```env
EMAIL=your_email
PASSWORD=your_email_password
TARGET_PRICE=your_target_price
PRODUCT_URL=the_amazon_product_url
```

## Usage

Run the script to start tracking the price of the specified product:

```bash
python main.py
```

## Example Output

After running the script, you'll get an email alert if the price drops below your target price:

**Subject:**

*Your Samsung 990 EVO SSD 1TB, PCIe Gen 4x4, Gen 5x2 M.2 2280 NVMe Internal Solid State Drive, Speeds Up to 5,000MB/s,
Upgrade Storage for PC Computer, Laptop, MZ-V9E1T0B/AM, Black is at a new record low*

**Body:**

*Samsung 990 EVO SSD 1TB, PCIe Gen 4x4, Gen 5x2 M.2 2280 NVMe Internal Solid State Drive, Speeds Up to 5,000MB/s,
Upgrade Storage for PC Computer, Laptop, MZ-V9E1T0B/AM, Black is currently at $84.99*

## Features

- **Web Scraping:** Uses Beautiful Soup to scrape the product price from Amazon.
- **Price Checking:** Compares the current price with the target price.
- **Email Alerts:** Sends an email alert when the price drops below the target price.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.