from os import getenv

from dotenv import load_dotenv

from billboard_client import BillboardClient
from billboard_scraper import BillboardScraper
from spotify_client import SpotifyClient

load_dotenv()

SPOTIFY_CLIENT_ID = getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

print("Welcome to your Billboard Top 100 Playlist Creator!")
"""
year = int(input("What year were you born in? "))
month = int(input("What month were you born in? "))
day = int(input("What day were you born in? "))
"""

year = 1996
month = 3
day = 16

playlist_name = f"{year}-{month}-{day} Billboard 100"
playlist_description = f"Top 100 songs from Billboard for {month}/{day}/{year}."

client = BillboardClient()
spotify_client = SpotifyClient(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)

client.build_url(year=year, month=month, day=day)


def fetch_hot_songs():
    html = client.fetch_website()

    scraper = BillboardScraper(html=html)

    songs = scraper.get_songs()

    client.reset_url()

    return songs


def search_songs_uris(songs: list) -> list:
    songs_uris = []

    for song in songs:
        search_result = spotify_client.search_song(song)
        song_uri = search_result["tracks"]["items"][0]["uri"]
        print(f"Fount song_uri for {song_uri} or {song}")
        songs_uris.append(song_uri)

    return songs_uris


def save_playlist(songs_uris):
    playlist = spotify_client.create_playlist(name=playlist_name, description=playlist_description)
    playlist_id = playlist["id"]

    spotify_client.add_songs_to_playlist(playlist_id, songs_uris)

    return playlist


songs = fetch_hot_songs()
print(f"{len(songs)} songs scrapped from billboard.")

songs_uris = search_songs_uris(songs)
print(f"{len(songs_uris)} songs found in spotify.")

created_playlist = save_playlist(songs_uris)
print(
    f"Your new playlist was created in {created_playlist["name"]}, visit at {created_playlist["external_urls"]["spotify"]}.")
