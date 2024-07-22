from constants import *
from movie_repository import MovieRepository
from website_client import WebsiteClient
from website_scrapper import WebsiteScrapper

client = WebsiteClient(url=EMPIRE_TOP)
repo = MovieRepository(path=DATA_PATH)

html = client.fetch_page()

scrapper = WebsiteScrapper(html=html)

movies = scrapper.get_all_headings("h3")

for movie in movies:
    movie_title = " ".join(movie.split(" ")[1:])
    repo.add_movie(movie_title)

repo.save()
