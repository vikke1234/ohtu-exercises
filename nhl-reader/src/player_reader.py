import requests

class PlayerReader:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_players(self):
        return requests.get(self.url).json()
