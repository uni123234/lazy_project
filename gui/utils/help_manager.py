"""
This module provides a HelpManager class for showing help dialogs related 
to various buttons in the application's user interface.
"""

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class HelpManager:
    """
    HelpManager provides help dialogs for the different buttons in the user interface.

    Methods:
    - show_create_help: Shows help dialog for the 'Create' button.
    - show_update_help: Shows help dialog for the 'Update' button.
    - show_delete_help: Shows help dialog for the 'Delete' button.
    - show_serialize_help: Shows help dialog for the 'Serialize' button.
    - show_help: Shows general help and links to external documentation.
    """

    def __init__(self, parent):
        """
        Initializes the HelpManager with a parent widget.

        Parameters:
        parent (QWidget): The parent widget of the help dialogs.
        """
        self.parent = parent

    def show_create_help(self):
        """
        Displays a help dialog explaining the functionality of the 'Create' button.

        The 'Create' button is responsible for creating a new template using
        the TemplateManager and displaying the JSON representation in the editor.
        """
        help_dialog = QDialog(self.parent)
        help_dialog.setWindowTitle("Create Button Help")
        help_layout = QVBoxLayout()

        help_text = """
        The 'Create' button is responsible for creating a new template. 
        When you click this button, a new template will be generated using 
        the TemplateManager, and its JSON representation will be displayed 
        in the JSON editor.
        """
        help_label = QLabel(help_text)
        help_layout.addWidget(help_label)

        help_dialog.setLayout(help_layout)
        help_dialog.exec_()

    def show_update_help(self):
        """
        Displays a help dialog explaining the functionality of the 'Update' button.

        The 'Update' button updates the selected template with the content
        currently in the JSON editor.
        """
        help_dialog = QDialog(self.parent)
        help_dialog.setWindowTitle("Update Button Help")
        help_layout = QVBoxLayout()

        help_text = """
        The 'Update' button updates the selected template with the content 
        currently in the JSON editor. It reads the text from the editor and 
        replaces the existing template with the new JSON data.
        """
        help_label = QLabel(help_text)
        help_layout.addWidget(help_label)

        help_dialog.setLayout(help_layout)
        help_dialog.exec_()

    def show_delete_help(self):
        """
        Displays a help dialog explaining the functionality of the 'Delete' button.

        The 'Delete' button removes the selected technology from the list.
        """
        help_dialog = QDialog(self.parent)
        help_dialog.setWindowTitle("Delete Button Help")
        help_layout = QVBoxLayout()

        help_text = """
        The 'Delete' button removes the selected technology from the technology list. 
        Once deleted, the template is removed from the dropdown and JSON data.
        """
        help_label = QLabel(help_text)
        help_layout.addWidget(help_label)

        help_dialog.setLayout(help_layout)
        help_dialog.exec_()

    def show_serialize_help(self):
        """
        Displays a help dialog explaining the functionality of the 'Serialize' button.

        The 'Serialize' button saves the content of the JSON editor to a file
        in JSON format.
        """
        help_dialog = QDialog(self.parent)
        help_dialog.setWindowTitle("Serialize Button Help")
        help_layout = QVBoxLayout()

        help_text = """
        The 'Serialize' button saves the content of the JSON editor to a file 
        in JSON format. It uses the JsonSerializer to handle the process of 
        saving the file on your system.
        """
        help_label = QLabel(help_text)
        help_layout.addWidget(help_label)

        help_dialog.setLayout(help_layout)
        help_dialog.exec_()

    def show_help(self):
        """
        Displays a general help dialog with a link to external documentation.
        """
        help_dialog = QDialog(self.parent)
        help_dialog.setWindowTitle("Help")
        help_layout = QVBoxLayout()

        help_text = """
        For detailed documentation of the application and its buttons, 
        please visit the following link:
        """
        help_label = QLabel(help_text)
        help_layout.addWidget(help_label)

        # github_link = QLabel(
        #     '<a href="https://github.com/your-repository/documentation">GitHub Documentation</a>'
        # )
        # github_link.setOpenExternalLinks(True)
        # help_layout.addWidget(github_link)

        help_dialog.setLayout(help_layout)
        help_dialog.exec_()
