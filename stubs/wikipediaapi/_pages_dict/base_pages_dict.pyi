from collections.abc import Iterable
from typing import Protocol

from .._enums import CoordinatesProp as CoordinatesProp
from .._enums import CoordinateType as CoordinateType
from .._enums import Direction as Direction
from .._enums import WikiCoordinatesProp as WikiCoordinatesProp
from .._enums import WikiCoordinateType as WikiCoordinateType
from .._enums import WikiDirection as WikiDirection
from .._image.async_wikipedia_image import AsyncWikipediaImage as AsyncWikipediaImage
from .._image.wikipedia_image import WikipediaImage as WikipediaImage
from .._page._base_wikipedia_page import BaseWikipediaPage as BaseWikipediaPage
from .._page.async_wikipedia_page import AsyncWikipediaPage as AsyncWikipediaPage
from .._page.wikipedia_page import WikipediaPage as WikipediaPage
from .._resources import BaseWikipediaResource as BaseWikipediaResource
from .._types import Coordinate as Coordinate
from .._types import GeoPoint as GeoPoint
from .._types import ImageInfo as ImageInfo
from .async_pages_dict import AsyncPagesDict as AsyncPagesDict
from .pages_dict import PagesDict as PagesDict

class _SyncBatchWiki(Protocol):
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
    def batch_images(
        self,
        pages: list[WikipediaPage],
        *,
        limit: int = 10,
        images: Iterable[str] | None = None,
        direction: WikiDirection = ...,
    ) -> dict[str, PagesDict]: ...

class _AsyncBatchWiki(Protocol):
    async def batch_coordinates(
        self,
        pages: list[AsyncWikipediaPage],
        *,
        limit: int = 10,
        primary: WikiCoordinateType = ...,
        prop: Iterable[WikiCoordinatesProp] = ...,
        distance_from_point: GeoPoint | None = None,
        distance_from_page: AsyncWikipediaPage | None = None,
    ) -> dict[AsyncWikipediaPage, list[Coordinate]]: ...
    async def batch_images(
        self,
        pages: list[AsyncWikipediaPage],
        *,
        limit: int = 10,
        images: Iterable[str] | None = None,
        direction: WikiDirection = ...,
    ) -> dict[str, PagesDict]: ...

class _SyncImageWiki(Protocol):
    def batch_imageinfo(
        self, images: list[WikipediaImage], *, prop: tuple[str, ...] = ..., limit: int = 1
    ) -> dict[str, list[ImageInfo]]: ...

class _AsyncImageWiki(Protocol):
    async def batch_imageinfo(
        self, images: list[AsyncWikipediaImage], *, prop: tuple[str, ...] = ..., limit: int = 1
    ) -> dict[str, list[ImageInfo]]: ...
