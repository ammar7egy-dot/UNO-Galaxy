from .base_button import BaseButton


class SecondaryButton(BaseButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setObjectName("SecondaryButton")