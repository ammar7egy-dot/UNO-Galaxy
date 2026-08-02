from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

from ui.widgets.buttons.primary_button import PrimaryButton


class SettingsPage(QWidget):

    about_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(20)

        title = QLabel("Settings")

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setFont(
            QFont(
                "Segoe UI",
                30,
                QFont.Weight.Bold
            )
        )

        self.about_button = PrimaryButton(
            "About"
        )

        self.about_button.clicked.connect(
            self.about_clicked.emit
        )

        self.back_button = PrimaryButton(
            "← Back"
        )

        layout.addWidget(title)
        layout.addWidget(
            self.about_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        layout.addWidget(
            self.back_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )