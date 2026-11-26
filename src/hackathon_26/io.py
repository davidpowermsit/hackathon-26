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


def prompt_bool(prompt: str) -> str:
    """Ask until the user enters either y or n."""
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "n"):
            return value
        print("Input must be 'y' or 'n'. Please try again.")


def prompt_keywords(prompt: str) -> list[str]:
    """Ask until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip().lower()
        if value:
            keywords: list[str] = [x.strip() for x in value.split(",")]
            if len(keywords) > 1:
                return keywords
        print("Input cannot be empty and remember to seperate with ','.")
