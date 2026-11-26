import csv
from dataclasses import asdict, dataclass, fields
from pathlib import Path

BASE_SCORE = 1000

SAVE_DIR = Path(__file__).parent / "data"
scoreboard_path = SAVE_DIR / "scoreboard.csv"


@dataclass
class Score:
    timestamp: str
    username: str
    steps: int
    keywords: int
    score: int


def calculate(predicted_keywords: int, actual_keywords: int) -> int:
    if not 0 <= actual_keywords <= predicted_keywords:
        raise ValueError("actual keywords must be between 1 and the prediction")
    accuracy = actual_keywords / predicted_keywords
    return round(BASE_SCORE * accuracy)


def save(new_user_score: Score) -> None:
    """Takes a new score and saves it to storage"""
    fieldnames = [f.name for f in fields(Score)]
    entry = asdict(new_user_score)

    needs_header = not scoreboard_path.exists()

    with open(scoreboard_path, "a", newline="") as scoreboard_obj:
        writer = csv.DictWriter(scoreboard_obj, fieldnames=fieldnames)
        if needs_header:
            writer.writeheader()
        writer.writerow(entry)


def load() -> list[Score]:
    """Loads all scores from storage and represents them as an object"""
    scoreboard: list[Score] = []

    with open(scoreboard_path, newline="") as scoreboard_objt:
        reader = csv.DictReader(scoreboard_objt)
        for row in reader:
            entry = Score(
                timestamp=row["timestamp"].strip(),
                username=row["username"].strip(),
                steps=int(row["steps"].strip()),
                keywords=int(row["keywords"].strip()),
                score=int(row["score"].strip()),
            )
            scoreboard.append(entry)

    return sorted(scoreboard, key=lambda x: x.score, reverse=True)
