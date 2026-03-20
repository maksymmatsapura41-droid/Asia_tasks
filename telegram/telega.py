from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import logging
from aiohttp import web
import aiohttp
import asyncio
import os
from dotenv import load_dotenv
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove

load_dotenv()
token = os.getenv('token')
GITHUB_TOKEN = os.getenv('github_api_token')
repo_name = os.getenv('repo_name')
repo_owner = os.getenv('repo_owner')
my_bot = Bot(token=token)
chat_id = 479413823

my_dispatcher = Dispatcher()

async def github_webhook_handler(request):
    data = await request.json()
    event = request.headers.get('X-GitHub-Event') # incoming event type
    if event == 'workflow_run':
        name = data['workflow_run']['name']
        conclusion = data['workflow_run']['conclusion']
        status = data['workflow_run']['status']
        if conclusion:
            await my_bot.send_message(chat_id, f'{name}: {conclusion}')
        await my_bot.send_message(chat_id, f'{name}: {status}')

def get_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='START')
    keyboard.button(text='STATUS')
    return keyboard.as_markup(resize_keyboard=True)

@my_dispatcher.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(reply_markup=get_keyboard(), text='You have typed /start')
    # await message.answer(f'Hello human {message.from_user.full_name}, you are {message.from_user.json}')


@my_dispatcher.message(F.text.lower()=='start')
async def action_start(message: types.Message):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/blank.yml/dispatches'
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {'ref':'main'}
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data, headers=headers) as answer:
            result_status = answer.status
            if result_status == 204:
                await message.answer(f'Github action started', reply_markup=ReplyKeyboardRemove())
            else:
                await message.answer(f'Smth went wrong: {result_status}', reply_markup=ReplyKeyboardRemove())

@my_dispatcher.message(F.text.lower()=='status')
async def action_status(message: types.Message):
    url = f"https://api.github.com/repos/{repo_name}/{repo_owner}/actions/runs"
    headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
    }
    params = {"per_page": 5}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers, params=params) as answer:
            result = await answer.json()
            

# @my_dispatcher.message(F.text)
# async def cmd_start(message: types.Message):
#     await message.answer(f'Please repeat, {message.chat.id}')

async def main():
    logging.basicConfig(level=logging.INFO)
    app = web.Application()
    app.router.add_post('/webhook/github', github_webhook_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    server_port = web.TCPSite(runner, '0.0.0.0', 8888)
    await server_port.start()
    await my_dispatcher.start_polling(my_bot)

    try:
        await asyncio.Event().wait()
    finally:
        await runner.cleanup()

if __name__=='__main__':
    asyncio.run(main())