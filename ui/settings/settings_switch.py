from PySide6.QtCore import (
    Qt,
    Signal,
    Property,
    QPropertyAnimation,
)

from PySide6.QtGui import (
    QColor,
    QPainter,
)

from PySide6.QtWidgets import QWidget

from ui.theme.colors import Colors


class SettingsSwitch(QWidget):

    toggled = Signal(bool)

    def __init__(
        self,
        checked=False,
        parent=None,
    ):

        super().__init__(parent)

        self._checked = checked
        self._offset = 24 if checked else 4

        self.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.setFixedSize(
            52,
            30,
        )

        self.animation = QPropertyAnimation(
            self,
            b"offset",
            self,
        )

        self.animation.setDuration(
            180
        )


    def get_offset(self):

        return self._offset


    def set_offset(
        self,
        value,
    ):

        self._offset = value

        self.update()


    offset = Property(
        float,
        get_offset,
        set_offset,
    )


    def isChecked(self):

        return self._checked


    def setChecked(
        self,
        checked,
    ):

        if self._checked == checked:
            return

        self._checked = checked

        self.animation.stop()

        self.animation.setStartValue(
            self._offset
        )

        self.animation.setEndValue(
            24 if checked else 4
        )

        self.animation.start()

        self.toggled.emit(
            checked
        )


    def mousePressEvent(
        self,
        event,
    ):

        if event.button() == Qt.MouseButton.LeftButton:

            self.setChecked(
                not self._checked
            )

        super().mousePressEvent(
            event
        )


    def paintEvent(
        self,
        event,
    ):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )


        track = QColor(
            Colors.PRIMARY
            if self._checked
            else Colors.SECONDARY
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        painter.setBrush(
            track
        )

        painter.drawRoundedRect(
            self.rect(),
            15,
            15,
        )


        painter.setBrush(
            QColor(
                Colors.TEXT
            )
        )

        painter.drawEllipse(
            int(self._offset),
            4,
            22,
            22,
        )

        painter.end()