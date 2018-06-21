from tornado import gen
from tornado.httpclient import AsyncHTTPClient

async def fetch_weather_data():
    http_client = AsyncHTTPClient()
    response = await http_client.fetch('http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')

    return response.body