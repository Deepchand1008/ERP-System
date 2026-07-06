"""
Page Registry.
"""

from typing import Type

from PySide6.QtWidgets import QWidget


class PageRegistry:
    """
    Stores all registered pages.
    """

    def __init__(self) -> None:

        self._pages: dict[str, Type[QWidget]] = {}

    def register(
        self,
        route: str,
        page: Type[QWidget],
    ) -> None:

        self._pages[route] = page

    def get(
        self,
        route: str,
    ) -> Type[QWidget] | None:

        return self._pages.get(route)

    def contains(
        self,
        route: str,
    ) -> bool:

        return route in self._pages