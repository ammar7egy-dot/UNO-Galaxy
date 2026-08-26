from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from ui.widgets.buttons.play_button import PlayButton


class PlayPanel(QWidget):

    play_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(0)

        self.play_button = PlayButton(
            "▶ PLAY"
        )

        self.play_button.setMinimumSize(
            280,
            72,
        )

        self.play_button.clicked.connect(
            self.play_clicked.emit
        )

        layout.addWidget(
            self.play_button,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )