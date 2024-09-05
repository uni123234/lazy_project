"""
This module contains the GUI implementation for the Lazy Project application.
"""

import json
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QLabel,
    QComboBox,
    QDialog,
    QLineEdit,
)
from .utils import TemplateManager, SearchManager, MenuManager, ThemeManager, JsonSerializer


class LazyProjectGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.template_manager = TemplateManager(self.statusBar())
        self.theme_manager = ThemeManager(self)
        self.menu_manager = MenuManager(self, self.theme_manager)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Lazy Project GUI")
        self.setGeometry(100, 100, 800, 600)

        content_layout = QVBoxLayout()

        # Кнопка "Create"
        self.create_button = QPushButton("Create", self)
        self.create_button.clicked.connect(self.create_template)
        content_layout.addWidget(self.create_button)

        # Кнопка "Update"
        self.update_button = QPushButton("Update", self)
        self.update_button.clicked.connect(self.update_template)
        content_layout.addWidget(self.update_button)

        # Кнопка "Delete"
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.clicked.connect(self.delete_specific_technology)
        content_layout.addWidget(self.delete_button)

        # Кнопка "Serialize"
        self.serialize_button = QPushButton("Serialize", self)
        self.serialize_button.clicked.connect(self.serialize_template)
        content_layout.addWidget(self.serialize_button)

        # JSON-редактор
        self.json_editor = QTextEdit(self)
        self.json_editor.setPlaceholderText("JSON content will appear here...")
        content_layout.addWidget(self.json_editor)

        # Поле для пошуку
        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setPlaceholderText("Search...")
        content_layout.addWidget(self.search_line_edit)

        # Вибір технології (ComboBox)
        self.technology_selector = QComboBox(self)
        content_layout.addWidget(self.technology_selector)

        container = QWidget()
        container.setLayout(content_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.search_manager = SearchManager(self, self.json_editor, self.search_line_edit)
        self.json_serializer = JsonSerializer(self, self.template_manager, self.json_editor, self.technology_selector)

        self.load_json_data()
        self.template_manager.populate_technology_selector(self.technology_selector)
        self.theme_manager.apply_theme()

    def load_style(self, style_file):
        try:
            style_path = "gui/resources/" + style_file
            with open(style_path, "r", encoding="utf-8") as file:
                style = file.read()
                self.setStyleSheet(style)
        except FileNotFoundError:
            self.statusBar().showMessage(f"Style file {style_file} not found")

    def load_json_data(self):
        json_data = self.template_manager.load_json_data()
        if json_data:
            self.json_editor.setPlainText(json.dumps(json_data, indent=4))

    def create_template(self):
        json_text, message = self.template_manager.create_template()
        if json_text:
            self.json_editor.setPlainText(json_text)
        self.statusBar().showMessage(message)

    def update_template(self):
        json_text = self.json_editor.toPlainText()
        message = self.template_manager.update_template(json_text)
        if "successfully" in message:
            self.load_json_data()
            self.template_manager.populate_technology_selector(self.technology_selector)
        self.statusBar().showMessage(message)

    def delete_specific_technology(self):
        selected_technology = self.technology_selector.currentText()
        message = self.template_manager.delete_specific_technology(selected_technology)
        self.statusBar().showMessage(message)
        if "removed successfully" in message:
            self.load_json_data()
            self.template_manager.populate_technology_selector(self.technology_selector)

    def serialize_template(self):
        self.json_serializer.serialize_template()

    def show_help(self):
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle("Help")
        help_layout = QVBoxLayout()
        help_label = QLabel("Help content goes here.")
        help_layout.addWidget(help_label)
        help_dialog.setLayout(help_layout)
        help_dialog.exec_()
