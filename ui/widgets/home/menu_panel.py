from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
)

from ui.widgets.buttons.primary_button import PrimaryButton


class MenuPanel(QFrame):

    settings_clicked = Signal()
    about_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        self.setFixedWidth(260)

        self.setStyleSheet("""
            QFrame {
                background: rgba(255,255,255,12);
                border: 1px solid rgba(255,255,255,25);
                border-radius: 16px;
            }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        layout.setSpacing(12)

        self.settings_button = PrimaryButton(
            "⚙ Settings"
        )

        self.about_button = PrimaryButton(
            "ℹ About"
        )

        self.settings_button.clicked.connect(
            self.settings_clicked.emit
        )

        self.about_button.clicked.connect(
            self.about_clicked.emit
        )

        layout.addWidget(self.settings_button)
        layout.addWidget(self.about_button)

     