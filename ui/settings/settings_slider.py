
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSlider,
    QSizePolicy,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class SettingsSlider(QWidget):

    def __init__(
        self,
        value=80,
        minimum=0,
        maximum=100,
        parent=None,
    ):

        super().__init__(parent)

        self.setup_ui(
            value,
            minimum,
            maximum,
        )

    # ==========================
    # UI
    # ==========================

    def setup_ui(
        self,
        value,
        minimum,
        maximum,
    ):

        self.layout = QHBoxLayout(self)

        self.layout.setContentsMargins(
            0, 0, 0, 0
        )

        self.slider = QSlider(
            Qt.Orientation.Horizontal
        )

        self.slider.setRange(
            minimum,
            maximum
        )

        self.slider.setValue(value)

        self.slider.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        self.layout.addWidget(
            self.slider,
            1
        )

        self.value_label = QLabel(
            f"{value}%"
        )

        self.value_label.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.value_label.setMinimumWidth(36)

        self.value_label.setStyleSheet(
            f"""
            color: {Colors.TEXT_SECONDARY};
            background: transparent;
            """
        )

        self.layout.addWidget(
            self.value_label
        )

        self.slider.valueChanged.connect(
            self.update_label
        )

        self.update_responsive_layout()

    # ==========================
    # Slider Style
    # ==========================

    def update_slider_style(
        self,
        groove_height,
        handle_size,
        handle_margin,
    ):

        self.slider.setStyleSheet(
            f"""
            QSlider::groove:horizontal {{

                height: {groove_height}px;

                background: {Colors.BORDER};

                border-radius: {groove_height // 2}px;

            }}

            QSlider::sub-page:horizontal {{

                background: {Colors.PRIMARY};

                border-radius: {groove_height // 2}px;

            }}

            QSlider::handle:horizontal {{

                background: {Colors.TEXT};

                width: {handle_size}px;

                margin: -{handle_margin}px 0;

                border-radius: {handle_size // 2}px;

            }}
            """
        )

    # ==========================
    # Label
    # ==========================

    def update_label(self, value):

        self.value_label.setText(
            f"{value}%"
        )

    # ==========================
    # Value Methods
    # ==========================

    def value(self):

        return self.slider.value()

    def setValue(self, value):

        self.slider.setValue(value)

        self.update_label(value)

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()

        if width <= 250:
            spacing = 6
            font_size = 11
            groove_height = 4
            handle_size = 12
            handle_margin = 4

        elif width <= 400:
            spacing = 9
            font_size = 12
            groove_height = 5
            handle_size = 14
            handle_margin = 5

        else:
            spacing = 12
            font_size = 13
            groove_height = 6
            handle_size = 16
            handle_margin = 5

        self.layout.setSpacing(spacing)

        self.value_label.setFont(
            Fonts.body(font_size)
        )

        self.update_slider_style(
            groove_height,
            handle_size,
            handle_margin
        )

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
