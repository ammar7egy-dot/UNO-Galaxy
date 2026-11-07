
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QSizePolicy,
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

        self.trailing = trailing

        self.setup_ui(title)

    def setup_ui(self, title):

        self.layout = QHBoxLayout(self)

        self.title_label = QLabel(title)

        self.title_label.setFont(
            Fonts.body(15)
        )

        self.title_label.setStyleSheet(
            f"""
            color: {Colors.TEXT};
            """
        )

        self.title_label.setWordWrap(True)

        self.title_label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )

        self.layout.addWidget(
            self.title_label,
            1
        )

        if self.trailing is not None:

            self.trailing.setSizePolicy(
                QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Fixed
            )

            self.layout.addWidget(
                self.trailing,
                alignment=Qt.AlignmentFlag.AlignRight
            )

        self.update_responsive_layout()

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()

        if width <= 400:
            vertical_margin = 4
            spacing = 8
            font_size = 12

        elif width <= 650:
            vertical_margin = 5
            spacing = 12
            font_size = 13

        else:
            vertical_margin = 6
            spacing = 16
            font_size = 15

        self.layout.setContentsMargins(
            0,
            vertical_margin,
            0,
            vertical_margin
        )

        self.layout.setSpacing(spacing)

        self.title_label.setFont(
            Fonts.body(font_size)
        )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
