"""
TemplateManager class for handling template operations.

This module provides functionalities to create, update, delete, serialize,
and load project templates in JSON format. It also includes methods to
populate a QComboBox with technology data from the JSON file.
"""
import json
import os
from PyQt5.QtWidgets import QFileDialog
from app import ProjectError, DirectoryError, AdminDataError, ADMINS_FILE_PATH
from .utils import build_project_structure


class TemplateManager:
    """
    Manages project templates including creation, update, deletion, and serialization.
    """

    def __init__(self, status_bar):
        """
        Initializes TemplateManager with a status bar.

        Args:
            status_bar: Status bar widget to display messages.
        """
        self.status_bar = status_bar

    def create_template(self):
        """
        Creates a new template based on the user's selected directory.

        Returns:
            Tuple containing JSON string of the project structure and a status message.
        """
        directory = QFileDialog.getExistingDirectory(None, "Choose project directory")
        if directory:
            try:
                project_structure = build_project_structure(directory)
                with open(ADMINS_FILE_PATH, "w", encoding="utf-8") as file:
                    json.dump(project_structure, file, indent=4)
                return (
                    json.dumps(project_structure, indent=4),
                    "Admins JSON created successfully",
                )
            except (AdminDataError, DirectoryError, ProjectError) as e:
                return None, f"Error creating project structure: {str(e)}"
            except (IOError, json.JSONDecodeError) as e:
                return f"Error handling file or JSON: {str(e)}"


    def update_template(self, json_text):
        """
        Updates the existing template with the provided JSON text.

        Args:
            json_text: JSON string to update the template.

        Returns:
            Status message indicating success or failure.
        """
        if json_text:
            try:
                data = json.loads(json_text)
                with open(ADMINS_FILE_PATH, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
                return "Admins JSON updated successfully"
            except json.JSONDecodeError:
                return "Invalid JSON format"
            except (AdminDataError, DirectoryError, ProjectError) as e:
                return f"Error updating admins JSON: {str(e)}"


    def delete_specific_technology(self, technology):
        """
        Deletes all projects with the specified technology from the JSON file.

        Args:
            technology: Technology to remove from the JSON data.

        Returns:
            Status message indicating success or failure.
        """
        try:
            with open(ADMINS_FILE_PATH, "r", encoding="utf-8") as file:
                json_data = json.load(file)

            json_data["projects"] = [
                project
                for project in json_data.get("projects", [])
                if project["technology"] != technology
            ]

            with open(ADMINS_FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(json_data, file, indent=4)

            return f"{technology} technology removed successfully."
        except FileNotFoundError:
            return "Admins JSON file not found"
        except (AdminDataError, DirectoryError, ProjectError) as e:
            return f"Error updating admins JSON: {str(e)}"

    def serialize_template(self, json_text, file_name):
        """
        Serializes the JSON text to a specified file.

        Args:
            json_text: JSON string to serialize.
            file_name: Path to the file where JSON will be saved.

        Returns:
            Status message indicating success or failure.
        """
        if file_name:
            if json_text:
                try:
                    data = json.loads(json_text)
                    with open(file_name, "w", encoding="utf-8") as file:
                        json.dump(data, file, indent=4)
                    return "Admins JSON serialized successfully"
                except json.JSONDecodeError:
                    return "Invalid JSON format"
                except (AdminDataError, DirectoryError, ProjectError) as e:
                    return f"Error serializing admins JSON: {str(e)}"
        return None

    def load_json_data(self):
        """
        Loads JSON data from the admins file.

        Returns:
            Loaded JSON data or None if file does not exist.
        """
        try:
            if os.path.exists(ADMINS_FILE_PATH):
                with open(ADMINS_FILE_PATH, "r", encoding="utf-8") as file:
                    return json.load(file)
            else:
                return None
        except (IOError, json.JSONDecodeError) as e:
            return f"Error handling file or JSON: {str(e)}"
        return None

    def populate_technology_selector(self, combo_box):
        """
        Populates the QComboBox with technologies from the JSON file.

        Args:
            combo_box: QComboBox widget to be populated.
        """
        json_data = self.load_json_data()
        if json_data:
            technologies = {
                project.get("technology") for project in json_data.get("projects", [])
            }
            combo_box.clear()
            combo_box.addItems(sorted(technologies))
