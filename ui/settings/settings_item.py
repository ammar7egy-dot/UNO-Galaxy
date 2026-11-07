
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QPushButton

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsItem(QPushButton):

    clicked_item = Signal(str)

    def __init__(self, text, parent=None):

        super().__init__(text, parent)

        self.page_name = text
        self.active = False

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setMinimumHeight(38)

        self.clicked.connect(
            self.on_clicked
        )

        self.update_responsive_style()
        self.update_style()

    # ==========================
    # Click
    # ==========================

    def on_clicked(self):

        self.clicked_item.emit(
            self.page_name
        )

    # ==========================
    # Active State
    # ==========================

    def set_active(self, active):

        self.active = active

        self.update_style()

    # ==========================
    # Responsive Style
    # ==========================

    def update_responsive_style(self):

        height = self.height()

        if height <= 42:
            font_size = 11
            left_padding = 10

        elif height <= 50:
            font_size = 13
            left_padding = 14

        else:
            font_size = 15
            left_padding = 18

        self.setFont(
            Fonts.body(font_size)
        )

        self.setStyleSheet(
            self.get_style(left_padding)
        )

    # ==========================
    # Style
    # ==========================

    def get_style(self, left_padding):

        if self.active:

            return f"""
            QPushButton {{

                background: rgba(79,70,229,30);

                color: {Colors.TEXT};

                border: none;

                border-left: 4px solid {Colors.PRIMARY};

                border-radius: 12px;

                text-align: left;

                padding-left: {left_padding}px;

                font-weight: 600;

            }}

            QPushButton:hover {{

                background: rgba(79,70,229,42);

            }}

            QPushButton:pressed {{

                background: rgba(79,70,229,54);

            }}
            """

        return f"""
        QPushButton {{

            background: transparent;

            color: {Colors.TEXT_SECONDARY};

            border: none;

            border-left: 4px solid transparent;

            border-radius: 12px;

            text-align: left;

            padding-left: {left_padding}px;

        }}

        QPushButton:hover {{

            background: rgba(255,255,255,10);

            color: {Colors.TEXT};

        }}

        QPushButton:pressed {{

            background: rgba(255,255,255,18);

        }}
        """

    def update_style(self):

        height = max(
            self.height(),
            self.minimumHeight(),
        )

        if height <= 42:
            left_padding = 10

        elif height <= 50:
            left_padding = 14

        else:
            left_padding = 18

        self.setStyleSheet(
            self.get_style(left_padding)
        )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_style()
