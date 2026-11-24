from .._http_client import AsyncHTTPClient as AsyncHTTPClient
from .._resources import AsyncWikipediaResource as AsyncWikipediaResource

class AsyncWikipedia(AsyncWikipediaResource, AsyncHTTPClient): ...
