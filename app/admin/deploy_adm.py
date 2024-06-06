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
        projects = data.get("projects", [])
        for project in projects:
            if project["technology"] == technology:
                return project
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
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    tech = admin_data["technology"]
    tech_path = project_path  # os.path.join(project_path, tech)
    os.makedirs(tech_path, exist_ok=True)

    for file_info in admin_data["files"]:
        file_subdir, file_name = os.path.split(file_info["name"])
        if file_subdir:
            subdir_path = os.path.join(tech_path, file_subdir)
            os.makedirs(subdir_path, exist_ok=True)
            file_path = os.path.join(subdir_path, file_name)
        else:
            file_path = os.path.join(tech_path, file_name)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_info["content"])

    print(
        f"Project '{project_name}' created successfully in directory '{project_dir}'!"
    )


def add_remove_code_image(project_dir, technology, action):
    """
    Add or remove code files from the project.
    """
    # TODO: ??????
    project_code_dir = os.path.join(project_dir, technology, "db")
    os.makedirs(project_code_dir, exist_ok=True)

    admin_data = get_admin_data(technology)
    if not admin_data:
        raise NotImplementedError(f"Admin data not found for {technology}.")

    if action == "add":
        for file_info in admin_data["files"]:
            file_subdir, file_name = os.path.split(file_info["name"])
            if file_subdir == "db":
                file_path = os.path.join(project_code_dir, file_name)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(file_info["content"])
                print(f"Code file '{file_name}' added successfully.")
    elif action == "remove":
        for file_info in admin_data["files"]:
            file_subdir, file_name = os.path.split(file_info["name"])
            if file_subdir == "db":
                file_path = os.path.join(project_code_dir, file_name)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Code file '{file_name}' removed successfully.")
                else:
                    print(f"Error: Code file '{file_name}' not found.")
    else:
        print("Error: Invalid action. Please use 'add' or 'remove'.")


def edit_code_image(project_dir, technology, code_file, new_content):
    """
    Edit a code file in the project.
    """
    project_code_dir = os.path.join(project_dir, technology, "db")
    file_path = os.path.join(project_code_dir, code_file)

    if os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Code file '{code_file}' edited successfully.")
    else:
        print(f"Error: Code file '{code_file}' not found.")
