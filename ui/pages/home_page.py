from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from ui.widgets.starfield_widget import StarfieldWidget

from ui.widgets.home.home_header import HomeHeader
from ui.widgets.home.play_panel import PlayPanel
from ui.widgets.home.profile_button import ProfileButton
from ui.widgets.home.menu_panel import MenuPanel


class HomePage(QWidget):

    play_clicked = Signal()
    settings_clicked = Signal()
    about_clicked = Signal()
    profile_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):

        self.background = StarfieldWidget(self)

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setContentsMargins(
            50,
            35,
            50,
            35,
        )

        self.main_layout.setSpacing(24)

        self.header = HomeHeader()

        self.play_panel = PlayPanel()

        self.profile_button = ProfileButton()

        self.menu_panel = MenuPanel()

        self.main_layout.addWidget(
            self.header
        )

        self.main_layout.addStretch(2)

        self.main_layout.addWidget(
            self.play_panel,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        self.main_layout.addStretch(1)

        bottom_layout = QHBoxLayout()

        bottom_layout.setSpacing(30)

        bottom_layout.addWidget(
            self.profile_button,
            alignment=Qt.AlignmentFlag.AlignLeft
        )

        bottom_layout.addStretch()

        bottom_layout.addWidget(
            self.menu_panel,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        self.main_layout.addLayout(
            bottom_layout
        )

    def connect_signals(self):

        self.play_panel.play_clicked.connect(
            self.play_clicked.emit
        )

        self.menu_panel.settings_clicked.connect(
            self.settings_clicked.emit
        )

        self.menu_panel.about_clicked.connect(
            self.about_clicked.emit
        )

        self.profile_button.profile_clicked.connect(
            self.profile_clicked.emit
        )

    def resizeEvent(self, event):

        self.background.setGeometry(
            self.rect()
        )

        super().resizeEvent(event)