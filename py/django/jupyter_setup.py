#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A script that's needed to setup django if it's not already running on a server.
# Without this, you won't be able to import django modules

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
