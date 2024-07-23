from requests import get

from constants import *


class BillboardClient:
    def __init__(self) -> None:
        self._url = BILLBOARD_TOP_PAGE

    def fetch_website(self):
        return get(self._url).text

    def reset_url(self):
        self._url = BILLBOARD_TOP_PAGE

    def build_url(self, year: int, month: int, day: int) -> str:
        url_with_year = self._url.replace(YEAR_PATTERN, f"{year:02d}")
        url_with_month = url_with_year.replace(MONTH_PATTERN, f"{month:02d}")
        url_with_day = url_with_month.replace(DAY_PATTERN, f"{day:02d}")

        self._url = url_with_day
