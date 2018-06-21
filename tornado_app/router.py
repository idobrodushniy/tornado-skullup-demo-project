from tornado_app.handlers import *
from tornado.web import url

ROUTER = [
    url(r"/", MainHandler),
    url(r"/second", AdditionalHandler)
]
