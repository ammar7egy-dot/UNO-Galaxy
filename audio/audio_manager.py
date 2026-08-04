from pathlib import Path

from PySide6.QtCore import QObject, QUrl
from PySide6.QtMultimedia import (
    QAudioOutput,
    QMediaPlayer,
)


class AudioManager(QObject):

    def __init__(self):
        super().__init__()

        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()

        self.player.setAudioOutput(
            self.audio_output
        )

        self.audio_output.setVolume(
            0.25
        )

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

        # تشغيل متكرر بدون إعادة تشغيل يدوية
        self.player.setLoops(-1)

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

    def set_volume(self, volume):

        volume = max(
            0.0,
            min(
                1.0,
                volume,
            ),
        )

        self.audio_output.setVolume(
            volume
        )

    def volume(self):

        return self.audio_output.volume()

    def is_playing(self):

        return (
            self.player.playbackState()
            == QMediaPlayer.PlaybackState.PlayingState
        )