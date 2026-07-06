import sys

from PySide6.QtWidgets import QApplication

from core.framework.ui import BaseMainWindow


app = QApplication(sys.argv)

window = BaseMainWindow()

window.show()

app.exec()