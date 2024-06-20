import os
import json
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QComboBox, QDialog, QFileDialog
from PyQt5.QtCore import Qt

class LazyProjectGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lazy Project GUI')
        self.setGeometry(100, 100, 800, 600)

        # Set window always on top with workaround for window manager
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)

        # Main layout
        main_layout = QVBoxLayout()

        # Buttons
        self.create_button = QPushButton('Create', self)
        self.create_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px; }")
        self.create_button.clicked.connect(self.create_template)
        main_layout.addWidget(self.create_button)

        self.update_button = QPushButton('Update', self)
        self.update_button.setStyleSheet("QPushButton { background-color: #007BFF; color: white; border: none; padding: 10px; }")
        self.update_button.clicked.connect(self.update_template)
        main_layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Delete', self)
        self.delete_button.setStyleSheet("QPushButton { background-color: #DC3545; color: white; border: none; padding: 10px; }")
        self.delete_button.clicked.connect(self.delete_template)
        main_layout.addWidget(self.delete_button)

        self.serialize_button = QPushButton('Serialize', self)
        self.serialize_button.setStyleSheet("QPushButton { background-color: #17A2B8; color: white; border: none; padding: 10px; }")
        self.serialize_button.clicked.connect(self.serialize_template)
        main_layout.addWidget(self.serialize_button)

        # JSON Editor
        self.json_editor = QTextEdit(self)
        self.json_editor.setStyleSheet("QTextEdit { background-color: #ffffff; color: #333; border: 1px solid #ccc; padding: 5px; }")
        main_layout.addWidget(self.json_editor)

        # Color scheme selector
        self.color_selector = QComboBox(self)
        self.color_selector.addItems(['Light', 'Dark'])
        self.color_selector.setStyleSheet("QComboBox { background-color: #ffffff; color: #333; padding: 5px; }")
        self.color_selector.currentIndexChanged.connect(self.change_color_scheme)
        main_layout.addWidget(self.color_selector)

        # Help button
        self.help_button = QPushButton('Help', self)
        self.help_button.setStyleSheet("QPushButton { background-color: #6C757D; color: white; border: none; padding: 10px; }")
        self.help_button.clicked.connect(self.show_help)
        main_layout.addWidget(self.help_button)

        # Container widget
        container = QWidget()
        container.setStyleSheet("background-color: #f0f0f0;")
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Set initial color scheme
        self.change_color_scheme()

    def create_template(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose project directory")
        if directory:
            project_structure = self.build_project_structure(directory)
            if project_structure:
                try:
                    with open('admins.json', 'w') as file:
                        json.dump(project_structure, file, indent=4)
                    self.json_editor.setPlainText(json.dumps(project_structure, indent=4))
                    self.statusBar().showMessage('Admins JSON created successfully')
                except Exception as e:
                    self.statusBar().showMessage(f'Error saving admins JSON: {str(e)}')
            else:
                self.statusBar().showMessage('Failed to build project structure')

    def build_project_structure(self, directory):
        project = {"projects": []}
        project_id = 1
        for root, dirs, files in os.walk(directory):
            root_path = os.path.relpath(root, directory)
            project_data = {
                "id": project_id,
                "technology": "your_technology_here",  # Replace with appropriate technology
                "project_tree": self.build_tree(root, root_path, dirs, files)
            }
            project["projects"].append(project_data)
            project_id += 1
        return project

    def build_tree(self, root, root_path, dirs, files):
        tree = []
        for directory in dirs:
            dir_path = os.path.join(root_path, directory)
            children = self.build_tree(os.path.join(root, directory), dir_path, os.listdir(os.path.join(root, directory)), [])
            tree.append({
                "name": directory,
                "is_folder": True,
                "children": children
            })
        for file in files:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
            tree.append({
                "name": file,
                "is_folder": False,
                "content": content
            })
        return tree

    def update_template(self):
        json_text = self.json_editor.toPlainText()
        if json_text:
            try:
                data = json.loads(json_text)
                with open('admins.json', 'w') as file:
                    json.dump(data, file, indent=4)
                self.statusBar().showMessage('Admins JSON updated successfully')
            except json.JSONDecodeError:
                self.statusBar().showMessage('Invalid JSON format')
        else:
            self.statusBar().showMessage('No JSON data to update the admins JSON')

    def delete_template(self):
        try:
            os.remove('admins.json')
            self.statusBar().showMessage('Admins JSON deleted successfully')
        except FileNotFoundError:
            self.statusBar().showMessage('Admins JSON file not found')

    def serialize_template(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Admins JSON As", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_name:
            json_text = self.json_editor.toPlainText()
            if json_text:
                try:
                    data = json.loads(json_text)
                    with open(file_name, 'w') as file:
                        json.dump(data, file, indent=4)
                    self.statusBar().showMessage('Admins JSON serialized successfully')
                except json.JSONDecodeError:
                    self.statusBar().showMessage('Invalid JSON format')

    def change_color_scheme(self):
        color = self.color_selector.currentText()
        if color == 'Light':
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    font-size: 12px;
                }
                
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 10px;
                }
                
                QTextEdit {
                    background-color: #ffffff;
                    color: #333;
                    border: 1px solid #ccc;
                    padding: 5px;
                }
                
                QComboBox {
                    background-color: #ffffff;
                    color: #333;
                    padding: 5px;
                }
                
                QDialog {
                    background-color: #ffffff;
                }
                
                QLabel {
                    color: #333;
                }
            """)
        else:  # Dark
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #333333;
                    font-family: Arial, sans-serif;
                    font-size: 12px;
                    color: white;
                }
                
                QPushButton {
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    padding: 10px;
                }
                
                QTextEdit {
                    background-color: #1C1C1C;
                    color: #ffffff;
                    border: 1px solid #555;
                    padding: 5px;
                }
                
                QComboBox {
                    background-color: #1C1C1C;
                    color: #ffffff;
                    padding: 5px;
                }
                
                QDialog {
                    background-color: #1C1C1C;
                    color: #ffffff;
                }
                
                QLabel {
                    color: #ffffff;
                }
            """)

    def show_help(self):
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle('Help')
        help_dialog.setStyleSheet("QDialog { background-color: #ffffff; }")
        help_layout = QVBoxLayout()
        help_label = QLabel('Here you can create, update, delete, and serialize admins JSON. Choose the interface color from the list. If you have any questions, press the Help button.')
        help_label.setStyleSheet("QLabel { color: #333; }")
        help_layout.addWidget(help_label)
        help_dialog.setLayout(help_layout)
        help_dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LazyProjectGUI()
    ex.show()
    sys.exit(app.exec_())
