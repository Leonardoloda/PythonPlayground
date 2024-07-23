from bs4 import BeautifulSoup


class WebsiteScraper:
    def __init__(self, html: str) -> None:
        self._soup = BeautifulSoup(html, "html.parser")

    def format_score(self, score: str) -> int:
        return int(score.split(" ")[0])

    def get_all_news(self) -> list:
        title_tags = self._soup.select(".titleline > a")[:-1]
        score_tags = self._soup.select(".score")

        news = []

        for i in range(len(title_tags)):
            news.append({
                "title": title_tags[i].text,
                "score": self.format_score(score_tags[i].text),
                "link": title_tags[i].get("href")
            })

        return news
