"""
This module contains utility functions for managing project files and handling
command-line arguments.

Functions:
- parse_project_name: Extracts technology and specifier from the project name.
- write_to_json: Writes data to a JSON file.
- get_admin_data: Retrieves administrative data for a given technology.
- read_from_json: Reads data from a JSON file.
- create_project_files: Creates project files based on administrative data.
- add_code_file: Adds a new code file to the specified project.
- remove_code_file: Removes a code file from the specified project.
- edit_code_file: Edits a code file in the specified project.
- create_and_run_project: Creates and runs a project based on technology and name.
- validate_arguments: Validates command-line arguments.

Exceptions:
- DirectoryError: Raised when a directory does not exist.
- CommandError: Raised when an invalid command is encountered.
"""

import os
import json
import sys

from app.settings import CommandError, DirectoryError, UsageError, AVAILABLE_COMMANDS


def parse_project_name(project_name):
    """Parse the project name to extract technology and specifier."""
    if "_" in project_name:
        technology, specifier = project_name.split("_")
    else:
        technology = project_name
        specifier = None
    return technology, specifier


def write_to_json(file_path, data):
    """Write data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_admin_data(technology):
    """Get administrative data for a given technology."""
    with open("db/admin/admins.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        projects = data.get("projects", [])
        for project in projects:
            if project["technology"] == technology:
                return project
        return None


def read_from_json(file_path):
    """Read data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_project_files(project_dir, project_name, admin_data):
    """Create project files based on administrative data."""
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    tech = admin_data["technology"]
    tech_path = os.path.join(project_path, tech)
    os.makedirs(tech_path, exist_ok=True)

    for file_info in admin_data["files"]:
        file_path = os.path.join(tech_path, file_info["name"])
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_info["content"])

    print(
        f"Project '{project_name}' created successfully in directory '{project_dir}'!"
    )


def add_code_file(project_dir, technology, file_name, content):
    """Add a code file to the specified project."""
    tech_path = os.path.join(project_dir, technology)
    os.makedirs(tech_path, exist_ok=True)

    file_path = os.path.join(tech_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return print(
        f"Code file '{file_name}' added successfully in '{technology}' project."
    )


def remove_code_file(project_dir, technology, file_name):
    """Remove a code file from the specified project."""
    file_path = os.path.join(project_dir, technology, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        return print(
            f"Code file '{file_name}' removed successfully from '{technology}' project."
        )
    else:
        return print(
            f"Error: Code file '{file_name}' not found in '{technology}' project."
        )


def edit_code_file(project_dir, technology, file_name, new_content):
    """Edit a code file in the specified project."""
    file_path = os.path.join(project_dir, technology, file_name)

    if os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
        return print(
            f"Code file '{file_name}' edited successfully in '{technology}' project."
        )
    else:
        return print(
            f"Error: Code file '{file_name}' not found in '{technology}' project."
        )


def create_and_run_project(technology, project_dir, project_name):
    """Create and run a project based on technology and project name."""
    project_data = get_admin_data(technology)
    if project_data:
        create_project_files(project_dir, project_name, project_data["project_tree"])



def validate_arguments():
    """Validate the command-line arguments."""
    if len(sys.argv) < 4:
        raise UsageError()

    command, project_dir, project_name = sys.argv[1:4]

    if not os.path.isdir(project_dir):
        raise DirectoryError(project_dir)

    if command not in AVAILABLE_COMMANDS:
        raise CommandError(command)

    return command, project_dir, project_name
