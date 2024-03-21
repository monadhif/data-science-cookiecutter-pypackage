#!/usr/bin/env python
import re
import subprocess
import sys

project_name = "{{ cookiecutter.project_name }}"
print("I'm the pre_gen_project.py hook!!!")
print(f"Checking project name: {project_name}")
print("Checking python version: {{ cookiecutter.python_version }}")


# Check if project_name contains only letters, numbers, hyphens, underscores or spaces
if not re.match(r"^[\w -]+$", project_name):
    print(
        f"ERROR: The project name ({project_name}) is not valid. It must contain only letters, numbers, hyphens, underscores, or spaces."
    )
    sys.exit(1)


python_version = "{{ cookiecutter.python_version }}"
# Check if the selected python version is available on the system
try:
    output = subprocess.check_output("python --version", shell=True, encoding='UTF-8')
    print("type of output: ", type(output))
    if not output.startswith(f"Python {python_version}"):
        print(output)
        print(f"Python {python_version} is not installed. Please install it and try again.")
        sys.exit(1)
except subprocess.CalledProcessError:
    print("Python is not installed. Please install it and try again.")
    sys.exit(1)
# check if the slected use_dependency_manager is installed
use_dependency_manager = "{{ cookiecutter.use_dependency_manager }}"
if use_dependency_manager == "poetry":
    try:
        output = subprocess.check_output("poetry --version", shell=True, encoding='UTF-8')
    except subprocess.CalledProcessError:
        print("Poetry is not installed. Please install it and try again.")
        sys.exit(1)
elif use_dependency_manager == "pipenv":
    try:
        output = subprocess.check_output("pipenv --version", shell=True, encoding='UTF-8')
    except subprocess.CalledProcessError:
        print("Pipenv is not installed. Please install it and try again.")
        sys.exit(1)
elif use_dependency_manager == "none":
    print("No dependency manager chosen. Skipping environment setup.")
else:
    print("Unknown dependency manager. Please choose either poetry, pipenv or none.")
    sys.exit(1)










print("All checks passed!")
