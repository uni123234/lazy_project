import os
import json

from db.db import write_to_json, get_admin_data

def create_project_files(project_dir, project_name, admin_data):
    """
    Create project files based on administrative data.

    Args:
        project_dir (str): The directory where the project will be created.
        project_name (str): The name of the project.
        admin_data (dict): Administrative data containing information about the project.

    Raises:
        TypeError: If admin_data is not a dictionary.
    """
    # Create the main project directory
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Check if admin_data is a dictionary
    if not isinstance(admin_data, dict):
        raise TypeError("admin_data should be a dictionary.")

    # Extract technology information and create technology-specific directory
    tech = admin_data["technology"]
    tech_path = os.path.join(project_path, tech)
    os.makedirs(tech_path, exist_ok=True)

    # Add .gitignore file if specified in project_tree
    project_tree = admin_data.get("project_tree", [])
    project_tree.append(
        {
            "name": ".gitignore",
            "is_folder": False,
            "content": admin_data.get(".gitignore", ""),
        }
    )

    # Iterate through project_tree to create files and directories
    for file_info in project_tree:
        if file_info.get("children"):
            # If file_info contains children, recursively create nested files and directories
            create_nested_files(tech_path, file_info)
        else:
            # Create individual file
            file_name = file_info["name"]
            file_content = file_info.get("content", "")
            if file_content is None:
                file_content = ""
            file_path = os.path.join(tech_path, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(file_content)

    # Print success message
    print(f"Project '{project_name}' created successfully in directory '{project_dir}'!")
    return

def create_nested_files(parent_path, file_info):
    """
    Recursively create nested files and directories.

    Args:
        parent_path (str): The parent directory where the nested files/directories will be created.
        file_info (dict): Information about the file or directory to be created.
    """
    if file_info.get("children"):
        # If file_info contains children, create a directory and recursively create nested files and directories
        dir_name = file_info["name"]
        dir_path = os.path.join(parent_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        for child_info in file_info["children"]:
            create_nested_files(dir_path, child_info)
    else:
        # Create individual file
        file_name = file_info["name"]
        file_content = file_info.get("content", "")
        if file_content is None:
            file_content = ""
        file_path = os.path.join(parent_path, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_content)
    return None

def create_project_files_two(project_dir, project_name, project_tree):
    """
    Create project files based on project tree structure.

    Args:
        project_dir (str): The directory where the project will be created.
        project_name (str): The name of the project.
        project_tree (list): The structure of the project containing information about files and directories.
    """
    # Create the main project directory
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Iterate through project_tree to create files and directories
    for item in project_tree:
        item_name = item["name"]
        item_path = os.path.join(project_path, item_name)
        if item.get("is_folder"):
            # If item is a folder, create a directory and handle its children recursively
            os.makedirs(item_path, exist_ok=True)
            children = item.get("children", [])
            if children:
                # Create a dictionary to pass as admin_data
                admin_data = {
                    "technology": "default_tech",  # Or some other default value
                    "project_tree": children
                }
                create_project_files(project_path, item_name, admin_data)
        else:
            # Create individual file
            content = item.get("content", "")  # Ensure content is not None
            if content is None:
                content = ""  # Default empty string if content is None
            with open(item_path, "w", encoding="utf-8") as file:
                file.write(content)

    # Print success message
    print(f"Project '{project_name}' created successfully in directory '{project_dir}'!")
    return
