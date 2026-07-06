"""
Base Page.
"""

from PySide6.QtWidgets import QWidget


class BasePage(QWidget):
    """
    Base page for every ERP module.
    """

    def __init__(self) -> None:
        super().__init__()

        self._build()

    def _build(self) -> None:
        """
        Override in child class.
        """