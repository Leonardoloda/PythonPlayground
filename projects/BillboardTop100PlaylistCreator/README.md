# Billboard Top 100 Playlist Creator

This project fetches the Billboard Top 100 songs for a user-specified year, scrapes the Billboard page to get the songs,
and uses the Spotify API to create a playlist with those songs.

## Table of Contents

1. [Overview](#overview)
2. [Setup](#setup)
3. [Features](#features)
3. [Usage](#usage)
4. [Contributing](#contributing)

## Overview

The BillboardTop100PlaylistCreator allows you to:

1. Fetch the Billboard Top 100 songs for a specific year.
2. Scrape the Billboard website to get the list of songs.
3. Create a Spotify playlist with the scraped songs.

## Setup

1. Sign up for an API key at Spotify for Developers.
2. Obtain your Spotify User ID, Client ID, and Client Secret.
3. Ensure access to the Billboard website for scraping.

4. Create a .env file in the project directory and add your Spotify API credentials:

```env
SPOTIFY_CLIENT_ID="SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET="SPOTIFY_CLIENT_ID"
```

## Features

- **Billboard Scraping:** Fetches the top 100 songs for a specified year from the Billboard website.
- **Spotify Playlist Creation:** Creates a playlist on Spotify with the fetched songs.
- **Automated Song Addition:** Automatically adds the fetched songs to the created Spotify playlist.

## Usage

Run the script to fetch the Billboard Top 100 songs and create a Spotify playlist:

```bash
python main.py
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.