from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QLabel,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsValueButton(QPushButton):

    clicked_value = Signal()

    def __init__(
        self,
        value="",
        parent=None,
    ):

        super().__init__(parent)

        self.value = value

        self.setup_ui()

        self.clicked.connect(
            self.clicked_value.emit
        )


    def setup_ui(self):

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setMinimumWidth(
            150
        )

        self.setFixedHeight(
            42
        )


        self.setStyleSheet(
            f"""
            QPushButton {{

                background: transparent;

                border: none;

                border-radius: 12px;

                padding: 0px 8px;

            }}

            QPushButton:hover {{

                background: rgba(255,255,255,14);

            }}

            QPushButton:pressed {{

                background: rgba(255,255,255,25);

            }}
            """
        )


        layout = QHBoxLayout(
            self
        )

        layout.setContentsMargins(
            8,
            0,
            8,
            0
        )

        layout.setSpacing(
            12
        )


        self.value_label = QLabel(
            self.value
        )

        self.value_label.setFont(
            Fonts.body(14)
        )

        self.value_label.setAlignment(
            Qt.AlignmentFlag.AlignRight |
            Qt.AlignmentFlag.AlignVCenter
        )

        self.value_label.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};

            background:transparent;
            """
        )


        layout.addWidget(
            self.value_label,
            1
        )


        # Arrow

        self.arrow = QLabel(
            "❯"
        )

        self.arrow.setFont(
            Fonts.body(16)
        )

        self.arrow.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.arrow.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};

            background:transparent;
            """
        )


        layout.addWidget(
            self.arrow
        )


    def set_value(
        self,
        value,
    ):

        self.value = value

        self.value_label.setText(
            value
        )