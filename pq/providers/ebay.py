from pq.providers import BaseProvider
from pq.providers import Match


class Provider(BaseProvider):
    def __init__(self):
        BaseProvider.__init__(self)

        self.name = "Ebay"
        self.url = "https://www.ebay.com"

    def find_matches(self):
        match = Match()
        match.name = "Ebay1"
        match.description = "Ebay1 match"
        match.price = 42.21
        match.url = self.url
        self.matches.append(match)

        match = Match()
        match.name = "Ebay2"
        match.description = "Ebay2 match"
        match.price = 42.21
        match.url = self.url
        self.matches.append(match)
