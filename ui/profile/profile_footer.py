from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class ProfileFooter(QWidget):

    edit_clicked = Signal()

    def __init__(
        self,
        version="v0.3.0",
        joined="August 2026",
        parent=None,
    ):

        super().__init__(parent)

        self.version = version
        self.joined = joined

        self.setup_ui()


    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setSpacing(
            8
        )


        self.version_label = QLabel(
            f"Version: {self.version}"
        )

        self.version_label.setFont(
            Fonts.body(12)
        )

        self.version_label.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};
            """
        )


        self.joined_label = QLabel(
            f"Joined: {self.joined}"
        )

        self.joined_label.setFont(
            Fonts.body(12)
        )

        self.joined_label.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};
            """
        )


        layout.addWidget(
            self.version_label
        )

        layout.addWidget(
            self.joined_label
        )


        button_layout = QHBoxLayout()

        button_layout.addStretch()


        self.edit_button = QPushButton(
            "Edit Profile"
        )

        self.edit_button.setFixedHeight(
            40
        )

        self.edit_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.edit_button.setStyleSheet(
            f"""
            QPushButton {{

                background:{Colors.PRIMARY};

                color:white;

                border:none;

                border-radius:12px;

                padding:0 25px;

            }}

            QPushButton:hover {{

                background:{Colors.PRIMARY_HOVER};

            }}
            """
        )


        self.edit_button.clicked.connect(
            self.edit_clicked.emit
        )


        button_layout.addWidget(
            self.edit_button
        )


        layout.addLayout(
            button_layout
        )