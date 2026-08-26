from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
)

from ui.profile.stat_card_widget import StatCardWidget


class StatsGridWidget(QWidget):

    def __init__(
        self,
        games=0,
        wins=0,
        losses=0,
        win_rate=0,
        parent=None,
    ):

        super().__init__(parent)

        self.games = games
        self.wins = wins
        self.losses = losses
        self.win_rate = win_rate

        self.setup_ui()


    def setup_ui(self):

        layout = QGridLayout(self)

        layout.setSpacing(
            14
        )


        self.games_card = StatCardWidget(
            "Games",
            self.games
        )

        self.wins_card = StatCardWidget(
            "Wins",
            self.wins
        )

        self.losses_card = StatCardWidget(
            "Losses",
            self.losses
        )

        self.rate_card = StatCardWidget(
            "Win Rate",
            f"{self.win_rate}%"
        )


        layout.addWidget(
            self.games_card,
            0,
            0
        )

        layout.addWidget(
            self.wins_card,
            0,
            1
        )

        layout.addWidget(
            self.losses_card,
            1,
            0
        )

        layout.addWidget(
            self.rate_card,
            1,
            1
        )


    def update_stats(
        self,
        games,
        wins,
        losses,
        win_rate,
    ):

        self.games_card.set_value(
            games
        )

        self.wins_card.set_value(
            wins
        )

        self.losses_card.set_value(
            losses
        )

        self.rate_card.set_value(
            f"{win_rate}%"
        )