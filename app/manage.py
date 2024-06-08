import os
import sys

# Importing functions from custom modules
from db.db import validate_arguments, parse_project_name, get_admin_data
from .admin.deploy_adm import create_project_files_two, create_project_files

# Importing constants and custom exceptions from settings module
from app.settings import (
    AVAILABLE_TEMPLATES,
    AVAILABLE_COMMANDS,
    TemplateCommands,
    Root,
    ProjectError,
    UsageError,
    CommandError,
    DirectoryError,
    TemplateError,
    AdminDataError,
)


def main():
    """
    Main function to execute the script.
    """
    try:
        # Validate command-line arguments
        command, project_dir, project_name = validate_arguments()

        # Parse project name to extract technology and specifier
        technology, specifier = parse_project_name(project_name)

        # Get administrative data for the specified technology
        admin_data = get_admin_data(technology)
        if not admin_data:
            raise AdminDataError(technology)

        # Create project files based on the retrieved administrative data
        create_project_files_two(project_dir, project_name, admin_data["project_tree"])

    except ProjectError as e:
        # Handle custom project-related errors
        print(f"Error: {e.message}")
        sys.exit(1)


if __name__ == "__main__":
    # Execute main function if the script is run directly
    main()
