from PySide6.QtGui import QIcon

from .base_button import BaseButton
from ui.theme.colors import Colors


class IconButton(BaseButton):
    def __init__(self, icon=None, parent=None):
        super().__init__("", parent)

        if icon:
            self.setIcon(QIcon(icon))

        self.setObjectName("IconButton")

        self.setStyleSheet(
            f"""
            QPushButton#IconButton {{
                background-color: {Colors.SURFACE};
                color: {Colors.TEXT};
                border: none;
                border-radius: 25px;
                font-size: 22px;
            }}

            QPushButton#IconButton:hover {{
                background-color: {Colors.PRIMARY};
            }}

            QPushButton#IconButton:pressed {{
                background-color: {Colors.PRIMARY_PRESSED};
            }}
            """
        )