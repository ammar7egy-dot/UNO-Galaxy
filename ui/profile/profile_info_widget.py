from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

from ui.profile.avatar_widget import AvatarWidget
from ui.profile.level_widget import LevelWidget

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class ProfileInfoWidget(QWidget):

    def __init__(
        self,
        name="Player",
        player_id="UG-XXXX-XXXX",
        parent=None,
    ):

        super().__init__(parent)

        self.name = name
        self.player_id = player_id

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setup_ui()


    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(
            10
        )


        self.avatar = AvatarWidget(
            90
        )

        layout.addWidget(
            self.avatar,
            alignment=Qt.AlignmentFlag.AlignCenter
        )


        self.name_label = QLabel(
            self.name
        )

        self.name_label.setFont(
            Fonts.title(24)
        )

        self.name_label.setStyleSheet(
            f"""
            QLabel {{
                color:{Colors.TEXT};
                background:transparent;
                border:none;
            }}
            """
        )

        self.name_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            self.name_label
        )


        self.id_label = QLabel(
            f"ID: {self.player_id}"
        )

        self.id_label.setFont(
            Fonts.body(13)
        )

        self.id_label.setStyleSheet(
            f"""
            QLabel {{
                color:{Colors.TEXT_SECONDARY};
                background:transparent;
                border:none;
            }}
            """
        )

        self.id_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            self.id_label
        )


        self.level_widget = LevelWidget(
            level=1,
            xp=0,
            max_xp=100,
        )

        layout.addWidget(
            self.level_widget
        )


    def update_profile(
        self,
        name,
        player_id,
    ):

        self.name_label.setText(
            name
        )

        self.id_label.setText(
            f"ID: {player_id}"
        )