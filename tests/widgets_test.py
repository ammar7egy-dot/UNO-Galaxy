from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

from ui.widgets.buttons.primary_button import PrimaryButton
from ui.widgets.buttons.secondary_button import SecondaryButton
from ui.widgets.buttons.icon_button import IconButton


class WidgetsTest(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("UNO! Galaxy - Widgets Test")

        layout = QVBoxLayout()

        primary = PrimaryButton("Play")
        secondary = SecondaryButton("Settings")
        icon = IconButton()

        layout.addWidget(primary)
        layout.addWidget(secondary)
        layout.addWidget(icon)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])

    window = WidgetsTest()
    window.show()

    app.exec()