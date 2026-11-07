
from PySide6.QtCore import (
    QTimer,
    QPropertyAnimation,
)

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QGraphicsOpacityEffect,
)

from ui.pages.splash_page import SplashPage
from audio.audio_manager import AudioManager
from ui.profile.player_card_overlay import PlayerCardOverlay


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self._pages_created = False
        self._fade_animation = None

        self.setup_window()

        self.audio = AudioManager()

        self.setup_pages()

        self.start_splash()

    # ==========================
    # Window
    # ==========================

    def setup_window(self):
        self.setWindowTitle("UNO! Galaxy")

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

        self.adjust_window_to_screen()

    def adjust_window_to_screen(self):
        screen = self.screen()

        if screen is None:
            self.resize(1280, 720)
            return

        available = screen.availableGeometry()

        width = min(1280, available.width())
        height = min(720, available.height())

        self.resize(width, height)

        self.move(
            available.center() - self.rect().center()
        )

    # ==========================
    # Pages
    # ==========================

    def setup_pages(self):
        self.stack = QStackedWidget()

        self.splash_page = SplashPage()

        self.stack.addWidget(self.splash_page)

        self.setCentralWidget(self.stack)

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

        # Audio
        self.settings_page.audio_page.set_audio_manager(
            self.audio
        )

        # Add Pages
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.play_page)
        self.stack.addWidget(self.settings_page)
        self.stack.addWidget(self.about_page)

        self.connect_signals()

        self._pages_created = True

    # ==========================
    # Signals
    # ==========================

    def connect_signals(self):
        self.home_page.play_clicked.connect(
            self.show_play_page
        )

        self.home_page.settings_clicked.connect(
            self.show_settings_page
        )

        self.home_page.about_clicked.connect(
            self.show_about_page
        )

        self.play_page.back_button.clicked.connect(
            self.show_home_page
        )

        self.settings_page.back_clicked.connect(
            self.show_home_page
        )

        self.about_page.back_clicked.connect(
            self.show_home_page
        )

        self.home_page.profile_clicked.connect(
            self.show_player_card
        )

    # ==========================
    # Splash
    # ==========================

    def start_splash(self):
        self.stack.setCurrentWidget(self.splash_page)

        QTimer.singleShot(
            3000,
            self.show_home_page
        )

    # ==========================
    # Fade Transition
    # ==========================

    def fade_transition(self, page):
        self.stack.setCurrentWidget(page)

        effect = QGraphicsOpacityEffect(page)

        page.setGraphicsEffect(effect)

        animation = QPropertyAnimation(
            effect,
            b"opacity",
            self
        )

        animation.setDuration(400)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)

        self._fade_animation = animation

        animation.start()

    # ==========================
    # Navigation
    # ==========================

    def show_home_page(self):
        self.create_pages()

        self.fade_transition(self.home_page)

        self.audio.play_music()

    def show_play_page(self):
        self.fade_transition(self.play_page)

    def show_settings_page(self):
        self.fade_transition(self.settings_page)

    def show_about_page(self):
        self.fade_transition(self.about_page)

    # ==========================
    # Profile
    # ==========================

    def show_player_card(self):
        self.player_overlay = PlayerCardOverlay(self)

        self.player_overlay.open()
