import os


def add_remove_code_image(project_dir, code_files_dir, action):
    """
    Add or remove code files from the project.
    """
    project_code_dir = os.path.join(
        project_dir, "db"
    )  # Assuming 'db' directory in the project
    os.makedirs(project_code_dir, exist_ok=True)

    if action == "add":
        for filename in os.listdir(code_files_dir):
            file_path = os.path.join(code_files_dir, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    content = file.read()
                with open(
                    os.path.join(project_code_dir, filename), "w"
                ) as project_file:
                    project_file.write(content)
                    print(f"Code file '{filename}' added successfully.")
    elif action == "remove":
        for filename in os.listdir(code_files_dir):
            file_path = os.path.join(project_code_dir, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Code file '{filename}' removed successfully.")
            else:
                print(f"Error: Code file '{filename}' not found.")
    else:
        print("Error: Invalid action. Please use 'add' or 'remove'.")


def edit_code_image(project_dir, code_file, new_content):
    """
    Edit a code file in the project.
    """
    project_code_dir = os.path.join(project_dir, "db")
    file_path = os.path.join(project_code_dir, code_file)

    if os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(new_content)
        print(f"Code file '{code_file}' edited successfully.")
    else:
        print(f"Error: Code file '{code_file}' not found.")
