
from PySide6.QtCore import Qt, Signal, QUrl
from PySide6.QtGui import QFont, QDesktopServices
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
    QSizePolicy,
)

from ui.widgets.buttons.primary_button import PrimaryButton
from ui.theme.colors import Colors


class AboutPage(QWidget):

    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setup_ui()

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title = QLabel("UNO! Galaxy")

        self.title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title.setStyleSheet(
            f"""
            color: {Colors.PRIMARY};
            """
        )

        # About Card
        self.card = QFrame()

        self.card.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )

        self.card.setMaximumWidth(420)

        self.card.setStyleSheet(
            f"""
            QFrame {{
                background-color: {Colors.SURFACE};
                border-radius: 18px;
            }}
            """
        )

        self.card_layout = QVBoxLayout(self.card)

        self.version = QLabel("Version 0.2.0")
        self.developer = QLabel("Developer: Ammar")

        self.description = QLabel(
            "One Universe. Every UNO.\n\n"
            "A new UNO experience."
        )

        self.card_labels = [
            self.version,
            self.developer,
            self.description
        ]

        for label in self.card_labels:

            label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            label.setWordWrap(True)

            self.card_layout.addWidget(label)

        # GitHub Button
        self.github_button = PrimaryButton("GitHub")

        self.github_button.clicked.connect(
            self.open_github
        )

        # Back Button
        self.back_button = PrimaryButton("← Back")

        self.back_button.clicked.connect(
            self.back_clicked.emit
        )

        # Main Layout
        self.main_layout.addWidget(self.title)

        self.main_layout.addWidget(
            self.card,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.main_layout.addWidget(
            self.github_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.main_layout.addWidget(
            self.back_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.update_responsive_layout()

    # ==========================
    # GitHub
    # ==========================

    def open_github(self):

        QDesktopServices.openUrl(
            QUrl(
                "https://github.com/ammar7egy-dot/UNO-Galaxy"
            )
        )

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()
        height = self.height()

        if width <= 500:
            title_size = 27
            card_width = max(220, width - 48)
            margin = 14
            spacing = 10
            label_size = 11

        elif width <= 800:
            title_size = 33
            card_width = min(380, width - 60)
            margin = 18
            spacing = 14
            label_size = 12

        else:
            title_size = 40
            card_width = 420
            margin = 22
            spacing = 18
            label_size = 13

        if height <= 500:
            spacing = min(spacing, 8)
            margin = min(margin, 10)

        self.title.setFont(
            QFont(
                "Segoe UI",
                title_size,
                QFont.Weight.Bold
            )
        )

        self.card.setFixedWidth(card_width)

        self.main_layout.setContentsMargins(
            margin,
            margin,
            margin,
            margin
        )

        self.main_layout.setSpacing(spacing)

        self.card_layout.setContentsMargins(
            margin,
            margin,
            margin,
            margin
        )

        self.card_layout.setSpacing(spacing)

        for label in self.card_labels:

            label.setFont(
                QFont(
                    "Segoe UI",
                    label_size
                )
            )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
