"""
Base Dialog.
"""

from PySide6.QtWidgets import QDialog


class BaseDialog(QDialog):
    """
    Base dialog.
    """

    def __init__(self) -> None:
        super().__init__()

        self._build()

    def _build(self) -> None:
        """
        Override in child class.
        """