import os
from pathlib import Path

project_name = 'networksecurity'

list_of_files = [
    ".gthub/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/cloud/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/logging/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "notebooks/research.ipynb",
    "app.py",
    "Makefile",
    ".env"
]

# creating project structure
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f"Creating directory {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            # logging.info(f"Creating empty file: {filepath}")

    else:
        # logging.info(f"{filename} is already exists")
        pass