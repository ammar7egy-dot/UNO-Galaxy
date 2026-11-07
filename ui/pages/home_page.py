
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

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.background = StarfieldWidget(self)

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setContentsMargins(
            50, 35, 50, 35
        )

        self.main_layout.setSpacing(24)

        # Header
        self.header = HomeHeader()

        # Main Play Panel
        self.play_panel = PlayPanel()

        # Bottom Elements
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

        self.bottom_layout = QHBoxLayout()

        self.bottom_layout.setSpacing(30)

        self.bottom_layout.addWidget(
            self.profile_button,
            alignment=Qt.AlignmentFlag.AlignLeft,
        )

        self.bottom_layout.addStretch()

        self.bottom_layout.addWidget(
            self.menu_panel,
            alignment=Qt.AlignmentFlag.AlignRight,
        )

        self.main_layout.addLayout(
            self.bottom_layout
        )

        self.update_responsive_layout()

    # ==========================
    # Signals
    # ==========================

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

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()
        height = self.height()

        if width <= 900:
            horizontal_margin = 20
        elif width <= 1150:
            horizontal_margin = 32
        else:
            horizontal_margin = 50

        if height <= 550:
            vertical_margin = 12
            layout_spacing = 10
        elif height <= 700:
            vertical_margin = 22
            layout_spacing = 16
        else:
            vertical_margin = 35
            layout_spacing = 24

        self.main_layout.setContentsMargins(
            horizontal_margin,
            vertical_margin,
            horizontal_margin,
            vertical_margin,
        )

        self.main_layout.setSpacing(
            layout_spacing
        )

        self.bottom_layout.setSpacing(
            max(10, min(30, width // 40))
        )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        self.background.setGeometry(
            self.rect()
        )

        self.update_responsive_layout()

        super().resizeEvent(event)
