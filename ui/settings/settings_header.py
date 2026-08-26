from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)

from ui.widgets.buttons.icon_button import IconButton

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsHeader(QWidget):

    back_clicked = Signal()

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setup_ui()


    def setup_ui(self):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(
            16
        )


        self.back_button = IconButton("←")

        self.back_button.setFixedSize(
            42,
            42
        )

        self.back_button.clicked.connect(
            self.back_clicked.emit
        )

        layout.addWidget(
            self.back_button
        )


        self.title = QLabel(
            "Settings"
        )

        self.title.setFont(
            Fonts.title(28)
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