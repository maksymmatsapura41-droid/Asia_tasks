from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import logging
from aiohttp import web
import asyncio

token = ''

my_bot = Bot(token=token)
chat_id = 479413823

my_dispatcher = Dispatcher()

async def github_webhook_handler(request):
    data = await request.json()
    print(data)
    mod_data = data['repository']['full_name']
    await my_bot.send_message(chat_id, mod_data)

@my_dispatcher.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f'Hello human {message.from_user.full_name}, you are {message.from_user.json}')

@my_dispatcher.message(F.text.lower()=='привет')
async def cmd_start(message: types.Message):
    await message.answer(f'Hi there')

@my_dispatcher.message(F.text)
async def cmd_start(message: types.Message):
    await message.answer(f'Please repeat, {message.chat.id}')

async def main():
    logging.basicConfig(level=logging.INFO)
    # await my_dispatcher.start_polling(my_bot)
    app = web.Application()
    app.router.add_post('/webhook/github', github_webhook_handler)
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