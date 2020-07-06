#! /usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "valkuilwebservice",
    version = "2.0.2",
    author = "Maarten van Gompel",
    author_email = "proycon@anaproy.nl",
    description = ("Spelling correction webservice"),
    license = "GPL",
    keywords = "valkuil spelling correction webservice rest nlp",
    url = "https://github.com/proycon/valkuil-gecco",
    packages=['valkuilwebservice'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3.3", #3.0, 3.1 and 3.2 are not supported by flask
        "Programming Language :: Python :: 3.4", #3.0, 3.1 and 3.2 are not supported by flask
        "Programming Language :: Python :: 3.5", #3.0, 3.1 and 3.2 are not supported by flask
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    package_data = {'valkuilwebservice':['*.yml','*.wsgi'] },
    include_package_data=True,
    install_requires=['CLAM >= 3.0', 'natsort', 'gecco']
)
