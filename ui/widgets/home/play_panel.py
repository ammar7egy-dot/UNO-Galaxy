
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QSizePolicy,
)

from ui.widgets.buttons.play_button import PlayButton


class PlayPanel(QWidget):

    play_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            0, 0, 0, 0
        )

        self.layout.setSpacing(0)

        self.play_button = PlayButton("▶ PLAY")

        self.play_button.setMinimumSize(
            200, 58
        )

        self.play_button.setMaximumSize(
            420, 100
        )

        self.play_button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        self.play_button.clicked.connect(
            self.play_clicked.emit
        )

        self.layout.addWidget(
            self.play_button,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

    # ==========================
    # Responsive
    # ==========================

    def resizeEvent(self, event):

        width = self.width()

        button_width = int(width * 0.45)

        button_width = max(
            200,
            min(420, button_width),
        )

        button_height = int(
            button_width * 0.25
        )

        button_height = max(
            58,
            min(100, button_height),
        )

        self.play_button.setFixedSize(
            button_width,
            button_height,
        )

        super().resizeEvent(event)
