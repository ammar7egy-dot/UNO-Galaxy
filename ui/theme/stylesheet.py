from ui.theme.colors import Colors


def get_stylesheet() -> str:
    return f"""
    QWidget {{
        background-color: {Colors.BACKGROUND};
        color: {Colors.TEXT};
    }}

    QLabel {{
        background: transparent;
        color: {Colors.TEXT};
    }}

    /* Primary Button */
    QPushButton#PrimaryButton {{
        background-color: {Colors.PRIMARY};
        color: {Colors.TEXT};
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
    }}

    QPushButton#PrimaryButton:hover {{
        background-color: {Colors.PRIMARY_HOVER};
    }}

    QPushButton#PrimaryButton:pressed {{
        background-color: {Colors.PRIMARY_PRESSED};
    }}

    /* Secondary Button */
    QPushButton#SecondaryButton {{
        background-color: transparent;
        color: {Colors.TEXT};
        border: 2px solid {Colors.PRIMARY};
        border-radius: 12px;
        padding: 10px 20px;
    }}

    QPushButton#SecondaryButton:hover {{
        background-color: {Colors.PRIMARY_HOVER};
    }}

    /* Icon Button */
    QPushButton#IconButton {{
        background-color: transparent;
        border-radius: 20px;
        padding: 8px;
    }}

    QPushButton#IconButton:hover {{
        background-color: {Colors.PRIMARY_HOVER};
    }}
    """