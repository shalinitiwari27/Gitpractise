import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO,
                    format = "[%(asctime)s : %(levelname)s] : %(message)s")

while True:
    project_name = input("Enter project name: ")
    if project_name != "":
        break

logging.info(f"Project created with name {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Pipeline/__init__.py",
    f"src/{project_name}/Entity/__init__.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Configuration/__init__.py",
    f"src/{project_name}/Data_access/__init__.py",
    f"src/{project_name}/Cloud_storage/__init__.py",
    f"src/{project_name}/ML/__init__.py",
    f"src/{project_name}/Constants/__init__.py",
    f"src/{project_name}/Exception.py",
    f"src/{project_name}/Logger.py",
    f"Tests/__init__.py",
    f"Tests/Unit/__init__.py",
    f"Tests/Integration/__init__.py",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "tox.ini",
    "setup.cfg",
    "init_setup.sh",
    "pyproject.toml",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Directory created with name {filedir}")
    if(not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"file created with name {filename}")
    else:
        logging.info(f"File already exists")