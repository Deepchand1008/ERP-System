"""
Navigation Manager.
"""

from PySide6.QtWidgets import QWidget


class NavigationManager:
    """
    Controls page navigation.
    """

    def __init__(self) -> None:

        self._registry = None

        self._container: QWidget | None = None

    def set_registry(self, registry) -> None:

        self._registry = registry

    def set_container(
        self,
        widget: QWidget,
    ) -> None:

        self._container = widget

    def navigate(
        self,
        route: str,
    ) -> None:

        if self._registry is None:
            raise RuntimeError("Page registry not configured.")

        if self._container is None:
            raise RuntimeError("Workspace not configured.")

        page_class = self._registry.get(route)

        if page_class is None:
            raise RuntimeError(f"Route '{route}' not found.")

        page = page_class()

        page.setParent(self._container)

        page.show()