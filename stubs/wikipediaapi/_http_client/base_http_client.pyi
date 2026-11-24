import abc
from abc import ABC
from typing import Any

from _typeshed import Incomplete

from .._version import __version_str__ as __version_str__
from ..exceptions import WikiConnectionError as WikiConnectionError
from ..exceptions import WikiHttpError as WikiHttpError
from ..exceptions import WikiHttpTimeoutError as WikiHttpTimeoutError
from ..exceptions import WikiInvalidJsonError as WikiInvalidJsonError
from ..exceptions import WikiRateLimitError as WikiRateLimitError
from ..extract_format import ExtractFormat as ExtractFormat

USER_AGENT: Incomplete
MIN_USER_AGENT_LEN: int
MAX_LANG_LEN: int
log: Incomplete

class BaseHTTPClient(ABC, metaclass=abc.ABCMeta):
    language: Incomplete
    variant: Incomplete
    extract_format: Incomplete
    def __init__(
        self,
        user_agent: str,
        language: str = "en",
        variant: str | None = None,
        extract_format: ExtractFormat = ...,
        headers: dict[str, Any] | None = None,
        extra_api_params: dict[str, Any] | None = None,
        max_retries: int = 3,
        retry_wait: float = 1.0,
        **kwargs: Any,
    ) -> None: ...
