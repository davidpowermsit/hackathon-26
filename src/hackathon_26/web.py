import httpx
from bs4 import BeautifulSoup


class Wikibee:
    def go_to_page(self, url: str) -> tuple[str, list[tuple[str, str]]]:
        headers = {"User-Agent": "MSITSEPHACK26 (davidpowermsit@gmail.com)"}
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
