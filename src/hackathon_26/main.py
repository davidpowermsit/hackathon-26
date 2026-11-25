from hackathon_26 import display, engine, io, scoring
from hackathon_26.web import Wikibee

TARGETS = ["Ford Mustang", "Blue whale", "Cosmic ray", "Pizza", "Eiffel Tower", "Aaron Swartz"]


def main() -> None:
    wikiclient = Wikibee()

    display.intro()
    username = io.prompt_text("Please enter your username: ")

    display.menu(TARGETS)
    chosen_target_id = io.prompt_int("Choose: ", 0, len(TARGETS) - 1)

    display.keyword_message()
    keywords = io.prompt_keywords("Keywords: ")
    # Add the target so the user does not have to
    keywords.append(TARGETS[chosen_target_id])

    status, steps = engine.run(wikiclient, TARGETS[chosen_target_id], keywords.copy())
    score = scoring.calculate(len(keywords), steps)

    # subtract 1 from steps and keywords total as Target step doesn't count
    display.score(status, score, username, max(0, steps - 1), len(keywords) - 1)


if __name__ == "__main__":
    main()
