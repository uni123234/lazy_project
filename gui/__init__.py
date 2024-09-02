"""
This package contains the core components of the LazyProject application.

Modules:
- gui: Contains the graphical user interface elements of LazyProject.
- utils.template_manager: Provides functionality for managing and using templates.

This package initializes the LazyProject application and its components.
"""

from .gui import LazyProjectGUI
from .utils.template_manager import TemplateManager
from .manage import main
