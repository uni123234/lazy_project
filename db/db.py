import json
import os

admins_file_path = "db/admin/admins.json"
users_file_path = "db/user/users.json"

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

admins_data = {
    "main_content": """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
""",
    "run_content": """
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
""",
    "requirements": """
fastapi
uvicorn
""",
    ".gitignore": """
*.pyc
__pycache__
.env
""",
    "Readme": """
## FastAPI API Example

This project contains a basic FastAPI API with two endpoints:

* `"/"`: Returns a JSON object with the text "Hello": "World".
* `"/items/{item_id}"`: Takes an `item_id` parameter (integer) and returns a JSON object with the `item_id` and an optional `q` parameter (string).

### Usage

1. Create a project folder.
2. Create a file named `main.py` and paste the code from `admins_data["main_content"]`.
3. Create a file named `requirements.txt` and add `fastapi uvicorn`.
4. Install the dependencies using `pip install -r requirements.txt`.
5. Run the API using the command `uvicorn main:app --host=127.0.0.1 --port=8000`.

### Additional Information

* FastAPI documentation: https://fastapi.tiangolo.com/tutorial/first-steps/
* How to write a FastAPI API: https://www.youtube.com/watch?v=SORiTsvnU28
"""
}

write_to_json(admins_file_path, admins_data)

users_content = {"command": "fastapi_quick"}
write_to_json(users_file_path, users_content)
