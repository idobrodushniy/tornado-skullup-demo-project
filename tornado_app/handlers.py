from tornado import web
from tornado_app.fetch import fetch_weather_data

class MainHandler(web.RequestHandler):
    async def get(self):
        data = await fetch_weather_data()
        self.write(data)


class AdditionalHandler(web.RequestHandler):
    def get(self):
        self.write("Second url")
