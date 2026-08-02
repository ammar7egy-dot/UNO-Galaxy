from PySide6.QtWidgets import QApplication

from ui.theme.stylesheet import get_stylesheet


class Theme:

    @staticmethod
    def apply(app: QApplication):
        app.setStyle("Fusion")
        app.setStyleSheet(get_stylesheet())