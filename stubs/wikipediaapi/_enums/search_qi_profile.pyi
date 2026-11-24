from enum import Enum

class SearchQiProfile(Enum):
    CLASSIC = "classic"
    CLASSIC_NO_BOOST_LINKS = "classic_noboostlinks"
    EMPTY = "empty"
    ENGINE_AUTO_SELECT = "engine_autoselect"
    GROWTH_UNDERLINKED = "growth_underlinked"
    MLR_1024RS = "mlr-1024rs"
    MLR_1024RS_NEXT = "mlr-1024rs-next"
    POPULAR_INCLINKS = "popular_inclinks"
    POPULAR_INCLINKS_PV = "popular_inclinks_pv"
    WSUM_INCLINKS = "wsum_inclinks"
    WSUM_INCLINKS_PV = "wsum_inclinks_pv"

WikiSearchQiProfile = SearchQiProfile | str

def search_qi_profile2str(qi_profile: WikiSearchQiProfile) -> str: ...
