#!/usr/bin/env python

from distutils.core import setup

setup(
    name="{{ cookiecutter.django_project_name }}",
    version="1.0",
    description="Django Utility",
    author="Vishal P",
    author_email="vi6hal@gmail.com",
    url="https://www.python.org/sigs/distutils-sig/",
    packages=["distutils", "distutils.command"],
)
