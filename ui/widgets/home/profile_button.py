from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import QWidget


class ProfileButton(QWidget):

    profile_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(170, 60)

        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._hover = False

    def enterEvent(self, event):

        self._hover = True
        self.update()

        super().enterEvent(event)

    def leaveEvent(self, event):

        self._hover = False
        self.update()

        super().leaveEvent(event)

    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:
            self.profile_clicked.emit()

        super().mousePressEvent(event)

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        if self._hover:
            bg = QColor(255, 255, 255, 24)
        else:
            bg = QColor(255, 255, 255, 14)

        painter.setBrush(bg)

        painter.setPen(
            QPen(
                QColor(255, 255, 255, 35),
                1,
            )
        )

        painter.drawRoundedRect(
            self.rect().adjusted(0, 0, -1, -1),
            14,
            14,
        )

        avatar_rect = self.rect().adjusted(
            10,
            10,
            -110,
            -10,
        )

        painter.setBrush(
            QColor("#4F46E5")
        )

        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(avatar_rect)

        painter.setPen(Qt.GlobalColor.white)

        font = QFont()

        font.setPointSize(12)
        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            avatar_rect,
            Qt.AlignmentFlag.AlignCenter,
            "G",
        )

        painter.setPen(
            QColor("#FFFFFF")
        )

        font.setPointSize(11)
        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            68,
            28,
            "Guest",
        )

        painter.setPen(
            QColor(180, 180, 180)
        )

        font.setPointSize(9)
        font.setBold(False)

        painter.setFont(font)

        painter.drawText(
            68,
            46,
            "Profile",
        )