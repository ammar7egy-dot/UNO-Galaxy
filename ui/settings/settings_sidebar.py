from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from ui.settings.settings_item import SettingsItem


class SettingsSidebar(QWidget):

    page_changed = Signal(str)

    def __init__(self, parent=None):

        super().__init__(parent)

        self.items = {}

        self.current_page = "General"

        self.setup_ui()


    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(
            8
        )


        pages = [

            "General",
            "Audio",
            "Appearance",
            "Language",
            "Gameplay",
            "About",

        ]


        for page in pages:

            item = SettingsItem(page)

            item.clicked_item.connect(
                self.change_page
            )

            layout.addWidget(
                item
            )

            self.items[page] = item


        layout.addStretch()

        self.set_current_page(
            "General"
        )


    def set_current_page(
        self,
        page,
    ):

        self.current_page = page

        for name, item in self.items.items():

            item.set_active(
                name == page
            )


    def change_page(
        self,
        page,
    ):

        self.set_current_page(
            page
        )

        self.page_changed.emit(
            page
        )