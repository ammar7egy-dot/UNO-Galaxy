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

    def __init__(
        self,
        parent=None,
    ):

        super().__init__(parent)

        self.settings = SettingsManager()
        self.audio_manager = None

        self.setup_ui()
        self.connect_signals()


    def set_audio_manager(
        self,
        audio_manager,
    ):

        self.audio_manager = audio_manager

        muted = self.audio_manager.is_muted()

        if muted:
            volume = 0
        else:
            volume = self.audio_manager.volume()

        with QSignalBlocker(
            self.music_slider.slider
        ):
            self.music_slider.setValue(
                volume
            )

        with QSignalBlocker(
            self.mute_switch
        ):
            self.mute_switch.setChecked(
                muted
            )


    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(
            24
        )


        # ==========================
        # Music
        # ==========================

        music_card = SettingsCard(
            "Music"
        )

        volume = self.settings.get(
            "audio",
            "music_volume"
        )

        self.music_slider = SettingsSlider(
            value=volume
        )

        music_card.add_widget(
            SettingsRow(
                "Music Volume",
                self.music_slider
            )
        )

        layout.addWidget(
            music_card
        )


        # ==========================
        # Audio Options
        # ==========================

        options_card = SettingsCard(
            "Audio Options"
        )

        muted = self.settings.get(
            "audio",
            "mute_music"
        )

        self.mute_switch = SettingsSwitch(
            muted
        )

        options_card.add_widget(
            SettingsRow(
                "Mute Music",
                self.mute_switch
            )
        )

        layout.addWidget(
            options_card
        )

        layout.addStretch()


    def connect_signals(self):

        self.music_slider.slider.valueChanged.connect(
            self.change_volume
        )

        self.mute_switch.toggled.connect(
            self.change_mute
        )


    def change_volume(
        self,
        value,
    ):

        if not self.audio_manager:
            return

        value = int(value)

        # ==========================
        # Volume = 0
        # ==========================

        if value == 0:

            # تفعيل الكتم تلقائياً
            if not self.audio_manager.is_muted():

                self.audio_manager.mute(
                    True
                )

            with QSignalBlocker(
                self.mute_switch
            ):

                self.mute_switch.setChecked(
                    True
                )

            return


        # ==========================
        # Volume > 0
        # ==========================

        if self.audio_manager.is_muted():

            self.audio_manager.mute(
                False
            )


        self.audio_manager.set_volume(
            value
        )


        # إلغاء الكتم تلقائياً
        if self.mute_switch.isChecked():

            with QSignalBlocker(
                self.mute_switch
            ):

                self.mute_switch.setChecked(
                    False
                )


    def change_mute(
        self,
        checked,
    ):

        if not self.audio_manager:
            return

        checked = bool(checked)


        # ==========================
        # MUTE
        # ==========================

        if checked:

            self.audio_manager.mute(
                True
            )

            with QSignalBlocker(
                self.music_slider.slider
            ):

                self.music_slider.setValue(
                    0
                )


        # ==========================
        # UNMUTE
        # ==========================

        else:

            self.audio_manager.mute(
                False
            )

            volume = self.audio_manager.volume()

            # إذا كان الصوت ما زال 0
            # استرجع آخر مستوى محفوظ
            if volume == 0:

                volume = self.settings.get(
                    "audio",
                    "last_music_volume"
                )

                self.audio_manager.set_volume(
                    volume
                )


            with QSignalBlocker(
                self.music_slider.slider
            ):

                self.music_slider.setValue(
                    volume
                )