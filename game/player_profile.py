from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import date


@dataclass
class PlayerProfile:

    # ==========================
    # Identity
    # ==========================

    player_id: str = ""
    display_name: str = "Player"
    avatar: str = "default"

    join_date: str = date.today().isoformat()

    # ==========================
    # Statistics
    # ==========================

    games_played: int = 0
    wins: int = 0
    losses: int = 0

    longest_win_streak: int = 0
    current_win_streak: int = 0

    # ==========================
    # Game
    # ==========================

    version: str = "0.3.0"

    # ==========================
    # Computed
    # ==========================

    @property
    def win_rate(self) -> float:

        if self.games_played == 0:
            return 0.0

        return round(
            (self.wins / self.games_played) * 100,
            1,
        )

    # ==========================
    # Serialization
    # ==========================

    def to_dict(self):

        data = asdict(self)

        data["win_rate"] = self.win_rate

        return data

    @classmethod
    def from_dict(cls, data):

        return cls(
            player_id=data.get(
                "player_id",
                "",
            ),
            display_name=data.get(
                "display_name",
                "Player",
            ),
            avatar=data.get(
                "avatar",
                "default",
            ),
            join_date=data.get(
                "join_date",
                date.today().isoformat(),
            ),
            games_played=data.get(
                "games_played",
                0,
            ),
            wins=data.get(
                "wins",
                0,
            ),
            losses=data.get(
                "losses",
                0,
            ),
            longest_win_streak=data.get(
                "longest_win_streak",
                0,
            ),
            current_win_streak=data.get(
                "current_win_streak",
                0,
            ),
            version=data.get(
                "version",
                "0.3.0",
            ),
        )