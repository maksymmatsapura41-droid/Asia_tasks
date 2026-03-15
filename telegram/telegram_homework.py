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
import asyncio
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

token = ''

my_bot = Bot(token=token)
chat_id = 479413823

my_dispatcher = Dispatcher()

class WeatherStates(StatesGroup):
    waiting_for_city = State()
    confirming_details = State()

@my_dispatcher.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(f'Hello {message.from_user.first_name}! Enter the city name...')
    await state.set_state(WeatherStates.waiting_for_city)

async def get_weather(request):
    data = await request.json()
    print(data)
    weather = '+15'
    await my_bot.send_message(chat_id, weather)

@my_dispatcher.message(WeatherStates.waiting_for_city)
async def process_city(message: types.Message, state: FSMContext):
    city = message.text
    
    await message.answer(f"There is a nice wather in {city}")
    await state.clear()

@my_dispatcher.message(F.text)
async def cmd_start2(message: types.Message):
    await message.answer(f'Please repeat, {message.chat.id}')

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