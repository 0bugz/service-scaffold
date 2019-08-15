import os
import sys
from os import path
from pathlib import Path

def create_project_sub_dir(project_root, name, dir_name, home_dir, port, files = []):
    project_sub_dir = "{}/{}".format(project_root, dir_name)
    Path(project_sub_dir).mkdir(parents=True, exist_ok=True)
    for file in files:
        template_path = "templates/{}".format(file)
        file_path = "{}/{}".format(project_sub_dir, file)
        if Path(template_path).exists():
            with open(template_path, "r", encoding="utf-8") as f_in, open(file_path, "w", encoding="utf-8") as f_out:
                contents = f_in.read()
                contents = contents.replace("{{HOME_DIR}}", home_dir)
                contents = contents.replace("{{PORT}}", port)
                contents = contents.replace("{{service_name}}", name)
                f_out.write(contents)
        else:
            Path(file_path).touch()

def create_project(dir_path, name, home_dir, port):
    project_root = "{}/{}".format(dir_path, name)
    Path(project_root).mkdir(parents=True, exist_ok=True)

    create_project_sub_dir(project_root, name, 'config', home_dir, port, files = ['test.cfg'])
    create_project_sub_dir(project_root, name, 'install', home_dir, port, files = ['requirements.txt'])
    create_project_sub_dir(project_root, name, 'src', home_dir, port, files = ['app.py'])
    create_project_sub_dir(project_root, name, 'tests', home_dir, port, files = ['basic_tests.py'])
    create_project_sub_dir(project_root, name, ".", home_dir, port, files = ['.dockerignore', '.env', 'docker-compose.yml', 'Dockerfile', 'run-docker.sh'])

if __name__ == '__main__':
    no_of_args = len(sys.argv)
    if no_of_args != 5:
        print("Usage: python project_scaffold.py <dir> <name> <home_dir> <port>")
        exit(1)

    create_project(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
