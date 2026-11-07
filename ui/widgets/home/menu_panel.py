
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QSizePolicy,
)

from ui.widgets.buttons.primary_button import PrimaryButton


class MenuPanel(QFrame):

    settings_clicked = Signal()
    about_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):

        self.setMinimumWidth(150)
        self.setMaximumWidth(260)

        self.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed,
        )

        self.setStyleSheet("""
            QFrame {
                background: rgba(255,255,255,12);
                border: 1px solid rgba(255,255,255,25);
                border-radius: 16px;
            }
        """)

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            20, 20, 20, 20
        )

        self.layout.setSpacing(12)

        self.settings_button = PrimaryButton(
            "⚙ Settings"
        )

        self.about_button = PrimaryButton(
            "ℹ About"
        )

        self.settings_button.clicked.connect(
            self.settings_clicked.emit
        )

        self.about_button.clicked.connect(
            self.about_clicked.emit
        )

        self.layout.addWidget(self.settings_button)
        self.layout.addWidget(self.about_button)

    def resizeEvent(self, event):

        width = self.width()

        if width <= 180:
            margin = 10
            spacing = 7

        elif width <= 220:
            margin = 14
            spacing = 9

        else:
            margin = 20
            spacing = 12

        self.layout.setContentsMargins(
            margin, margin, margin, margin
        )

        self.layout.setSpacing(spacing)

        super().resizeEvent(event)
