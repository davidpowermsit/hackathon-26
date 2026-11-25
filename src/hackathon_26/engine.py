from hackathon_26.web import Wikibee

MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"


def matching_anchor_text(wiki_page: list[tuple[str, str]], keywords: list[str]) -> list[tuple[str, str]]:
    return [
        (link, anachor_text)
        for link, anachor_text in wiki_page
        if any(k.lower() == anachor_text.lower() for k in keywords)
    ]


def search_page_for_keyword(
    client: Wikibee, wiki_page: list[tuple[str, str]], keywords: list[str]
) -> tuple[str, list[tuple[str, str]]] | None:
    matches = matching_anchor_text(wiki_page, keywords)
    if matches:
        page_title, wiki_page = client.go_to_page(matches[0][0])
        return page_title, wiki_page
    return None


def run(client: Wikibee, target: str, keywords: list[str]) -> tuple[bool, int]:
    page_title, wiki_page = client.go_to_page(MAIN_PAGE)

    steps: int = 0
    while True:
        result = search_page_for_keyword(client, wiki_page, keywords)
        if result is None:
            # Lose
            return False, steps
        page_title, wiki_page = result
        steps += 1
        if page_title.lower() in keywords:
            keywords.remove(page_title.lower())

        # Win check
        if page_title.lower() == target.lower():
            return True, steps
