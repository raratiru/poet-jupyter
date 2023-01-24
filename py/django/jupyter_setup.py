#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A script that's needed to setup django if it's not already running on a server.
# Without this, you won't be able to import django modules
# Inspired from: https://blog.theodo.com/2020/11/django-jupyter-vscode-setup/
# Setting in vscode:
# "jupyter.runStartupCommands": [
#     "%load_ext autoreload\n%autoreload 2",
#     "import os,sys;sys.path.insert(0, os.environ.get('POET_PROJECT_PATH'))",
#     "from py.django import jupyter_setup"
# ]

import os
import sys

import django

# Add the project base directory to the sys.path
# This means the script will look in the base directory for any module imports
# Therefore you'll be able to import analysis.models etc
sys.path.insert(0, os.environ.get("POET_PROJECT_DJANGO_PATH"))

#  Allow queryset filtering asynchronously when running in a Jupyter notebook
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# This is for setting up django
django.setup()
