from PySide6.QtCore import (
    Qt,
    QPropertyAnimation,
)

from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QVBoxLayout,
    QGraphicsOpacityEffect,
    QScrollArea,
)

from ui.profile.profile_header import ProfileHeader
from ui.profile.profile_info_widget import ProfileInfoWidget
from ui.profile.stats_grid_widget import StatsGridWidget
from ui.profile.profile_footer import ProfileFooter


class PlayerCardOverlay(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setup_ui()
        self.setup_animation()


    def setup_ui(self):

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )


        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        self.card = QFrame()

        self.card.setFixedSize(
            560,
            720
        )

        self.card.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground
        )

        self.card.setStyleSheet(
            """
            QFrame {
                background-color: #1E1E1E;
                border: none;
                border-radius: 24px;
            }
            """
        )


        card_layout = QVBoxLayout(
            self.card
        )

        card_layout.setContentsMargins(
            25,
            20,
            25,
            20
        )

        card_layout.setSpacing(
            15
        )


        self.header = ProfileHeader()

        self.header.close_clicked.connect(
            self.close_overlay
        )

        card_layout.addWidget(
            self.header
        )


        self.scroll = QScrollArea()

        self.scroll.setWidgetResizable(
            True
        )

        self.scroll.setFrameShape(
            QFrame.Shape.NoFrame
        )

        self.scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        self.scroll.viewport().setStyleSheet(
            """
            QWidget {
                background: transparent;
                border: none;
            }
            """
        )

        self.scroll.setStyleSheet(
            """
            QScrollArea {
                background: transparent;
                border: none;
            }

            QScrollBar:vertical {
                width: 5px;
                background: transparent;
            }

            QScrollBar::handle:vertical {
                background: #4F46E5;
                border-radius: 3px;
            }
            """
        )


        self.content = QWidget()

        self.content.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )


        content_layout = QVBoxLayout(
            self.content
        )

        content_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        content_layout.setSpacing(
            18
        )


        self.profile_info = ProfileInfoWidget()

        content_layout.addWidget(
            self.profile_info
        )


        self.stats = StatsGridWidget()

        content_layout.addWidget(
            self.stats
        )


        self.footer = ProfileFooter()

        content_layout.addWidget(
            self.footer
        )


        self.scroll.setWidget(
            self.content
        )


        card_layout.addWidget(
            self.scroll
        )


        main_layout.addWidget(
            self.card,
            alignment=Qt.AlignmentFlag.AlignCenter
        )


    def setup_animation(self):

        self.effect = QGraphicsOpacityEffect(
            self
        )

        self.setGraphicsEffect(
            self.effect
        )


        self.fade = QPropertyAnimation(
            self.effect,
            b"opacity"
        )

        self.fade.setDuration(
            250
        )

        self.fade.setStartValue(
            0
        )

        self.fade.setEndValue(
            1
        )


    def open(self):

        if self.parent():

            self.setGeometry(
                self.parent().rect()
            )

        self.show()

        self.raise_()

        self.fade.start()


    def close_overlay(self):

        self.hide()


    def resizeEvent(self, event):

        if self.parent():

            self.setGeometry(
                self.parent().rect()
            )

        super().resizeEvent(event)


    def mousePressEvent(self, event):

        if not self.card.geometry().contains(
            event.position().toPoint()
        ):

            self.close_overlay()