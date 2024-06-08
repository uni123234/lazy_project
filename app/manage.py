from enum import StrEnum
import os
import sys
from .admin.deploy_adm import (
    create_project_files,
    get_admin_data,
)


class TemplateCommands(StrEnum):
    # TEMPLATE COMMANDS
    FASTAPI: str = "fastapi_quick"
    AIOGRAM: str = "aiogram_quick"
    FLASK: str = "flask_quick"


AVAILABLE_COMMANDS = list(TemplateCommands.__members__.values())


def main():
    """
    Entry point for project management commands.
    """
    if len(sys.argv) < 4:
        print("Usage: python main.py <command> <project_directory> <project_name>")
        print("Available commands:", ", ".join(AVAILABLE_COMMANDS))
        return 1

    _root, command, project_dir, project_name, *c = sys.argv
    if not os.path.isdir(project_dir):
        raise NotImplementedError(f"Project directory '{project_dir}' does not exist.")
    if command not in AVAILABLE_COMMANDS:
        print("Usage: python main.py <command> <project_directory> <project_name>")
        print("Available commands:", ", ".join(AVAILABLE_COMMANDS))
        return 1

    technology, specifier = project_name.split("_")

    admin_data = get_admin_data(technology)
    if admin_data:
        create_project_files(project_dir, project_name, admin_data)
    else:
        print(f"Error: Admin data not found for {technology}.")
        return 1


if __name__ == "__main__":
    exit(main())
