from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


class BaseButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setup_base()

    def setup_base(self):
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.setProperty("pressed", True)

        self.style().unpolish(self)
        self.style().polish(self)

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setProperty("pressed", False)

        self.style().unpolish(self)
        self.style().polish(self)

        super().mouseReleaseEvent(event)