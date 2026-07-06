"""
Base Widget.
"""

from PySide6.QtWidgets import QWidget


class BaseWidget(QWidget):
    """
    Base reusable widget.
    """

    def __init__(self) -> None:
        super().__init__()

        self._build()

    def _build(self) -> None:
        """
        Override in child class.
        """