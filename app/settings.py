import os
import json
from enum import Enum, unique

class ProjectError(Exception):
    """Base class for project-related exceptions."""
    
class UsageError(ProjectError):
    """Exception raised for usage errors."""

    def __init__(self):
        self.message = (
            "Usage: python main.py <command> <project_directory> <project_name>\n"
            f"Available commands: {', '.join(AVAILABLE_COMMANDS)}\n"
            f"Available templates: {', '.join(AVAILABLE_TEMPLATES)}"
        )
        super().__init__(self.message)

class CommandError(ProjectError):
    """Exception raised for invalid commands."""

    def __init__(self, command):
        self.message = (
            f"Invalid command '{command}'.\n"
            f"Available commands: {', '.join(AVAILABLE_COMMANDS)}"
        )
        super().__init__(self.message)

class DirectoryError(ProjectError):
    """Exception raised for directory-related errors."""

    def __init__(self, project_dir):
        self.message = f"Project directory '{project_dir}' does not exist."
        super().__init__(self.message)

class TemplateError(ProjectError):
    """Exception raised for invalid templates."""

    def __init__(self, template):
        self.message = (
            f"Invalid template '{template}'.\n"
            f"Available templates: {', '.join(AVAILABLE_TEMPLATES)}"
        )
        super().__init__(self.message)

class AdminDataError(ProjectError):
    """Exception raised for admin data retrieval errors."""

    def __init__(self, technology):
        self.message = f"Error: Admin data not found for technology '{technology}'."
        super().__init__(self.message)

ADMINS_FILE_PATH = "db/admin/admins.json"

def load_technologies(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('technologies', [])
    except FileNotFoundError:
        raise AdminDataError('File not found')
    except json.JSONDecodeError:
        raise AdminDataError('Invalid JSON format')

# Load technologies from the JSON file
technologies = load_technologies(ADMINS_FILE_PATH)

@unique
class TemplateCommands(Enum):
    # Initialize with hardcoded technologies
    FASTAPI = "fastapi"
    AIOGRAM = "aiogram"
    FLASK = "flask"

    @classmethod
    def add_technology(cls, technology):
        if technology.upper() not in cls.__members__:
            cls._member_map_[technology.upper()] = cls(technology)
            cls._value2member_map_[technology] = cls(technology)

# Dynamically add technologies from the JSON file
for tech in technologies:
    TemplateCommands.add_technology(tech)

class Root(Enum):
    serialize = "serialize_template"
    update = "update_template"
    delete = "delete_template"
    deserialize = "deserialize_template"

AVAILABLE_TEMPLATES = [tech.value for tech in TemplateCommands]
AVAILABLE_COMMANDS = [cmd.value for cmd in Root]

# Example usage to verify the dynamic addition
if __name__ == "__main__":
    print("Available Templates:", AVAILABLE_TEMPLATES)
    print("Available Commands:", AVAILABLE_COMMANDS)
