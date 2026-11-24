from collections.abc import Iterable, Mapping
from typing import Any

from .._enums import CoordinatesProp as CoordinatesProp
from .._enums import CoordinateType as CoordinateType
from .._enums import Direction as Direction
from .._enums import WikiCoordinatesProp as WikiCoordinatesProp
from .._enums import WikiCoordinateType as WikiCoordinateType
from .._enums import WikiDirection as WikiDirection
from .._page._base_wikipedia_page import BaseWikipediaPage as BaseWikipediaPage
from .._page.wikipedia_page import WikipediaPage as WikipediaPage
from .._resources import BaseWikipediaResource as BaseWikipediaResource
from .._types import Coordinate as Coordinate
from .._types import GeoPoint as GeoPoint

class PagesDict(dict[str, BaseWikipediaPage[Any]]):
    def __init__(
        self, wiki: BaseWikipediaResource | None = None, data: Mapping[str, BaseWikipediaPage[Any]] | None = None
    ) -> None: ...
    def coordinates(
        self,
        *,
        limit: int = 10,
        primary: WikiCoordinateType = ...,
        prop: Iterable[WikiCoordinatesProp] = ...,
        distance_from_point: GeoPoint | None = None,
        distance_from_page: WikipediaPage | None = None,
    ) -> dict[WikipediaPage, list[Coordinate]]: ...
    def images(
        self, *, limit: int = 10, images: Iterable[str] | None = None, direction: WikiDirection = ...
    ) -> dict[str, PagesDict]: ...
