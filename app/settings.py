import json
import os


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
    with open("db/admin/admins.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        admins = data.get("projects", [])
        for admin in admins:
            if admin["technology"] == technology:
                return admin
        return None


def create_project_files(project_dir, project_name, admin_data):
    """
    Creates the necessary project files based on the specified technology in the project directory.

    Args:
        project_dir (str): The absolute path to the project directory.
        project_name (str): The name of the project to create.
        admin_data (dict): Dictionary containing admin data for the technology.

    Returns:
        None.
    """
    # Create project directory
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    tech = admin_data["technology"]
    tech_path = os.path.join(project_path, tech)
    os.makedirs(tech_path, exist_ok=True)

    for file_info in admin_data["files"]:
        file_path = os.path.join(tech_path, file_info["name"])
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_info["content"])

    print(f"Project '{project_name}' created successfully in directory '{project_dir}'!")