# News Scrapper

This project scrapes all the news from YCombinator's Hacker News and returns the link to the highest-rated news article.

## Table of contents

1. [Overview](#overview)
2. [Usage](#usage)
3. [How it works](#how-it-works)
4. [Example output](#example-output)
5. [Features](#features)
6. [Contributing](#contributing)
7.

## Overview

The YCombinator News Scraper allows you to:

- Scrape news articles from YCombinator's Hacker News.
- Extract the highest-rated news article link.

## Usage

Run the script to scrape YCombinator's Hacker News and get the highest-rated news link:

```shell
python main.py
```

## How It Works

1. **Make a Request:** Sends a request to the YCombinator Hacker News website to fetch the HTML content of the page.
2. **Parse HTML:** Uses Beautiful Soup to parse the HTML content and find all news articles and their scores.
3. **Extract Highest-Rated Article:** Iterates through the articles and their scores to find the highest-rated news
   article and extracts the link of the highest-rated news article.

## Example Output

After running the script, you'll get the link to the highest-rated news article:

```shell
29 news fount, here's the top rated new
Open source AI is the path forward read more here: https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/
```

## Features

- Web Scraping: Uses Beautiful Soup to scrape news articles from YCombinator's Hacker News.
- Highest-Rated Article Extraction: Extracts and returns the link to the highest-rated news article.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.