import subprocess
import sys

if "{{ cookiecutter.create_virtualenv }}" != "none":
    virtualenv_option = "{{ cookiecutter.create_virtualenv }}"
    if virtualenv_option == "conda":
        subprocess.check_call(
            [
                "conda",
                "create",
                "--name",
                "{{ cookiecutter.project_slug }}",
                "python={{ cookiecutter.python_version }}",
            ]
        )
    elif virtualenv_option == "venv":
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "venv",
                ".venv",
                "--prompt",
                "{{ cookiecutter.project_slug }}",
                "--upgrade",
            ]
        )
        subprocess.check_call(
            [".venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"]
        )
        subprocess.check_call([".venv/bin/python", "-m", "pip", "install", "wheel"])
        subprocess.check_call(
            [".venv/bin/python", "-m", "pip", "install", "setuptools"]
        )
        subprocess.check_call(
            [".venv/bin/python", "-m", "pip", "install", "virtualenv"]
        )
        subprocess.check_call(
            [
                ".venv/bin/python",
                "-m",
                "pip",
                "install",
                f"python=={{ cookiecutter.python_version }}",
            ]
        )
    elif virtualenv_option == "virtualenv":
        subprocess.check_call(
            ["virtualenv", "-p", f"python{{ cookiecutter.python_version }}", ".venv"]
        )
        subprocess.check_call(
            [".venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"]
        )
        subprocess.check_call([".venv/bin/python", "-m", "pip", "install", "wheel"])
        subprocess.check_call(
            [".venv/bin/python", "-m", "pip", "install", "setuptools"]
        )
        subprocess.check_call(
            [".venv/bin/python", "-m", "pip", "install", "virtualenv"]
        )
else:
    print("Virtual environment creation skipped.")
