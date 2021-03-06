#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""
    Now its time to write the teacher tips.....
    Django tips from the couse,
    the port 8000 is the default.
    the  __pycache__ is just a cache file.
    the files asgi.py and wsgi.py are used to deploy the project, 
    The settings.py its some thing that you dont have to be afraid.
"""

import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "password_generador.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
