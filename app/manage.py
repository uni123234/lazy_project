import os
from user.deploy import create_project_files  # Assuming create_project_files.py is in the same directory

def main():
  """
  Entry point for project management commands.
  """
  # Check if first argument is a valid command
  if len(sys.argv) < 2 or sys.argv[1] not in ["create_project"]:
    print(f"Usage: {sys.argv[0]} <command> [arguments]")
    print("Available commands:")
    print("  create_project: Creates a new project with specified name.")
    return 1

  # Handle specific commands
  if sys.argv[1] == "create_project":
    if len(sys.argv) < 3:
      print("Error: Please provide a project name.")
      return 1
    project_name = sys.argv[2]
    admins_data = {  # Replace with your default admin data structure
      "main_content": "...",
      "run_content": "...",
      "requirements": "...",
      ".gitignore": "...",
      "Readme": "...",
    }
    create_project_files(project_name, admins_data)
    print(f"Project '{project_name}' created successfully!")

if __name__ == "__main__":
  import sys
  exit(main())
