from PySide6.QtCore import Qt, Signal, QUrl
from PySide6.QtGui import QFont, QDesktopServices
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame,
)

from ui.widgets.buttons.primary_button import PrimaryButton
from ui.theme.colors import Colors


class AboutPage(QWidget):

    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(18)

        title = QLabel(
            "UNO! Galaxy"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setFont(
            QFont(
                "Segoe UI",
                40,
                QFont.Weight.Bold
            )
        )

        title.setStyleSheet(
            f"""
            color: {Colors.PRIMARY};
            """
        )


        card = QFrame()

        card.setFixedWidth(
            420
        )

        card.setStyleSheet(
            f"""
            QFrame {{
                background-color: {Colors.SURFACE};
                border-radius: 18px;
                padding: 20px;
            }}
            """
        )


        card_layout = QVBoxLayout(card)

        version = QLabel(
            "Version 0.1.0"
        )

        developer = QLabel(
            "Developer: Ammar"
        )

        description = QLabel(
            "One Universe. Every UNO.\n\n"
            "A new UNO experience."
        )

        for label in [
            version,
            developer,
            description
        ]:
            label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            card_layout.addWidget(
                label
            )


        self.github_button = PrimaryButton(
            "GitHub"
        )

        self.github_button.clicked.connect(
            self.open_github
        )


        self.back_button = PrimaryButton(
            "← Back"
        )

        self.back_button.clicked.connect(
            self.back_clicked.emit
        )


        layout.addWidget(
            title
        )

        layout.addWidget(
            card
        )

        layout.addWidget(
            self.github_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            self.back_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )


    def open_github(self):

        QDesktopServices.openUrl(
            QUrl(
                "https://github.com/ammar7egy-dot/UNO-Galaxy"
            )
        )