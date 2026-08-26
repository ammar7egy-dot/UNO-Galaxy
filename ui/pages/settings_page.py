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
            color:{Colors.TEXT_SECONDARY};
            """
        )

        layout.addWidget(
            label
        )


class SettingsPage(QWidget):

    back_clicked = SettingsHeader.back_clicked

    def __init__(self):

        super().__init__()

        self.setup_ui()

        self.connect_signals()


    def setup_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(
            40,
            30,
            40,
            30
        )

        root.setSpacing(
            25
        )


        self.header = SettingsHeader()

        root.addWidget(
            self.header
        )


        body = QHBoxLayout()

        body.setSpacing(
            30
        )


        self.sidebar = SettingsSidebar()

        self.sidebar.setFixedWidth(
            220
        )

        body.addWidget(
            self.sidebar
        )


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


        self.stack.addWidget(
            self.general_page
        )

        self.stack.addWidget(
            self.audio_page
        )

        self.stack.addWidget(
            self.appearance_page
        )

        self.stack.addWidget(
            self.language_page
        )

        self.stack.addWidget(
            self.gameplay_page
        )

        self.stack.addWidget(
            self.about_page
        )


        body.addWidget(
            self.stack,
            1
        )


        root.addLayout(
            body
        )


    def connect_signals(self):

        self.sidebar.page_changed.connect(
            self.change_page
        )

        self.header.back_clicked.connect(
            self.back_clicked.emit
        )


    def change_page(
        self,
        page,
    ):

        pages = {

            "General": 0,

            "Audio": 1,

            "Appearance": 2,

            "Language": 3,

            "Gameplay": 4,

            "About": 5,

        }

        self.stack.setCurrentIndex(
            pages.get(
                page,
                0,
            )
        )