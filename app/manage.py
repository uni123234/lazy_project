from enum import StrEnum
import os
import sys
from .admin.deploy_adm import (
    create_project_files,
    get_admin_data,
    add_remove_code_image,
    edit_code_image,
)


class TemplateCommands(StrEnum):
    # TEMPLATE COMMANDS
    FASTAPI: str = "fastapi_quick"
    AIOGRAM: str = "aiogram_quick"
    FLASK: str = "flask_quick"


# USAGE:... import TemplateCommands as tc


class CRUDCommands(StrEnum):
    # CRUD COMMANDS
    CREATE: str = "add_code"
    DELETE: str = "remove_code"
    EDIT: str = "edit_code"


# USAGE:... import CRUDCommands as crud

AVAILABLE_COMMANDS = list(TemplateCommands.__members__.values()) + list(
    CRUDCommands.__members__.values()
)


def main():
    """
    Entry point for project management commands.
    """
    if len(sys.argv) < 3:
        raise NotImplementedError("Low arguments count")
    if len(sys.argv) < 4:
        raise NotImplementedError("Please provide a project name.")

    _root, command, project_dir, project_name, *c = sys.argv
    if not os.path.isdir(project_dir):
        raise NotImplementedError(f"Project directory '{project_dir}' does not exist.")
    if command not in AVAILABLE_COMMANDS:
        print(f"Usage: {_root} <command> <project_directory> <project_name>")
        raise NotImplementedError(f"Available commands: {AVAILABLE_COMMANDS}")

    technology, specifier = command.split("_")
    if command in ["add_code", "remove_code"]:
        # if len(sys.argv) < 5:
        #     raise NotImplementedError("Please provide the technology.")
        technology, specifier = project_name.split("_")

        action, *c = command.split("_")
        print(f"{action=}")
        add_remove_code_image(project_dir, technology, action)

    elif command == "edit_code":
        # if len(sys.argv) < 6:
        #     raise NotImplementedError(
        #         "Please provide the technology and code file name."
        #     )
        code_file = sys.argv[5]
        new_content = input("Enter new content for the file:\n")
        edit_code_image(project_dir, technology, code_file, new_content)
    else:
        admin_data = get_admin_data(technology)
        if admin_data:
            create_project_files(project_dir, project_name, admin_data)
        else:
            raise NotImplementedError(f"Admin data not found for {technology}.")


if __name__ == "__main__":
    exit(main())
