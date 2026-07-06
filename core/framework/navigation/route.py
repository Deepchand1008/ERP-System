"""
Navigation Route.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Route:
    """
    Represents a page route.
    """

    name: str

    title: str

    permission: str = ""