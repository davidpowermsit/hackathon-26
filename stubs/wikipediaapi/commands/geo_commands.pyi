import wikipediaapi

from .base import CoordinateInfo as CoordinateInfo
from .base import CoordinateType as CoordinateType
from .base import GeoSearchKwargs as GeoSearchKwargs
from .base import GeoSearchResult as GeoSearchResult
from .base import GeoSearchSort as GeoSearchSort
from .base import Globe as Globe
from .base import PageNotFoundError as PageNotFoundError
from .base import add_options as add_options
from .base import coordinate_type2str as coordinate_type2str
from .base import create_wikipedia_instance as create_wikipedia_instance
from .base import fetch_page as fetch_page
from .base import geosearch_sort2str as geosearch_sort2str
from .base import globe2str as globe2str
from .base import parse_bbox_string as parse_bbox_string
from .base import validate_enum_value as validate_enum_value

def get_page_coordinates(
    wiki: wikipediaapi.Wikipedia, title: str, namespace: int = 0, limit: int = 10, primary: str = "primary"
) -> list[CoordinateInfo]: ...
def format_coordinates(coords: list[CoordinateInfo], output_format: str) -> str: ...
def geosearch(
    wiki: wikipediaapi.Wikipedia,
    coord: str | None = None,
    page_title: str | None = None,
    bbox: str | None = None,
    radius: int = 1000,
    max_dim: int | None = None,
    sort: str = "distance",
    limit: int = 10,
    globe: str = "earth",
    ns: int = 0,
    primary: str | None = None,
) -> list[GeoSearchResult]: ...
def format_geosearch(results: list[GeoSearchResult], output_format: str) -> str: ...
def get_geosearch_results(wiki: wikipediaapi.Wikipedia, **kwargs) -> list[GeoSearchResult]: ...
def register_commands(cli_group) -> None: ...
