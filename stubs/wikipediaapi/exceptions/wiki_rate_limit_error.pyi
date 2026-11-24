from _typeshed import Incomplete

from .wiki_http_error import WikiHttpError as WikiHttpError

class WikiRateLimitError(WikiHttpError):
    retry_after: Incomplete
    def __init__(self, url: str, retry_after: int | None = None) -> None: ...
