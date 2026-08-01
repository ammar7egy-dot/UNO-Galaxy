from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QStackedWidget

from ui.pages.splash_page import SplashPage
from ui.pages.home_page import HomePage
from ui.pages.play_page import PlayPage
from ui.pages.settings_page import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_window()
        self.setup_pages()
        self.connect_signals()
        self.start_splash()

    def setup_window(self):
        self.setWindowTitle("UNO! Galaxy")
        self.setFixedSize(1280, 720)

    def setup_pages(self):
        self.stack = QStackedWidget()

        self.splash_page = SplashPage()
        self.home_page = HomePage()
        self.play_page = PlayPage()
        self.settings_page = SettingsPage()

        self.stack.addWidget(self.splash_page)
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.play_page)
        self.stack.addWidget(self.settings_page)

        self.setCentralWidget(self.stack)

    def connect_signals(self):
        # Home
        self.home_page.play_clicked.connect(self.show_play_page)
        self.home_page.settings_clicked.connect(self.show_settings_page)

        # Back buttons
        self.play_page.back_button.clicked.connect(self.show_home_page)
        self.settings_page.back_button.clicked.connect(self.show_home_page)

    def start_splash(self):
        self.stack.setCurrentWidget(self.splash_page)
        QTimer.singleShot(2000, self.show_home_page)

    def show_home_page(self):
        self.stack.setCurrentWidget(self.home_page)

    def show_play_page(self):
        self.stack.setCurrentWidget(self.play_page)

    def show_settings_page(self):
        self.stack.setCurrentWidget(self.settings_page)