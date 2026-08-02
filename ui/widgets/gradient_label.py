from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import (
    QColor,
    QFont,
    QFontMetrics,
    QLinearGradient,
    QPainter,
    QPainterPath,
    QPen,
)
from PySide6.QtWidgets import QWidget


class GradientLabel(QWidget):

    def __init__(
        self,
        text="",
        font_size=64,
        parent=None,
    ):
        super().__init__(parent)

        self.text = text

        self.font = QFont(
            "Segoe UI",
            font_size,
            QFont.Weight.Black,
        )

        self.colors = (
            QColor("#FFE66D"),
            QColor("#FFB703"),
            QColor("#FB8500"),
        )

        self.outline_color = QColor("#FFF8DC")

        self.outline_width = 2

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

    def sizeHint(self):

        metrics = QFontMetrics(self.font)

        return QSize(
            metrics.horizontalAdvance(self.text) + 40,
            metrics.height() + 40,
        )

    def minimumSizeHint(self):
        return self.sizeHint()
    
    def build_path(self):

        metrics = QFontMetrics(self.font)

        width = metrics.horizontalAdvance(self.text)

        x = (self.width() - width) / 2

        y = (
            self.height()
            + metrics.ascent()
            - metrics.descent()
        ) / 2

        path = QPainterPath()

        path.addText(
            x,
            y,
            self.font,
            self.text,
        )

        return path

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.setRenderHint(
            QPainter.RenderHint.TextAntialiasing
        )

        path = self.build_path()

        # ==========================
        # Glow
        # ==========================

        glow_pen = QPen(
            QColor(255, 200, 40, 45)
        )

        glow_pen.setWidth(14)

        glow_pen.setJoinStyle(
            Qt.PenJoinStyle.RoundJoin
        )

        painter.setPen(glow_pen)

        painter.drawPath(path)

        gradient = QLinearGradient(
            0,
            0,
            self.width(),
            0,
        )

        gradient.setColorAt(
            0.0,
            self.colors[0],
        )

        gradient.setColorAt(
            0.5,
            self.colors[1],
        )

        gradient.setColorAt(
            1.0,
            self.colors[2],
        )

        painter.fillPath(
            path,
            gradient,
        )
        
        # ==========================
        # Highlight
        # ==========================

        highlight = QLinearGradient(
            0,
            0,
            0,
            self.height()
        )

        highlight.setColorAt(
            0,
            QColor(255, 255, 255, 120)
        )

        highlight.setColorAt(
            0.45,
            QColor(255, 255, 255, 0)
        )

        painter.fillPath(
            path,
            highlight
        )

        pen = QPen(
            self.outline_color,
            self.outline_width,
        )

        pen.setJoinStyle(
            Qt.PenJoinStyle.RoundJoin
        )

        painter.setPen(pen)

        painter.drawPath(path)