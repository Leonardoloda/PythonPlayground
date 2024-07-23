from bs4 import BeautifulSoup
from pyperclip import copy


class BillboardScraper:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        copy(self.soup.prettify())

    def get_songs(self) -> list:
        songs_tags = self.soup.select("li > #title-of-a-story")

        songs = [song.text.strip() for song in songs_tags]

        return songs
