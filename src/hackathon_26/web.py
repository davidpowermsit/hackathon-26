import httpx
from bs4 import BeautifulSoup

headers = {"User-Agent": "MSITSEPHACK26 (davidpowermsit@gmail.com)"}
MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"


def go_to_page(url: str) -> tuple[str, list[tuple[str, str]]]:
    with httpx.Client(headers=headers, follow_redirects=True) as client:
        response = client.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    title_tag = soup.title
    page_title = title_tag.get_text(strip=True) if title_tag else ""
    wiki_page = [
        (str(a["href"]), a.get_text(strip=True))
        for a in soup.find_all("a", href=True)
        if str(a["href"]).startswith("https://en.wikipedia.org/wiki/")
    ]

    return page_title, wiki_page


title, links = go_to_page(MAIN_PAGE)
print(title)
print(len(links), " Links")
