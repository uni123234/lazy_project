from PyQt5.QtWidgets import QAction
from .help_manager import HelpManager


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
        self.help_manager = HelpManager(parent)
        self.init_menu()

    def init_menu(self):
        """
        Initializes the menus and their actions.
        Adds File, View, and Help menus to the main menu bar.
        """
        menubar = self.parent.menuBar()

        view_menu = menubar.addMenu("View")
        theme_action = QAction("Toggle Theme", self.parent)
        theme_action.triggered.connect(self.theme_manager.toggle_theme)
        view_menu.addAction(theme_action)

        help_menu = menubar.addMenu("Help")

        help_action = QAction("Help", self.parent)
        help_action.triggered.connect(self.help_manager.show_help)
        help_menu.addAction(help_action)

        create_help_action = QAction("Create Help", self.parent)
        create_help_action.triggered.connect(self.help_manager.show_create_help)
        help_menu.addAction(create_help_action)

        update_help_action = QAction("Update Help", self.parent)
        update_help_action.triggered.connect(self.help_manager.show_update_help)
        help_menu.addAction(update_help_action)

        delete_help_action = QAction("Delete Help", self.parent)
        delete_help_action.triggered.connect(self.help_manager.show_delete_help)
        help_menu.addAction(delete_help_action)

        serialize_help_action = QAction("Serialize Help", self.parent)
        serialize_help_action.triggered.connect(self.help_manager.show_serialize_help)
        help_menu.addAction(serialize_help_action)
