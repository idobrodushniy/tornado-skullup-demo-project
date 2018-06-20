import tornado.ioloop
import tornado.web

import tornado.gen


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Okey we have started our development with Tornado and it will be cool!!!!")

class AdditionalHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Second url")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/second/", AdditionalHandler)
    ], autoreload=True, debug=True, serve_traceback=True)


app = make_app()
app.listen(8000)
tornado.ioloop.IOLoop.current().start()
