import re
import sys

project_name = "{{ cookiecutter.project_name }}"

# Check if project_name contains only letters, numbers, hyphens or underscores
if not re.match(r"^[\w-]+$", project_name):
    print(
        f"ERROR: The project name ({project_name}) is not valid. It must contain only letters, numbers, hyphens or underscores."
    )
    sys.exit(1)
