import sys
from PyQt5.QtWidgets import QApplication
from gui import LazyProjectGUI


def main():
    """
    Main function to initialize and run the LazyProject application.

    Sets up the QApplication, creates the main window instance, 
    displays it, and starts the application's event loop.
    """
    app = QApplication(sys.argv)
    window = LazyProjectGUI()
    window.show()
    sys.exit(app.exec_())