"""
Application Host.

Responsible for starting the ERP application.
"""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from core.application.context import ApplicationContext
from core.framework.bootstrap import Bootstrap


class ApplicationHost:
    """
    Controls the lifetime of the ERP application.
    """

    def __init__(self) -> None:
        self._app: QApplication | None = None
        self._context: ApplicationContext | None = None

    @property
    def app(self) -> QApplication:
        if self._app is None:
            raise RuntimeError("Application has not been created.")
        return self._app

    @property
    def context(self) -> ApplicationContext:
        if self._context is None:
            raise RuntimeError("Application context is not initialized.")
        return self._context

    def start(self) -> int:
        """
        Start the application.
        """

        self._context = Bootstrap.initialize()

        self._app = QApplication(sys.argv)

        #
        # Next Phase:
        # Theme Engine
        # Font Loader
        # Splash Screen
        # Main Window
        #

        return self._app.exec()