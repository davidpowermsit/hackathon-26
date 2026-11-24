from enum import Enum

class SearchProp(Enum):
    SIZE = "size"
    WORDCOUNT = "wordcount"
    TIMESTAMP = "timestamp"
    SNIPPET = "snippet"
    TITLE_SNIPPET = "titlesnippet"
    REDIRECT_TITLE = "redirecttitle"
    REDIRECT_SNIPPET = "redirectsnippet"
    SECTION_TITLE = "sectiontitle"
    SECTION_SNIPPET = "sectionsnippet"
    IS_FILE_MATCH = "isfilematch"
    CATEGORY_SNIPPET = "categorysnippet"
    SCORE = "score"
    HAS_RELATED = "hasrelated"
    EXTENSION_DATA = "extensiondata"

WikiSearchProp = SearchProp | str

def search_prop2str(prop: WikiSearchProp) -> str: ...
