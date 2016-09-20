"""
WSGI config for Djangogirls project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('C:/Users/pilar/Bitnami Django Stack projects/Djangogirls')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/pilar/Bitnami Django Stack projects/Djangogirls/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Djangogirls.settings")

application = get_wsgi_application()
