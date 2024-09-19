#!/usr/bin/env python
import os
import sys

WIN = sys.platform.startswith('win')

def activate_venv():
    """Provide instructions to activate the virtual environment based on the OS."""
    venv_dir = ".venv"

    if not os.path.exists(venv_dir):
        print("Virtual environment not found.")
        return False

    if WIN:
        activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
        print(f"To activate the virtual environment on Windows, run: \n{activate_script}")
        print("To deactivate the virtual environment, run 'deactivate' command.")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        print(f"To activate the virtual environment on Unix-based systems, run: \nsource {activate_script}")
    
    return True

def main():
    """Post-generation hook to provide instructions for activating the virtual environment."""
    # Check the dependency manager choice from cookiecutter context
    use_dependency_manager = "{{ cookiecutter.dependency_manager }}".lower()

    if use_dependency_manager == "none":
        # In case of 'none', assume virtual environment creation was desired
        if activate_venv():
            print("Activation instructions displayed.")
        else:
            print("No virtual environment found to activate.")
    else:
        print("No virtual environment setup required for this dependency manager.")

    print("Project setup completed successfully!")

if __name__ == "__main__":
    main()
