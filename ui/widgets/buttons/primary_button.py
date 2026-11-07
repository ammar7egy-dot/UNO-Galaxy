
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QSizePolicy

from .base_button import BaseButton
from ui.theme.colors import Colors


class PrimaryButton(BaseButton):

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setObjectName("PrimaryButton")

        self.setMinimumSize(100, 42)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        self.setStyleSheet(
            f"""
            QPushButton#PrimaryButton {{
                background-color: {Colors.PRIMARY};
                color: {Colors.TEXT};
                border: none;
                border-radius: 16px;
                padding: 8px 16px;
            }}

            QPushButton#PrimaryButton:hover {{
                background-color: {Colors.PRIMARY_HOVER};
            }}

            QPushButton#PrimaryButton:pressed {{
                background-color: {Colors.PRIMARY_PRESSED};
            }}
            """
        )

    def resizeEvent(self, event):

        height = self.height()

        font = self.font()
        font.setPointSize(
            max(9, min(14, int(height * 0.28)))
        )

        self.setFont(font)

        super().resizeEvent(event)
