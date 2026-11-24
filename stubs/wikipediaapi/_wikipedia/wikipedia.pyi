from .._http_client import USER_AGENT as USER_AGENT
from .._http_client import SyncHTTPClient as SyncHTTPClient
from .._resources import WikipediaResource as WikipediaResource

class Wikipedia(WikipediaResource, SyncHTTPClient): ...
