from collections.abc import Iterable
from typing import Any

from .._enums import CoordinatesProp as CoordinatesProp
from .._enums import CoordinateType as CoordinateType
from .._enums import Direction as Direction
from .._enums import GeoSearchSort as GeoSearchSort
from .._enums import Globe as Globe
from .._enums import Namespace as Namespace
from .._enums import RedirectFilter as RedirectFilter
from .._enums import SearchSort as SearchSort
from .._enums import WikiCoordinatesProp as WikiCoordinatesProp
from .._enums import WikiCoordinateType as WikiCoordinateType
from .._enums import WikiDirection as WikiDirection
from .._enums import WikiGeoSearchSort as WikiGeoSearchSort
from .._enums import WikiGlobe as WikiGlobe
from .._enums import WikiNamespace as WikiNamespace
from .._enums import WikiRedirectFilter as WikiRedirectFilter
from .._enums import WikiSearchInfo as WikiSearchInfo
from .._enums import WikiSearchProp as WikiSearchProp
from .._enums import WikiSearchQiProfile as WikiSearchQiProfile
from .._enums import WikiSearchSort as WikiSearchSort
from .._enums import WikiSearchWhat as WikiSearchWhat
from .._image.wikipedia_image import WikipediaImage as WikipediaImage
from .._page.wikipedia_page import WikipediaPage as WikipediaPage
from .._pages_dict import ImagesDict as ImagesDict
from .._pages_dict import PagesDict as PagesDict
from .._params.coordinates_params import CoordinatesParams as CoordinatesParams
from .._params.geo_search_params import GeoSearchParams as GeoSearchParams
from .._params.imageinfo_params import ImageInfoParams as ImageInfoParams
from .._params.images_params import ImagesParams as ImagesParams
from .._params.random_params import RandomParams as RandomParams
from .._params.search_params import SearchParams as SearchParams
from .._types import Coordinate as Coordinate
from .._types import GeoBox as GeoBox
from .._types import GeoPoint as GeoPoint
from .._types import ImageInfo as ImageInfo
from .._types import SearchResults as SearchResults
from .base_wikipedia_resource import BaseWikipediaResource as BaseWikipediaResource

class WikipediaResource(BaseWikipediaResource):
    def page(self, title: str, ns: WikiNamespace = ..., unquote: bool = False) -> WikipediaPage: ...
    def article(self, title: str, ns: WikiNamespace = ..., unquote: bool = False) -> WikipediaPage: ...
    def extracts(self, page: WikipediaPage, **kwargs: Any) -> str: ...
    def info(self, page: WikipediaPage) -> WikipediaPage: ...
    def langlinks(self, page: WikipediaPage, **kwargs: Any) -> PagesDict: ...
    def links(self, page: WikipediaPage, **kwargs: Any) -> PagesDict: ...
    def backlinks(self, page: WikipediaPage, **kwargs: Any) -> PagesDict: ...
    def categories(self, page: WikipediaPage, **kwargs: Any) -> PagesDict: ...
    def categorymembers(self, page: WikipediaPage, **kwargs: Any) -> PagesDict: ...
    def coordinates(
        self,
        page: WikipediaPage,
        *,
        limit: int = 10,
        primary: WikiCoordinateType = ...,
        prop: Iterable[WikiCoordinatesProp] = ...,
        distance_from_point: GeoPoint | None = None,
        distance_from_page: WikipediaPage | None = None,
    ) -> list[Coordinate]: ...
    def batch_coordinates(
        self,
        pages: list[WikipediaPage],
        *,
        limit: int = 10,
        primary: WikiCoordinateType = ...,
        prop: Iterable[WikiCoordinatesProp] = ...,
        distance_from_point: GeoPoint | None = None,
        distance_from_page: WikipediaPage | None = None,
    ) -> dict[WikipediaPage, list[Coordinate]]: ...
    def images(
        self,
        page: WikipediaPage,
        *,
        limit: int = 10,
        images: Iterable[str] | None = None,
        direction: WikiDirection = ...,
    ) -> ImagesDict: ...
    def batch_images(
        self,
        pages: list[WikipediaPage],
        *,
        limit: int = 10,
        images: Iterable[str] | None = None,
        direction: WikiDirection = ...,
    ) -> dict[str, ImagesDict]: ...
    def imageinfo(self, image: WikipediaImage, *, prop: tuple[str, ...] = ..., limit: int = 1) -> list[ImageInfo]: ...
    def batch_imageinfo(
        self, images: list[WikipediaImage], *, prop: tuple[str, ...] = ..., limit: int = 1
    ) -> dict[str, list[ImageInfo]]: ...
    def geosearch(
        self,
        *,
        coord: GeoPoint | None = None,
        page: WikipediaPage | None = None,
        bbox: GeoBox | None = None,
        radius: int = 500,
        max_dim: int | None = None,
        sort: WikiGeoSearchSort = ...,
        limit: int = 10,
        globe: WikiGlobe = ...,
        ns: WikiNamespace = ...,
        prop: Iterable[WikiCoordinatesProp] | None = None,
        primary: WikiCoordinateType | None = None,
    ) -> PagesDict: ...
    def random(
        self,
        *,
        ns: WikiNamespace = ...,
        filter_redirect: WikiRedirectFilter = ...,
        min_size: int | None = None,
        max_size: int | None = None,
        limit: int = 1,
    ) -> PagesDict: ...
    def search(
        self,
        query: str,
        *,
        ns: WikiNamespace = ...,
        limit: int = 10,
        prop: Iterable[WikiSearchProp] | None = None,
        info: Iterable[WikiSearchInfo] | None = None,
        sort: WikiSearchSort = ...,
        what: WikiSearchWhat | None = None,
        interwiki: bool = False,
        enable_rewrites: bool = False,
        qi_profile: WikiSearchQiProfile | None = None,
    ) -> SearchResults: ...
    def pages(self, titles: list[str], ns: WikiNamespace = ...) -> PagesDict: ...
