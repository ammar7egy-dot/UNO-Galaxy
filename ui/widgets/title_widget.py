
import math

from PySide6.QtCore import (
    Qt,
    QSize,
    Property,
    QPropertyAnimation,
    QEasingCurve,
)

from PySide6.QtGui import (
    QColor,
    QFontMetrics,
    QLinearGradient,
    QPainter,
    QPainterPath,
    QPen,
)

from PySide6.QtWidgets import (
    QWidget,
    QSizePolicy,
)

from ui.theme.fonts import Fonts


class TitleWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.uno_text = "UNO!"
        self.galaxy_text = "G  A  L  A  X  Y"

        self.uno_font = Fonts.title()
        self.galaxy_font = Fonts.galaxy()

        self._shine = -0.35

        # Shine Animation
        self.animation = QPropertyAnimation(
            self,
            b"shinePosition",
        )

        self.animation.setDuration(2500)
        self.animation.setStartValue(-0.35)
        self.animation.setEndValue(1.35)
        self.animation.setLoopCount(-1)

        self.animation.start()

        # Logo Entrance Animation
        self._logo_progress = 0.0

        self.logo_animation = QPropertyAnimation(
            self,
            b"logoProgress",
        )

        self.logo_animation.setDuration(900)

        self.logo_animation.setStartValue(0.0)
        self.logo_animation.setEndValue(1.0)

        self.logo_animation.setEasingCurve(
            QEasingCurve.Type.OutCubic
        )

        self.logo_animation.start()

        # Responsive Size
        self.setMinimumSize(240, 100)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

    def sizeHint(self):
        return QSize(600, 190)

    # ==========================
    # Shine Property
    # ==========================

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

    # ==========================
    # Logo Progress Property
    # ==========================

    def getLogoProgress(self):
        return self._logo_progress

    def setLogoProgress(self, value):
        self._logo_progress = value
        self.update()

    logoProgress = Property(
        float,
        getLogoProgress,
        setLogoProgress,
    )

    # ==========================
    # Responsive Painting
    # ==========================

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        # Keep the original logo proportions.
        design_width = 600
        design_height = 190

        scale = min(
            self.width() / design_width,
            self.height() / design_height,
        )

        scale = min(scale, 1.15)

        if scale <= 0:
            painter.end()
            return

        progress = self._logo_progress

        logo_scale = 0.90 + (0.10 * progress)

        # Center the scaled design.
        painter.save()

        painter.setClipRect(self.rect())

        painter.translate(
            self.width() / 2,
            self.height() / 2,
        )

        painter.scale(
            scale,
            scale,
        )

        painter.translate(
            -design_width / 2,
            -design_height / 2,
        )

        painter.save()

        painter.setOpacity(progress)

        painter.translate(
            design_width / 2,
            design_height / 2,
        )

        painter.scale(
            logo_scale,
            logo_scale,
        )

        painter.translate(
            -design_width / 2,
            -design_height / 2,
        )

        # UNO!
        self.draw_uno(
            painter,
            design_width,
            90,
        )

        # GALAXY
        self.draw_galaxy(
            painter,
            design_width,
            35,
            90,
        )

        painter.restore()
        painter.restore()

        painter.end()

    # ==========================
    # Draw UNO
    # ==========================

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
            widget_width - text_width
        ) / 2

        baseline = font_size + 12

        path = QPainterPath()

        path.addText(
            x,
            baseline,
            self.uno_font,
            self.uno_text,
        )

        # UNO Glow
        glow_layers = [
            (22, 12),
            (18, 20),
            (14, 35),
            (10, 55),
            (6, 90),
        ]

        for width, alpha in glow_layers:

            pen = QPen(
                QColor(
                    255,
                    205,
                    60,
                    alpha,
                ),
                width,
            )

            pen.setJoinStyle(
                Qt.PenJoinStyle.RoundJoin
            )

            painter.setPen(pen)
            painter.drawPath(path)

        # UNO Gradient
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

        # Shine Animation
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
            painter.window(),
            shine,
        )

        painter.restore()

        # UNO Outline
        pen = QPen(
            QColor("#FFFFFF"),
            3,
        )

        pen.setJoinStyle(
            Qt.PenJoinStyle.RoundJoin
        )

        painter.setPen(pen)
        painter.drawPath(path)

        # N Star
        phase = self._shine

        if -0.04 <= phase <= 0.10:

            t = (phase + 0.04) / 0.14

            glow = math.sin(
                t * math.pi
            )

            alpha = int(255 * glow)

            outer = 3.0 + glow * 3.0
            inner = outer * 0.45

            metrics = QFontMetrics(
                self.uno_font
            )

            u_width = metrics.horizontalAdvance("U")
            n_width = metrics.horizontalAdvance("N")

            star_x = (
                x
                + u_width
                + (n_width / 2)
            )

            star_y = (
                baseline
                - font_size * 0.42
            )

            painter.save()

            painter.setPen(
                Qt.PenStyle.NoPen
            )

            star = QPainterPath()

            for i in range(10):

                angle = math.radians(
                    -90 + i * 36
                )

                radius = (
                    outer if i % 2 == 0
                    else inner
                )

                px = (
                    star_x
                    + math.cos(angle) * radius
                )

                py = (
                    star_y
                    + math.sin(angle) * radius
                )

                if i == 0:
                    star.moveTo(px, py)
                else:
                    star.lineTo(px, py)

            star.closeSubpath()

            painter.fillPath(
                star,
                QColor(
                    255,
                    255,
                    255,
                    alpha,
                ),
            )

            painter.restore()

    # ==========================
    # Draw GALAXY
    # ==========================

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

        text_width = metrics.horizontalAdvance(
            self.galaxy_text
        )

        x = (
            widget_width - text_width
        ) / 2

        # Entrance Animation
        progress = self._logo_progress

        offset = int(
            8 * (1 - progress)
        )

        alpha = int(
            255 * progress
        )

        painter.save()

        painter.setOpacity(
            alpha / 255
        )

        y = (
            uno_size
            + galaxy_size
            + 32
            + offset
        )

        gradient = QLinearGradient(
            0,
            y - 20,
            0,
            y + 10,
        )

        gradient.setColorAt(
            0.0,
            QColor("#EAF8FF"),
        )

        gradient.setColorAt(
            0.35,
            QColor("#A9E5FF"),
        )

        gradient.setColorAt(
            0.70,
            QColor("#5AB7FF"),
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

        painter.restore()
