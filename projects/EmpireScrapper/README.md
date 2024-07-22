# Empire Scrapper

This project uses Beautiful Soup (bs4) to scrape the list of the top 100 movies from the Empire Online website. The
scraped data is then saved into a CSV file.

## Table of Contents

1. [Overview](#overview)
2. [Usage](#usage)
3. [How it works](#how-it-works)
4. [Example Output](#example-output)
5. [Features](#features)
6. [Contributing](#contributing)

## Overview

The Empire Scraper helps you:

- Scrape the list of the top 100 movies from the Empire Online website.
- Extract movie titles using a selector for the h3 tag with a specific class.
- Save the extracted data into a CSV file for easy access and analysis.

## Usage

Run the script to scrape the top 100 movies and save them into a CSV file:

```bash
python main.py
```

## How It Works

**1. Make a Request:**
Sends a request to the specified URL to fetch the HTML content of the page.

**2. Parse HTML:**
Uses Beautiful Soup to parse the HTML content and find all h3 tags with the specified class.

**3. Extract Movie Titles:**
Extracts the text from each h3 tag and stores the movie titles in a list.

**4. Save to CSV:**
Writes the movie titles along with their ranks into a CSV file.

## Example Output

After running the script, you'll have a CSV file named top_100_movies.csv with the following structure:

```csv
position,movie
1,The Shawshank Redemption
2,The Godfather
3,The Dark Knight
```

## Features

- **Web Scraping:** Uses Beautiful Soup to scrape data from a website.
- **CSV Export:** Saves the scraped data into a CSV file for easy access and analysis.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.
