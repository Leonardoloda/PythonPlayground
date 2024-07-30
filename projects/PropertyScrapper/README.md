# Property Scrapper

This project uses web scraping to fetch property details from Zillow and automates filling out a Google Form for each
property using Selenium.

## Table of Contents

Overview
Setup
Usage
Features
Contributing

## Overview

The Zillow Property Scraper and Google Form Filler allows you to:

- Scrape property details from Zillow.
- Automatically fill out a Google Form with the scraped property details.

## Setup

1. Create a .env file in the project directory and add your environment variables:

```env
GOOGLE_FORM_URL=your_google_form_url
ZILLOW_URL=your_zillow_url
```

## Usage

Run the script to start scraping Zillow and filling out the Google Form:

```bash
python main.py
```

## How It Works

1. **Fetch Zillow Page Content:** the script fetches the HTML content from the Zillow URL.
2. **Initialize Bots:** the script initializes the ZillowBot with the fetched page content and the GoogleBot with the
   Google Form URL.
3. **Fetch Properties:** the script retrieves the list of properties from the Zillow page and prints the total number of
   properties found.
4. **Process Each Property:** the script processes each property by loading the Google Form page, filling the form with
   property details, and submitting the form.

## Example Output

After running the script, you'll see the progress of fetching and submitting properties:

```shell
Fetching Zillow page content...
Initializing ZillowBot...
Initializing GoogleBot...
Fetching properties from Zillow...
Found 10 properties.
Processing property 1 of 10: Property(price: $500,000, url: https://example.com/property1, address: 1234 Example St, City, Country)
Form submitted for property 1 of 10.
Processing property 2 of 10: Property(price: $600,000, url: https://example.com/property2, address: 5678 Example Ave, City, Country)
Form submitted for property 2 of 10.
...
All properties have been processed and submitted.
```

## Features

- **Web Scraping:** Scrapes property details from Zillow.
- **Automated Form Filling:** Automatically fills out a Google Form with the scraped property details.
- **Progress Tracking:** Tracks and prints the progress of processing and submitting each property.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.