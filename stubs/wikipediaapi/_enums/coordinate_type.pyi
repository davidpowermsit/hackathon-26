from enum import Enum

class CoordinateType(Enum):
    ALL = "all"
    PRIMARY = "primary"
    SECONDARY = "secondary"

WikiCoordinateType = CoordinateType | str

def coordinate_type2str(ctype: WikiCoordinateType) -> str: ...
