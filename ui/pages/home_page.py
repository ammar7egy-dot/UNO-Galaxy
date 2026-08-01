from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class HomePage(QWidget):

    play_clicked = Signal()
    settings_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(40, 30, 40, 30)

        # Top Bar
        top_layout = QHBoxLayout()
        top_layout.addStretch()

        self.settings_button = QPushButton("⚙")
        self.settings_button.setFixedSize(50, 50)

        top_layout.addWidget(self.settings_button)

        # Center
        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_layout.setSpacing(20)

        self.title_label = QLabel("UNO! Galaxy")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Segoe UI", 36, QFont.Weight.Bold))

        self.subtitle_label = QLabel("One Universe. Every UNO.")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setFont(QFont("Segoe UI", 12))

        self.play_button = QPushButton("PLAY")
        self.play_button.setFixedSize(320, 80)
        self.play_button.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))

        center_layout.addWidget(self.title_label)
        center_layout.addWidget(self.subtitle_label)
        center_layout.addSpacing(25)
        center_layout.addWidget(
            self.play_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        main_layout.addLayout(top_layout)
        main_layout.addStretch()
        main_layout.addLayout(center_layout)
        main_layout.addStretch()

    def connect_signals(self):
        self.play_button.clicked.connect(self.play_clicked.emit)
        self.settings_button.clicked.connect(self.settings_clicked.emit)