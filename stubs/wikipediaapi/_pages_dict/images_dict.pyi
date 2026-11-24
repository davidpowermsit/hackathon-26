from collections.abc import Mapping
from typing import Any

from .._image.wikipedia_image import WikipediaImage as WikipediaImage
from .._page._base_wikipedia_page import BaseWikipediaPage as BaseWikipediaPage
from .._resources import BaseWikipediaResource as BaseWikipediaResource
from .._types import ImageInfo as ImageInfo

class ImagesDict(dict[str, BaseWikipediaPage[Any]]):
    def __init__(
        self, wiki: BaseWikipediaResource | None = None, data: Mapping[str, BaseWikipediaPage[Any]] | None = None
    ) -> None: ...
    def imageinfo(self, *, prop: tuple[str, ...] = ..., limit: int = 1) -> dict[str, list[ImageInfo]]: ...
