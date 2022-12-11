import os

from setuptools import setup

import sphinx_gitstamp

long_description = open(
    "README.rst" if os.path.exists("README.rst") else "README.md"
).read()

setup(
    name="sphinx-gitstamp",
    description="git timestamp generator for Sphinx",
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Topic :: Documentation :: Sphinx",
        "Programming Language :: Python :: 3",
        "Framework :: Sphinx :: Extension",
    ],
    version=sphinx_gitstamp.__version__,
    author="Jared Dillard",
    author_email="jared.dillard@gmail.com",
    install_requires=["six", "sphinx >= 1.2", "gitpython"],
    url="https://github.com/jdillard/sphinx-gitstamp",
    license="MIT",
    packages=["sphinx_gitstamp"],
)
