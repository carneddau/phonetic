"""Module for simple helper methods with no dependencies within the package"""

from functools import cache
from importlib.metadata import version as _version

from rich.console import Console


@cache
def package() -> str:
    """Get the name of the top-level package"""
    return __name__.split(".")[0]


@cache
def version() -> str:
    """Get the version of the top-level package"""
    return _version(package())


err_console = Console(stderr=True, style="red")
console = Console(stderr=False)
