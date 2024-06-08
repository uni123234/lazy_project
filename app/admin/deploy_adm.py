import os
import json


# FIXME: DRY, DO NOT FUGGING REPEAT
def write_to_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# TODO: add annotations
def get_admin_data(technology):
    with open("db/admin/admins.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        admins = data.get("projects", [])
        for admin in admins:
            if admin["technology"] == technology:
                return admin
        return None


# TODO: add annotations
# BUG: WTF DOES IT RETURNS?
def create_project_files(project_dir, project_name, admin_data):
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    tech = admin_data["technology"]
    tech_path = os.path.join(project_path, tech)
    os.makedirs(tech_path, exist_ok=True)

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


# TODO: add annotations
# BUG: WTF DOES IT RETURNS?
def create_nested_files(parent_path, file_info):
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
