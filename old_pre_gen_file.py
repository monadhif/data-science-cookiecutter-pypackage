#!/usr/bin/env python
# import os
# import subprocess
# import sys
# from textwrap import dedent

# WIN = sys.platform.startswith('win')

# try:
#     import venv
# except ImportError:
#     venv = None

# try:
#     import virtualenv
# except ImportError:
#     virtualenv = None

# VIRTUALENV_AVAILABLE = venv or virtualenv

# def execute_cmd(args, check=True):
#     """Execute a shell command and handle errors."""
#     try:
#         result = subprocess.run(args, shell=WIN, cwd=os.getcwd(), check=check, capture_output=True, text=True)
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         print(f"Command failed: {e}")
#         print(e.output)
#         return None

# def create_venv(path):
#     """Create a virtual environment."""
#     if venv:
#         venv.create(path, with_pip=True)
#     elif virtualenv:
#         execute_cmd([sys.executable, '-m', 'virtualenv', path])
#     else:
#         print("Neither venv nor virtualenv is available.")
#         sys.exit(1)

# def activate_venv():
#     """Activate the virtual environment."""
#     venv_dir = ".venv"
#     if WIN:
#         activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
#     else:
#         activate_script = os.path.join(venv_dir, "bin", "activate")
#         activate_script = f"source {activate_script}"
    
#     if WIN:
#         command = f"{activate_script} && python -m pip install --upgrade pip setuptools"
#     else:
#         command = f"{activate_script} && pip install --upgrade pip setuptools"

#     if execute_cmd(command):
#         print("Virtual environment activated and updated.")
#     else:
#         print("Failed to activate or update the virtual environment.")
#         sys.exit(1)

# def main():
#     print("Starting project setup...")
    
#     # Create virtual environment
#     if not os.path.exists(".venv"):
#         create_venv(".venv")
    
#     # Activate virtual environment and install/update packages
#     activate_venv()

#     # Handle dependency manager setup if needed
#     use_dependency_manager = "{{ cookiecutter.use_dependency_manager }}"
#     if use_dependency_manager == "poetry":
#         print("Setting up Poetry...")
#         if execute_cmd("poetry --version") is None:
#             print("Poetry not found. Installing Poetry...")
#             if execute_cmd("curl -sSL https://install.python-poetry.org | python -"):
#                 print("Poetry installed successfully.")
#             else:
#                 print("Failed to install Poetry.")
#                 sys.exit(1)
#         else:
#             print("Poetry already installed.")
#             print("The Poetry version is: ", execute_cmd("poetry --version"))
#             # print("Creating pyproject.toml...")
#             # Create pyproject.toml file as needed


#     elif use_dependency_manager == "pipenv":
#         print("Setting up Pipenv...")
#         if execute_cmd("pipenv --version") is None:
#             print("Pipenv not found. Installing Pipenv...")
#             if execute_cmd("pip install pipenv"):
#                 print("Pipenv installed successfully.")
#             else:
#                 print("Failed to install Pipenv.")
#                 sys.exit(1)
#         else:
#             print("Pipenv already installed.")
#             print("The Pipenv version is: ", execute_cmd("pipenv --version"))
#             #
#             print("Creating Pipenv environment...")
#         # Set up Pipenv environment as needed

#     elif use_dependency_manager == "none":
#         print("No dependency manager chosen. Skipping setup.")

#     else:
#         print("Unknown dependency manager selected.")
#         sys.exit(1)

#     print("Project setup completed successfully!")

# if __name__ == "__main__":
#     main()
