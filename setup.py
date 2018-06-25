import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname).read())

setup(
    name="footballscoring",
    version = "0.1",
    author = "Dominik Zapf",
    author_email = "dominik.zapf@tu-ilmenau.de",
    description = ("A utility package for managing a american football game, "\
    "including scoring, down, distance and so on, Game Clock and game setup with "\
    "team names and logos. Can be used for further implementation like live tickers"\
    "or displaying scoreboards."),
    license = "Apache License 2.0",
    keywords = "american football scoring scoreboard liveticker",
    url = "TODO:",
    packages = ['footballscoring', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Beta",
        "Topic :: Utilities",
        "License :: Apache License 2.0"
    ]
)