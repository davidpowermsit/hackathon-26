from datetime import datetime

from hackathon_26 import display, engine, io, scoring
from hackathon_26.web import Wikibee

TARGETS = ["Ford Mustang", "Blue whale", "Cosmic ray", "Pizza", "Eiffel Tower", "Aaron Swartz"]


def main() -> None:
    while True:
        wikiclient = Wikibee()

        display.intro()
        username = io.prompt_text("\nPlease enter your username: ")

        display.menu(TARGETS)
        chosen_target_id = io.prompt_int("Choose: ", 0, len(TARGETS) - 1)

        display.keyword_message()
        keywords = io.prompt_keywords("\nKeywords: ")

        # Target must be in keywords list to make final page jump
        if TARGETS[chosen_target_id] not in keywords:
            keywords.append(TARGETS[chosen_target_id])

        status, steps = engine.run(wikiclient, TARGETS[chosen_target_id], keywords.copy())
        if status:
            # target hop dosen't count
            steps = max(0, steps - 1)
        keywords_used = len(keywords) - 1  # target dosen't count
        user_score = scoring.calculate(status, keywords_used, steps)
        game_time = datetime.now().strftime("%d.%m.%Y %H:%M")

        score = scoring.Score(
            timestamp=game_time,
            username=username,
            steps=steps,
            keywords=keywords_used,
            score=user_score,
        )

        try:
            scoring.save(score)
        except (FileNotFoundError, PermissionError, OSError):
            print("An error occurred and your save leaderboard entry was not saved.")

        display.score(status, score)

        view_scoreboard = io.prompt_bool("\nWould you like to see the scoreboard? (y/n): ")
        if view_scoreboard == "y":
            data = scoring.load()
            display.scoreboard(data)

        exit_game = io.prompt_bool("\nWould you like to play again? (y/n): ")
        if exit_game == "n":
            break


if __name__ == "__main__":
    main()
