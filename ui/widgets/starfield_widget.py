from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QPainter, QLinearGradient
from PySide6.QtWidgets import QWidget

import random


class Star:

    def __init__(self, layer):
        self.layer = layer

        self.x = 0
        self.y = 0

        self.radius = layer + 1

        self.alpha = random.randint(100, 255)

        self.twinkle = random.uniform(0.5, 1.5)

        self.direction = random.choice([-1, 1])

        self.speed = 0.15 * layer

    def randomize(self, w, h):

        self.x = random.uniform(0, w)
        self.y = random.uniform(0, h)


class StarfieldWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )

        self.stars = []

        self.initialized = False

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(16)

        

    def initializeStars(self):

        if self.initialized:
            return

        w = max(1, self.width())
        h = max(1, self.height())

        for _ in range(45):
            star = Star(1)
            star.randomize(w, h)
            self.stars.append(star)

        for _ in range(35):
            star = Star(2)
            star.randomize(w, h)
            self.stars.append(star)

        for _ in range(20):
            star = Star(3)
            star.randomize(w, h)
            self.stars.append(star)

        self.initialized = True

    def showEvent(self, event):

     self.initializeStars()

     super().showEvent(event)

    def resizeEvent(self, event):

        w = max(1, self.width())
        h = max(1, self.height())

        if self.initialized:

            for star in self.stars:

                if star.x > w:
                    star.x = random.uniform(0, w)

                if star.y > h:
                    star.y = random.uniform(0, h)

        super().resizeEvent(event)

    def animate(self):

        if not self.initialized:
            return

        w = max(1, self.width())
        h = max(1, self.height())

        for star in self.stars:

            star.alpha += (
                star.direction * star.twinkle
            )

            if star.alpha >= 255:
                star.alpha = 255
                star.direction = -1

            elif star.alpha <= 90:
                star.alpha = 90
                star.direction = 1

            star.y += star.speed

            if star.y > h:
                star.y = -10
                star.x = random.uniform(0, w)

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        gradient = QLinearGradient(
            0,
            0,
            0,
            self.height(),
        )

        gradient.setColorAt(
            0,
            QColor("#050816"),
        )

        gradient.setColorAt(
            0.5,
            QColor("#0E1630"),
        )

        gradient.setColorAt(
            1,
            QColor("#1A2040"),
        )

        painter.fillRect(
            self.rect(),
            gradient,
        )

        painter.setPen(Qt.PenStyle.NoPen)

        for star in self.stars:

            painter.setBrush(
                QColor(
                    255,
                    255,
                    255,
                    int(star.alpha),
                )
            )

            painter.drawEllipse(
                int(star.x),
                int(star.y),
                star.radius,
                star.radius,
            )