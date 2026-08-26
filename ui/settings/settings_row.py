from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsRow(QWidget):

    def __init__(
        self,
        title,
        trailing=None,
        parent=None,
    ):

        super().__init__(parent)

        self.setup_ui(
            title,
            trailing,
        )


    def setup_ui(
        self,
        title,
        trailing,
    ):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            0,
            6,
            0,
            6,
        )

        layout.setSpacing(
            16,
        )


        self.title_label = QLabel(
            title
        )

        self.title_label.setFont(
            Fonts.body(15)
        )

        self.title_label.setStyleSheet(
            f"""
            color:{Colors.TEXT};
            """
        )

        layout.addWidget(
            self.title_label
        )


        layout.addStretch()


        if trailing is not None:

            layout.addWidget(
                trailing,
                alignment=Qt.AlignmentFlag.AlignRight,
            )