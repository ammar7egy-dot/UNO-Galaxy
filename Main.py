import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

from ui.theme.theme import Theme

from ui.theme.fonts import Fonts


def main():
    app = QApplication(sys.argv)

    Theme.apply(app)
    Fonts.load()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()