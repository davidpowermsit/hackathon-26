from enum import Enum

class Direction(Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

WikiDirection = Direction | str

def direction2str(direction: WikiDirection) -> str: ...
