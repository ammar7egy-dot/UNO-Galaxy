
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QLabel,
)

from ui.settings.settings_header import SettingsHeader
from ui.settings.settings_sidebar import SettingsSidebar
from ui.settings.general_page import GeneralPage
from ui.settings.audio_page import AudioPage

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class ComingSoonPage(QWidget):

    def __init__(self, title):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        label = QLabel(
            f"{title}\n\nComing Soon"
        )

        label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        label.setFont(
            Fonts.title(24)
        )

        label.setStyleSheet(
            f"""
            color: {Colors.TEXT_SECONDARY};
            """
        )

        layout.addWidget(label)


class SettingsPage(QWidget):

    back_clicked = SettingsHeader.back_clicked

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.connect_signals()

        self.update_responsive_layout()

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.root_layout = QVBoxLayout(self)

        self.root_layout.setContentsMargins(
            40, 30, 40, 30
        )

        self.root_layout.setSpacing(25)

        # Header
        self.header = SettingsHeader()

        self.root_layout.addWidget(
            self.header
        )

        # Body
        self.body_layout = QHBoxLayout()

        self.body_layout.setSpacing(30)

        # Sidebar
        self.sidebar = SettingsSidebar()

        self.body_layout.addWidget(
            self.sidebar
        )

        # Pages
        self.stack = QStackedWidget()

        self.general_page = GeneralPage()
        self.audio_page = AudioPage()

        self.appearance_page = ComingSoonPage(
            "Appearance"
        )

        self.language_page = ComingSoonPage(
            "Language"
        )

        self.gameplay_page = ComingSoonPage(
            "Gameplay"
        )

        self.about_page = ComingSoonPage(
            "About"
        )

        self.stack.addWidget(self.general_page)
        self.stack.addWidget(self.audio_page)
        self.stack.addWidget(self.appearance_page)
        self.stack.addWidget(self.language_page)
        self.stack.addWidget(self.gameplay_page)
        self.stack.addWidget(self.about_page)

        self.body_layout.addWidget(
            self.stack,
            1
        )

        self.root_layout.addLayout(
            self.body_layout,
            1
        )

    # ==========================
    # Signals
    # ==========================

    def connect_signals(self):

        self.sidebar.page_changed.connect(
            self.change_page
        )

        self.header.back_clicked.connect(
            self.back_clicked.emit
        )

    # ==========================
    # Navigation
    # ==========================

    def change_page(self, page):

        pages = {
            "General": 0,
            "Audio": 1,
            "Appearance": 2,
            "Language": 3,
            "Gameplay": 4,
            "About": 5,
        }

        self.stack.setCurrentIndex(
            pages.get(page, 0)
        )

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()
        height = self.height()

        # Margins
        if width <= 900:
            horizontal_margin = 18
        elif width <= 1150:
            horizontal_margin = 28
        else:
            horizontal_margin = 40

        if height <= 550:
            vertical_margin = 12
            root_spacing = 10
        elif height <= 700:
            vertical_margin = 20
            root_spacing = 16
        else:
            vertical_margin = 30
            root_spacing = 25

        self.root_layout.setContentsMargins(
            horizontal_margin,
            vertical_margin,
            horizontal_margin,
            vertical_margin,
        )

        self.root_layout.setSpacing(
            root_spacing
        )

        # Sidebar Width
        if width <= 850:
            sidebar_width = 160
            body_spacing = 14

        elif width <= 1100:
            sidebar_width = 190
            body_spacing = 20

        else:
            sidebar_width = 220
            body_spacing = 30

        self.sidebar.setFixedWidth(
            sidebar_width
        )

        self.body_layout.setSpacing(
            body_spacing
        )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
