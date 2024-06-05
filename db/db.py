import json
import os
from app import create_project_files


def write_to_json(file_path, data):
    """
    Function to write data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (dict): Data to write.

    Returns:
        None.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_admin_data(technology):
    """
    Get admin data for a specific technology.

    Args:
        technology (str): The technology for which to retrieve admin data.

    Returns:
        dict: Admin data for the specified technology.
    """
    with open("admins.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        projects = data.get("projects", [])
        for project in projects:
            if project["technology"] == technology:
                return project
        return None


def create_and_run_project(technology, project_dir, project_name):
    """
    Create and run project files for the specified technology.

    Args:
        technology (str): The technology for which to create project files.
        project_dir (str): Directory where the project will be created.
        project_name (str): Name of the project.

    Returns:
        None.
    """
    project_data = get_admin_data(technology)
    if project_data:
        create_project_files(project_dir, project_name, project_data)


# Create and run projects for each technology
create_and_run_project("fastapi", "fastapi_project_dir", "fastapi_project")
create_and_run_project("aiogram", "aiogram_project_dir", "aiogram_project")
create_and_run_project("flask", "flask_project_dir", "flask_project")

# Write commands to users.json
users_content = {"commands": ["fastapi_quick", "aiogram_quick", "flask_quick"]}
write_to_json("db/user/users.json", users_content)
