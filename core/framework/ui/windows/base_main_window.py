"""
Base Main Window.

All ERP windows must inherit from this class.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow


class BaseMainWindow(QMainWindow):
    """
    Base window for the ERP.
    """

    def __init__(self) -> None:
        super().__init__()

        self._initialize_window()
        self._create_ui()
        self._connect_signals()

    def _initialize_window(self) -> None:
        """
        Configure default window settings.
        """

        self.setWindowTitle("ORM Repair ERP")

        self.resize(1400, 850)

        self.setMinimumSize(1200, 700)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    def _create_ui(self) -> None:
        """
        Create UI.

        Override in child class.
        """

    def _connect_signals(self) -> None:
        """
        Connect signals.

        Override in child class.
        """