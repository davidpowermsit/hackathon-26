from enum import Enum

class Globe(Enum):
    EARTH = "earth"
    MARS = "mars"
    MOON = "moon"
    VENUS = "venus"

WikiGlobe = Globe | str

def globe2str(globe: WikiGlobe) -> str: ...
