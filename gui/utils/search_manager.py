"""
This module manages search functionality within the JSON editor.
It provides real-time search capabilities and highlights matching text.
"""

from PyQt5.QtCore import Qt

class SearchManager:
    """
    Manages search operations within the JSON editor, including real-time text search
    and highlighting of matching text.
    """

    def __init__(self, parent, json_editor, search_line_edit):
        """
        Initializes the SearchManager with the parent widget, JSON editor, and search line edit.

        :param parent: The parent widget (typically a QMainWindow or QWidget).
        :param json_editor: The text editor widget where the search is performed.
        :param search_line_edit: The line edit widget used for entering search terms.
        """
        self.parent = parent
        self.json_editor = json_editor
        self.search_line_edit = search_line_edit
        self.search_line_edit.textChanged.connect(self.search_text)

    def search_text(self):
        """
        Performs a search based on the text in the search line edit.
        Highlights the matching text and updates the status bar with search results.
        """
        search_term = self.search_line_edit.text()
        cursor = self.json_editor.textCursor()
        cursor.movePosition(cursor.Start)
        char_format = cursor.charFormat()
        char_format.setBackground(Qt.yellow)
        cursor.setCharFormat(char_format)
        cursor = self.json_editor.textCursor()

        if search_term:
            cursor = self.json_editor.document().find(search_term, cursor)
            if cursor.isNull():
                self.parent.statusBar().showMessage("No matches found")
            else:
                self.json_editor.setTextCursor(cursor)
                self.parent.statusBar().showMessage("Text found")
        else:
            self.json_editor.setTextCursor(cursor)
            self.parent.statusBar().showMessage("")
