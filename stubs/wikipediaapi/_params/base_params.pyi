from typing import Any, ClassVar

class _BaseParams:
    PREFIX: ClassVar[str]
    FIELD_MAP: ClassVar[dict[str, str]]
    def to_api(self) -> dict[str, str]: ...
    def cache_key(self) -> tuple[tuple[str, Any], ...]: ...
