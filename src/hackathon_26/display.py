from hackathon_26.scoring import Score

WIDTH = 70

INTRO = """\
The goal is to get from the Wikipedia homepage to a given Target
using as few keywords as possible.

Choose your keywords carefully:
  - Too specific and you'll get stuck.
  - Too vague and you'll get stuck too.

Every keyword you use costs you points."""


def intro() -> None:
    print(f"{' Wiki Maze ':*^{WIDTH}}")
    print()
    print(INTRO)
    print()
    print("*" * WIDTH)


def score(status: bool, score: Score) -> None:
    if status:
        print(f"Congratulations, {score.username}. You found the target!")
    print(f"your scored {score.score} by using {score.steps} of your {score.keywords} keywords.")


def menu(targets: list[str]) -> None:
    """Show the Targets and return the index of the player's choice."""
    print("Which Target would you like to choose?")
    for index, target in enumerate(targets):
        print(f"  {index} - {target}")


def keyword_message() -> None:
    print("Last step, enter your keywords.")
    print("Can can take a few seconds to run your keywords through the mazer")
    print("After its finished running you will see your score.")


def scoreboard(scores: list[Score]) -> None:
    print(f"{'Scoreboard':*^WIDTH}")
    for score in scores:
        print(f"{score.timestamp} - {score.username} - {score.steps} - {score.score}")
        print("*" * WIDTH)
