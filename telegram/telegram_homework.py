# 1. Команда /start и приветствие:
# При вводе команды /start бот должен поприветствовать пользователя.
# Сразу после приветствия бот должен отправить сообщение: "Введите название города, чтобы узнать погоду".
# Бот должен войти в состояние ожидания (FSM) названия города. СМОТРИ ФАЙЛ ПОДСКАЗКУ.
# 2. Обработка названия города:
# Создать хендлер, который срабатывает только тогда, когда бот находится в состоянии "ожидания города".
# Внутри хендлера отправить асинхронный запрос к OpenWeatherMap API.
# Логика ответа:
# Если город найден: отправить сообщение с текстом (например: "В городе Киев сейчас +15°C, облачно").
# Если город не найден (ошибка 404): ответить пользователю: "К сожалению, я не нашел такой город. Попробуйте еще раз".
# После успешного или ошибочного ответа - завершить состояние (или оставить пользователя в нем для нового поиска, на выбор).
# 3. Фильтр на стикеры (Custom Filter):
# Реализовать хендлер, который реагирует исключительно на стикеры.
# Условие: Если пользователь присылает любой стикер, бот должен ответить текстом: "Красивый стикер! Но я понимаю только названия городов. Введите город:".
# Реализовать это через встроенный фильтр Magic Filter (например, F.sticker).
# 4. Обработка API (Utils):
# Вынести логику запроса к API в отдельную асинхронную функцию в файле utils.py.
# Функция должна принимать название города и возвращать отформатированную строку или словарь с данными.

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import logging
from aiohttp import web
import aiohttp
import asyncio
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

token = ''
openweathermap_api_key = ''

my_bot = Bot(token=token)
chat_id = 479413823

my_dispatcher = Dispatcher()

class WeatherStates(StatesGroup):
    waiting_for_city = State()
    confirming_details = State()

@my_dispatcher.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f'Привет {message.from_user.first_name}! Введи название города...')
    await state.set_state(WeatherStates.waiting_for_city)

@my_dispatcher.message(F.sticker)
async def process_sticker(message: types.Message, state: FSMContext):
    await message.answer("Красивый стикер! Но я понимаю только названия городов. Введи город:")
    await state.set_state(WeatherStates.waiting_for_city)

# todo: support country code (uk, pl)
async def get_weather(city):
    units = 'metric'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={openweathermap_api_key}&units={units}'
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                json_data = await response.json()
                print('[INFO] response data: ', json_data)
                if json_data['cod'] == '404':
                    return f'К сожалению, я не нашел такой город {city}. Попробуйте еще раз'
                else:
                    return f"В городе {city} сейчас {json_data['main']['temp']}°C {json_data['weather'][0]['description']}"
        except Exception as e:
            return city, str(e)

@my_dispatcher.message(WeatherStates.waiting_for_city)
async def process_city(message: types.Message, state: FSMContext):
    city = message.text
    result = await get_weather(city)
    tg_message = await message.answer(result)
    await my_bot.send_message(chat_id, tg_message)
    await state.clear()

async def main():
    logging.basicConfig(level=logging.INFO)
    await my_dispatcher.start_polling(my_bot)
    app = web.Application()
    runner = web.AppRunner(app)
    await runner.setup()
    server_port = web.TCPSite(runner, '0.0.0.0', 8888)
    await server_port.start()
    try:
        await asyncio.Event().wait()
    finally:
        await runner.cleanup()

if __name__=='__main__':
    asyncio.run(main())