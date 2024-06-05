import os
import sys
import json
from settings import create_project


def main():
    """
    Entry point for project management commands.
    """
    # Check if first argument is a valid command
    if len(sys.argv) < 3 or sys.argv[1] not in [
        "fastapi_quick",
        "aiogram_quick",
        "flask_quick",
    ]:
        print(f"Usage: {sys.argv[0]} <command> <project_directory> <project_name>")
        print("Available commands: fastapi_quick, aiogram_quick, flask_quick")
        return 1

    # Get project directory from command line arguments
    project_dir = sys.argv[2]

    # Check if project directory exists
    if not os.path.isdir(project_dir):
        print(f"Error: Project directory '{project_dir}' does not exist.")
        return 1

    # Handle specific commands
    if sys.argv[1] == "fastapi_quick":
        if len(sys.argv) < 4:
            print("Error: Please provide a project name.")
            return 1
        project_name = sys.argv[3]
        create_project(project_dir, project_name, "fastapi")

    elif sys.argv[1] == "aiogram_quick":
        if len(sys.argv) < 4:
            print("Error: Please provide a project name.")
            return 1
        project_name = sys.argv[3]
        create_project(project_dir, project_name, "aiogram")

    elif sys.argv[1] == "flask_quick":
        if len(sys.argv) < 4:
            print("Error: Please provide a project name.")
            return 1
        project_name = sys.argv[3]
        create_project(project_dir, project_name, "flask")


if __name__ == "__main__":
    exit(main())
