#! /usr/bin/env python2.7
import os
import sys

sys.path.append('/home/httpd/users/niru/neurosite')
sys.path.append('/home/httpd/users/niru/neurosite/main')
sys.path.append('/usr/local/virt_python/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
