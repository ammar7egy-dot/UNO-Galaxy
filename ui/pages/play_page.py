
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QSizePolicy,
)


class PlayPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.update_responsive_layout()

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.main_layout.setContentsMargins(
            30, 30, 30, 30
        )

        self.main_layout.setSpacing(20)

        # Title
        self.title = QLabel("Play")

        self.title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title.setFont(
            QFont(
                "Segoe UI",
                30,
                QFont.Weight.Bold,
            )
        )

        # Back Button
        self.back_button = QPushButton("← Back")

        self.back_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.back_button.setMinimumSize(
            110, 38
        )

        self.back_button.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self.main_layout.addWidget(
            self.title
        )

        self.main_layout.addWidget(
            self.back_button,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()
        height = self.height()

        # Title Font
        title_size = int(
            min(width * 0.055, height * 0.09)
        )

        title_size = max(
            20,
            min(36, title_size),
        )

        self.title.setFont(
            QFont(
                "Segoe UI",
                title_size,
                QFont.Weight.Bold,
            )
        )

        # Button Size
        button_width = max(
            110,
            min(180, int(width * 0.16)),
        )

        button_height = max(
            38,
            min(52, int(height * 0.09)),
        )

        self.back_button.setFixedSize(
            button_width,
            button_height,
        )

        # Layout Spacing
        if height <= 500:
            spacing = 10
            margin = 12

        elif height <= 700:
            spacing = 16
            margin = 20

        else:
            spacing = 20
            margin = 30

        self.main_layout.setSpacing(
            spacing
        )

        self.main_layout.setContentsMargins(
            margin,
            margin,
            margin,
            margin,
        )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
