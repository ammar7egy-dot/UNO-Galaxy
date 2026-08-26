import json
import os


class SettingsManager:

    def __init__(self):

        self.path = "game/settings.json"

        self.defaults = {

            "audio": {

                "music_volume": 100,

                "last_music_volume": 100,

                "sfx_volume": 100,

                "mute_music": False,

            },

            "general": {

                "animations": True,

                "particles": True,

                "reduce_motion": False,

                "language": "English",

                "ui_scale": "100%",

            }

        }

        self.settings = {}

        self.load()


    def load(self):

        if os.path.exists(self.path):

            try:

                with open(
                    self.path,
                    "r",
                    encoding="utf-8",
                ) as file:

                    self.settings = json.load(file)

            except Exception:

                self.settings = self.defaults.copy()

        else:

            self.settings = self.defaults.copy()

            self.save()


        # إضافة أي مفاتيح جديدة عند تحديث اللعبة

        self.merge_defaults(
            self.settings,
            self.defaults,
        )


    def merge_defaults(
        self,
        data,
        defaults,
    ):

        changed = False

        for key, value in defaults.items():

            if key not in data:

                data[key] = value

                changed = True

            elif isinstance(value, dict):

                if self.merge_defaults(
                    data[key],
                    value,
                ):
                    changed = True

        if changed:

            self.save()

        return changed


    def save(self):

        os.makedirs(
            os.path.dirname(self.path),
            exist_ok=True,
        )

        with open(
            self.path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                self.settings,
                file,
                indent=4,
                ensure_ascii=False,
            )


    def get(
        self,
        section,
        key,
    ):

        return self.settings[section][key]


    def set(
        self,
        section,
        key,
        value,
    ):

        self.settings[section][key] = value

        self.save()