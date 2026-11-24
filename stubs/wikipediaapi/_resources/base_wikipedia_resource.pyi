from abc import ABC
from collections.abc import Callable as Callable
from typing import TypeVar

from _typeshed import Incomplete

from .._enums import Namespace as Namespace
from .._enums import WikiNamespace as WikiNamespace
from .._page._base_wikipedia_page import BaseWikipediaPage as BaseWikipediaPage
from .._page.wikipedia_page import WikipediaPage as WikipediaPage
from .._page.wikipedia_page_section import WikipediaPageSection as WikipediaPageSection
from .._pages_dict import ImagesDict as ImagesDict
from .._pages_dict import PagesDict as PagesDict
from .._params.coordinates_params import CoordinatesParams as CoordinatesParams
from .._params.geo_search_params import GeoSearchParams as GeoSearchParams
from .._params.imageinfo_params import ImageInfoParams as ImageInfoParams
from .._params.images_params import ImagesParams as ImagesParams
from .._params.random_params import RandomParams as RandomParams
from .._params.search_params import SearchParams as SearchParams
from .._types import Coordinate as Coordinate
from .._types import GeoSearchMeta as GeoSearchMeta
from .._types import ImageInfo as ImageInfo
from .._types import SearchMeta as SearchMeta
from .._types import SearchResults as SearchResults
from ..extract_format import ExtractFormat as ExtractFormat

T = TypeVar("T")
RE_SECTION: Incomplete

class BaseWikipediaResource(ABC):
    language: str
    variant: str | None
    extract_format: ExtractFormat
