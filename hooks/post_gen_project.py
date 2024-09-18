#!/usr/bin/env python
import os
import subprocess
import sys

WIN = sys.platform.startswith('win')

def execute_cmd(args, shell=False):
    """Execute shell commands and return output."""
    try:
        result = subprocess.run(args, shell=shell, cwd=os.getcwd(), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)

def activate_venv():
    """Activate virtual environment based on the OS."""
    venv_dir = ".venv"

    if WIN:
        activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
        print(f"Activating virtual environment for Windows: {activate_script}")
        command = f"{activate_script}"
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        print(f"Activating virtual environment for Unix-based system: {activate_script}")
        command = f"source {activate_script}"
    
    if WIN:
        # On Windows, use os.system to run batch script
        os.system(f'cmd /k "{activate_script}"')
    else:
        # On Unix-like systems, use shell execution
        print(f"Run the following command to activate your virtual environment: \nsource {activate_script}")
        # Depending on the shell used, you might have to just print the command for manual activation.

def main():
    """Post-generation hook to activate the virtual environment."""
    create_virtualenv = "{{ cookiecutter.create_virtualenv }}".lower()
    
    if create_virtualenv == "yes":
        print("Virtual environment creation completed.")
        activate_venv()
    else:
        print("Skipping virtual environment activation.")
    
    print("Project setup completed successfully!")

if __name__ == "__main__":
    main()
