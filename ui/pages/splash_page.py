from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
    QGraphicsOpacityEffect,
)

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts

from ui.widgets.title_widget import TitleWidget
from ui.widgets.starfield_widget import StarfieldWidget


class SplashPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.start_animation()


    def setup_ui(self):

        self.setStyleSheet("""
            background-color: transparent;
        """)


        # ==========================
        # Star Background
        # ==========================

        self.stars = StarfieldWidget(self)

        self.stars.lower()


        # ==========================
        # Content
        # ==========================

        self.content = QWidget(self)

        layout = QVBoxLayout(
            self.content
        )

        layout.setContentsMargins(
            60,
            40,
            60,
            40
        )


        layout.addStretch()


        self.title = TitleWidget()

        layout.addWidget(
            self.title,
            alignment=Qt.AlignmentFlag.AlignCenter
        )


        layout.addSpacing(10)


        self.subtitle = QLabel(
            "One Universe. Every UNO."
        )

        self.subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.subtitle.setFont(
            Fonts.body(14)
        )

        self.subtitle.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};
            """
        )


        layout.addWidget(
            self.subtitle,
            alignment=Qt.AlignmentFlag.AlignCenter
        )


        layout.addSpacing(35)


        self.loading = QProgressBar()

        self.loading.setRange(
            0,
            0
        )

        self.loading.setFixedSize(
            260,
            8
        )


        self.loading.setStyleSheet(
            f"""
            QProgressBar {{
                background:{Colors.SURFACE};
                border:none;
                border-radius:4px;
            }}

            QProgressBar::chunk {{
                background:{Colors.PRIMARY};
                border-radius:4px;
            }}
            """
        )


        layout.addWidget(
            self.loading,
            alignment=Qt.AlignmentFlag.AlignCenter
        )


        layout.addStretch()


        self.version = QLabel(
            "Version 0.2.0"
        )

        self.version.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.version.setFont(
            Fonts.body(10)
        )

        self.version.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};
            """
        )


        layout.addWidget(
            self.version
        )


    def resizeEvent(self, event):

        self.stars.setGeometry(
            self.rect()
        )

        self.content.setGeometry(
            self.rect()
        )


        super().resizeEvent(event)


    def showEvent(self, event):

        self.stars.setGeometry(
            self.rect()
        )

        self.content.setGeometry(
            self.rect()
        )


        super().showEvent(event)


    def start_animation(self):

        self.effect = QGraphicsOpacityEffect()

        self.content.setGraphicsEffect(
            self.effect
        )


        self.effect.setOpacity(
            0.35
        )


        self.animation = QPropertyAnimation(
            self.effect,
            b"opacity",
        )


        self.animation.setDuration(
            800
        )


        self.animation.setStartValue(
            0.35
        )


        self.animation.setEndValue(
            1.0
        )


        self.animation.start()