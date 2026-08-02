from PySide6.QtCore import QTimer, QPropertyAnimation
from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QGraphicsOpacityEffect,
)

from ui.pages.splash_page import SplashPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self._pages_created = False

        self.setup_window()
        self.setup_pages()

        self.start_splash()

    def setup_window(self):

        self.setWindowTitle("UNO! Galaxy")

        self.resize(1280, 720)

        self.setMinimumSize(800, 450)

        self.setAutoFillBackground(True)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #050816;
            }

            QStackedWidget {
                background-color: #050816;
            }
        """)

    def setup_pages(self):

        self.stack = QStackedWidget()

        self.splash_page = SplashPage()

        self.stack.addWidget(
            self.splash_page
        )

        self.setCentralWidget(
            self.stack
        )

    def create_pages(self):

        if self._pages_created:
            return

        from ui.pages.home_page import HomePage
        from ui.pages.play_page import PlayPage
        from ui.pages.settings_page import SettingsPage
        from ui.pages.about_page import AboutPage


        self.home_page = HomePage()
        self.play_page = PlayPage()
        self.settings_page = SettingsPage()
        self.about_page = AboutPage()


        self.stack.addWidget(
            self.home_page
        )

        self.stack.addWidget(
            self.play_page
        )

        self.stack.addWidget(
            self.settings_page
        )

        self.stack.addWidget(
            self.about_page
        )


        self.connect_signals()

        self._pages_created = True


    def connect_signals(self):

        self.home_page.play_clicked.connect(
            self.show_play_page
        )

        self.home_page.settings_clicked.connect(
            self.show_settings_page
        )

        self.settings_page.about_clicked.connect(
            self.show_about_page
        )

        self.play_page.back_button.clicked.connect(
            self.show_home_page
        )

        self.settings_page.back_button.clicked.connect(
            self.show_home_page
        )

        self.about_page.back_clicked.connect(
            self.show_settings_page
        )


    def start_splash(self):

        self.stack.setCurrentWidget(
            self.splash_page
        )

        QTimer.singleShot(
            3000,
            self.show_home_page
        )


    def fade_transition(self, page):

        self.stack.setCurrentWidget(page)

        effect = QGraphicsOpacityEffect(page)

        page.setGraphicsEffect(
            effect
        )


        animation = QPropertyAnimation(
            effect,
            b"opacity",
            self
        )

        animation.setDuration(
            400
        )

        animation.setStartValue(
            0.0
        )

        animation.setEndValue(
            1.0
        )


        self._fade_animation = animation

        animation.start()


    def show_home_page(self):

        self.create_pages()

        self.fade_transition(
            self.home_page
        )


    def show_play_page(self):

        self.fade_transition(
            self.play_page
        )


    def show_settings_page(self):

        self.fade_transition(
            self.settings_page
        )


    def show_about_page(self):

        self.fade_transition(
            self.about_page
        )