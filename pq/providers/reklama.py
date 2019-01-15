from pq.providers import BaseProvider
from pq.providers import Match


class Provider(BaseProvider):
    def __init__(self):
        BaseProvider.__init__(self)

        self.name = "Reklāma.lv"
        self.url = "http://www.reklama.lv"

    def find_matches(self):
        match = Match()
        match.name = "Reklama1"
        match.description = "Reklama1 match"
        match.price = 42.21
        match.url = self.url
        self.matches.append(match)

        match = Match()
        match.name = "Reklama2"
        match.description = "Reklama2 match"
        match.price = 42.21
        match.url = self.url
        self.matches.append(match)
