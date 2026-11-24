from typing import Any

from ..exceptions import WikiRateLimitError as WikiRateLimitError

class _RetryAfterWait:
    def __init__(self, retry_wait: float) -> None: ...
    def __call__(self, retry_state: Any) -> float: ...
