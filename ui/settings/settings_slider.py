from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QSlider,
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


    def setup_ui(
        self,
        value,
        minimum,
        maximum,
    ):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(
            12,
        )


        self.slider = QSlider(
            Qt.Orientation.Horizontal
        )

        self.slider.setRange(
            minimum,
            maximum,
        )

        self.slider.setValue(
            value,
        )

        self.slider.setStyleSheet(
            f"""
            QSlider::groove:horizontal {{
                height:6px;
                background:{Colors.BORDER};
                border-radius:3px;
            }}

            QSlider::sub-page:horizontal {{
                background:{Colors.PRIMARY};
                border-radius:3px;
            }}

            QSlider::handle:horizontal {{
                background:{Colors.TEXT};
                width:16px;
                margin:-5px 0;
                border-radius:8px;
            }}
            """
        )

        layout.addWidget(
            self.slider,
            1,
        )


        self.value_label = QLabel(
            f"{value}%"
        )

        self.value_label.setFont(
            Fonts.body(13)
        )

        self.value_label.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};
            """
        )

        layout.addWidget(
            self.value_label
        )


        self.slider.valueChanged.connect(
            self.update_label
        )


    def update_label(
        self,
        value,
    ):

        self.value_label.setText(
            f"{value}%"
        )


    def value(self):

        return self.slider.value()


    def setValue(
        self,
        value,
    ):

        self.slider.setValue(
            value
        )

        self.update_label(
            value
        )