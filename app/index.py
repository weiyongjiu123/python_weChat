#WSGI

from wsgiref.simple_server import make_server
from app import application

httpd = make_server('', 80, application)
httpd.serve_forever()