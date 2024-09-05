"""
This module manages the application's theme, allowing toggling between dark and light modes.
It applies the appropriate CSS file based on the current theme mode.
"""


class ThemeManager:
    """
    Manages the application's theme settings, including toggling between dark and light modes.
    """

    def __init__(self, parent):
        """
        Initializes the ThemeManager with the parent widget.

        :param parent: The parent widget (typically a QMainWindow or QWidget) that can load styles.
        """
        self.parent = parent
        self.is_dark_mode = False

    def toggle_theme(self):
        """
        Toggles between dark and light theme modes and applies the selected theme.
        """
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def apply_theme(self):
        """
        Applies the current theme by loading the appropriate CSS file.
        """
        theme_file = "dark_theme.css" if self.is_dark_mode else "light_theme.css"
        self.parent.load_style(theme_file)
