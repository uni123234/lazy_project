"""
This module initializes the app package for the lazy_project.

It includes imports for error handling, command and template management,
and technology loading.

Imports:
- ProjectError, UsageError, CommandError, DirectoryError, TemplateError, 
- AdminDataError: Custom error classes.
- TemplateCommands, Root: Classes or functions related to templates and root operations.
- load_technologies: Function to load available technologies.
- ADMINS_FILE_PATH, AVAILABLE_COMMANDS, AVAILABLE_TEMPLATES: Configuration constants.
- technologies: Dictionary or list of technologies.
- main: Entry point for managing commands.

This module sets up the necessary components and configurations for the application.
"""

from .settings import (
    ProjectError,
    UsageError,
    CommandError,
    DirectoryError,
    TemplateError,
    AdminDataError,
    TemplateCommands,
    Root,
    load_technologies,
    ADMINS_FILE_PATH,
    AVAILABLE_COMMANDS,
    AVAILABLE_TEMPLATES,
    technologies,
)
from .manage import main
