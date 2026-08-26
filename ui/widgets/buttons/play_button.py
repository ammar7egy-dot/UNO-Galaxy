from PySide6.QtCore import (
    Qt,
    Property,
    QPropertyAnimation,
    QEasingCurve,
)
from PySide6.QtGui import (
    QColor,
    QLinearGradient,
    QPainter,
)
from PySide6.QtWidgets import QPushButton

from ui.theme.colors import Colors


class PlayButton(QPushButton):

    def __init__(self, text="PLAY", parent=None):
        super().__init__(text, parent)

        self._shine_position = -0.35

        self.setMouseTracking(True)

        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {Colors.PRIMARY};
                color: {Colors.TEXT};

                border: 2px solid rgba(255, 255, 255, 35);
                border-radius: 20px;

                padding: 12px 40px;

                font-size: 18px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: {Colors.PRIMARY_HOVER};
                border: 2px solid rgba(255, 255, 255, 90);
            }}

            QPushButton:pressed {{
                background-color: {Colors.PRIMARY_PRESSED};
            }}
            """
        )

        self.shine_animation = QPropertyAnimation(
            self,
            b"shinePosition",
            self
        )

        self.shine_animation.setDuration(450)

        self.shine_animation.setStartValue(-0.35)
        self.shine_animation.setEndValue(1.35)

        self.shine_animation.setEasingCurve(
            QEasingCurve.Type.InOutCubic
        )

    def get_shine_position(self):
        return self._shine_position

    def set_shine_position(self, value):
        self._shine_position = value
        self.update()

    shinePosition = Property(
        float,
        get_shine_position,
        set_shine_position
    )

    def enterEvent(self, event):

        self.shine_animation.stop()

        self._shine_position = -0.35

        self.shine_animation.start()

        super().enterEvent(event)

    def leaveEvent(self, event):

        self.shine_animation.stop()

        self._shine_position = -0.35

        self.update()

        super().leaveEvent(event)

    def paintEvent(self, event):

     super().paintEvent(event)

     painter = QPainter(self)

     painter.setRenderHint(
        QPainter.RenderHint.Antialiasing
    )

    # ======================
    # Glass Reflection
    # ======================

     glass = QLinearGradient(
        0,
        0,
        0,
        self.height() * 0.55,
    )

     glass.setColorAt(
        0.0,
        QColor(255, 255, 255, 70)
    )

     glass.setColorAt(
        0.18,
        QColor(255, 255, 255, 28)
    )

     glass.setColorAt(
        0.45,
        QColor(255, 255, 255, 10)
    )

     glass.setColorAt(
        1.0,
        QColor(255, 255, 255, 0)
    )

     painter.setPen(Qt.PenStyle.NoPen)

     painter.setBrush(glass)

     painter.drawRoundedRect(
        self.rect().adjusted(
            4,
            4,
            -4,
            -self.height() // 2,
        ),
        16,
        16,
    )

    # ======================
    # Premium Shine
    # ======================

     if self._shine_position >= -0.3:

        painter.setClipRect(
            self.rect().adjusted(
                2,
                2,
                -2,
                -2,
            )
        )

        width = self.width()
        height = self.height()

        shine_x = self._shine_position * width

        shine_width = int(width * 0.22)

        gradient = QLinearGradient(
            shine_x - shine_width,
            -height * 0.3,
            shine_x + shine_width,
            height * 1.3,
        )

        gradient.setColorAt(
            0.00,
            QColor(255, 255, 255, 0)
        )

        gradient.setColorAt(
            0.35,
            QColor(255, 255, 255, 15)
        )

        gradient.setColorAt(
            0.46,
            QColor(255, 255, 255, 70)
        )

        gradient.setColorAt(
            0.50,
            QColor(255, 255, 255, 190)
        )

        gradient.setColorAt(
            0.54,
            QColor(255, 255, 255, 70)
        )

        gradient.setColorAt(
            0.65,
            QColor(255, 255, 255, 15)
        )

        gradient.setColorAt(
            1.00,
            QColor(255, 255, 255, 0)
        )

        painter.fillRect(
            self.rect(),
            gradient,
        )

     painter.end()