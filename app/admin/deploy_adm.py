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

    # Add .gitignore content to project_tree
    project_tree = admin_data.get("project_tree", [])
    project_tree.append(
        {
            "name": ".gitignore",
            "is_folder": False,
            "content": admin_data.get(".gitignore", ""),
        }
    )

    for file_info in project_tree:
        if file_info.get("children"):
            create_nested_files(tech_path, file_info)
        else:
            file_name = file_info["name"]
            file_content = file_info.get("content", "")
            file_path = os.path.join(tech_path, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(file_content)

    print(
        f"Project '{project_name}' created successfully in directory '{project_dir}'!"
    )


def create_nested_files(parent_path, file_info):
    """
    Creates nested files and directories recursively.

    Args:
        parent_path (str): The absolute path to the parent directory.
        file_info (dict): Information about the file or directory.

    Returns:
        None.
    """
    if file_info.get("children"):
        dir_name = file_info["name"]
        dir_path = os.path.join(parent_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        for child_info in file_info["children"]:
            create_nested_files(dir_path, child_info)
    else:
        file_name = file_info["name"]
        file_content = file_info.get("content", "")  # Provide default empty string
        if file_content is None:
            file_content = ""  # Ensure file_content is a string
        file_path = os.path.join(parent_path, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_content)

