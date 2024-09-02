"""
This module contains the GUI implementation for the Lazy Project application.
"""

import json
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QLabel,
    QComboBox,
    QDialog,
    QFileDialog,
    QSpacerItem,
    QSizePolicy,
    QLineEdit,
)
from PyQt5.QtCore import Qt, QPoint
from .utils import TemplateManager


class LazyProjectGUI(QMainWindow):
    """
    Main window class for the Lazy Project GUI application.
    """
    def __init__(self):
        """
        Initializes the LazyProjectGUI window, sets up the template manager, and
        initializes UI components.
        """
        super().__init__()
        self.template_manager = TemplateManager(self.statusBar())
        self.is_moving = False
        self.offset = QPoint()
        self.is_dark_mode = False
        self.is_fullscreen = False  # Track fullscreen state
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface components and layout of the main window.
        """
        self.setWindowTitle("Lazy Project GUI")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        main_layout = QVBoxLayout()

        title_bar_layout = QHBoxLayout()
        title_bar_layout.setContentsMargins(0, 0, 0, 0)
        title_bar_layout.setSpacing(5)

        title_bar_widget = QWidget(self)
        title_bar_widget.setObjectName("title_bar_widget")
        title_bar_widget.setFixedHeight(40)
        title_bar_widget.setLayout(title_bar_layout)

        title_label = QLabel("Lazy Project GUI", self)
        title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        title_bar_layout.addWidget(title_label)

        # Help button
        self.help_button = QPushButton("?", self)
        self.help_button.setObjectName("help_button")
        self.help_button.setFixedSize(30, 30)
        self.help_button.clicked.connect(self.show_help)
        title_bar_layout.addWidget(self.help_button)

        # Theme toggle button
        self.theme_toggle_button = QPushButton("🌕", self)
        self.theme_toggle_button.setObjectName("theme_toggle_button")
        self.theme_toggle_button.setFixedSize(30, 30)
        self.theme_toggle_button.clicked.connect(self.toggle_theme)
        title_bar_layout.addWidget(self.theme_toggle_button)

        self.minimize_button = QPushButton("_", self)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setFixedSize(30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        title_bar_layout.addWidget(self.minimize_button)

        self.maximize_button = QPushButton("⬜", self)
        self.maximize_button.setObjectName("maximize_button")
        self.maximize_button.setFixedSize(30, 30)
        self.maximize_button.clicked.connect(self.toggle_maximize)
        title_bar_layout.addWidget(self.maximize_button)

        self.close_button = QPushButton("X", self)
        self.close_button.setObjectName("close_button")
        self.close_button.setFixedSize(30, 30)
        self.close_button.clicked.connect(self.close)
        title_bar_layout.addWidget(self.close_button)

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(10, 10, 10, 10)
        content_layout.setSpacing(10)

        self.create_button = QPushButton("Create", self)
        self.create_button.setFocusPolicy(Qt.StrongFocus)
        self.create_button.clicked.connect(self.create_template)
        content_layout.addWidget(self.create_button)

        self.update_button = QPushButton("Update", self)
        self.update_button.setFocusPolicy(Qt.StrongFocus)
        self.update_button.clicked.connect(self.update_template)
        content_layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setFocusPolicy(Qt.StrongFocus)
        self.delete_button.clicked.connect(self.delete_specific_technology)
        content_layout.addWidget(self.delete_button)

        self.serialize_button = QPushButton("Serialize", self)
        self.serialize_button.setFocusPolicy(Qt.StrongFocus)
        self.serialize_button.clicked.connect(self.serialize_template)
        content_layout.addWidget(self.serialize_button)

        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setPlaceholderText("Search...")
        self.search_line_edit.textChanged.connect(self.search_text)
        content_layout.addWidget(self.search_line_edit)

        self.json_editor = QTextEdit(self)
        self.json_editor.setPlaceholderText("JSON content will appear here...")
        self.json_editor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        content_layout.addWidget(self.json_editor)

        self.technology_selector = QComboBox(self)
        content_layout.addWidget(self.technology_selector)

        content_layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        container = QWidget()
        container.setLayout(content_layout)

        main_layout.addWidget(title_bar_widget)
        main_layout.addWidget(container)

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.load_json_data()
        self.template_manager.populate_technology_selector(self.technology_selector)
        self.apply_theme()

    def toggle_theme(self):
        """
        Toggles between dark and light themes, and updates the UI accordingly.
        """
        self.is_dark_mode = not self.is_dark_mode
        self.theme_toggle_button.setText("🌑" if self.is_dark_mode else "🌕")
        self.apply_theme()

    def apply_theme(self):
        """
        Applies the current theme to the UI by loading the appropriate CSS file.
        """
        theme_file = "dark_theme.css" if self.is_dark_mode else "light_theme.css"
        self.load_style(theme_file)

    def toggle_maximize(self):
        """
        Toggles the window between maximized and normal states.
        """
        if self.isMaximized():
            self.showNormal()
            self.maximize_button.setText("⬜")
        else:
            self.showMaximized()
            self.maximize_button.setText("❐")

    def toggle_fullscreen(self):
        """
        Toggles the window between fullscreen and normal modes.
        """
        if self.is_fullscreen:
            self.showNormal()
            self.fullscreen_button.setText("Fullscreen")
        else:
            self.showFullScreen()
            self.fullscreen_button.setText("Exit Fullscreen")
        self.is_fullscreen = not self.is_fullscreen

    def load_json_data(self):
        """
        Loads JSON data from the template manager and displays it in the JSON editor.
        """
        json_data = self.template_manager.load_json_data()
        if json_data:
            self.json_editor.setPlainText(json.dumps(json_data, indent=4))

    def create_template(self):
        """
        Creates a new template and updates the JSON editor with the new content.
        """
        json_text, message = self.template_manager.create_template()
        if json_text:
            self.json_editor.setPlainText(json_text)
        self.statusBar().showMessage(message)

    def update_template(self):
        """
        Updates the existing template with the content from the JSON editor.
        """
        json_text = self.json_editor.toPlainText()
        message = self.template_manager.update_template(json_text)
        if "successfully" in message:
            self.load_json_data()
            self.template_manager.populate_technology_selector(self.technology_selector)
        self.statusBar().showMessage(message)

    def delete_specific_technology(self):
        """
        Deletes the currently selected technology from the template.
        """
        selected_technology = self.technology_selector.currentText()
        message = self.template_manager.delete_specific_technology(selected_technology)
        self.statusBar().showMessage(message)
        if "removed successfully" in message:
            self.load_json_data()
            self.template_manager.populate_technology_selector(self.technology_selector)

    def serialize_template(self):
        """
        Opens a file dialog to save the current JSON content to a file.
        """
        selected_technology = self.technology_selector.currentText()
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            f"Save {selected_technology.capitalize()} JSON As",
            "",
            "JSON Files (*.json);;All Files (*)",
            options=options,
        )
        if file_name:
            json_text = self.json_editor.toPlainText()
            message = self.template_manager.serialize_template(json_text, file_name)
            self.statusBar().showMessage(message)

    def search_text(self):
        """
        Searches for the text entered in the search bar and highlights
        the occurrences in the JSON editor.
        """
        search_term = self.search_line_edit.text()
        cursor = self.json_editor.textCursor()
        cursor.movePosition(cursor.Start)
        format = cursor.charFormat()
        format.setBackground(Qt.yellow)
        cursor.setCharFormat(format)
        cursor = self.json_editor.textCursor()

        if search_term:
            cursor = self.json_editor.document().find(search_term, cursor)
            if cursor.isNull():
                self.statusBar().showMessage("No matches found")
            else:
                self.json_editor.setTextCursor(cursor)
                self.statusBar().showMessage("Text found")
        else:
            self.json_editor.setTextCursor(cursor)
            self.statusBar().showMessage("")

    def load_style(self, style_file):
        """
        Loads and applies a CSS style sheet to the application.

        Args:
            style_file (str): The name of the CSS file to load.
        """
        try:
            style_path = "gui/resources/" + style_file
            with open(style_path, "r", encoding='utf-8') as file:
                style = file.read()
                self.setStyleSheet(style)
        except FileNotFoundError:
            self.statusBar().showMessage(f"Style file {style_file} not found")

    def show_help(self):
        """
        Displays a dialog with help information about the application and its features.
        """
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle("Help")
        help_layout = QVBoxLayout()
        help_label = QLabel(
            """
            Here you can create, update, delete, and serialize admins JSON. 
            Use the search bar to find text and the Fullscreen button for easier editing. 
            If you have any questions, press the Help button.
            """
        )
        help_label.setWordWrap(True)
        help_layout.addWidget(help_label)
        help_dialog.setLayout(help_layout)
        help_dialog.exec_()

    def mouse_press_event(self, event):
        """
        Handles mouse press events to enable window dragging.

        Args:
            event (QMouseEvent): The mouse press event.
        """
        if event.button() == Qt.LeftButton:
            self.is_moving = True
            self.offset = event.pos()

    def mouse_move_event(self, event):
        """
        Handles mouse move events to update the window position during dragging.

        Args:
            event (QMouseEvent): The mouse move event.
        """
        if self.is_moving:
            self.move(event.globalPos() - self.offset)

    def mouse_release_event(self, event):
        """
        Handles mouse release events to stop window dragging.

        Args:
            event (QMouseEvent): The mouse release event.
        """
        self.is_moving = False
