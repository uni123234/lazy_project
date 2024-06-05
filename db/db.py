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
    with open("admins.json", "r", encoding="utf-8") as f:
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
    tech_path = os.path.join(project_path, tech)
    os.makedirs(tech_path, exist_ok=True)

    for file_info in admin_data["files"]:
        file_path = os.path.join(tech_path, file_info["name"])
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_info["content"])

    print(f"Project '{project_name}' created successfully in directory '{project_dir}'!")

def add_code_file(project_dir, technology, file_name, content):
    """
    Add a code file to the project.

    Args:
        project_dir (str): Directory where the project is located.
        technology (str): Technology used in the project.
        file_name (str): Name of the file to add.
        content (str): Content to write into the file.
    """
    tech_path = os.path.join(project_dir, technology)
    os.makedirs(tech_path, exist_ok=True)

    file_path = os.path.join(tech_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"Code file '{file_name}' added successfully in '{technology}' project.")

def remove_code_file(project_dir, technology, file_name):
    """
    Remove a code file from the project.

    Args:
        project_dir (str): Directory where the project is located.
        technology (str): Technology used in the project.
        file_name (str): Name of the file to remove.
    """
    file_path = os.path.join(project_dir, technology, file_name)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Code file '{file_name}' removed successfully from '{technology}' project.")
    else:
        print(f"Error: Code file '{file_name}' not found in '{technology}' project.")

def edit_code_file(project_dir, technology, file_name, new_content):
    """
    Edit a code file in the project.

    Args:
        project_dir (str): Directory where the project is located.
        technology (str): Technology used in the project.
        file_name (str): Name of the file to edit.
        new_content (str): New content to write into the file.
    """
    file_path = os.path.join(project_dir, technology, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Code file '{file_name}' edited successfully in '{technology}' project.")
    else:
        print(f"Error: Code file '{file_name}' not found in '{technology}' project.")

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

def validate_commands(commands, valid_technologies):
    """
    Validate if the commands in users.json exist in admins.json.

    Args:
        commands (list): List of commands from users.json.
        valid_technologies (list): List of valid technologies from admins.json.

    Returns:
        list: List of valid commands.
    """
    valid_commands = [cmd for cmd in commands if cmd.split('_')[0] in valid_technologies]
    return valid_commands

def main():
    with open("admins.json", "r", encoding="utf-8") as f:
        admin_data = json.load(f)
        valid_technologies = [project["technology"] for project in admin_data["projects"]]

    with open("db/user/users.json", "r", encoding="utf-8") as f:
        user_data = json.load(f)
        user_commands = user_data.get("commands", [])
    
    valid_commands = validate_commands(user_commands, valid_technologies)
    
    for cmd in valid_commands:
        tech = cmd.split('_')[0]
        create_and_run_project(tech, f"{tech}_project_dir", f"{tech}_project")

    # Write valid commands back to users.json
    write_to_json("db/user/users.json", {"commands": valid_commands})

if __name__ == "__main__":
    main()
