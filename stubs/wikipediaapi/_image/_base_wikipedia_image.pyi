import abc
from typing import Any

from .._page._base_wikipedia_page import BaseWikipediaPage as BaseWikipediaPage

class BaseWikipediaImage(BaseWikipediaPage[Any], metaclass=abc.ABCMeta): ...
