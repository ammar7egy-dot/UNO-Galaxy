
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QSizePolicy,
)

from ui.settings.settings_item import SettingsItem


class SettingsSidebar(QWidget):

    page_changed = Signal(str)

    def __init__(self, parent=None):

        super().__init__(parent)

        self.items = {}
        self.current_page = "General"

        self.setup_ui()

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.layout = QVBoxLayout(self)

        self.layout.setContentsMargins(
            0, 0, 0, 0
        )

        self.layout.setSpacing(8)

        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Expanding,
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

            self.layout.addWidget(item)

            self.items[page] = item

        self.layout.addStretch()

        self.set_current_page("General")

    # ==========================
    # Page Selection
    # ==========================

    def set_current_page(self, page):

        if page not in self.items:
            return

        self.current_page = page

        for name, item in self.items.items():

            item.set_active(
                name == page
            )

    def change_page(self, page):

        if page not in self.items:
            return

        self.set_current_page(page)

        self.page_changed.emit(page)

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        height = self.height()

        if height <= 500:
            spacing = 4

        elif height <= 700:
            spacing = 6

        else:
            spacing = 8

        self.layout.setSpacing(spacing)

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
