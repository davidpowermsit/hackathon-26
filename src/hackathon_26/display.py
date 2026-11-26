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
    print(f"{' Scoreboard ':*^{WIDTH}}")
    if not scores:
        print(f"{'No Scores Recorded Yet':^{WIDTH}}")
        print("*" * WIDTH)
        return

    # define the widths for each row
    row = "{:>4}  {:<19}  {:<14}  {:>5}  {:>8}  {:>7}"

    print(row.format("Rank", "Date", "Player", "Steps", "Keywords", "Score"))
    print("-" * WIDTH)
    for rank, s in enumerate(scores, start=1):
        print(row.format(rank, s.timestamp[:19], s.username[:14], s.steps, s.keywords, s.score))
    print("*" * WIDTH)
