from bs4 import BeautifulSoup

# As working with any file, first we need to get the content
HTML_PATH = "files/website.html"


def get_file_content(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


html = get_file_content(HTML_PATH)

# You need to create a soup by passing the content and the parser
soup = BeautifulSoup(html, 'html.parser')

# You have the entire document
print(soup.prettify())

# Now you can get any attribute
title = soup.title
print(title)

# You can also get attributes
print(soup.title.string)

# You can query for any kind of tag
print(soup.a)

# Instead of just finding one, you can fetch ultiple
all_anchor_tags = soup.find_all("a")
print(all_anchor_tags)

# you can also use the name
all_p = soup.find_all(name="p")
print(all_p)

# You can lop on it to fetch the needed info
for a in all_anchor_tags:
    # You can get attributes by using the .get
    print("Link", a.get('href'))

# You can combine multiple tags to query

heading = soup.find(name="h1", id="name")
print("heading", heading)

# Instead of using class, you need to use the class_
section_heading = soup.find(name="h3", class_="heading")
print("Section heading", section_heading)

# You can also query bry drilling down into the element or use any css selectors
company_url = soup.select_one("p a")

all_headings = soup.select(".heading")
print("All headings", all_headings)

# You can also get the html from a remote site by requesting it
from requests import get

NEWS_WEBSITE = "https://news.ycombinator.com/"

response = get(NEWS_WEBSITE)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
