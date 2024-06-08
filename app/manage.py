import os
import sys
import json
from .admin.deploy_adm import create_project_files, get_admin_data
from .settings import TEMPLATES_FILE_PATH, read_from_json


class TemplateCommands(StrEnum):
    # TEMPLATE COMMANDS
    FASTAPI: str = "fastapi_quick"
    AIOGRAM: str = "aiogram_quick"
    FLASK: str = "flask_quick"


class Root(StrEnum):
    serialize: str = "serialize_template"
    update: str = "update_template"
    delete: str = "delete_template"
    deserialize: str = "deserialize_template"


AVAILABLE_TEMPLATES = list(TemplateCommands.__members__.values())
AVAILABLE_COMMANDS = list(Root.__members__.values())


def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <command> <project_directory> <project_name>")
        print("Available commands:", ", ".join(AVAILABLE_COMMANDS))
        print("Available templates:", ", ".join(AVAILABLE_TEMPLATES))
        return 1

    _root, command, project_dir, project_name, *c = sys.argv
    if not os.path.isdir(project_dir):
        raise NotImplementedError(f"Project directory '{project_dir}' does not exist.")
    if command not in AVAILABLE_TEMPLATES:
        print("Available commands:", ",".join(AVAILABLE_COMMANDS))
        print("Usage: python main.py <command> <project_directory> <templates_name>")
        print("Available templates:", ", ".join(AVAILABLE_TEMPLATES))
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
