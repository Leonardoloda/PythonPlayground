from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from constants import *


class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.sp = Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=SPOTIFY_REDIRECT_URL,
            scope=SPOTIFY_SCOPE))

    def search_song(self, song_name: str) -> str:
        return self.sp.search(q=song_name, limit=1, offset=0, type='track', market='US')

    def get_user_id(self) -> str:
        user = self.sp.current_user()

        return user["id"]

    def create_playlist(self, name: str, description: str) -> str:
        return self.sp.user_playlist_create(name=name, description=description, public=True, user=self.get_user_id())

    def add_songs_to_playlist(self, playlist_id: str, songs: list) -> str:
        self.sp.playlist_add_items(playlist_id=playlist_id, items=songs)
