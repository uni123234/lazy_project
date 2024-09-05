"""
LazyProjectGUI is the main class for the graphical user interface (GUI) 
that manages project templates, themes, and interactions with JSON data.
"""

import json
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QComboBox,
    QLineEdit,
)
from .utils import (
    TemplateManager,
    SearchManager,
    MenuManager,
    ThemeManager,
    JsonSerializer,
    HelpManager,
)



class LazyProjectGUI(QMainWindow):
    """
    LazyProjectGUI class handles the layout, widgets, and their functionality
    for managing templates and JSON data within a user-friendly interface.

    Methods:
    - init_ui: Initializes the user interface components.
    - load_style: Loads a specific stylesheet for the GUI.
    - load_json_data: Loads the JSON data into the editor.
    - create_template: Creates a new template and displays it in the editor.
    - update_template: Updates the selected template based on the editor content.
    - delete_specific_technology: Deletes the selected technology from the list.
    - serialize_template: Saves the content of the JSON editor to a file.
    """

    def __init__(self):
        """
        Initializes LazyProjectGUI and sets up managers for templates, themes,
        and menus. It also sets up the help and search functionality.
        """
        super().__init__()

        # Initializing managers
        self.template_manager = TemplateManager(self.statusBar())
        self.theme_manager = ThemeManager(self)
        self.menu_manager = MenuManager(self, self.theme_manager)
        self.help_manager = HelpManager(self)

        self.init_ui()

    def init_ui(self):
        """
        Sets up the layout of the application, including buttons, text editor,
        and dropdowns. Connects buttons to their respective methods.
        """
        self.setWindowTitle("Lazy Project GUI")
        self.setGeometry(100, 100, 800, 600)

        content_layout = QVBoxLayout()

        self.create_button = QPushButton("Create", self)
        self.create_button.setToolTip(
            "Creates a new template and displays it in the JSON editor."
        )
        self.create_button.clicked.connect(self.create_template)
        content_layout.addWidget(self.create_button)

        self.update_button = QPushButton("Update", self)
        self.update_button.setToolTip(
            "Updates the selected template based on the JSON editor content."
        )
        self.update_button.clicked.connect(self.update_template)
        content_layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setToolTip(
            "Deletes the currently selected technology from the list."
        )
        self.delete_button.clicked.connect(self.delete_specific_technology)
        content_layout.addWidget(self.delete_button)

        self.serialize_button = QPushButton("Serialize", self)
        self.serialize_button.setToolTip(
            "Saves the content of the JSON editor to a file in JSON format."
        )
        self.serialize_button.clicked.connect(self.serialize_template)
        content_layout.addWidget(self.serialize_button)

        self.json_editor = QTextEdit(self)
        self.json_editor.setPlaceholderText("JSON content will appear here...")
        self.json_editor.setToolTip("A text editor for editing and viewing JSON data.")
        content_layout.addWidget(self.json_editor)

        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setPlaceholderText("Search...")
        self.search_line_edit.setToolTip("Search for technologies by name.")
        content_layout.addWidget(self.search_line_edit)

        self.technology_selector = QComboBox(self)
        self.technology_selector.setToolTip("Select a technology from the list.")
        content_layout.addWidget(self.technology_selector)

        container = QWidget()
        container.setLayout(content_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.search_manager = SearchManager(
            self, self.json_editor, self.search_line_edit
        )
        self.json_serializer = JsonSerializer(
            self, self.template_manager, self.json_editor, self.technology_selector
        )

        self.load_json_data()
        self.template_manager.populate_technology_selector(self.technology_selector)
        self.theme_manager.apply_theme()

    def load_style(self, style_file):
        """
        Loads a CSS stylesheet for the GUI.

        Parameters:
        - style_file (str): The name of the CSS file to load.
        """
        try:
            style_path = "gui/resources/" + style_file
            with open(style_path, "r", encoding="utf-8") as file:
                style = file.read()
                self.setStyleSheet(style)
        except FileNotFoundError:
            self.statusBar().showMessage(f"Style file {style_file} not found")

    def load_json_data(self):
        """
        Loads the current JSON data into the editor from the TemplateManager.
        """
        json_data = self.template_manager.load_json_data()
        if json_data:
            self.json_editor.setPlainText(json.dumps(json_data, indent=4))

    def create_template(self):
        """
        Creates a new template using the TemplateManager and displays the
        JSON content in the editor.
        """
        json_text, message = self.template_manager.create_template()
        if json_text:
            self.json_editor.setPlainText(json_text)
        self.statusBar().showMessage(message)

    def update_template(self):
        """
        Updates the currently selected template with the JSON data from the editor.
        """
        json_text = self.json_editor.toPlainText()
        message = self.template_manager.update_template(json_text)
        if "successfully" in message:
            self.load_json_data()
            self.template_manager.populate_technology_selector(self.technology_selector)
        self.statusBar().showMessage(message)

    def delete_specific_technology(self):
        """
        Deletes the currently selected technology from the list using TemplateManager.
        """
        selected_technology = self.technology_selector.currentText()
        message = self.template_manager.delete_specific_technology(selected_technology)
        self.statusBar().showMessage(message)
        if "removed successfully" in message:
            self.load_json_data()
            self.template_manager.populate_technology_selector(self.technology_selector)

    def serialize_template(self):
        """
        Serializes (saves) the content of the JSON editor to a file using JsonSerializer.
        """
        self.json_serializer.serialize_template()
