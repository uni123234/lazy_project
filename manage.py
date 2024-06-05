import os
import sys
import json
from app.user.deploy import create_project_files  # Assuming create_project_files is in user/deploy.py

def main():
    """
    Entry point for project management commands.
    """
    # Check if first argument is a valid command
    if len(sys.argv) < 3 or sys.argv[1] not in ["fastapi_quick"]:
        print(f"Usage: {sys.argv[0]} fastapi_quick <project_directory> <project_name>")
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

        # Load admin data from JSON file
        with open('db/admin/admins.json', 'r', encoding='utf-8') as f:
            admins_data = json.load(f)

        create_project_files(project_dir, project_name, admins_data)
        print(f"Project '{project_name}' created successfully in directory '{project_dir}'!")

if __name__ == "__main__":
    exit(main())
