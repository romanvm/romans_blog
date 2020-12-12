#!/usr/bin/env python
import os
import sys

from dotenv import read_dotenv

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

read_dotenv(os.path.join(THIS_DIR, '.env'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "romans_blog.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
