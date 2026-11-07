
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsCard(QFrame):

    def __init__(self, title, parent=None):

        super().__init__(parent)

        self.title = title

        self.setup_ui()

    def setup_ui(self):

        self.setObjectName("SettingsCard")

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )

        self.setStyleSheet(
            f"""
            QFrame#SettingsCard {{

                background-color: {Colors.SURFACE};

                border: 1px solid rgba(255,255,255,22);

                border-radius: 20px;

            }}

            QFrame#SettingsCard:hover {{

                border: 1px solid rgba(255,255,255,40);

            }}
            """
        )

        self.layout = QVBoxLayout(self)

        self.title_label = QLabel(self.title)

        self.title_label.setStyleSheet(
            f"""
            color: {Colors.TEXT};
            padding-bottom: 4px;
            """
        )

        self.layout.addWidget(
            self.title_label
        )

        self.update_responsive_layout()

    # ==========================
    # Add Widgets
    # ==========================

    def add_widget(self, widget):

        self.layout.addWidget(widget)

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()

        if width <= 450:
            horizontal_margin = 12
            vertical_margin = 14
            spacing = 10
            title_size = 15
            radius = 14

        elif width <= 750:
            horizontal_margin = 18
            vertical_margin = 18
            spacing = 12
            title_size = 17
            radius = 16

        else:
            horizontal_margin = 24
            vertical_margin = 22
            spacing = 16
            title_size = 19
            radius = 20

        self.layout.setContentsMargins(
            horizontal_margin,
            vertical_margin,
            horizontal_margin,
            vertical_margin
        )

        self.layout.setSpacing(spacing)

        self.title_label.setFont(
            Fonts.title(title_size)
        )

        self.setStyleSheet(
            f"""
            QFrame#SettingsCard {{

                background-color: {Colors.SURFACE};

                border: 1px solid rgba(255,255,255,22);

                border-radius: {radius}px;

            }}

            QFrame#SettingsCard:hover {{

                border: 1px solid rgba(255,255,255,40);

            }}
            """
        )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
