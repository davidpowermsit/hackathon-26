from typing import Any

from _typeshed import Incomplete

from .base_http_client import BaseHTTPClient as BaseHTTPClient

log: Incomplete

class SyncHTTPClient(BaseHTTPClient):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
