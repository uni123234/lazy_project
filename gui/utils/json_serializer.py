"""
This module provides functionality for serializing templates to JSON files
using PyQt5. It includes a class for handling the serialization process
and interacting with the user through a file-saving dialog.
"""

from PyQt5.QtWidgets import QFileDialog


class JsonSerializer:
    """
    Handles the serialization of templates to JSON files, providing
    a GUI file-saving dialog for users to save the files.
    """

    def __init__(self, parent, template_manager, json_editor, technology_selector):
        """
        Initializes the JsonSerializer with the necessary components.

        :param parent: The parent widget (typically a QMainWindow or QWidget).
        :param template_manager: The manager responsible for handling template operations.
        :param json_editor: The widget (e.g., QTextEdit) containing the JSON to be serialized.
        :param technology_selector: The widget (e.g., QComboBox) that selects the technology type.
        """
        self.parent = parent
        self.template_manager = template_manager
        self.json_editor = json_editor
        self.technology_selector = technology_selector

    def serialize_template(self):
        """
        Opens a file dialog to save the current template as a JSON file.
        The method retrieves the JSON from the editor and calls the template manager
        to handle the serialization process.
        """
        selected_technology = self.technology_selector.currentText()
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self.parent,
            f"Save {selected_technology.capitalize()} JSON As",
            "",
            "JSON Files (*.json);;All Files (*)",
            options=options,
        )
        if file_name:
            json_text = self.json_editor.toPlainText()
            message = self.template_manager.serialize_template(json_text, file_name)
            self.parent.statusBar().showMessage(message)
