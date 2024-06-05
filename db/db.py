import json
import os
from settings import create_project_files


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
    with open("db.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        admins = data.get("admins", [])
        for admin in admins:
            if admin["technology"] == technology:
                return admin
        return None


# Command: fastapi_quick
admins_data = get_admin_data("fastapi")
if admins_data:
    create_project_files("project_dir", "project_name", [admins_data])

# Command: aiogram_quick
admins_data = get_admin_data("aiogram")
if admins_data:
    create_project_files("project_dir", "project_name", [admins_data])

# Command: flask_quick
admins_data = get_admin_data("flask")
if admins_data:
    create_project_files("project_dir", "project_name", [admins_data])

# Command for users.json
users_content = {"commands": ["fastapi_quick", "aiogram_quick", "flask_quick"]}
write_to_json("db/user/users.json", users_content)
