import wikipediaapi

from .base import CategoryMember as CategoryMember
from .base import PageNotFoundError as PageNotFoundError
from .base import add_options as add_options
from .base import create_wikipedia_instance as create_wikipedia_instance
from .base import fetch_page as fetch_page
from .base import format_page_dict as format_page_dict

def get_page_categories(wiki: wikipediaapi.Wikipedia, title: str, namespace: int = 0) -> wikipediaapi.PagesDict: ...
def get_category_members(
    wiki: wikipediaapi.Wikipedia, title: str, max_level: int = 0, namespace: int = 0
) -> list[CategoryMember]: ...
def format_category_members(members: list[CategoryMember], output_format: str) -> str: ...
def register_commands(cli_group) -> None: ...
