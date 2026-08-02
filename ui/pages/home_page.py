from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from ui.widgets.buttons.primary_button import PrimaryButton
from ui.widgets.buttons.icon_button import IconButton
from ui.widgets.starfield_widget import StarfieldWidget
from ui.widgets.title_widget import TitleWidget
from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class HomePage(QWidget):

    play_clicked = Signal()
    settings_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):

        # ==========================
        # Background
        # ==========================

        self.background = StarfieldWidget(self)
        self.background.lower()

        # ==========================
        # Foreground
        # ==========================

        self.content = QWidget(self)
        self.content.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )
        self.content.setStyleSheet(
            "background: transparent;"
        )
        self.content.raise_()

        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(
            60,
            40,
            60,
            40,
        )

        # ==========================
        # Top Bar
        # ==========================

        top_layout = QHBoxLayout()
        top_layout.addStretch()

        self.settings_button = IconButton()
        self.settings_button.setText("⚙")
        self.settings_button.setFixedSize(52, 52)

        top_layout.addWidget(self.settings_button)

        main_layout.addLayout(top_layout)

        main_layout.addStretch()

        # ==========================
        # Center
        # ==========================

        center_layout = QVBoxLayout()
        center_layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        center_layout.setSpacing(18)

        self.title = TitleWidget()

        self.subtitle = QLabel(
            "One Universe. Every UNO."
        )

        self.subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.subtitle.setFont(
            Fonts.body(15)
        )

        self.subtitle.setStyleSheet(
            f"""
            color: {Colors.TEXT_SECONDARY};
            background: transparent;
            """
        )

        self.play_button = PrimaryButton("PLAY")

        self.play_button.setMinimumSize(
            340,
            78,
        )

        self.play_button.setMaximumWidth(
            420,
        )

        self.play_button.setFont(
            QFont(
                "Segoe UI",
                17,
                QFont.Weight.Bold,
            )
        )

        center_layout.addWidget(
            self.title,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        center_layout.addSpacing(10)

        center_layout.addWidget(
            self.subtitle,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        center_layout.addSpacing(45)

        center_layout.addWidget(
            self.play_button,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        main_layout.addLayout(center_layout)

        main_layout.addStretch()

        # ==========================
        # Version
        # ==========================

        self.version = QLabel("Version 0.1.0")

        self.version.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.version.setFont(
            Fonts.body(10)
        )

        self.version.setStyleSheet(
            f"""
            color: {Colors.TEXT_SECONDARY};
            background: transparent;
            """
        )

        main_layout.addWidget(
            self.version
        )

    def resizeEvent(self, event):

        self.background.setGeometry(
            self.rect()
        )

        self.content.setGeometry(
            self.rect()
        )

        super().resizeEvent(event)

    def showEvent(self, event):

        self.background.setGeometry(
            self.rect()
        )

        self.content.setGeometry(
            self.rect()
        )

        super().showEvent(event)

    def connect_signals(self):

        self.play_button.clicked.connect(
            self.play_clicked.emit
        )

        self.settings_button.clicked.connect(
            self.settings_clicked.emit
        )