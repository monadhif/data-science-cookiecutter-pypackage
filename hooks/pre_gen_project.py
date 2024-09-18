#!/usr/bin/env python
import os
import re
import subprocess
import sys

def check_python_version(python_version):
    try:
        output = subprocess.check_output(f"py -{python_version} -V", shell=True, universal_newlines=True)
        print(f"Python {python_version} is installed.")
        return True
    except subprocess.CalledProcessError:
        print(f"Python {python_version} is not installed.")
        return False

def get_python_path(version):
    try:
        output = subprocess.check_output("py -0p", shell=True, universal_newlines=True)
        for line in output.splitlines():
            parts = line.split()
            if len(parts) >= 2 and parts[0].strip() == f"-{version}-64":
                python_path = " ".join(parts[1:])
                print(f"Python {version} found.")
                return python_path
        print(f"Python {version} is not installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while getting Python paths: {e}")
    return None

def create_virtualenv(python_version):
    venv_dir = ".venv"
    python_exe = get_python_path(python_version)
    if python_exe is None:
        print(f"Failed to find Python {python_version} path.")
        return False
    try:
        print(f"Creating virtual environment with Python {python_version}...")
        subprocess.check_call([python_exe, "-m", "venv", venv_dir])
        return True
    except subprocess.CalledProcessError as creation_error:
        print(f"Failed to create virtual environment: {creation_error}")
        return False

def activate_virtualenv():
    venv_dir = ".venv"
    if os.name == 'nt':
        activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
        command = activate_script
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        command = f"source {activate_script}"
    try:
        print("Activating virtual environment...")
        subprocess.check_call(command, shell=True)
        activated_python_version = get_current_python_version()
        if activated_python_version:
            print(f"Virtual environment activated with Python {activated_python_version}.")
            return True
        else:
            print("Failed to determine the activated Python version.")
            return False
    except subprocess.CalledProcessError as activation_error:
        print(f"Failed to activate virtual environment: {activation_error}")
        return False

def get_current_python_version():
    try:
        output = subprocess.check_output("python -V", shell=True, universal_newlines=True)
        version_info = output.strip().split()[1]
        return version_info
    except Exception as e:
        print(f"Error occurred while getting the current Python version: {e}")
        return None

def main():
    project_name = "{{ cookiecutter.project_name }}"
    author_name = "{{ cookiecutter.author_name }}"
    author_email = "{{ cookiecutter.author_email }}"
    python_version = "{{ cookiecutter.python_version }}"
    use_dependency_manager = "{{ cookiecutter.use_dependency_manager }}"

    print("I'm the pre_gen_project.py hook!!!")
    print(f"Checking project name: {project_name}")
    print(f"Checking Python version: {python_version}")

    # Validate project name
    if not re.match(r"^[\w -]+$", project_name):
        print(f"ERROR: The project name ({project_name}) is not valid. It must contain only letters, numbers, hyphens, underscores, or spaces.")
        sys.exit(1)

    # Check if the selected Python version is installed
    if not check_python_version(python_version):
        print(f"ERROR: Python {python_version} is required but not installed.")
        sys.exit(1)

    venv_dir = ".venv"
    if not os.path.exists(venv_dir):
        create_venv = input(f"Virtual environment is not found. Do you want to create a virtual environment with Python {python_version}? (y/n): ")
        if create_venv.lower() == "y":
            if create_virtualenv(python_version):
                print("Virtual environment created successfully.")
            else:
                print("Failed to create virtual environment. Exiting.")
                sys.exit(1)
        else:
            print("Virtual environment not created. Exiting.")
            sys.exit(1)

    if not activate_virtualenv():
        print("Failed to activate virtual environment. Exiting.")
        sys.exit(1)

    # Handle dependency manager setup
    if use_dependency_manager == "poetry":
        try:
            print("Checking if Poetry is installed...")
            subprocess.check_output("poetry -V", shell=True)
        except subprocess.CalledProcessError:
            print("Poetry is not installed. Installing Poetry...")
            try:
                subprocess.check_output("curl -sSL https://install.python-poetry.org | python -", shell=True)
            except subprocess.CalledProcessError as e:
                print("Failed to install Poetry:", e.output)
                sys.exit(1)

        print("Creating pyproject.toml file...")
        with open("pyproject.toml", "w", encoding="utf-8") as f:
            f.write("[tool.poetry]\n")
            f.write(f"name = \"{project_name}\"\n")
            f.write("version = \"0.1.0\"\n")
            f.write("description = \"\"\n")
            f.write(f"authors = [\"{author_name} <{author_email}>\"]\n")
            f.write("\n")
            f.write("[tool.poetry.dependencies]\n")
            f.write(f"python = \"{python_version}\"\n")

        print("Installing dependencies with Poetry...")
        try:
            subprocess.check_output(f"poetry install --python={python_version}", shell=True)
        except subprocess.CalledProcessError as e:
            print("Failed to install dependencies with Poetry:", e.output)
            sys.exit(1)
    elif use_dependency_manager == "pipenv":
        try:
            output = subprocess.check_output("pipenv --version", shell=True, encoding='UTF-8')
        except subprocess.CalledProcessError:
            print("Pipenv is not installed. Installing it now...")
            subprocess.run("pip install pipenv", shell=True, check=True)
    elif use_dependency_manager == "none":
        print("No dependency manager chosen. Skipping environment setup.")
    else:
        print("Unknown dependency manager. Please choose either poetry, pipenv, or none.")
        sys.exit(1)

    print("All checks passed!")

if __name__ == "__main__":
    main()
