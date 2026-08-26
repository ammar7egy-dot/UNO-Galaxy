from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QPainter,
    QColor,
    QFont,
)
from PySide6.QtWidgets import QWidget

from ui.theme.colors import Colors


class StatCardWidget(QWidget):

    def __init__(
        self,
        title,
        value,
        parent=None,
    ):

        super().__init__(parent)

        self.title = title
        self._value = value

        self.setFixedSize(
            120,
            70,
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )


    def set_value(
        self,
        value,
    ):

        self._value = value

        self.update()


    def paintEvent(
        self,
        event,
    ):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )


        painter.setPen(
            QColor(
                Colors.TEXT_SECONDARY
            )
        )

        painter.setFont(
            QFont(
                "Inter",
                11,
            )
        )

        painter.drawText(
            0,
            15,
            self.width(),
            20,
            Qt.AlignmentFlag.AlignCenter,
            str(self.title),
        )


        painter.setPen(
            QColor(
                Colors.TEXT
            )
        )

        painter.setFont(
            QFont(
                "Inter",
                22,
                QFont.Weight.Bold,
            )
        )


        painter.drawText(
            0,
            35,
            self.width(),
            30,
            Qt.AlignmentFlag.AlignCenter,
            str(self._value),
        )


        painter.end()