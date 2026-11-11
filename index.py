import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(_file_)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'COFFEESSHOPsettings')


from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()