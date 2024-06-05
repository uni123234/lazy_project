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
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def create_project_files(project_dir, project_name, admins_data):
    """
    Creates the necessary project files for a FastAPI API in the specified directory.

    Args:
        project_dir (str): The absolute path to the project directory.
        project_name (str): The name of the project to create.
        admins_data (dict): Data to write to the project files.

        admins_data should have the following structure:

        {
            "main_content": (str) Content for main.py,
            "run_content": (str) Content for uvicorn startup script,
            "requirements": (str) List of required dependencies,
            ".gitignore": (str) Git ignore patterns,
            "Readme": (str) Project description and usage instructions,
        }
    """

    # Create project directory
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Define file paths within the project directory
    admins_file_path = os.path.join(project_path, "lazy_project/db/admin/admins.json")
    users_file_path = os.path.join(project_path, "lazy_project/db/user/users.json")
    main_py_path = os.path.join(project_path, "main.py")
    run_py_path = os.path.join(project_path, "run.py")
    requirements_path = os.path.join(project_path, "requirements.txt")
    gitignore_path = os.path.join(project_path, ".gitignore")
    readme_path = os.path.join(project_path, "Readme.md")

    # Ensure directories exist
    os.makedirs(os.path.dirname(admins_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(users_file_path), exist_ok=True)

    # Write content to each file
    write_to_json(admins_file_path, admins_data)

    with open(main_py_path, "w", encoding='utf-8') as f:
        f.write(admins_data["main_content"])
    
    with open(run_py_path, "w", encoding='utf-8') as f:
        f.write(admins_data["run_content"])

    with open(requirements_path, "w", encoding='utf-8') as f:
        f.write(admins_data["requirements"])

    with open(gitignore_path, "w", encoding='utf-8') as f:
        f.write(admins_data[".gitignore"])

    with open(readme_path, "w", encoding='utf-8') as f:
        f.write(admins_data["Readme"])
