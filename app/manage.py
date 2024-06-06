import os
import sys
from .admin.deploy_adm import create_project_files, get_admin_data, add_remove_code_image, edit_code_image


def main():
    """
    Entry point for project management commands.
    """
    # Check if first argument is a valid command
    if len(sys.argv) < 3 or sys.argv[1] not in [
        "fastapi_quick",
        "aiogram_quick",
        "flask_quick",
        "add_code",
        "remove_code",
        "edit_code",
    ]:
        print(f"Usage: {sys.argv[0]} <command> <project_directory> <project_name>")
        print("Available commands: fastapi_quick, aiogram_quick, flask_quick, add_code, remove_code, edit_code")
        return 1

    # Get project directory from command line arguments
    project_dir = sys.argv[2]

    # Check if project directory exists
    if not os.path.isdir(project_dir):
        print(f"Error: Project directory '{project_dir}' does not exist.")
        return 1

    if len(sys.argv) < 4:
        print("Error: Please provide a project name.")
        return 1

    project_name = sys.argv[3]

    # Handle specific commands
    if sys.argv[1] == "fastapi_quick":
        admin_data = get_admin_data("fastapi")
        if admin_data:
            create_project_files(project_dir, project_name, admin_data)
        else:
            print("Error: Admin data not found for fastapi.")

    elif sys.argv[1] == "aiogram_quick":
        admin_data = get_admin_data("aiogram")
        if admin_data:
            create_project_files(project_dir, project_name, admin_data)
        else:
            print("Error: Admin data not found for aiogram.")

    elif sys.argv[1] == "flask_quick":
        admin_data = get_admin_data("flask")
        if admin_data:
            create_project_files(project_dir, project_name, admin_data)
        else:
            print("Error: Admin data not found for flask.")

    elif sys.argv[1] in ["add_code", "remove_code"]:
        if len(sys.argv) < 5:
            print("Error: Please provide the technology.")
            return 1
        technology = sys.argv[4]
        action = "add" if sys.argv[1] == "add_code" else "remove"
        add_remove_code_image(project_dir, technology, action)

    elif sys.argv[1] == "edit_code":
        if len(sys.argv) < 6:
            print("Error: Please provide the technology and code file name.")
            return 1
        technology = sys.argv[4]
        code_file = sys.argv[5]
        new_content = input("Enter new content for the file:\n")
        edit_code_image(project_dir, technology, code_file, new_content)


if __name__ == "__main__":
    exit(main())
