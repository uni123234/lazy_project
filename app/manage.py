from enum import StrEnum
import os
import sys
import json  # FIXME: unused lib
from .settings import create_project_files, get_admin_data


# TODO: keep it automated and use module system
class TemplateCommands(StrEnum):
    FASTAPI = "fastapi"
    AIOGRAM = "aiogram"
    FLASK = "flask"


class Root(StrEnum):
    serialize = "serialize_template"
    update = "update_template"
    delete = "delete_template"
    deserialize = "deserialize_template"


# ~

# TODO: Settings class???
AVAILABLE_TEMPLATES = list(TemplateCommands.__members__.values())
AVAILABLE_COMMANDS = list(Root.__members__.values())
# ~


def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <command> <project_directory> <project_name>")
        print("Available commands:", ", ".join(AVAILABLE_COMMANDS))
        print("Available templates:", ", ".join(AVAILABLE_TEMPLATES))
        return 1  # TODO: RAISE AN ERROR

    _root, command, project_dir, project_name, *c = sys.argv
    if not os.path.isdir(project_dir):
        raise NotImplementedError(f"Project directory '{project_dir}' does not exist.")
    if command not in AVAILABLE_COMMANDS:
        print("Available commands:", ", ".join(AVAILABLE_COMMANDS))
        print("Usage: python main.py <command> <project_directory> <project_name>")
        print("Available templates:", ", ".join(AVAILABLE_TEMPLATES))
        return 1  # TODO: RAISE AN ERROR

    if "_" in project_name:
        technology, specifier = project_name.split("_")
    else:
        technology = project_name
        specifier = None
    # FIXME: DONT USED MEDIATOR(db/db.py/create_and_run_project)
    admin_data = get_admin_data(technology)
    if admin_data:
        create_project_files(project_dir, project_name, admin_data["project_tree"])
    else:
        print(f"Error: Admin data not found for {technology}.")
        return 1  # TODO: RAISE AN ERROR


if __name__ == "__main__":
    exit(main())
