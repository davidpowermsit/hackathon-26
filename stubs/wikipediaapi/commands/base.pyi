from typing import TypedDict

import wikipediaapi
from wikipediaapi._enums import CoordinateType as CoordinateType
from wikipediaapi._enums import GeoSearchSort as GeoSearchSort
from wikipediaapi._enums import Globe as Globe
from wikipediaapi._enums import RedirectFilter as RedirectFilter
from wikipediaapi._enums import SearchSort as SearchSort
from wikipediaapi._enums import WikiCoordinateType as WikiCoordinateType
from wikipediaapi._enums import WikiGeoSearchSort as WikiGeoSearchSort
from wikipediaapi._enums import WikiGlobe as WikiGlobe
from wikipediaapi._enums import WikiRedirectFilter as WikiRedirectFilter
from wikipediaapi._enums import WikiSearchSort as WikiSearchSort
from wikipediaapi._enums import coordinate_type2str as coordinate_type2str
from wikipediaapi._enums import geosearch_sort2str as geosearch_sort2str
from wikipediaapi._enums import globe2str as globe2str
from wikipediaapi._enums import redirect_filter2str as redirect_filter2str
from wikipediaapi._enums import search_sort2str as search_sort2str

class GeoSearchKwargs(TypedDict, total=False):
    coord: wikipediaapi.GeoPoint
    page: wikipediaapi.WikipediaPage
    bbox: wikipediaapi.GeoBox
    radius: int
    max_dim: int | None
    sort: WikiGeoSearchSort
    limit: int
    globe: WikiGlobe
    ns: int
    primary: WikiCoordinateType | None

class RandomKwargs(TypedDict, total=False):
    ns: int
    filter_redirect: WikiRedirectFilter
    min_size: int | None
    max_size: int | None
    limit: int

class SearchKwargs(TypedDict, total=False):
    ns: int
    limit: int
    sort: WikiSearchSort

class SectionInfo(TypedDict):
    title: str
    level: int
    indent: int

class PageInfo(TypedDict, total=False):
    title: str
    pageid: int | None
    namespace: int
    exists: bool
    language: str
    fullurl: str | None
    canonicalurl: str | None
    displaytitle: str | None

class CoordinateInfo(TypedDict, total=False):
    lat: float
    lon: float
    primary: bool
    globe: str
    type: str | None
    name: str | None
    dim: int | None
    country: str | None
    region: str | None
    dist: float | None

class GeoSearchResult(TypedDict, total=False):
    title: str
    dist: float | None
    lat: float | None
    lon: float | None
    primary: bool | None

class CategoryMember(TypedDict):
    title: str
    ns: int
    level: int

class RandomPageResult(TypedDict, total=False):
    title: str
    pageid: int | None

class SearchResult(TypedDict, total=False):
    title: str
    pageid: int | None
    size: int | None
    wordcount: int | None
    timestamp: str | None
    snippet: str | None

class SearchResults(TypedDict, total=False):
    totalhits: int
    pages: list[SearchResult]
    suggestion: str | None

def create_wikipedia_instance(
    user_agent: str,
    language: str,
    variant: str | None,
    extract_format: str,
    max_retries: int = 3,
    retry_wait: float = 1.0,
) -> wikipediaapi.Wikipedia: ...
def fetch_page(wiki: wikipediaapi.Wikipedia, title: str, namespace: int) -> wikipediaapi.WikipediaPage: ...
def format_page_dict(pages: wikipediaapi.PagesDict, output_format: str) -> str: ...

class PageNotFoundError(Exception): ...
class SectionNotFoundError(Exception): ...

def validate_enum_value(value: str, enum_class, converter_func, param_name: str): ...
def parse_bbox_string(bbox_str: str) -> wikipediaapi.GeoBox: ...
def add_options(options): ...
def format_sections(sections: list[SectionInfo], output_format: str) -> str: ...
def format_page_info(info: PageInfo, output_format: str) -> str: ...
