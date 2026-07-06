"""
ERP Main Window.
"""

from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
    QWidget,
    QHBoxLayout,
)

from core.framework.ui.windows import BaseMainWindow


class MainWindow(BaseMainWindow):
    """
    ERP Main Window.
    """

    def __init__(self) -> None:

        super().__init__()

    def _create_ui(self) -> None:

        self._build_workspace()

        self._build_statusbar()

    def _connect_signals(self) -> None:
        """
        Connect signals.
        """

    def _build_workspace(self) -> None:

        self.workspace = QWidget()

        self.workspace_layout = QHBoxLayout(self.workspace)

        self.setCentralWidget(self.workspace)

    def _build_statusbar(self) -> None:

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)