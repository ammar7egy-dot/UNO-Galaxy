
from PySide6.QtCore import QSignalBlocker

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from ui.settings.settings_card import SettingsCard
from ui.settings.settings_row import SettingsRow
from ui.settings.settings_slider import SettingsSlider
from ui.settings.settings_switch import SettingsSwitch

from game.settings_manager import SettingsManager


class AudioPage(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.settings = SettingsManager()
        self.audio_manager = None

        self.setup_ui()
        self.connect_signals()

    # ==========================
    # Audio Manager
    # ==========================

    def set_audio_manager(self, audio_manager):

        self.audio_manager = audio_manager

        muted = self.audio_manager.is_muted()

        if muted:
            volume = 0
        else:
            volume = self.audio_manager.volume()

        with QSignalBlocker(self.music_slider.slider):
            self.music_slider.setValue(volume)

        with QSignalBlocker(self.mute_switch):
            self.mute_switch.setChecked(muted)

    # ==========================
    # UI
    # ==========================

    def setup_ui(self):

        self.main_layout = QVBoxLayout(self)

        self.main_layout.setContentsMargins(
            0, 0, 0, 0
        )

        # Music
        self.music_card = SettingsCard("Music")

        volume = self.settings.get(
            "audio",
            "music_volume"
        )

        self.music_slider = SettingsSlider(
            value=volume
        )

        self.music_card.add_widget(
            SettingsRow(
                "Music Volume",
                self.music_slider
            )
        )

        self.main_layout.addWidget(
            self.music_card
        )

        # Audio Options
        self.options_card = SettingsCard("Audio Options")

        muted = self.settings.get(
            "audio",
            "mute_music"
        )

        self.mute_switch = SettingsSwitch(
            muted
        )

        self.options_card.add_widget(
            SettingsRow(
                "Mute Music",
                self.mute_switch
            )
        )

        self.main_layout.addWidget(
            self.options_card
        )

        self.main_layout.addStretch()

        self.update_responsive_layout()

    # ==========================
    # Signals
    # ==========================

    def connect_signals(self):

        self.music_slider.slider.valueChanged.connect(
            self.change_volume
        )

        self.mute_switch.toggled.connect(
            self.change_mute
        )

    # ==========================
    # Volume
    # ==========================

    def change_volume(self, value):

        if not self.audio_manager:
            return

        value = int(value)

        # Volume = 0
        if value == 0:

            if not self.audio_manager.is_muted():

                self.audio_manager.mute(True)

            with QSignalBlocker(self.mute_switch):
                self.mute_switch.setChecked(True)

            return

        # Volume > 0
        if self.audio_manager.is_muted():

            self.audio_manager.mute(False)

        self.audio_manager.set_volume(value)

        # Automatically unmute
        if self.mute_switch.isChecked():

            with QSignalBlocker(self.mute_switch):
                self.mute_switch.setChecked(False)

    # ==========================
    # Mute
    # ==========================

    def change_mute(self, checked):

        if not self.audio_manager:
            return

        checked = bool(checked)

        # MUTE
        if checked:

            self.audio_manager.mute(True)

            with QSignalBlocker(self.music_slider.slider):
                self.music_slider.setValue(0)

        # UNMUTE
        else:

            self.audio_manager.mute(False)

            volume = self.audio_manager.volume()

            # Restore last saved volume if necessary
            if volume == 0:

                volume = self.settings.get(
                    "audio",
                    "last_music_volume"
                )

                self.audio_manager.set_volume(volume)

            with QSignalBlocker(self.music_slider.slider):
                self.music_slider.setValue(volume)

    # ==========================
    # Responsive Layout
    # ==========================

    def update_responsive_layout(self):

        width = self.width()
        height = self.height()

        if width <= 500:
            spacing = 12

        elif width <= 800:
            spacing = 16

        else:
            spacing = 24

        if height <= 500:
            spacing = min(spacing, 10)

        self.main_layout.setSpacing(spacing)

    # ==========================
    # Resize
    # ==========================

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_responsive_layout()
