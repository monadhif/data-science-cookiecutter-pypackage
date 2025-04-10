
# 🚀 Ultimate Cookiecutter Template for Python Data Science Projects
A highly customizable Cookiecutter template designed for setting up Python **Data Science** projects with minimal hassle. It supports various virtual environments and dependency management systems, making it easy for you to jumpstart your data science workflow.

## ⚡ Features
- **Author Customization**: Easily set your name and email.
- **Flexible Project Structure**: Automatically generates a well-organized project tailored to your needs.
- **Python Version Support**: Choose from Python versions `3.7`, `3.8`, `3.9`, and `3.11`.
- **Dependency Management**:
  - **None** (with options for `venv` or `virtualenv`)
  - **Poetry**
  - **Pipenv**
  - **Conda**

## 🛠️ How to Use This Template

### Prerequisites
Before using the template, make sure you have the following installed:

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)
- Python (one of the supported versions: `3.7`, `3.8`, `3.9`, `3.11`)
- Optionally, install `Poetry`, `Pipenv`, or `Conda` (the project will install your chosen dependency manager if it's not already installed).

### Usage

1. Generate your project with Cookiecutter:

    ```bash
    cookiecutter https://github.com/monadhif/data-science-cookiecutter-pypackage
    ```

2. Fill out the prompts for project details:
    - **Author name**: Your name.
    - **Author email**: Your email.
    - **Project name**: Name of your data science project.
    - **Python version**: Choose one of the supported versions (`3.7`, `3.8`, `3.9`, `3.11`).
    - **Dependency manager**: Pick from `none`, `Poetry`, `Pipenv`, or `Conda`.

3. If you choose `none` for the dependency manager, you will be prompted to choose between `venv` or `virtualenv` for creating a virtual environment, or opt for no environment at all.

4. Setup complete! The script configures your project with the selected environment or dependency manager.

### Example

```bash
cookiecutter https://github.com/monadhif/data-science-cookiecutter-pypackage


When prompted, fill in the required fields:

```bash
author_name [Your Name]: Mona Lisa
author_email [Your Email]: mona.lisa@gmail.com
project_name [Python Project Name]: My Data Science Package
python_version [3.7|3.8|3.9|3.11]: 3.9
use_dependency_manager [none|poetry|pipenv|conda]: none
```

If you choose `none` for the dependency manager:

```bash
Choose virtual environment tool:
 1 - None
 2 - venv
 3 - virtualenv
Enter your choice (1/2/3): 1
```

After project setup, activate the virtual environment using the provided instructions.

## 📁 Project Structure

After generating the project, the structure will look like this:

```
my-data-science-package/
│
├── .venv/                         # Virtual environment (if venv/virtualenv is used)
├── data/                          # Data folder (for raw and processed data)
│   ├── external/                  # External data (e.g., third-party data)
│   ├── processed/                 # Processed data (cleaned or transformed)
│   └── raw/                       # Raw data (original data)
├── docs/                          # Documentation folder
├── notebooks/                     # Jupyter notebooks folder
├── source/                        # Main package directory
│   ├── __init__.py                # Package init file
│   ├── models/                    # Folder for machine learning models
│   ├── data/                      # Data processing scripts
│   └── visualization/             # Visualization scripts
├── pyproject.toml                 # Poetry config (if Poetry is used)
├── Pipfile                        # Pipenv config (if Pipenv is used)
├── environment.yml                # Conda environment file (if Conda is used)
├── README.md                      # Project README
└── setup.py                       # Package setup script


```

## 🧰 Dependency Management Options

### 1. No Dependency Manager (Virtual Environment Only)

If you select `none`, you will be able to choose between:

- **`venv`**: A lightweight virtual environment manager bundled with Python.
- **`virtualenv`**: A more feature-rich alternative for creating isolated Python environments.

### 2. Poetry

If you select `Poetry`, the script will:
- Set up a `pyproject.toml` file to define your dependencies.
- Use `Poetry` to create and manage the virtual environment.
- Install dependencies defined in `pyproject.toml`.

### 3. Pipenv

If you select `Pipenv`, the script will:
- Set up a `Pipfile` for managing your dependencies.
- Use `Pipenv` to create and manage the virtual environment.
- Install dependencies defined in the `Pipfile`.

### 4. Conda

If you select `Conda`, the script will:
- Create a Conda environment for your project.
- Install the specified Python version and dependencies within the Conda environment.

## 🛠️ Activating Your Virtual Environment

Once your virtual environment or dependency manager is set up, you can activate the environment as follows:

### venv/virtualenv

- **Windows**:
    ```bash
    .venv\Scripts\activate
    ```
- **macOS/Linux**:
    ```bash
    source .venv/bin/activate
    ```

### Poetry

To activate the virtual environment managed by `Poetry`:

```bash
poetry shell
```

### Pipenv

To activate the `Pipenv` environment:

```bash
pipenv shell
```

### Conda

For Conda, activate the environment with:

```bash
conda activate my_data_science_package_env
```

## 🤝 Contributions

We welcome contributions to improve and extend this template. Feel free to submit issues or pull requests on the GitHub repository.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
