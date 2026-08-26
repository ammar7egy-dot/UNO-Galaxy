from PySide6.QtCore import QSignalBlocker
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QMenu,
)

from ui.settings.settings_card import SettingsCard
from ui.settings.settings_row import SettingsRow
from ui.settings.settings_switch import SettingsSwitch
from ui.settings.settings_value_button import SettingsValueButton

from game.settings_manager import SettingsManager


class GeneralPage(QWidget):

    def __init__(
        self,
        parent=None,
    ):

        super().__init__(parent)

        self.settings = SettingsManager()

        self.setup_ui()
        self.connect_signals()


    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(
            24,
        )


        # ==========================
        # Load Settings
        # ==========================

        animations = self.settings.get(
            "general",
            "animations"
        )

        particles = self.settings.get(
            "general",
            "particles"
        )

        reduce_motion = self.settings.get(
            "general",
            "reduce_motion"
        )

        language = self.settings.get(
            "general",
            "language"
        )

        ui_scale = self.settings.get(
            "general",
            "ui_scale"
        )


        # ==========================
        # Experience
        # ==========================

        experience_card = SettingsCard(
            "Experience"
        )

        self.animations_switch = SettingsSwitch(
            animations
        )

        self.particles_switch = SettingsSwitch(
            particles
        )

        self.reduce_motion_switch = SettingsSwitch(
            reduce_motion
        )


        experience_card.add_widget(
            SettingsRow(
                "Animations",
                self.animations_switch,
            )
        )

        experience_card.add_widget(
            SettingsRow(
                "Particle Effects",
                self.particles_switch,
            )
        )

        experience_card.add_widget(
            SettingsRow(
                "Reduce Motion",
                self.reduce_motion_switch,
            )
        )

        layout.addWidget(
            experience_card
        )


        # ==========================
        # Interface
        # ==========================

        interface_card = SettingsCard(
            "Interface"
        )

        self.language_button = SettingsValueButton(
            language
        )

        self.scale_button = SettingsValueButton(
            ui_scale
        )


        interface_card.add_widget(
            SettingsRow(
                "Language",
                self.language_button,
            )
        )

        interface_card.add_widget(
            SettingsRow(
                "UI Scale",
                self.scale_button
            )
        )

        layout.addWidget(
            interface_card
        )

        layout.addStretch()


    def connect_signals(self):

        self.animations_switch.toggled.connect(
            self.change_animations
        )

        self.particles_switch.toggled.connect(
            self.change_particles
        )

        self.reduce_motion_switch.toggled.connect(
            self.change_reduce_motion
        )

        self.language_button.clicked_value.connect(
            self.open_language_menu
        )

        self.scale_button.clicked_value.connect(
            self.open_scale_menu
        )


    # ==========================
    # Experience
    # ==========================

    def change_animations(
        self,
        enabled,
    ):

        self.settings.set(
            "general",
            "animations",
            bool(enabled)
        )


    def change_particles(
        self,
        enabled,
    ):

        self.settings.set(
            "general",
            "particles",
            bool(enabled)
        )


    def change_reduce_motion(
        self,
        enabled,
    ):

        self.settings.set(
            "general",
            "reduce_motion",
            bool(enabled)
        )


    # ==========================
    # Language
    # ==========================

    def open_language_menu(self):

        menu = QMenu(
            self
        )

        menu.setStyleSheet(
            """
            QMenu {
                background-color: #1E1E1E;
                border: 1px solid #3A3A3A;
                border-radius: 10px;
                padding: 6px;
            }

            QMenu::item {
                color: white;
                padding: 10px 24px;
                border-radius: 6px;
            }

            QMenu::item:selected {
                background-color: #4F46E5;
            }
            """
        )


        english_action = menu.addAction(
            "English"
        )

        arabic_action = menu.addAction(
            "العربية"
        )


        selected_action = menu.exec(
            self.language_button.mapToGlobal(
                self.language_button.rect().bottomLeft()
            )
        )


        if selected_action == english_action:

            self.change_language(
                "English"
            )

        elif selected_action == arabic_action:

            self.change_language(
                "العربية"
            )


    def change_language(
        self,
        language,
    ):

        self.settings.set(
            "general",
            "language",
            language
        )

        self.language_button.set_value(
            language
        )


    # ==========================
    # UI Scale
    # ==========================

    def open_scale_menu(self):

        menu = QMenu(
            self
        )

        menu.setStyleSheet(
            """
            QMenu {
                background-color: #1E1E1E;
                border: 1px solid #3A3A3A;
                border-radius: 10px;
                padding: 6px;
            }

            QMenu::item {
                color: white;
                padding: 10px 24px;
                border-radius: 6px;
            }

            QMenu::item:selected {
                background-color: #4F46E5;
            }
            """
        )


        scales = [
            "80%",
            "90%",
            "100%",
            "110%",
            "125%",
        ]


        actions = {}

        for scale in scales:

            actions[
                menu.addAction(scale)
            ] = scale


        selected_action = menu.exec(
            self.scale_button.mapToGlobal(
                self.scale_button.rect().bottomLeft()
            )
        )


        if selected_action in actions:

            self.change_scale(
                actions[selected_action]
            )


    def change_scale(
        self,
        scale,
    ):

        self.settings.set(
            "general",
            "ui_scale",
            scale
        )

        self.scale_button.set_value(
            scale
        )

        # إرسال التغيير إلى MainWindow
        window = self.window()

        if hasattr(
            window,
            "apply_ui_scale"
        ):

            window.apply_ui_scale(
                scale
            )


    # ==========================
    # Refresh
    # ==========================

    def refresh_settings(self):

        animations = self.settings.get(
            "general",
            "animations"
        )

        particles = self.settings.get(
            "general",
            "particles"
        )

        reduce_motion = self.settings.get(
            "general",
            "reduce_motion"
        )

        language = self.settings.get(
            "general",
            "language"
        )

        ui_scale = self.settings.get(
            "general",
            "ui_scale"
        )


        with QSignalBlocker(
            self.animations_switch
        ):

            self.animations_switch.setChecked(
                animations
            )


        with QSignalBlocker(
            self.particles_switch
        ):

            self.particles_switch.setChecked(
                particles
            )


        with QSignalBlocker(
            self.reduce_motion_switch
        ):

            self.reduce_motion_switch.setChecked(
                reduce_motion
            )


        self.language_button.set_value(
            language
        )

        self.scale_button.set_value(
            ui_scale
        )