"""
This module provides utilities for building a project structure.

It includes functions to traverse directories and create a hierarchical 
representation of the project, including files and directories.
"""

import os


def build_project_structure(directory):
    """
    Build a hierarchical representation of the project structure starting from a given directory.

    Args:
        directory (str): The root directory to start building the project structure.

    Returns:
        dict: A dictionary containing project details and the project tree.
    """
    project = {"projects": []}
    project_id = 1
    for root, dirs, files in os.walk(directory):
        root_path = os.path.relpath(root, directory)
        project_data = {
            "id": project_id,
            "technology": "your_technology_here",
            "project_tree": build_tree(root, root_path, dirs, files),
        }
        project["projects"].append(project_data)
        project_id += 1
    return project


def build_tree(root, root_path, dirs, files):
    """
    Recursively build a tree structure of directories and files.

    Args:
        root (str): The current directory path.
        root_path (str): The relative path of the current directory.
        dirs (list): List of directory names in the current directory.
        files (list): List of file names in the current directory.

    Returns:
        list: A list of dictionaries representing the directory and file structure.
    """
    tree = []
    for directory in dirs:
        dir_path = os.path.join(root_path, directory)
        children = build_tree(
            os.path.join(root, directory),
            dir_path,
            os.listdir(os.path.join(root, directory)),
            [],
        )
        tree.append({"name": directory, "is_folder": True, "children": children})
    for file in files:
        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
            content = f.read()
        tree.append({"name": file, "is_folder": False, "content": content})
    return tree
