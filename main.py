"""
main.py

This module contains the entry point for the LazyProject application. 
It allows you to run either the GUI version or the console version based on command-line arguments.
"""

import sys
import argparse
from PyQt5.QtWidgets import QApplication
from gui import LazyProjectGUI
from app import main as console_main


def run_gui():
    """
    Initialize and run the LazyProject GUI application.
    """
    app = QApplication(sys.argv)
    window = LazyProjectGUI()
    window.show()
    sys.exit(app.exec_())


def run_console():
    """
    Run the LazyProject console application.
    """
    sys.exit(console_main())


def main():
    """
    Main function to parse arguments and run the appropriate version of the application.
    """
    parser = argparse.ArgumentParser(description="Run the LazyProject application.")
    parser.add_argument(
        "--gui", action="store_true", help="Run the GUI version of the application."
    )
    parser.add_argument(
        "--console",
        action="store_true",
        help="Run the console version of the application.",
    )

    args = parser.parse_args()

    if args.gui:
        run_gui()
    elif args.console:
        run_console()
    else:
        print("Please specify either --gui or --console.")
        sys.exit(1)


if __name__ == "__main__":
    main()
