from _typeshed import Incomplete

from .wikipedia_exception import WikipediaException as WikipediaException

class WikiHttpTimeoutError(WikipediaException):
    url: Incomplete
    def __init__(self, url: str) -> None: ...
