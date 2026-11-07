
from PySide6.QtCore import Qt, Signal, QRectF
from PySide6.QtGui import QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import QWidget, QSizePolicy


class ProfileButton(QWidget):

    profile_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(130, 48)
        self.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Preferred,
        )

        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._hover = False

    def sizeHint(self):
        return self.minimumSizeHint()

    def minimumSizeHint(self):
        return self.minimumSize()

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

        width = self.width()
        height = self.height()

        # Background
        bg = (
            QColor(255, 255, 255, 24)
            if self._hover
            else QColor(255, 255, 255, 14)
        )

        painter.setBrush(bg)

        painter.setPen(
            QPen(
                QColor(255, 255, 255, 35),
                1,
            )
        )

        painter.drawRoundedRect(
            QRectF(0, 0, width - 1, height - 1),
            height * 0.23,
            height * 0.23,
        )

        # Avatar
        avatar_size = min(
            height * 0.67,
            width * 0.25,
        )

        avatar_x = width * 0.07
        avatar_y = (height - avatar_size) / 2

        avatar_rect = QRectF(
            avatar_x,
            avatar_y,
            avatar_size,
            avatar_size,
        )

        painter.setBrush(QColor("#4F46E5"))
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(avatar_rect)

        # Avatar letter
        avatar_font = QFont()
        avatar_font.setPointSize(
            max(9, int(height * 0.20))
        )
        avatar_font.setBold(True)

        painter.setFont(avatar_font)
        painter.setPen(Qt.GlobalColor.white)

        painter.drawText(
            avatar_rect,
            Qt.AlignmentFlag.AlignCenter,
            "G",
        )

        # Text position
        text_x = avatar_x + avatar_size + width * 0.07

        # Guest
        name_font = QFont()
        name_font.setPointSize(
            max(9, int(height * 0.18))
        )
        name_font.setBold(True)

        painter.setFont(name_font)
        painter.setPen(QColor("#FFFFFF"))

        painter.drawText(
            int(text_x),
            int(height * 0.47),
            "Guest",
        )

        # Profile
        subtitle_font = QFont()
        subtitle_font.setPointSize(
            max(8, int(height * 0.15))
        )
        subtitle_font.setBold(False)

        painter.setFont(subtitle_font)
        painter.setPen(QColor(180, 180, 180))

        painter.drawText(
            int(text_x),
            int(height * 0.77),
            "Profile",
        )
