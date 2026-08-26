from pathlib import Path

from PySide6.QtCore import QObject, QUrl
from PySide6.QtMultimedia import (
    QAudioOutput,
    QMediaPlayer,
)

from game.settings_manager import SettingsManager


class AudioManager(QObject):

    def __init__(self):

        super().__init__()

        self.settings = SettingsManager()

        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()

        self.player.setAudioOutput(
            self.audio_output
        )

        # ==========================
        # Load Settings
        # ==========================

        saved_volume = int(
            self.settings.get(
                "audio",
                "music_volume"
            )
        )

        self.last_volume = int(
            self.settings.get(
                "audio",
                "last_music_volume"
            )
        )

        muted = bool(
            self.settings.get(
                "audio",
                "mute_music"
            )
        )

        # ==========================
        # Initial Audio State
        # ==========================

        if muted:

            self.audio_output.setVolume(
                0
            )

        else:

            self.audio_output.setVolume(
                saved_volume / 100
            )

            if saved_volume > 0:

                self.last_volume = saved_volume

                self.settings.set(
                    "audio",
                    "last_music_volume",
                    saved_volume
                )

        self.audio_output.setMuted(
            muted
        )

        # ==========================
        # Music Source
        # ==========================

        audio_path = (
            Path(__file__).parent.parent
            / "assets"
            / "audio"
            / "background_music.mp3"
        )

        self.player.setSource(
            QUrl.fromLocalFile(
                str(audio_path)
            )
        )

        self.player.setLoops(
            -1
        )


    def play_music(self):

        if (
            self.player.playbackState()
            != QMediaPlayer.PlaybackState.PlayingState
        ):

            self.player.play()


    def pause_music(self):

        self.player.pause()


    def stop_music(self):

        self.player.stop()


    def set_volume(
        self,
        volume,
    ):

        volume = max(
            0,
            min(
                100,
                int(volume),
            ),
        )

        # ==========================
        # Save Volume
        # ==========================

        self.audio_output.setVolume(
            volume / 100
        )

        self.settings.set(
            "audio",
            "music_volume",
            volume
        )

        # ==========================
        # Update Last Volume
        # ==========================

        if volume > 0:

            self.last_volume = volume

            self.settings.set(
                "audio",
                "last_music_volume",
                volume
            )

        # ==========================
        # Unmute Automatically
        # ==========================

        if (
            volume > 0
            and self.audio_output.isMuted()
        ):

            self.audio_output.setMuted(
                False
            )

            self.settings.set(
                "audio",
                "mute_music",
                False
            )


    def volume(self):

        if self.audio_output.isMuted():

            return 0

        return int(
            self.audio_output.volume() * 100
        )


    def mute(
        self,
        enabled=True,
    ):

        enabled = bool(
            enabled
        )

        # ==========================
        # MUTE
        # ==========================

        if enabled:

            current_volume = int(
                self.settings.get(
                    "audio",
                    "music_volume"
                )
            )

            if current_volume > 0:

                self.last_volume = current_volume

                self.settings.set(
                    "audio",
                    "last_music_volume",
                    current_volume
                )

            self.audio_output.setMuted(
                True
            )

            self.audio_output.setVolume(
                0
            )

            self.settings.set(
                "audio",
                "music_volume",
                0
            )

        # ==========================
        # UNMUTE
        # ==========================

        else:

            volume = max(
                0,
                min(
                    100,
                    int(self.last_volume)
                )
            )

            self.audio_output.setMuted(
                False
            )

            self.audio_output.setVolume(
                volume / 100
            )

            self.settings.set(
                "audio",
                "music_volume",
                volume
            )

            self.settings.set(
                "audio",
                "last_music_volume",
                volume
            )


        self.settings.set(
            "audio",
            "mute_music",
            enabled
        )


    def is_muted(self):

        return self.audio_output.isMuted()


    def is_playing(self):

        return (
            self.player.playbackState()
            ==
            QMediaPlayer.PlaybackState.PlayingState
        )