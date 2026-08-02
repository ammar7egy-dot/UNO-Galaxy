from PySide6.QtGui import QFontDatabase, QFont


class Fonts:
    _loaded = False

    @classmethod
    def load(cls):
        if cls._loaded:
            return

        cls.bungee_family = cls._load_font(
            "assets/fonts/Bungee-Regular.ttf"
        )

        cls.orbitron_family = cls._load_font(
            "assets/fonts/Orbitron-VariableFont_wght.ttf"
        )

        cls.inter_family = cls._load_font(
            "assets/fonts/Inter-VariableFont_opsz,wght.ttf"
        )

        cls._loaded = True

    @staticmethod
    def _load_font(path):
        font_id = QFontDatabase.addApplicationFont(path)

        if font_id == -1:
            print(f"❌ Failed to load: {path}")
            return "Segoe UI"

        families = QFontDatabase.applicationFontFamilies(font_id)

        print(f"✅ Loaded: {families}")

        return families[0]

    @classmethod
    def title(cls, size=64):
        return QFont(cls.bungee_family, size)

    @classmethod
    def galaxy(cls, size=30):
        return QFont(cls.orbitron_family, size)

    @classmethod
    def body(cls, size=12):
        return QFont(cls.inter_family, size)

    @classmethod
    def button(cls, size=13):
        return QFont(cls.inter_family, size, QFont.Weight.DemiBold)