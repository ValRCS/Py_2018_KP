from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pq",
    version="0.1.0",
    license="MIT",
    description="Fetch listings from different online marketplaces",
    long_description=long_description,
    url="https://github.com/rhssk/Py_2018_KP",
    author="Rihards Skuja",
    author_email="rssk@protonmail.com",
    packages=find_packages(),
    install_requires=["PySide2", "requests", "beautifulsoup4"],
    tests_require=["pytest"],
)
