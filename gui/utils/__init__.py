"""
Initialization module for the 'utils' package in the 'gui' directory.

This package provides utility functions and classes used throughout the
'gui' module of the project.

Functions:
- build_tree: Function to build a project tree structure.
- build_project_structure: Function to set up the project structure.

Classes:
- TemplateManager: Class to manage and apply templates in the project.
"""

from .utils import build_tree, build_project_structure
from .template_manager import TemplateManager
from .json_serializer import JsonSerializer
from .menu_manager import MenuManager
from .them_manager import ThemeManager
from .search_manager import SearchManager
