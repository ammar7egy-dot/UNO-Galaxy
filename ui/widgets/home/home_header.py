
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts
from ui.widgets.title_widget import TitleWidget


class HomeHeader(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            0, 20, 0, 20
        )

        self.layout.setSpacing(12)

        self.title = TitleWidget()

        self.layout.addWidget(
            self.title,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        self.subtitle = QLabel(
            "One Universe. Every UNO."
        )

        self.subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.subtitle.setFont(
            Fonts.body(14)
        )

        self.subtitle.setStyleSheet(
            f"""
            color: {Colors.TEXT_SECONDARY};
            background: transparent;
            """
        )

        self.layout.addWidget(
            self.subtitle,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        self.layout.addStretch()

    # ==========================
    # Responsive Layout
    # ==========================

    def resizeEvent(self, event):

        width = self.width()
        height = self.height()

        if width <= 900:
            font_size = 12
            spacing = 6
            vertical_margin = 8

        elif width <= 1150:
            font_size = 13
            spacing = 9
            vertical_margin = 14

        else:
            font_size = 14
            spacing = 12
            vertical_margin = 20

        if height <= 550:
            vertical_margin = min(
                vertical_margin, 6
            )

        self.layout.setContentsMargins(
            0,
            vertical_margin,
            0,
            vertical_margin,
        )

        self.layout.setSpacing(spacing)

        self.subtitle.setFont(
            Fonts.body(font_size)
        )

        super().resizeEvent(event)
