from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("Settings")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 30, QFont.Weight.Bold))

        self.back_button = QPushButton("← Back")
        self.back_button.setFixedWidth(150)

        layout.addWidget(title)
        layout.addWidget(
            self.back_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )