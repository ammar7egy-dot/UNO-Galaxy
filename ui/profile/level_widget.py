from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
)

from PySide6.QtCore import Qt

from ui.theme.colors import Colors
from ui.theme.fonts import Fonts


class LevelWidget(QWidget):

    def __init__(
        self,
        level=1,
        xp=0,
        max_xp=100,
        parent=None,
    ):

        super().__init__(parent)

        self.level = level
        self.xp = xp
        self.max_xp = max_xp

        self.setup_ui()


    def setup_ui(self):

        layout = QVBoxLayout(
            self
        )

        layout.setSpacing(
            8
        )


        self.level_label = QLabel(
            f"Level {self.level}"
        )

        self.level_label.setFont(
            Fonts.galaxy(18)
        )

        self.level_label.setStyleSheet(
            f"""
            color:{Colors.TEXT};
            """
        )


        self.xp_label = QLabel(
            f"{self.xp} / {self.max_xp} XP"
        )

        self.xp_label.setFont(
            Fonts.body(12)
        )

        self.xp_label.setStyleSheet(
            f"""
            color:{Colors.TEXT_SECONDARY};
            """
        )


        self.progress = QProgressBar()

        self.progress.setMaximum(
            self.max_xp
        )

        self.progress.setValue(
            self.xp
        )

        self.progress.setFixedHeight(
            10
        )

        self.progress.setTextVisible(
            False
        )

        self.progress.setStyleSheet(
            f"""
            QProgressBar {{

                background:{Colors.SECONDARY};

                border-radius:5px;

            }}

            QProgressBar::chunk {{

                background:{Colors.PRIMARY};

                border-radius:5px;

            }}
            """
        )


        layout.addWidget(
            self.level_label
        )

        layout.addWidget(
            self.xp_label
        )

        layout.addWidget(
            self.progress
        )


    def update_xp(
        self,
        xp,
        max_xp,
    ):

        self.xp = xp
        self.max_xp = max_xp

        self.xp_label.setText(
            f"{xp} / {max_xp} XP"
        )

        self.progress.setMaximum(
            max_xp
        )

        self.progress.setValue(
            xp
        )