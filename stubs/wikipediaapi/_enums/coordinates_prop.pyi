from enum import Enum

class CoordinatesProp(Enum):
    COUNTRY = "country"
    DIM = "dim"
    GLOBE = "globe"
    NAME = "name"
    REGION = "region"
    TYPE = "type"

WikiCoordinatesProp = CoordinatesProp | str

def coordinates_prop2str(prop: WikiCoordinatesProp) -> str: ...
