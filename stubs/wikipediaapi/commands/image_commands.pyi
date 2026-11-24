import wikipediaapi

from .base import PageNotFoundError as PageNotFoundError
from .base import add_options as add_options
from .base import create_wikipedia_instance as create_wikipedia_instance
from .base import fetch_page as fetch_page

def get_page_images(
    wiki: wikipediaapi.Wikipedia, title: str, namespace: int = 0, limit: int = 10
) -> wikipediaapi.ImagesDict: ...
def format_images(images_dict: wikipediaapi.ImagesDict, output_format: str, with_imageinfo: bool = False) -> str: ...
def register_commands(cli_group) -> None: ...
