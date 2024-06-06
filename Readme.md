# Проект Управління / Project Management

Цей проект - система управління проектами для швидкої генерації початкових шаблонів для різних технологій. Ви можете легко створювати нові проекти за допомогою шаблонів та налаштовувати їх за своїми потребами.

This project is a project management system for quickly generating initial templates for various technologies. You can easily create new projects using templates and customize them to your needs.

## Використання / Usage

1. **Створіть проектний каталог / Create Project Directory**: Створіть нову теку для вашого проекту.

2. **Використовуйте команди управління / Use Management Commands**: Запустіть скрипт `manage.py` з потрібними командами для створення проекту або виконання дій з кодом.

   Приклади команд (Command Examples):

   - `python manage.py fastapi_quick /шлях/до/проекту НазваПроекту /path/to/project ProjectName`: Створює проект FastAPI з базовою структурою / Creates a FastAPI project with a basic structure.
   - `python manage.py aiogram_quick /шлях/до/проекту НазваПроекту /path/to/project ProjectName`: Створює проект AIogram з базовою структурою / Creates an AIogram project with a basic structure.
   - `python manage.py flask_quick /шлях/до/проекту НазваПроекту /path/to/project ProjectName`: Створює проект Flask з базовою структурою / Creates a Flask project with a basic structure.
   - `python manage.py add_code /шлях/до/проекту fastapi /path/to/project fastapi`: Додає код для FastAPI до існуючого проекту / Adds FastAPI code to an existing project.
   - `python manage.py remove_code /шлях/до/проекту fastapi /path/to/project fastapi`: Видаляє код FastAPI з проекту / Removes FastAPI code from the project.
   - `python manage.py edit_code /шлях/до/проекту fastapi main.py /path/to/project fastapi main.py`: Редагує код файлу `main.py` для проекту FastAPI / Edits the code of the `main.py` file for the FastAPI project.

3. **Налаштуйте проект / Customize Project**: Після створення проекту відредагуйте файли за своїми потребами. Додайте нові файли або змініть існуючі.

## Додаткова інформація / Additional Information

- [Документація FastAPI / FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/first-steps/): Документація зі швидкого створення API за допомогою FastAPI / Documentation for quickly creating APIs using FastAPI.
- [Документація AIogram / AIogram Documentation](https://docs.aiogram.dev/en/latest/): Офіційна документація AIogram для розробки ботів Telegram / Official documentation for AIogram for developing Telegram bots.
- [Документація Flask / Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/): Офіційна документація Flask для створення веб-додатків на Python / Official documentation for Flask for creating web applications in Python.

