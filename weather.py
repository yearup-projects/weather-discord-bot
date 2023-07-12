import os
import aiohttp
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('RAPID_API_KEY')

BASE_URL = 'https://weatherapi-com.p.rapidapi.com/current.json'

headers = {
    'X-RapidAPI-Key': API_KEY,
    'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com'
}


async def get_weather_data(query):
    _query = {'q': query}

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=headers,
                               params=_query) as response:
            if response.status == 200:
                weather_data = await response.json()
                print(weather_data)
                return weather_data
            else:
                return None
