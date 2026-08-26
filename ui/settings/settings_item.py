from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import QPushButton

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsItem(QPushButton):

    clicked_item = Signal(str)

    def __init__(
        self,
        text,
        parent=None,
    ):

        super().__init__(text, parent)

        self.page_name = text
        self.active = False

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setFixedHeight(48)

        self.setFont(
            Fonts.body(15)
        )

        self.clicked.connect(
            self.on_clicked
        )

        self.update_style()


    def on_clicked(self):

        self.clicked_item.emit(
            self.page_name
        )


    def set_active(
        self,
        active,
    ):

        self.active = active

        self.update_style()


    def update_style(self):

        if self.active:

            self.setStyleSheet(
                f"""
                QPushButton {{

                    background: rgba(79,70,229,30);

                    color: {Colors.TEXT};

                    border: none;

                    border-left: 4px solid {Colors.PRIMARY};

                    border-radius: 12px;

                    text-align: left;

                    padding-left: 18px;

                    font-weight: 600;

                }}

                QPushButton:hover {{

                    background: rgba(79,70,229,42);

                }}

                QPushButton:pressed {{

                    background: rgba(79,70,229,54);

                }}
                """
            )

        else:

            self.setStyleSheet(
                f"""
                QPushButton {{

                    background: transparent;

                    color: {Colors.TEXT_SECONDARY};

                    border: none;

                    border-left: 4px solid transparent;

                    border-radius: 12px;

                    text-align: left;

                    padding-left: 18px;

                }}

                QPushButton:hover {{

                    background: rgba(255,255,255,10);

                    color: {Colors.TEXT};

                }}

                QPushButton:pressed {{

                    background: rgba(255,255,255,18);

                }}
                """
            )