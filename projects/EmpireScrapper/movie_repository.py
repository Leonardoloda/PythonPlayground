import pandas


class MovieRepository:
    def __init__(self, path: str) -> None:
        self._path = path
        self._movies = pandas.DataFrame({
            "movie": []
        })

    def add_movie(self, movie: str) -> None:
        self._movies.loc[0] = [movie]
        self._movies.index = self._movies.index + 1
        self._movies.sort_index()

    def save(self) -> None:
        self._movies.to_csv(self._path, index_label="position")
