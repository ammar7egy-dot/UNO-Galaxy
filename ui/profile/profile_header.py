from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class ProfileHeader(QWidget):

    close_clicked = Signal()

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setup_ui()


    def setup_ui(self):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.title = QLabel(
            "PLAYER PROFILE"
        )

        self.title.setFont(
            Fonts.galaxy(22)
        )

        self.title.setStyleSheet(
            f"""
            color:{Colors.TEXT};
            """
        )

        layout.addWidget(
            self.title
        )

        layout.addStretch()


        self.close_button = QPushButton(
            "✕"
        )

        self.close_button.setFixedSize(
            36,
            36,
        )

        self.close_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.close_button.setStyleSheet(
            f"""
            QPushButton {{

                background:{Colors.SECONDARY};

                color:{Colors.TEXT};

                border:none;

                border-radius:18px;

                font-size:18px;

            }}

            QPushButton:hover {{

                background:{Colors.PRIMARY};

            }}
            """
        )

        self.close_button.clicked.connect(
            self.close_clicked.emit
        )

        layout.addWidget(
            self.close_button
        )