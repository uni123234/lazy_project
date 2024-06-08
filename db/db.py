import os
import json


# FIXME: DRY
def write_to_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# FIXME: DRY
def get_admin_data(technology):
    with open("admins.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        projects = data.get("projects", [])
        for project in projects:
            if project["technology"] == technology:
                return project
        return None


# FIXME: DRY
def create_project_files(project_dir, project_name, admin_data):
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    tech = admin_data["technology"]
    tech_path = os.path.join(project_path, tech)
    os.makedirs(tech_path, exist_ok=True)

    for file_info in admin_data["files"]:
        file_path = os.path.join(tech_path, file_info["name"])
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_info["content"])

    print(
        f"Project '{project_name}' created successfully in directory '{project_dir}'!"
    )


# FIXME: What does it returns?
# BUG: Prints must be only inside main fugging function
def add_code_file(project_dir, technology, file_name, content):
    tech_path = os.path.join(project_dir, technology)
    os.makedirs(tech_path, exist_ok=True)

    file_path = os.path.join(tech_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Code file '{file_name}' added successfully in '{technology}' project.")


def remove_code_file(project_dir, technology, file_name):
    file_path = os.path.join(project_dir, technology, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(
            f"Code file '{file_name}' removed successfully from '{technology}' project."
        )
    else:
        print(f"Error: Code file '{file_name}' not found in '{technology}' project.")


def edit_code_file(project_dir, technology, file_name, new_content):
    file_path = os.path.join(project_dir, technology, file_name)

    if os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Code file '{file_name}' edited successfully in '{technology}' project.")
    else:
        print(f"Error: Code file '{file_name}' not found in '{technology}' project.")


# FIXME: MEDAITOR ALERT!!!
def create_and_run_project(technology, project_dir, project_name):
    project_data = get_admin_data(technology)
    if project_data:
        create_project_files(project_dir, project_name, project_data)


# FIXME: MEDAITOR ALERT!!!
def validate_commands(commands, valid_technologies):
    valid_commands = [
        cmd for cmd in commands if cmd.split("_")[0] in valid_technologies
    ]
    return valid_commands


# FIXME: second main??? Use tests or checkings
def main():
    with open("admins.json", "r", encoding="utf-8") as f:
        admin_data = json.load(f)
        valid_technologies = [
            project["technology"] for project in admin_data["projects"]
        ]

    with open("db/user/users.json", "r", encoding="utf-8") as f:
        user_data = json.load(f)
        user_commands = user_data.get("commands", [])

    valid_commands = validate_commands(user_commands, valid_technologies)

    for cmd in valid_commands:
        tech = cmd.split("_")[0]
        create_and_run_project(tech, f"{tech}_project_dir", f"{tech}_project")

    # Write valid commands back to users.json
    write_to_json("db/user/users.json", {"commands": valid_commands})


# WTF???
if __name__ == "__main__":
    main()
