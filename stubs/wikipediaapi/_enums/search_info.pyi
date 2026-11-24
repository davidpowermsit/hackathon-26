from enum import Enum

class SearchInfo(Enum):
    REWRITTEN_QUERY = "rewrittenquery"
    SUGGESTION = "suggestion"
    TOTAL_HITS = "totalhits"

WikiSearchInfo = SearchInfo | str

def search_info2str(info: WikiSearchInfo) -> str: ...
