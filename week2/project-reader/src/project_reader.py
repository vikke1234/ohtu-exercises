from urllib import request
from project import Project
import toml
from pprint import pprint


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))
        pprint(content)
        name = content["tool"]["poetry"]["name"]
        description = content["tool"]["poetry"]["description"]
        deps = content["tool"]["poetry"]["dependencies"]
        dev_deps = content["tool"]["poetry"]["dev-dependencies"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, deps, dev_deps)
