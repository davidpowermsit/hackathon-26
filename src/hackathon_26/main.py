import wikipediaapi

from hackathon_26 import engine, scoring

TARGETS = ["Ford Mustang", "Blue whale", "Taylor Swift", "Pizza", "Eiffel Tower"]


def prompt_int(prompt: str, low: int, high: int) -> int:
    """Ask until the user enters a whole number between low and high."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")


def prompt_text(prompt: str) -> str:
    """Ask until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def prompt_keywords(prompt: str) -> list[str]:
    """Ask until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip().lower()
        if value:
            keywords: list[str] = value.split(",")
            if len(keywords) > 1:
                return keywords
        print("Input cannot be empty and remember to seperate with ','.")


def display_score(status: bool, score: int, username: str, steps: int, total_keys: int) -> None:
    if status:
        print(f"Congratulations, {username}. You found the target!")
    print(f"your scored {score} by using {steps} of your {total_keys} keywords.")


def display_into() -> None:
    print("Welcome to GAMENAME HERE.")
    print("The goal of this game is to guess as few keywords as possible that get you")
    print("from the Wikipedia homepage to some target, Albert Einstein for example.")
    print("Choose your keywords carfully. Be too specific and you will get stuck,")
    print("be too vague and the same will happen. Choose too many keywords and watch")
    print("your score drop.")


def display_menu(targets: list[str]) -> int:
    while True:
        print("Which Target would you like to choose? ")
        for num, target in enumerate(targets):
            print(f"{num} - {target}")
        choice = prompt_int("Choose: ", 0, len(targets))
        if choice:
            return choice
        print("Chose one of the targets (1-10)")


def run_game(keywords: list[str], target: str) -> int:
    keywords.append(target)
    return 1


def main() -> None:

    wikiclient = wikipediaapi.Wikipedia(user_agent="MSITSEPHACK26 (davidpowermsit@gmail.com)", language="en")

    display_into()
    username = prompt_text("Please enter your username: ")
    chosen_target_id = display_menu(TARGETS)
    print("OK! Lets get started.")
    print("Enter your keywords. We then wait and see what score your chosen keywords gets you!")
    keywords = prompt_keywords("Keywords: ")
    status, steps = engine.run(wikiclient, TARGETS[chosen_target_id], keywords)
    score = scoring.calculate(len(keywords), steps)
    display_score(status, score, username, steps, len(keywords))


if __name__ == "__main__":
    main()
