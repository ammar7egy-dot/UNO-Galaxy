
from PySide6.QtCore import (
    Qt,
    Signal,
    Property,
    QPropertyAnimation,
    QSize,
)

from PySide6.QtGui import (
    QColor,
    QPainter,
)

from PySide6.QtWidgets import (
    QWidget,
    QSizePolicy,
)

from ui.theme.colors import Colors


class SettingsSwitch(QWidget):

    toggled = Signal(bool)

    def __init__(self, checked=False, parent=None):

        super().__init__(parent)

        self._checked = bool(checked)
        self._offset = 1.0 if self._checked else 0.0

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setMinimumSize(42, 24)

        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed
        )

        self.animation = QPropertyAnimation(
            self,
            b"offset",
            self
        )

        self.animation.setDuration(180)

    # ==========================
    # Size
    # ==========================

    def sizeHint(self):

        return QSize(52, 30)

    # ==========================
    # Animation Property
    # ==========================

    def get_offset(self):

        return self._offset

    def set_offset(self, value):

        self._offset = value
        self.update()

    offset = Property(
        float,
        get_offset,
        set_offset
    )

    # ==========================
    # Checked State
    # ==========================

    def isChecked(self):

        return self._checked

    def setChecked(self, checked):

        checked = bool(checked)

        if self._checked == checked:
            return

        self._checked = checked

        self.animation.stop()

        self.animation.setStartValue(
            self._offset
        )

        self.animation.setEndValue(
            1.0 if checked else 0.0
        )

        self.animation.start()

        self.toggled.emit(checked)

    # ==========================
    # Mouse Interaction
    # ==========================

    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:

            self.setChecked(
                not self._checked
            )

            event.accept()
            return

        super().mousePressEvent(event)

    # ==========================
    # Drawing
    # ==========================

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        width = self.width()
        height = self.height()

        knob_size = height * 0.73
        margin = (height - knob_size) / 2

        minimum_x = margin
        maximum_x = width - knob_size - margin

        knob_x = (
            minimum_x
            + (maximum_x - minimum_x) * self._offset
        )

        # Track
        track = QColor(
            Colors.PRIMARY
            if self._checked
            else Colors.SECONDARY
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        painter.setBrush(track)

        painter.drawRoundedRect(
            self.rect(),
            height / 2,
            height / 2
        )

        # Knob
        painter.setBrush(
            QColor(Colors.TEXT)
        )

        painter.drawEllipse(
            int(knob_x),
            int(margin),
            int(knob_size),
            int(knob_size)
        )

        painter.end()
