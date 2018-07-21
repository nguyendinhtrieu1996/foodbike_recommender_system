import os
import sys

path = '/home/dinhtrieu1996/foodbike'
if path not in sys.path:
    sys.path.append(path)


os.os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prs_project.settings")

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())