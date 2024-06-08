from app.manage import main

if __name__ == "__main__":
    """
    This checks whether the script is being executed directly (not imported as a module).
    If so, it executes the main() function from the app.manage module.
    After main() finishes its execution, the program exits with the return code received from main().
    """
    exit(main())
