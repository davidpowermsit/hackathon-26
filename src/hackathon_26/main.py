TARGETS = ["Albert Einstein", "Britney Spears"]


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


def display_score(score: int, username: str) -> None:
    print(f"{username}, your score is in...")
    print(f"using NO_GUESSES you scored {score}")


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
    return 1


def main() -> None:
    display_into()
    username = prompt_text("Please enter your username: ")
    chosen_target_id = display_menu(TARGETS)
    print("OK! Lets get started. Enter your keywords. We then wait and see what your score will be.")
    keywords = prompt_keywords("Keywords: ")
    score: int = run_game(keywords, TARGETS[chosen_target_id])
    display_score(score, username)


if __name__ == "__main__":  # pragma: no cover
    main()
