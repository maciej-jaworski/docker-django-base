#!/usr/bin/env python
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if 'runserver' in sys.argv and os.environ.get('RUN_MAIN'):
        import ptvsd

        ptvsd.enable_attach(address=("0.0.0.0", 3000))

    execute_from_command_line(sys.argv)
