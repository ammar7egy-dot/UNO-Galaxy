from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import (
    QColor,
    QPainter,
    QLinearGradient,
    QRadialGradient,
)
from PySide6.QtWidgets import QWidget

import random
import math


class Star:

    COLORS = [
        QColor(255, 255, 255),
        QColor(180, 220, 255),
        QColor(210, 190, 255),
    ]


    def __init__(self, layer):

        self.layer = layer

        self.x = 0
        self.y = 0

        if layer == 1:

            self.radius = random.choice(
                [1, 1, 2]
            )

        elif layer == 2:

            self.radius = random.choice(
                [2, 2, 3]
            )

        else:

            self.radius = random.choice(
                [3, 4, 5]
            )


        self.alpha = random.randint(
            100,
            255
        )

        self.twinkle = random.uniform(
            0.4,
            1.8
        )

        self.direction = random.choice(
            [-1, 1]
        )

        self.speed = (
            0.08 * layer
            +
            random.uniform(
                0,
                0.08
            )
        )


        self.color = random.choice(
            self.COLORS
        )


        self.glow = (
            layer >= 3
        )


    def randomize(
        self,
        width,
        height
    ):

        self.x = random.uniform(
            0,
            width
        )

        self.y = random.uniform(
            0,
            height
        )



class DustParticle:

    def __init__(self):

        self.x = 0
        self.y = 0

        self.size = random.uniform(
            0.5,
            2
        )

        self.alpha = random.randint(
            20,
            80
        )

        self.speed = random.uniform(
            0.02,
            0.08
        )


    def randomize(
        self,
        width,
        height
    ):

        self.x = random.uniform(
            0,
            width
        )

        self.y = random.uniform(
            0,
            height
        )


class ShootingStar:

    def __init__(self):

        self.active = False

        self.x = 0
        self.y = 0

        self.length = random.randint(
            80,
            160
        )

        self.speed = random.uniform(
            8,
            14
        )

        self.angle = random.uniform(
    math.radians(150),
    math.radians(170)
    )
        self.alpha = 0


    def start(
        self,
        width,
        height
    ):

        self.active = True

        self.x = random.randint(
            0,
            width
        )

        self.y = random.randint(
            0,
            height // 2
        )

        self.alpha = 255

    def update(self):

        if not self.active:
            return


        self.x += (
            math.cos(self.angle)
            *
            self.speed
        )

        self.y += (
            math.sin(self.angle)
            *
            self.speed
        )


        self.alpha -= 8


        if self.alpha <= 0:

            self.active = False



