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

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            20,
            0,
            20,
        )

        layout.setSpacing(12)

        self.title = TitleWidget()

        layout.addWidget(
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

        layout.addWidget(
            self.subtitle,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        layout.addStretch()