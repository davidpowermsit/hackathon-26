from _typeshed import Incomplete

from .wikipedia_exception import WikipediaException as WikipediaException

class WikiHttpError(WikipediaException):
    status_code: Incomplete
    url: Incomplete
    def __init__(self, status_code: int, url: str) -> None: ...