class StarfieldWidget(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)


        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )


        self.stars = []

        self.dust_particles = []


        self.shooting_star = ShootingStar()


        self.initialized = False


        self.shooting_timer = 0



        self.timer = QTimer(self)


        self.timer.timeout.connect(
            self.animate
        )


        self.timer.start(16)



    def initializeStars(self):

        if self.initialized:
            return


        width = max(
            1,
            self.width()
        )

        height = max(
            1,
            self.height()
        )


        for _ in range(60):

            star = Star(1)

            star.randomize(
                width,
                height
            )

            self.stars.append(
                star
            )



        for _ in range(30):

            star = Star(2)

            star.randomize(
                width,
                height
            )

            self.stars.append(
                star
            )



        for _ in range(10):

            star = Star(3)

            star.randomize(
                width,
                height
            )

            self.stars.append(
                star
            )



        for _ in range(80):

            dust = DustParticle()

            dust.randomize(
                width,
                height
            )

            self.dust_particles.append(
                dust
            )


        self.initialized = True

    def animate(self):

     if not self.initialized:
        return

     width = max(1, self.width())
     height = max(1, self.height())

    # Stars

     for star in self.stars:

        star.alpha += (
            star.direction *
            star.twinkle
        )

        if star.alpha >= 255:

            star.alpha = 255
            star.direction = -1

        elif star.alpha <= 70:

            star.alpha = 70
            star.direction = 1

        star.y += star.speed

        if star.y > height:

            star.y = -10
            star.x = random.uniform(
                0,
                width
            )

    # Dust

     for dust in self.dust_particles:

        dust.y += dust.speed

        if dust.y > height:

            dust.y = -5
            dust.x = random.uniform(
                0,
                width
            )

    # Shooting Star

     self.shooting_timer += 1

     if (
        self.shooting_timer > 900
        and not self.shooting_star.active
    ):

        self.shooting_star.start(
            width,
            height
        )

        self.shooting_timer = 0

     self.shooting_star.update()

     self.update()


    def showEvent(self, event):

        self.initializeStars()

        super().showEvent(event)

    def resizeEvent(self, event):

        width = max(
            1,
            self.width()
        )

        height = max(
            1,
            self.height()
        )


        if self.initialized:

            # إعادة توزيع النجوم لتغطي الشاشة الجديدة
            for star in self.stars:

                star.x = random.uniform(
                    0,
                    width
                )

                star.y = random.uniform(
                    0,
                    height
                )


            # إعادة توزيع الغبار
            for dust in self.dust_particles:

                dust.x = random.uniform(
                    0,
                    width
                )

                dust.y = random.uniform(
                    0,
                    height
                )


        self.update()

        super().resizeEvent(event)

    def paintEvent(self, event):

     painter = QPainter(self)

     painter.setRenderHint(
        QPainter.RenderHint.Antialiasing
    )

    # ======================
    # Background
    # ======================

     gradient = QLinearGradient(
        0,
        0,
        0,
        self.height()
    )

     gradient.setColorAt(
        0.0,
        QColor("#02030A")
    )

     gradient.setColorAt(
        0.25,
        QColor("#070B18")
    )

     gradient.setColorAt(
        0.55,
        QColor("#101B3A")
    )

     gradient.setColorAt(
        0.8,
        QColor("#16244A")
    )

     gradient.setColorAt(
        1.0,
        QColor("#080D20")
    )

     painter.fillRect(
        self.rect(),
        gradient
    )

    # ======================
    # Nebula
    # ======================

     nebula_data = [

        (
            self.width() * 0.2,
            self.height() * 0.25,
            280,
            QColor(80, 120, 255, 35)
        ),

        (
            self.width() * 0.8,
            self.height() * 0.35,
            250,
            QColor(170, 90, 255, 25)
        ),

        (
            self.width() * 0.5,
            self.height() * 0.75,
            320,
            QColor(40, 180, 255, 20)
        )

    ]

     for x, y, radius, color in nebula_data:

        nebula = QRadialGradient(
            x,
            y,
            radius
        )

        nebula.setColorAt(
            0,
            color
        )

        nebula.setColorAt(
            1,
            QColor(
                0,
                0,
                0,
                0
            )
        )

        painter.fillRect(
            self.rect(),
            nebula
        )

     painter.setPen(
        Qt.PenStyle.NoPen
    )

    # ======================
    # Dust
    # ======================

     for dust in self.dust_particles:

        painter.setBrush(
            QColor(
                180,
                210,
                255,
                dust.alpha
            )
        )

        painter.drawEllipse(
            int(dust.x),
            int(dust.y),
            int(dust.size),
            int(dust.size)
        )

    # ======================
    # Stars
    # ======================

     for star in self.stars:

        if star.glow:

            glow = QRadialGradient(
                star.x,
                star.y,
                star.radius * 5
            )

            glow.setColorAt(
                0,
                QColor(
                    star.color.red(),
                    star.color.green(),
                    star.color.blue(),
                    int(star.alpha * 0.45)
                )
            )

            glow.setColorAt(
                1,
                QColor(
                    0,
                    0,
                    0,
                    0
                )
            )

            painter.setBrush(
                glow
            )

            painter.drawEllipse(
                int(star.x - star.radius * 5),
                int(star.y - star.radius * 5),
                star.radius * 10,
                star.radius * 10
            )

        painter.setBrush(
            QColor(
                star.color.red(),
                star.color.green(),
                star.color.blue(),
                int(star.alpha)
            )
        )

        painter.drawEllipse(
            int(star.x),
            int(star.y),
            star.radius,
            star.radius
        )

    # ======================
    # Shooting Star
    # ======================

     if self.shooting_star.active:

        star = self.shooting_star

        painter.setPen(
            QColor(
                255,
                255,
                255,
                star.alpha
            )
        )

        painter.drawLine(
            int(star.x),
            int(star.y),
            int(
                star.x -
                math.cos(star.angle)
                * star.length
            ),
            int(
                star.y -
                math.sin(star.angle)
                * star.length
            )
        )