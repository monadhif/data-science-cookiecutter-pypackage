#!/usr/bin/env python
import os
import re
import subprocess
import sys


def run_command(command, check=True, shell=True, capture_output=False):
    """Helper function to run shell commands with error handling."""
    try:
        result = subprocess.run(command, shell=shell, check=check, capture_output=capture_output, text=True)
        return result.stdout.strip() if capture_output else True
    except subprocess.CalledProcessError as error:
        print(f"Command failed: {error}")
        return None


def get_available_python_versions():
    """Get a list of installed Python versions."""
    versions = []
    if os.name == 'nt':  # Windows
        try:
            output = run_command("py -0", capture_output=True)
            for line in output.splitlines():
                version = re.search(r"\d+\.\d+", line)
                if version:
                    versions.append(version.group())
        except subprocess.CalledProcessError:
            print("Failed to get Python versions.")
    else:  # macOS/Linux
        try:
            output = run_command("ls /usr/bin/python*", capture_output=True)
            for line in output.splitlines():
                version = re.search(r"python(\d+\.\d+)", line)
                if version:
                    versions.append(version.group(1))
        except subprocess.CalledProcessError:
            print("Failed to get Python versions.")
    return versions


def check_python_version(python_version):
    """Check if the specified Python version is installed and return it if available."""
    if os.name == 'nt':  # Windows
        output = run_command(f"py -{python_version} --version", capture_output=True)
        if output and python_version in output:
            return python_version
    else:  # macOS/Linux
        output = run_command(f"python{python_version} --version", capture_output=True)
        if output and python_version in output:
            return python_version

    return None


def find_compatible_python_version(required_version):
    """Find the closest compatible Python version available on the system."""
    available_versions = get_available_python_versions()
    if required_version in available_versions:
        return required_version
    
    # Find the closest version available
    major, minor = map(int, required_version.split('.'))
    for version in available_versions:
        v_major, v_minor = map(int, version.split('.'))
        if v_major == major and v_minor >= minor:
            return version
    return available_versions[0] if available_versions else None


def create_virtualenv(python_version):
    """Create a virtual environment using the specified Python version."""
    venv_dir = ".venv"
    if not os.path.exists(venv_dir):
        available_version = check_python_version(python_version)
        if not available_version:
            print(f"Desired Python version {python_version} not found.")
            available_version = find_compatible_python_version(python_version)
            if not available_version:
                print("No compatible Python version found. Please install the required version.")
                return False
            print(f"Using available Python version {available_version} instead.")

        print(f"Creating virtual environment with Python {available_version}...")
        if os.name == 'nt':
            run_command(f"py -{available_version} -m venv {venv_dir}")
        else:
            run_command(f"python{available_version} -m venv {venv_dir}")
        print("Virtual environment created successfully.")
        return True
    else:
        print(f"Virtual environment already exists in {venv_dir}.")
    return False


def activate_virtualenv():
    """Activate the virtual environment."""
    venv_dir = ".venv"
    if os.name == 'nt':
        activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
        command = activate_script
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
        command = f"source {activate_script}"
    
    print(f"Activating virtual environment: {command}")
    return run_command(command, shell=True)


def install_poetry(python_version):
    """Install Poetry and initialize project dependencies."""
    if not run_command("poetry -V", capture_output=True):
        print("Poetry is not installed. Installing Poetry...")
        if not run_command("curl -sSL https://install.python-poetry.org | python -"):
            print("Failed to install Poetry.")
            sys.exit(1)

    print("Creating pyproject.toml file with Poetry...")
    run_command(f"poetry env use python{python_version}")
    run_command("poetry init --name '{{ cookiecutter.project_name }}' --author '{{ cookiecutter.author_name }}' --no-interaction")

    print("Installing dependencies with Poetry...")
    run_command(f"poetry install")


def install_pipenv(python_version):
    """Install Pipenv and set up the environment."""
    if not run_command("pipenv --version", capture_output=True):
        print("Pipenv is not installed. Installing Pipenv...")
        run_command("pip install pipenv")
    
    print(f"Creating Pipenv environment with Python {python_version}...")
    run_command(f"pipenv --python {python_version}")


def main():
    project_name = "{{ cookiecutter.project_name }}"
    python_version = "{{ cookiecutter.python_version }}"
    use_dependency_manager = "{{ cookiecutter.use_dependency_manager }}"

    print("Starting project setup...")
    print(f"Project name: {project_name}")
    print(f"Python version: {python_version}")

    # Create and activate the virtual environment
    if create_virtualenv(python_version):
        if not activate_virtualenv():
            print("Failed to activate virtual environment.")
            sys.exit(1)

    # Handle dependency manager setup
    if use_dependency_manager == "poetry":
        install_poetry(python_version)
    elif use_dependency_manager == "pipenv":
        install_pipenv(python_version)
    elif use_dependency_manager == "none":
        print("No dependency manager chosen. Skipping dependency installation.")
    else:
        print("Unknown dependency manager selected. Exiting.")
        sys.exit(1)

    print("Project setup completed successfully!")


if __name__ == "__main__":
    main()
