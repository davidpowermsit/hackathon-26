from enum import Enum

class SearchSort(Enum):
    CREATE_TIMESTAMP_ASC = "create_timestamp_asc"
    CREATE_TIMESTAMP_DESC = "create_timestamp_desc"
    INCOMING_LINKS_ASC = "incoming_links_asc"
    INCOMING_LINKS_DESC = "incoming_links_desc"
    JUST_MATCH = "just_match"
    LAST_EDIT_ASC = "last_edit_asc"
    LAST_EDIT_DESC = "last_edit_desc"
    NONE = "none"
    RANDOM = "random"
    RELEVANCE = "relevance"
    TITLE_NATURAL_ASC = "title_natural_asc"
    TITLE_NATURAL_DESC = "title_natural_desc"
    USER_RANDOM = "user_random"

WikiSearchSort = SearchSort | str

def search_sort2str(sort: WikiSearchSort) -> str: ...
