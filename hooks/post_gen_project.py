#!/usr/bin/env python
"""Post-generate hook for cookiecutter-pypackage-pyproject template."""
import os
import subprocess

python_version = "{{ cookiecutter.python_version }}"

# # Handle dependency manager
# if "{{ cookiecutter.use_dependency_manager }}" == "poetry":
#     # Check if Poetry is installed
#     if not subprocess.call("command -v poetry", shell=True):
#         print("Poetry could not be found, installing...")
#         subprocess.call(
#             "curl -sSL https://install.python-poetry.org | python -", shell=True
#         )

#     # Initialize a new Poetry project
#     print("Initializing a new Poetry project...")
#     subprocess.call("poetry new {{cookiecutter.project_name}}", shell=True)

#     # Move into the new project directory
#     os.chdir("{{cookiecutter.project_name}}")

#     # Set Python version in pyproject.toml
#     with open("pyproject.toml", "a", encoding="utf-8") as f:
#         f.write(f"\n[tool.poetry.dependencies]\npython = ^{python_version}")

#     # Install dependencies
#     print("Installing dependencies...")
#     subprocess.call("poetry install", shell=True)
# elif "{{ cookiecutter.use_dependency_manager }}" == "pipenv":
#     # Check if Pipenv is installed
#     if not subprocess.call("command -v pipenv", shell=True):
#         print("Pipenv could not be found, installing...")
#         subprocess.call("pip install pipenv", shell=True)

#     # Initialize a new Pipenv environment with the chosen Python version
#     print("Initializing a new Pipenv environment...")
#     subprocess.call(f"pipenv --python {python_version}", shell=True)

#     # Install dependencies
#     print("Installing dependencies...")
#     subprocess.call("pipenv install", shell=True)
# elif "{{ cookiecutter.use_dependency_manager }}" == "none":
#     print("No dependency manager chosen. Skipping environment setup.")
#     # Handle virtual environment creation
#     if "{{ cookiecutter.create_virtualenv }}" == "conda":
#         # Initialize a new Conda environment
#         print("Initializing a new Conda environment...")
#         subprocess.call(
#             f"conda create --name {{cookiecutter.project_name}} python={python_version}",
#             shell=True,
#         )
#     elif "{{ cookiecutter.create_virtualenv }}" == "virtualenv":
#         # Initialize a new Virtualenv environment
#         print("Initializing a new Virtualenv environment...")
#         subprocess.call(
#             f"virtualenv -p python{python_version} {{cookiecutter.project_name}}",
#             shell=True,
#         )
#     elif "{{ cookiecutter.create_virtualenv }}" == "venv":
#         # Initialize a new venv environment
#         print("Initializing a new venv environment...")
#         subprocess.call(
#             f"python{python_version} -m venv {{cookiecutter.project_name}}", shell=True
#         )
#     elif "{{ cookiecutter.create_virtualenv }}" == "none":
#         print("No virtual environment creation chosen. Skipping environment setup.")
