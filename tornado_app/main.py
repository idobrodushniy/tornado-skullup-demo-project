from tornado.ioloop import IOLoop
from tornado.web import Application

from tornado_app.router import ROUTER
import logging

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

if __name__ == "__main__":
    get_module_logger(__name__).info("HELLO WORLD!")

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
