import re
from PySide2 import QtWidgets

from pq.providers import BaseProvider
from pq.providers import Match


class Provider(BaseProvider):
    def __init__(self):
        BaseProvider.__init__(self)

        self.name = "SS.com"
        self.base_url = "https://www.ss.com"

    def find_matches(self):
        head_line = self.soup.find("tr", attrs={"id": "head_line"})
        table_body = head_line.parent
        rows = table_body.find_all("tr", {"id": re.compile(r"^tr_\d+$")})
        for row in rows:
            match = Match()
            match.description = row.find("div", attrs={"class": "d1"}).text
            # TODO: compile regex only once, not with each call
            # Work around <b> tags by getting the text of parent
            price_a = row.find_all(text=re.compile(r".*€.*"))[-1].parent.text
            match.price = price_a
            match.url = self.base_url + row.find_all("a", href=True)[0]["href"]
            self.matches.append(match)
