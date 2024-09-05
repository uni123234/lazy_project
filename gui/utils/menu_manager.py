"""
This module manages the creation and configuration of menus within the application.
It provides options for file operations, view settings, and help resources.
"""

from PyQt5.QtWidgets import QAction


class MenuManager:
    """
    Manages the application menus, including File, View, and Help menus.
    Provides actions for theme toggling and displaying help.
    """

    def __init__(self, parent, theme_manager):
        """
        Initializes the MenuManager with the parent widget and theme manager.

        :param parent: The parent widget (typically a QMainWindow or QWidget).
        :param theme_manager: The manager responsible for handling theme changes.
        """
        self.parent = parent
        self.theme_manager = theme_manager
        self.init_menu()

    def init_menu(self):
        """
        Initializes the menus and their actions.
        Adds File, View, and Help menus to the main menu bar.
        """
        menubar = self.parent.menuBar()

        file_menu = menubar.addMenu("File")

        view_menu = menubar.addMenu("View")
        theme_action = QAction("Toggle Theme", self.parent)
        theme_action.triggered.connect(self.theme_manager.toggle_theme)
        view_menu.addAction(theme_action)

        help_menu = menubar.addMenu("Help")
        help_action = QAction("Help", self.parent)
        help_action.triggered.connect(self.parent.show_help)
        help_menu.addAction(help_action)
