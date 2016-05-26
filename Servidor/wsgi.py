"""
WSGI config for Servidor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Servidor.settings") # ADD

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise # ADD

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Servidor.settings") # Comentado

application = get_wsgi_application()
application = DjangoWhiteNoise(application) # ADD
