from PySide6.QtCore import (
    Qt,
    QSize,
    Property,
    QPropertyAnimation,
)

from PySide6.QtGui import (
    QColor,
    QFontMetrics,
    QLinearGradient,
    QPainter,
    QPainterPath,
    QPen,
)

from PySide6.QtWidgets import QWidget

from ui.theme.fonts import Fonts


class TitleWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.uno_text = "UNO!"
        self.galaxy_text = "G  A  L  A  X  Y"

        self._shine = -0.35

        self.setMinimumHeight(190)
        self.setMinimumWidth(520)

        self.animation = QPropertyAnimation(
            self,
            b"shinePosition",
        )

        self.animation.setDuration(2500)
        self.animation.setStartValue(-0.35)
        self.animation.setEndValue(1.35)
        self.animation.setLoopCount(-1)
        self.animation.start()

    def sizeHint(self):
        return QSize(600, 190)

    def getShinePosition(self):
        return self._shine

    def setShinePosition(self, value):
        self._shine = value
        self.update()

    shinePosition = Property(
        float,
        getShinePosition,
        setShinePosition,
    )

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        painter.setRenderHint(
            QPainter.RenderHint.TextAntialiasing
        )

        width = self.width()

        uno_size = max(
            48,
            int(width * 0.12),
        )

        galaxy_size = max(
            20,
            int(uno_size * 0.38),
        )

        self.uno_font = Fonts.title(uno_size)
        self.galaxy_font = Fonts.galaxy(galaxy_size)

        self.draw_uno(
            painter,
            width,
            uno_size,
        )

        self.draw_galaxy(
            painter,
            width,
            galaxy_size,
            uno_size,
        )

    def draw_uno(
        self,
        painter,
        widget_width,
        font_size,
    ):

        metrics = QFontMetrics(
            self.uno_font
        )

        text_width = metrics.horizontalAdvance(
            self.uno_text
        )

        x = (
            widget_width
            - text_width
        ) / 2

        baseline = font_size + 12

        path = QPainterPath()

        path.addText(
            x,
            baseline,
            self.uno_font,
            self.uno_text,
        )

        glow = [
            (22, 12),
            (18, 20),
            (14, 35),
            (10, 55),
            (6, 90),
        ]

        for pen_width, alpha in glow:

            pen = QPen(
                QColor(
                    255,
                    205,
                    60,
                    alpha,
                ),
                pen_width,
            )

            pen.setJoinStyle(
                Qt.PenJoinStyle.RoundJoin
            )

            painter.setPen(pen)

            painter.drawPath(path)

        gradient = QLinearGradient(
            0,
            0,
            0,
            baseline,
        )

        gradient.setColorAt(
            0.00,
            QColor("#FFFCE6"),
        )

        gradient.setColorAt(
            0.18,
            QColor("#FFE58A"),
        )

        gradient.setColorAt(
            0.45,
            QColor("#FFD23F"),
        )

        gradient.setColorAt(
            0.72,
            QColor("#FFB703"),
        )

        gradient.setColorAt(
            1.00,
            QColor("#F77F00"),
        )

        painter.fillPath(
            path,
            gradient,
        )
        # ==========================
        # Shine Animation
        # ==========================

        painter.save()

        painter.setClipPath(path)

        shine = QLinearGradient(
            widget_width * self._shine - 120,
            0,
            widget_width * self._shine + 120,
            0,
        )

        shine.setColorAt(
            0.00,
            QColor(255, 255, 255, 0),
        )

        shine.setColorAt(
            0.50,
            QColor(255, 255, 255, 150),
        )

        shine.setColorAt(
            1.00,
            QColor(255, 255, 255, 0),
        )

        painter.fillRect(
            self.rect(),
            shine,
        )

        painter.restore()

        # ==========================
        # Outline
        # ==========================

        pen = QPen(
            QColor("#FFFFFF"),
            3,
        )

        pen.setJoinStyle(
            Qt.PenJoinStyle.RoundJoin
        )

        painter.setPen(pen)

        painter.drawPath(path)

    def draw_galaxy(
        self,
        painter,
        widget_width,
        galaxy_size,
        uno_size,
    ):

        painter.setFont(
            self.galaxy_font
        )

        metrics = QFontMetrics(
            self.galaxy_font
        )

        width = metrics.horizontalAdvance(
            self.galaxy_text
        )

        x = (
            widget_width
            - width
        ) / 2

        y = uno_size + galaxy_size + 32

        gradient = QLinearGradient(
            0,
            y - 20,
            0,
            y + 10,
        )

        gradient.setColorAt(
            0.0,
            QColor("#DDF4FF"),
        )

        gradient.setColorAt(
            0.5,
            QColor("#7ED3FF"),
        )

        gradient.setColorAt(
            1.0,
            QColor("#3B82F6"),
        )

        painter.setPen(
            QPen(
                gradient,
                1,
            )
        )

        painter.drawText(
            int(x),
            int(y),
            self.galaxy_text,
        )