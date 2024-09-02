"""
This module handles project-related exceptions and commands.
"""

import json
from enum import Enum, unique


class ProjectError(Exception):
    """Base class for project-related exceptions."""

    ...


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
    """Load technologies from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("technologies", [])
    except FileNotFoundError as exc:
        raise AdminDataError("File not found") from exc
    except json.JSONDecodeError as exc:
        raise AdminDataError("Invalid JSON format") from exc


# Load technologies from the JSON file
technologies = load_technologies(ADMINS_FILE_PATH)


@unique
class TemplateCommands(Enum):
    """Enum for template commands."""

    FASTAPI = "fastapi"
    AIOGRAM = "aiogram"
    FLASK = "flask"

    @classmethod
    def add_technology(cls, technology):
        """Add a new technology to the enum."""
        if technology.upper() not in cls.__members__:
            # Create a new Enum type dynamically
            new_enum = Enum(technology.upper(), [(technology.upper(), technology)])
            cls.__members__.update(new_enum.__members__)


# Dynamically add technologies from the JSON file
for tech in technologies:
    TemplateCommands.add_technology(tech)


class Root(Enum):
    """Enum for root commands."""

    SERIALIZE = "serialize_template"
    UPDATE = "update_template"
    DELETE = "delete_template"
    DESERIALIZE = "deserialize_template"


AVAILABLE_TEMPLATES = [tech.value for tech in TemplateCommands]
AVAILABLE_COMMANDS = [cmd.value for cmd in Root]

if __name__ == "__main__":
    """Main entry point for testing purposes."""
    print("Available Templates:", AVAILABLE_TEMPLATES)
    print("Available Commands:", AVAILABLE_COMMANDS)
