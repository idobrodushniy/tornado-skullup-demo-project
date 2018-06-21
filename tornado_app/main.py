from tornado.ioloop import IOLoop
from tornado.web import Application

from tornado_app.router import ROUTER


class StartApp(object):
    AUTORELOAD = True
    DEBUG = True
    SERVE_TRACEBACK = True
    PORT = 8000

    def start(self):
        Application(
            handlers=ROUTER, autoreload=self.AUTORELOAD,
            debug=self.DEBUG, serve_traceback=self.SERVE_TRACEBACK
        ).listen(self.PORT)


StartApp().start()
IOLoop.current().start()
