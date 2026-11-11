"""WSGI entry point for bootstrapdjango."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bootstrapdjango.settings")
application = get_wsgi_application()
app = application
