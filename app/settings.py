import os
import json


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


def create_project_files(project_dir, project_name, admins_data):
    """
    Creates the necessary project files based on the specified technology in the project directory.

    Args:
        project_dir (str): The absolute path to the project directory.
        project_name (str): The name of the project to create.
        admins_data (list): List of dictionaries containing admin data for each technology.

    Returns:
        None.
    """

    # Create project directory
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    for admin_data in admins_data:
        tech = admin_data["technology"]
        tech_path = os.path.join(project_path, "db", tech)
        os.makedirs(tech_path, exist_ok=True)

        for file_name, content in admin_data.items():
            if file_name != "technology":
                file_path = os.path.join(tech_path, file_name + ".json")
                write_to_json(file_path, content)

    print(
        f"Project '{project_name}' created successfully in directory '{project_dir}'!"
    )
