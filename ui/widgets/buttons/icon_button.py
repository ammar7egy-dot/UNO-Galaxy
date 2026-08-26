from PySide6.QtCore import Qt

from .base_button import BaseButton
from ui.theme.colors import Colors


class IconButton(BaseButton):

    def __init__(self, icon="", parent=None):

        super().__init__("", parent)

        self.setText(icon)

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setObjectName(
            "IconButton"
        )

        self.setStyleSheet(
            f"""
            QPushButton#IconButton {{

                background-color: {Colors.SURFACE};

                color: {Colors.TEXT};

                border: none;

                border-radius: 21px;

                font-size: 22px;

                font-weight: 600;

            }}

            QPushButton#IconButton:hover {{

                background-color: {Colors.PRIMARY};

            }}

            QPushButton#IconButton:pressed {{

                background-color: {Colors.PRIMARY_PRESSED};

            }}
            """
        )