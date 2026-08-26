from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsCard(QFrame):

    def __init__(
        self,
        title,
        parent=None,
    ):

        super().__init__(parent)

        self.title = title

        self.setup_ui()


    def setup_ui(self):

        self.setObjectName(
            "SettingsCard"
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

        self.layout.setContentsMargins(
            24,
            22,
            24,
            22,
        )

        self.layout.setSpacing(
            16,
        )


        self.title_label = QLabel(
            self.title
        )

        self.title_label.setFont(
            Fonts.title(19)
        )

        self.title_label.setStyleSheet(
            f"""
            color: {Colors.TEXT};
            padding-bottom: 4px;
            """
        )

        self.layout.addWidget(
            self.title_label
        )


    def add_widget(
        self,
        widget,
    ):

        self.layout.addWidget(
            widget
        )