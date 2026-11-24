import wikipediaapi

from .base import RandomKwargs as RandomKwargs
from .base import RandomPageResult as RandomPageResult
from .base import RedirectFilter as RedirectFilter
from .base import SearchKwargs as SearchKwargs
from .base import SearchResult as SearchResult
from .base import SearchResults as SearchResults
from .base import SearchSort as SearchSort
from .base import add_options as add_options
from .base import create_wikipedia_instance as create_wikipedia_instance
from .base import redirect_filter2str as redirect_filter2str
from .base import search_sort2str as search_sort2str
from .base import validate_enum_value as validate_enum_value

def get_random_pages(
    wiki: wikipediaapi.Wikipedia,
    limit: int = 1,
    ns: int = 0,
    filter_redirect: str = "nonredirects",
    min_size: int | None = None,
    max_size: int | None = None,
) -> list[RandomPageResult]: ...
def format_random(results: list[RandomPageResult], output_format: str) -> str: ...
def get_search_results(
    wiki: wikipediaapi.Wikipedia, query: str, limit: int = 10, ns: int = 0, sort: str = "relevance"
) -> SearchResults: ...
def format_search(results: SearchResults, output_format: str) -> str: ...
def register_commands(cli_group) -> None: ...
