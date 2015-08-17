#!/usr/bin/env python
# *-* coding: utf-8 *-*
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","rest.settings")
    from django.core.management import execute_from_command_line
    if(len(sys.argv) > 0 ):
        execute_from_command_line(sys.argv)
        #execute_from_command_line(['','runserver'])
    else:
        execute_from_command_line(['',"runserver"])
