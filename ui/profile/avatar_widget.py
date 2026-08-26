from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QPainter,
    QColor,
    QBrush,
    QPen,
)
from PySide6.QtWidgets import QWidget


class AvatarWidget(QWidget):

    def __init__(
        self,
        size=110,
        parent=None,
    ):

        super().__init__(parent)

        self.size = size

        self.setFixedSize(
            size,
            size,
        )


    def paintEvent(
        self,
        event,
    ):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )


        # Circle background

        painter.setBrush(
            QBrush(
                QColor("#4F46E5")
            )
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )


        painter.drawEllipse(
            0,
            0,
            self.size,
            self.size,
        )


        # Inner glow

        painter.setBrush(
            QBrush(
                QColor(
                    255,
                    255,
                    255,
                    40,
                )
            )
        )

        painter.drawEllipse(
            12,
            12,
            self.size - 24,
            self.size - 24,
        )


        # User icon

        painter.setPen(
            QPen(
                QColor("#FFFFFF"),
                3,
            )
        )

        painter.setBrush(
            Qt.BrushStyle.NoBrush
        )


        center = self.size // 2


        painter.drawEllipse(
            center - 18,
            center - 28,
            36,
            36,
        )


        painter.drawArc(
            center - 32,
            center + 5,
            64,
            45,
            0,
            180 * 16,
        )


        painter.end()