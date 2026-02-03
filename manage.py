#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError (
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
>>>>>>> 5bc8838b5f654247f288c163794d18a583226a96
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
<<<<<<< HEAD
    execute_from_command_line (sys.argv)


if __name__ == '__main__':
    main ()
=======
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
>>>>>>> 5bc8838b5f654247f288c163794d18a583226a96
