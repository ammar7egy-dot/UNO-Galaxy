from PySide6.QtCore import (
    QTimer,
    QPropertyAnimation,
)

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QGraphicsOpacityEffect,
)

from ui.pages.splash_page import SplashPage
from audio.audio_manager import AudioManager
from ui.profile.player_card_overlay import PlayerCardOverlay

from game.settings_manager import SettingsManager


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.settings = SettingsManager()

        self._pages_created = False

        self.ui_scale = 1.0

        self.setup_window()

        self.audio = AudioManager()

        self.setup_pages()

        self.load_ui_scale()

        self.start_splash()


    # ==========================
    # Window
    # ==========================

    def setup_window(self):

        self.setWindowTitle(
            "UNO! Galaxy"
        )

        self.resize(
            1280,
            720
        )

        self.setMinimumSize(
            800,
            450
        )

        self.setAutoFillBackground(
            True
        )

        self.setStyleSheet(
            """
            QMainWindow {

                background-color: #050816;

            }

            QStackedWidget {

                background-color: #050816;

            }
            """
        )


    # ==========================
    # Pages
    # ==========================

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


        # ==========================
        # Audio
        # ==========================

        self.settings_page.audio_page.set_audio_manager(
            self.audio
        )


        # ==========================
        # Add Pages
        # ==========================

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


        # تطبيق UI Scale بعد إنشاء الصفحات
        self.apply_ui_scale(
            self.ui_scale,
            save=False
        )


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
    # UI Scale
    # ==========================

    def load_ui_scale(self):

        scale = self.settings.get(
            "general",
            "ui_scale"
        )

        self.apply_ui_scale(
            scale,
            save=False
        )


    def apply_ui_scale(
        self,
        scale,
        save=True,
    ):

        # دعم 80 أو "80%"
        if isinstance(
            scale,
            str
        ):

            try:

                numeric_scale = float(
                    scale.replace(
                        "%",
                        ""
                    )
                )

            except ValueError:

                numeric_scale = 100

        else:

            numeric_scale = float(
                scale
            )


        numeric_scale = max(
            80,
            min(
                125,
                numeric_scale
            )
        )


        self.ui_scale = (
            numeric_scale / 100.0
        )


        # ==========================
        # Save
        # ==========================

        if save:

            self.settings.set(
                "general",
                "ui_scale",
                f"{int(numeric_scale)}%"
            )


        # ==========================
        # Application Font
        # ==========================

        app = QApplication.instance()

        if app:

            base_font = app.font()

            base_size = 10

            new_size = max(
                8,
                round(
                    base_size
                    * self.ui_scale
                )
            )

            base_font.setPointSize(
                new_size
            )

            app.setFont(
                base_font
            )


        # ==========================
        # Window Size
        # ==========================

        base_width = 1280
        base_height = 720

        new_width = int(
            base_width
            * self.ui_scale
        )

        new_height = int(
            base_height
            * self.ui_scale
        )


        minimum_width = int(
            800
            * self.ui_scale
        )

        minimum_height = int(
            450
            * self.ui_scale
        )


        self.setMinimumSize(
            max(
                800,
                minimum_width
            ),
            max(
                450,
                minimum_height
            )
        )


        # لا نغير الحجم إذا كانت النافذة مكبرة
        if not self.isMaximized():

            self.resize(
                max(
                    800,
                    new_width
                ),
                max(
                    450,
                    new_height
                )
            )


        # ==========================
        # Refresh Pages
        # ==========================

        if self._pages_created:

            self.settings_page.general_page.refresh_settings()


    # ==========================
    # Splash
    # ==========================

    def start_splash(self):

        self.stack.setCurrentWidget(
            self.splash_page
        )

        QTimer.singleShot(
            3000,
            self.show_home_page
        )


    # ==========================
    # Fade Transition
    # ==========================

    def fade_transition(
        self,
        page,
    ):

        self.stack.setCurrentWidget(
            page
        )


        effect = QGraphicsOpacityEffect(
            page
        )

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


    # ==========================
    # Navigation
    # ==========================

    def show_home_page(self):

        self.create_pages()

        self.fade_transition(
            self.home_page
        )

        self.audio.play_music()


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


    # ==========================
    # Profile
    # ==========================

    def show_player_card(self):

        self.player_overlay = PlayerCardOverlay(
            self
        )

        self.player_overlay.open()