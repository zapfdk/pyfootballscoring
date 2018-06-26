import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="footballscoring",
    version = "0.2",
    author = "Dominik Zapf",
    author_email = "dominik.zapf@tu-ilmenau.de",
    description = ("A utility package for managing a american football game, "\
    "including scoring, down, distance and so on, Game Clock and game setup with "\
    "team names and logos. Can be used for further implementation like live tickers"\
    "or displaying scoreboards."),
    license = "Apache License 2.0",
    keywords = "american football scoring scoreboard liveticker",
    url = "https://github.com/zapfdk/pyfootballscoring",
    packages = ['footballscoring', 'tests'],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires = [
        'apscheduler'
    ]
)