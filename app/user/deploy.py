import bson
import os

def write_to_bson(file_path, data):
  """
  Writes the provided data to a BSON file.

  Args:
      file_path (str): Path to the BSON file.
      data (dict): Data to be written in BSON format.
  """
  with open(file_path, "wb") as f: 
    f.write(bson.encode(data)) 


def create_project_files(project_name, admins_data):
    """
    Creates the necessary project files for a FastAPI API in the specified directory.

    Args:
        project_name (str): The name of the project to create.
        admins_data (dict): Data to write to the project files.

        admins_data should have the following structure:

        {
            "main_content": (str) Content for main.py,
            "run_content": (str) Content for uvicorn startup script,
            "requirements": (str) List of required dependencies,
            ".gitignore": (str) Git ignore patterns,
            "readme": (str) Project description and usage instructions,
            "user_verification_function": (callable) Function to verify user credentials (optional)
        }
    """

    # Prompt user for project directory path and get absolute path
    project_dir = os.path.abspath(
        input("Enter the absolute path to the project directory: ")
    )

    # Check if project directory exists, create if not
    os.makedirs(project_dir, exist_ok=True)

    # Define file paths within the project directory
    admins_file_path = os.path.join(project_dir, "db/admin/admins.bson")  # Placeholder for future admin data
    users_file_path = os.path.join(project_dir, "db/user/users.bson")  # Placeholder for user data (not used directly)
    main_py_path = os.path.join(project_dir, "main.py")
    run_content = os.path.join(project_dir, "run.py")
    requirements_path = os.path.join(project_dir, "requirements.txt")
    gitignore_path = os.path.join(project_dir, ".gitignore")
    readme_path = os.path.join(project_dir, "Readme.md")  # Use .md for markdown

    # Write content to each file
    write_to_bson(admins_file_path, admins_data)  # Assuming write_to_bson exists

    with open(main_py_path, "w") as f:
        f.write(admins_data["main_content"])
    
    with open(main_py_path, "w") as f:
        f.write(admins_data["run_content"])

    with open(requirements_path, "w") as f:
        f.write(admins_data["requirements"])

    with open(gitignore_path, "w") as f:
        f.write(admins_data[".gitignore"])

    with open(readme_path, "w") as f:
        f.write(admins_data["readme"])