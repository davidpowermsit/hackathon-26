from hackathon_26 import display, engine, io, scoring
from hackathon_26.web import Wikibee

TARGETS = ["Ford Mustang", "Blue whale", "Taylor Swift", "Pizza", "Eiffel Tower", "Aaron Swartz"]


def main() -> None:
    wikiclient = Wikibee()

    # title, links = wikiclient.go_to_page(MAIN_PAGE)

    display.intro()
    username = io.prompt_text("Please enter your username: ")

    display.menu(TARGETS)
    chosen_target_id = io.prompt_int("Choose: ", 0, len(TARGETS) - 1)

    display.keyword_message()
    keywords = io.prompt_keywords("Keywords: ")

    status, steps = engine.run(wikiclient, TARGETS[chosen_target_id], keywords)
    score = scoring.calculate(len(keywords), steps)

    display.score(status, score, username, steps, len(keywords))


if __name__ == "__main__":
    main()
