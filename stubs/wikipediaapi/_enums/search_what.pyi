from enum import Enum

class SearchWhat(Enum):
    NEAR_MATCH = "nearmatch"
    TEXT = "text"
    TITLE = "title"

WikiSearchWhat = SearchWhat | str

def search_what2str(what: WikiSearchWhat) -> str: ...
