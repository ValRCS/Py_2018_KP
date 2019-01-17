from bs4 import BeautifulSoup
import requests
import importlib
import pkgutil

from pq import providers


class BaseProvider:
    def __init__(self):
        self.name = None
        self.url = None
        self.soup = None
        self.matches = []

    def find_matches(self):
        pass

    def get_page(self, url):
        r = requests.get(url)
        self.soup = BeautifulSoup(r.text, features="html.parser")
        self.find_matches()


class Match:
    def __init__(self):
        self.name = None
        self.description = None
        self.price = None
        self.url = None
        self.image = None


def get_all():
    provider_list = []
    for importer, modname, ispkg in pkgutil.iter_modules(providers.__path__):
        provider = importlib.import_module(f"pq.providers.{modname}").Provider()
        provider_list.append(provider)

    return provider_list
