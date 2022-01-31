#!/bin/sh
gunicorn {{ cookiecutter.django_project_name }}.wsgi -c ../gunicornconfig.py
