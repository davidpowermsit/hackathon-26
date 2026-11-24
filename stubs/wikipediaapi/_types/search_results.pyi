from dataclasses import dataclass

from .._pages_dict import PagesDict as PagesDict

@dataclass
class SearchResults:
    pages: PagesDict
    totalhits: int = ...
    suggestion: str | None = ...
