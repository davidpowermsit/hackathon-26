from enum import Enum

class GeoSearchSort(Enum):
    DISTANCE = "distance"
    RELEVANCE = "relevance"

WikiGeoSearchSort = GeoSearchSort | str

def geosearch_sort2str(sort: WikiGeoSearchSort) -> str: ...
