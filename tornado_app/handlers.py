from tornado import web, escape
from tornado_app.fetch import fetch_weather_data
import logging
import json
import datetime
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

logger = get_module_logger('tornado_app')
logger.info('HELLO IN HANDLERS')

class MainHandler(web.RequestHandler):
    async def get(self):
        data = await fetch_weather_data()
        self.write(data)

    async def post(self):
        data = await fetch_weather_data()
        value = self.get_body_arguments('value')
        logger.info(f'NEW REQUEST with value = {json.loads(self.request.body)}')
        self.write('1')


class AdditionalHandler(web.RequestHandler):
    def get(self):
        self.write("Second url")
