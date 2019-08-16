import os
import sys
from os import path
from pathlib import Path

class ScaffoldBuilder:

    def __init__(self, project_root, name, home_dir, port, network_name):
        self.project_root = project_root
        self.name = name
        self.network_name = network_name
        self.home_dir = home_dir
        self.port = port

    def create_project_sub_dir(self, dir_name, files = []):
        root_dir = "{}/{}".format(self.project_root, self.name)
        project_sub_dir = "{}/{}".format(root_dir, dir_name)
        Path(project_sub_dir).mkdir(parents=True, exist_ok=True)
        for file in files:
            template_path = "templates/{}".format(file)
            file_path = "{}/{}".format(project_sub_dir, file)
            if Path(template_path).exists():
                with open(template_path, "r", encoding="utf-8") as f_in, open(file_path, "w", encoding="utf-8") as f_out:
                    contents = f_in.read()
                    contents = contents.replace("{{HOME_DIR}}", self.home_dir)
                    contents = contents.replace("{{PORT}}", self.port)
                    contents = contents.replace("{{service_name}}", self.name)
                    contents = contents.replace("{{network_name}}", self.network_name)
                    f_out.write(contents)
            else:
                Path(file_path).touch()

    def create_project(self):
        self.create_project_sub_dir('config', files = ['test.cfg'])
        self.create_project_sub_dir('install', files = ['requirements.txt'])
        self.create_project_sub_dir('src', files = ['app.py'])
        self.create_project_sub_dir('tests', files = ['basic_tests.py'])
        self.create_project_sub_dir(".", files = ['.dockerignore', '.env', '.gitignore', 'docker-compose.yml', 'Dockerfile', 'run-docker.sh'])

if __name__ == '__main__':
    no_of_args = len(sys.argv)
    if no_of_args != 6:
        print("Usage: python project_scaffold.py <dir> <name> <home_dir> <port> <network_name>")
        exit(1)

    sb = ScaffoldBuilder(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    sb.create_project()
