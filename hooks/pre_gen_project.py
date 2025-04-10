#!/usr/bin/env python
import re
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
        # Print out the error details to debug
        print(f"Command failed: {error}")
        # print(f"Error output: {error.stderr}")
        sys.exit(1)  # Exit the program, or you could return None depending on the use c

def get_available_python_versions():
    """Get a list of installed Python versions."""
    versions = []
    if WIN:
        output = run_command("py --list", capture_output=True)
        if output:
            versions = re.findall(r"-V:(\d+\.\d+)", output)
    else:
        output = run_command("ls /usr/bin/python*", capture_output=True)
        if output:
            versions = re.findall(r"python(\d+\.\d+)", output)
    return versions


def find_compatible_python_version(required_version, available_versions):
    """Find the closest compatible Python version available on the system."""
    if required_version in available_versions:
        return required_version

    major, minor = map(int, required_version.split('.'))
    for version in available_versions:
        v_major, v_minor = map(int, version.split('.'))
        if v_major == major and v_minor >= minor:
            return version
    return available_versions[0] if available_versions else None

def write_python_version(python_version):
    """Write the selected Python version to a temporary file."""
    with open(".compatible_python_version", "w") as f:
        f.write(python_version)


def main():
    selected_python_version = "{{ cookiecutter.python_version }}"
    available_versions = get_available_python_versions()

    print("Checking Python versions...")
    print(f"Selected Python version: {selected_python_version}")
    print(f"Available Python versions: {available_versions}")

    # Check if the selected Python version is installed
    if selected_python_version not in available_versions:
        print(f"Python {selected_python_version} is not installed.")
        compatible_version = find_compatible_python_version(selected_python_version, available_versions)
        if compatible_version:
            print(f"Using compatible Python version: {compatible_version}")
            # Update the context to use the compatible version
            write_python_version(compatible_version)
        else:
            print("ERROR: No compatible Python version found. Please install the required version.")
            sys.exit(1)
    else:
        print(f"Python {selected_python_version} is installed and will be used.")
        write_python_version(selected_python_version)

    print("\033[92mPre-generation validation completed successfully!\033[0m")

if __name__ == "__main__":
    main()