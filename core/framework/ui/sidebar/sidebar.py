"""
Sidebar Widget.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .sidebar_section import SidebarSection


class Sidebar(QWidget):
    """
    ERP Sidebar.
    """

    def __init__(self) -> None:
        super().__init__()

        self._sections: list[SidebarSection] = []

        self._list = QListWidget()

        self._build()

    def _build(self) -> None:

        self.setFixedWidth(240)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self._list)

    def add_section(
        self,
        section: SidebarSection,
    ) -> None:

        self._sections.append(section)

        header = QListWidgetItem(section.title)

        header.setFlags(Qt.ItemFlag.NoItemFlags)

        self._list.addItem(header)

        for item in section.items:

            self._list.addItem(item.title)