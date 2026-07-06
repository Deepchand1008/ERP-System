"""
ERP Main Window.
"""

from PySide6.QtWidgets import (
    QWidget,
    QStatusBar,
    QHBoxLayout,
)

from core.framework.ui.windows import BaseMainWindow

from core.framework.ui.sidebar import (
    Sidebar,
    SidebarItem,
    SidebarSection,
)


class MainWindow(BaseMainWindow):
    """
    Main Shell Window of the ERP.
    """

    def __init__(self) -> None:
        super().__init__()

    def _create_ui(self) -> None:
        """Create the main UI."""
        self._build_workspace()
        self._build_statusbar()

    def _connect_signals(self) -> None:
        """Connect all signals."""
        pass

    def _build_workspace(self) -> None:
        """Create sidebar and workspace."""

        self.workspace = QWidget()

        layout = QHBoxLayout(self.workspace)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # ---------------- Sidebar ---------------- #

        self.sidebar = Sidebar()

        main_section = SidebarSection("MAIN")

        main_section.add_item(
            SidebarItem(
                title="Dashboard",
                route="dashboard",
            )
        )

        main_section.add_item(
            SidebarItem(
                title="Customers",
                route="customers",
            )
        )

        main_section.add_item(
            SidebarItem(
                title="Repairs",
                route="repairs",
            )
        )

        main_section.add_item(
            SidebarItem(
                title="Engineers",
                route="engineers",
            )
        )

        main_section.add_item(
            SidebarItem(
                title="Payments",
                route="payments",
            )
        )

        self.sidebar.add_section(main_section)

        # ---------------- Workspace ---------------- #

        self.page_container = QWidget()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.page_container, 1)

        self.setCentralWidget(self.workspace)

    def _build_statusbar(self) -> None:
        """Create status bar."""

        status_bar = QStatusBar()

        status_bar.showMessage("Ready")

        self.setStatusBar(status_bar)