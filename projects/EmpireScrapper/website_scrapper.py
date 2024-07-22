from bs4 import BeautifulSoup


class WebsiteScrapper:
    def __init__(self, html: str) -> None:
        self._soup = BeautifulSoup(html, 'html.parser')

    def get_all_headings(self, tag: str) -> list:
        return [heading.text for heading in self._soup.find_all(tag)]
