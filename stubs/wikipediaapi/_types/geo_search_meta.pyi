from dataclasses import dataclass

@dataclass(frozen=True)
class GeoSearchMeta:
    dist: float
    lat: float
    lon: float
    primary: bool
