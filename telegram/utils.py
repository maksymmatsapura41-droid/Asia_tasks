import aiohttp

async def get_weather(city, openweathermap_api_key):
    units = 'metric'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={openweathermap_api_key}&units={units}'
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                json_data = await response.json()
                if json_data['cod'] == '404':
                    return f'К сожалению, я не нашел такой город {city}. Попробуйте еще раз'
                else:
                    return f"В городе {city} сейчас {json_data['main']['temp']}°C {json_data['weather'][0]['description']}"
        except Exception as e:
            return city, str(e)