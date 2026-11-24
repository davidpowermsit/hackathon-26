from enum import Enum

class RedirectFilter(Enum):
    ALL = "all"
    NONREDIRECTS = "nonredirects"
    REDIRECTS = "redirects"

WikiRedirectFilter = RedirectFilter | str

def redirect_filter2str(rfilter: WikiRedirectFilter) -> str: ...
