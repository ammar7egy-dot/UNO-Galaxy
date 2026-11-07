
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
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

        self.layout = QHBoxLayout(self)

        self.layout.setContentsMargins(
            0, 0, 0, 0
        )

        self.layout.setSpacing(16)

        self.back_button = IconButton("←")

        self.back_button.clicked.connect(
            self.back_clicked.emit
        )

        self.back_button.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed
        )

        self.layout.addWidget(
            self.back_button
        )

        self.title = QLabel("Settings")

        self.title.setStyleSheet(
            f"color: {Colors.TEXT};"
        )

        self.title.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Preferred
        )

        self.layout.addWidget(
            self.title
        )

        self.layout.addStretch()

        self.update_responsive_layout()

    def update_responsive_layout(self):

        width = self.width()

        if width <= 500:
            button_size = 36
            title_size = 21
            spacing = 10

        elif width <= 800:
            button_size = 40
            title_size = 24
            spacing = 12

        else:
            button_size = 42
            title_size = 28
            spacing = 16

        self.back_button.setFixedSize(
            button_size,
            button_size
        )

        self.title.setFont(
            Fonts.title(title_size)
        )

        self.layout.setSpacing(spacing)

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
