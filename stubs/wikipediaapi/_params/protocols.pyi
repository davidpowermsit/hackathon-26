from typing import Protocol

class _HasTitle(Protocol):
    @property
    def title(self) -> str: ...
