from wikipediaapi import Wikipedia, WikipediaPage


def matching_titles(titles: list[str], keywords: list[str]) -> list[str]:
    return [t for t in titles if any(k.lower() == t.lower() for k in keywords)]


def search_page_for_keyword(
    client: Wikipedia, titles: list[str], keywords: list[str]
) -> tuple[WikipediaPage, list[str]] | None:
    matches = matching_titles(titles, keywords)
    if matches:
        page = client.page(matches[0])
        titles = list(page.links)
        return page, titles
    return None


def run(client: Wikipedia, target: str, keywords: list[str]) -> tuple[bool, int]:
    page = client.page("Main_Page")
    titles = list(page.links)

    steps: int = 0
    while True:
        result = search_page_for_keyword(client, titles, keywords)
        if result is None:
            # Lose
            return False, steps
        page, titles = result
        steps += 1
        keywords.remove(page.title.lower())
        # Win check
        if page.title.lower() == target.lower():
            return True, steps
