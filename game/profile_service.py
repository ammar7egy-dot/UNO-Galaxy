import json
import random
import string
from pathlib import Path

from game.player_profile import PlayerProfile


class ProfileService:

    PROFILE_FILE = Path("player_profile.json")

    # ==========================
    # Public
    # ==========================

    @classmethod
    def load(cls) -> PlayerProfile:

        if not cls.PROFILE_FILE.exists():

            profile = PlayerProfile()

            profile.player_id = cls.generate_player_id()

            cls.save(profile)

            return profile

        with open(
            cls.PROFILE_FILE,
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        return PlayerProfile.from_dict(data)

    @classmethod
    def save(
        cls,
        profile: PlayerProfile,
    ):

        with open(
            cls.PROFILE_FILE,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                profile.to_dict(),
                file,
                indent=4,
                ensure_ascii=False,
            )

    # ==========================
    # Player ID
    # ==========================

    @staticmethod
    def generate_player_id() -> str:

        chars = (
            string.ascii_uppercase
            + string.digits
        )

        parts = []

        for _ in range(3):

            part = "".join(
                random.choice(chars)
                for _ in range(4)
            )

            parts.append(part)

        return "UG-" + "-".join(parts)