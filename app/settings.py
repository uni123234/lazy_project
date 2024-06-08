import os
import json


ADMINS_FILE_PATH = "db/admin/admins.json"


def write_to_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_project_files(project_dir, project_name, project_tree):
    project_path = os.path.join(project_dir, project_name)
    os.makedirs(project_path, exist_ok=True)

    for item in project_tree:
        item_name = item["name"]
        item_path = os.path.join(project_path, item_name)
        if item.get("is_folder"):
            os.makedirs(item_path, exist_ok=True)
            children = item.get("children", [])
            if children:
                create_project_files(project_path, item_name, children)
        else:
            content = item.get("content")
            if content is not None:
                with open(item_path, "w", encoding="utf-8") as file:
                    file.write(content)
            else:
                print(f"Error: Content is None for item {item_name}")

    print(
        f"Project '{project_name}' created successfully in directory '{project_dir}'!"
    )


def get_admin_data(technology):
    admin_data = read_from_json(ADMINS_FILE_PATH)
    projects = admin_data.get("projects", [])
    for project in projects:
        if project["technology"] == technology:
            return project
    return None
