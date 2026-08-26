from .base_button import BaseButton
from ui.theme.colors import Colors


class PrimaryButton(BaseButton):

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setObjectName("PrimaryButton")

        self.setStyleSheet(
            f"""
            QPushButton#PrimaryButton {{
                background-color: {Colors.PRIMARY};
                color: {Colors.TEXT};
                border: none;
                border-radius: 20px;
                padding: 12px 30px;
            }}

            QPushButton#PrimaryButton:hover {{
                background-color: {Colors.PRIMARY_HOVER};
            }}

            QPushButton#PrimaryButton:pressed {{
                background-color: {Colors.PRIMARY_PRESSED};
            }}
            """
        )