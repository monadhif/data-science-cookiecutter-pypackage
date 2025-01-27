#!/usr/bin/env python
import os
import subprocess
import sys

WIN = sys.platform.startswith('win')

def run_command(command, check=True, shell=True, capture_output=False):
    """Helper function to run shell commands with error handling."""
    try:
        result = subprocess.run(command, shell=shell, check=check, capture_output=capture_output, text=True)
        if capture_output:
            return result.stdout.strip()
        return True
    except subprocess.CalledProcessError as error:
        print(f"Command failed: {error}")
        sys.exit(1)

def create_virtualenv(python_version, use_venv=True):
    """Create a virtual environment using the specified Python version and tool."""
    venv_dir = ".venv"
    if not os.path.exists(venv_dir):
        print(f"Creating virtual environment with Python {python_version} using {'venv' if use_venv else 'virtualenv'}...")
        if WIN:
            run_command(f"py -{python_version} -m {'venv' if use_venv else 'virtualenv'} {venv_dir}")
        else:
            run_command(f"python{python_version} -m {'venv' if use_venv else 'virtualenv'} {venv_dir}")
        print("Virtual environment created successfully.")
        return True
    else:
        print(f"Virtual environment already exists in {venv_dir}.")
    return False

def activate_virtualenv():
    """Provide activation instructions for the virtual environment."""
    venv_dir = ".venv"
    if WIN:
        activate_script = os.path.join(venv_dir, "Scripts", "activate.bat")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")

    if not os.path.exists(activate_script):
        print(f"Activation script not found: {activate_script}")
        return False

    print(f"To activate the virtual environment, use the following command:")
    if WIN:
        print(f"   {activate_script}")
    else:
        print(f"   source {activate_script}")
    return True

def install_poetry(python_version):
    """Install Poetry and initialize project dependencies."""
    if not run_command("poetry -V", capture_output=True):
        print("Poetry is not installed. Installing Poetry...")
        run_command("curl -sSL https://install.python-poetry.org | python -")

    print("Creating pyproject.toml file with Poetry...")
    run_command(f"poetry env use python{python_version}")
    run_command("poetry init --name '{{ cookiecutter.project_name }}' --author '{{ cookiecutter.author_name }}' --no-interaction")

    print("Installing dependencies with Poetry...")
    run_command("poetry install")

def install_pipenv(python_version):
    """Install Pipenv and set up the environment."""
    if not run_command("pipenv --version", capture_output=True):
        print("Pipenv is not installed. Installing Pipenv...")
        run_command("pip install pipenv")

    print(f"Creating Pipenv environment with Python {python_version}...")
    run_command(f"pipenv --python {python_version}")

def install_conda(python_version):
    """Install Conda and set up the environment."""
    if not run_command("conda --version", capture_output=True):
        print("Conda is not installed. Please install Conda and try again.")
        sys.exit(1)

    env_name = "{{ cookiecutter.project_name|lower|replace(' ', '_') }}_env"
    print(f"Creating Conda environment with Python {python_version}...")
    run_command(f"conda create -n {env_name} python={python_version} --yes")
    print(f"Conda environment '{env_name}' created. Activate it with:")
    print(f"   conda activate {env_name}")

def get_template_python_version():
    """Read the compatible Python version from the temporary file."""
    try:
        with open(".compatible_python_version", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("ERROR: Compatible Python version file not found. Did the pre-generation step fail?")
        return None

def main():
    project_name = "{{ cookiecutter.project_name }}"
    python_version = get_template_python_version()
    use_dependency_manager = "{{ cookiecutter.use_dependency_manager }}"

    print("Starting post-generation setup...")
    print(f"Project name: {project_name}")
    print(f"Python version: {python_version}")
    print(f"Dependency manager: {use_dependency_manager}")

    if use_dependency_manager == "none":
        print("No dependency manager selected.")
        venv_tool = "venv"  # Default to venv
        if create_virtualenv(python_version, venv_tool == "venv"):
            activate_virtualenv()
        else:
            print("Virtual environment creation failed or skipped.")

    elif use_dependency_manager == "poetry":
        install_poetry(python_version)

    elif use_dependency_manager == "pipenv":
        install_pipenv(python_version)

    elif use_dependency_manager == "conda":
        install_conda(python_version)

    else:
        print("Unknown dependency manager selected. Exiting.")
        sys.exit(1)

    print("Post-generation setup completed successfully!")

    try:
        import os
        os.remove(".compatible_python_version")
    except OSError as e:
        print(f"Failed to clean up: {e}")
if __name__ == "__main__":
    main()