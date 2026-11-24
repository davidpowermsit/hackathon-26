import click
from wikipediaapi.commands import category_commands as category_commands
from wikipediaapi.commands import geo_commands as geo_commands
from wikipediaapi.commands import image_commands as image_commands
from wikipediaapi.commands import link_commands as link_commands
from wikipediaapi.commands import page_commands as page_commands
from wikipediaapi.commands import search_commands as search_commands

def cli() -> click.Group: ...
def main() -> None: ...
