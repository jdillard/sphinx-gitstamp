from setuptools import setup
import os

long_description = open('README.rst' if os.path.exists('README.rst') else 'README.md').read()
exec(compile(
    open('sphinx_gitstamp/version.py').read(), 'sphinx_gitstamp/version.py', 'exec'))

setup(
    name='sphinx-gitstamp',
    description='git timestamp generator for Sphinx',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Topic :: Documentation',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
      ],
    version=__version__,
    author='Jared Dillard',
    author_email='jared.dillard@gmail.com',
    install_requires=['six', 'sphinx >= 1.2', 'gitpython'],
    url="https://github.com/jdillard/sphinx-gitstamp",
    license='MIT',
    download_url="https://github.com/jdillard/sphinx-gitstamp/archive/v0.3.2.tar.gz",
    packages=['sphinx_gitstamp'],
 )
