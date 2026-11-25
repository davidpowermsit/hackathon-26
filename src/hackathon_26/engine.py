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
) -> tuple[str, str, list[tuple[str, str]]] | None:
    matches = matching_anchor_text(wiki_page, keywords)
    if matches:
        page_title, wiki_page = client.go_to_page(matches[0][0])
        return page_title, matches[0][1], wiki_page
    return None


def run(client: Wikibee, target: str, keywords: list[str]) -> tuple[bool, int]:
    page_title, wiki_page = client.go_to_page(MAIN_PAGE)

    steps: int = 0
    while True:
        result = search_page_for_keyword(client, wiki_page, keywords)
        if result is None:
            # Lose
            return False, steps
        page_title, anchor_text, wiki_page = result
        steps += 1
        # BUG: the anchor_text dosen't always match the new page's title
        if anchor_text.lower() in keywords:
            keywords.remove(anchor_text.lower())

        # Win check
        if target.lower() in page_title.lower():
            return True, steps
