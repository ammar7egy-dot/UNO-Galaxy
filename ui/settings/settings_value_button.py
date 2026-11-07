
from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsValueButton(QPushButton):

    clicked_value = Signal()

    def __init__(self, value="", parent=None):

        super().__init__(parent)

        self.value = value

        self.setup_ui()

        self.clicked.connect(
            self.clicked_value.emit
        )

    def setup_ui(self):

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setMinimumWidth(90)
        self.setMinimumHeight(36)

        self.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )

        self.setStyleSheet(
            """
            QPushButton {

                background: transparent;

                border: none;

                border-radius: 12px;

                padding: 0px 8px;

            }

            QPushButton:hover {

                background: rgba(255,255,255,14);

            }

            QPushButton:pressed {

                background: rgba(255,255,255,25);

            }
            """
        )

        self.layout = QHBoxLayout(self)

        self.layout.setContentsMargins(
            8, 0, 8, 0
        )

        self.value_label = QLabel(
            str(self.value)
        )

        self.value_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.value_label.setStyleSheet(
            f"""
            color: {Colors.TEXT_SECONDARY};
            background: transparent;
            """
        )

        self.value_label.setSizePolicy(
            QSizePolicy.Policy.Ignored,
            QSizePolicy.Policy.Preferred
        )

        self.layout.addWidget(
            self.value_label,
            1
        )

        self.arrow = QLabel("❯")

        self.arrow.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.arrow.setStyleSheet(
            f"""
            color: {Colors.TEXT_SECONDARY};
            background: transparent;
            """
        )

        self.layout.addWidget(
            self.arrow
        )

        self.update_responsive_layout()

    # ==========================
    # Value
    # ==========================

    def set_value(self, value):

        self.value = value

        self.value_label.setText(
            str(value)
        )

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()

        if width <= 110:
            font_size = 11
            arrow_size = 12
            spacing = 4

        elif width <= 160:
            font_size = 12
            arrow_size = 14
            spacing = 8

        else:
            font_size = 14
            arrow_size = 16
            spacing = 12

        self.value_label.setFont(
            Fonts.body(font_size)
        )

        self.arrow.setFont(
            Fonts.body(arrow_size)
        )

        self.layout.setSpacing(spacing)

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
