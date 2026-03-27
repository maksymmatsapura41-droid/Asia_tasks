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
import json
from commands import run_command

load_dotenv()
TOKEN = os.getenv('token')
GITHUB_TOKEN = os.getenv('github_api_token')
REPO_NAME = os.getenv('repo_name')
REPO_OWNER = os.getenv('repo_owner')
MY_BOT = Bot(token=TOKEN)
CHAT_ID = 479413823

my_dispatcher = Dispatcher()

async def github_webhook_handler(request):
    data = await request.json()
    event = request.headers.get('X-GitHub-Event') # incoming event type
    if event == 'workflow_run':
        name = data['workflow_run']['name']
        conclusion = data['workflow_run']['conclusion']
        status = data['workflow_run']['status']
        if conclusion:
            await MY_BOT.send_message(CHAT_ID, f'{name}: {conclusion}')
        await MY_BOT.send_message(CHAT_ID, f'{name}: {status}')

def get_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='START')
    keyboard.button(text='STATUS')
    keyboard.button(text='UPTIME')
    return keyboard.as_markup(resize_keyboard=True)

@my_dispatcher.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(reply_markup=get_keyboard(), text='You have typed /start')

@my_dispatcher.message(F.text.lower()=='uptime')
async def cmd_uptime(message: types.Message):
    result = run_command('uptime')
    await message.answer(f'{result}')

@my_dispatcher.message(F.text.lower()=='start')
async def action_start(message: types.Message):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/blank.yml/dispatches'
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {'ref':'main'}
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json=data, headers=headers) as answer:
            result_status = answer.status
            if result_status == 204:
                await message.answer(f'ACTION STARTED', reply_markup=ReplyKeyboardRemove())
            else:
                await message.answer(f'ERROR: {result_status}', reply_markup=ReplyKeyboardRemove())

@my_dispatcher.message(F.text.lower()=='status')
async def action_status(message: types.Message):
    url = f"https://api.github.com/repos/{REPO_NAME}/{REPO_OWNER}/actions/runs"
    headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
    }
    params = {"per_page": 5}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers, params=params) as answer:
            answer_status = answer.status
            result = await answer.json()
            # print(json.dumps(result, indent=2))
            status_info = {}
            if answer_status != 200:
                await message.answer(f'ERROR: {answer_status}')
            runs = result['workflow_runs']
            for run in runs:
                status_info[run['name']] = run['conclusion']
            await message.answer(f'ACTIONS STATUS:', reply_markup=ReplyKeyboardRemove())
            await MY_BOT.send_message(CHAT_ID, f'{json.dumps(status_info, indent=2)}')

async def main():
    logging.basicConfig(level=logging.INFO)
    app = web.Application()
    app.router.add_post('/webhook/github', github_webhook_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    server_port = web.TCPSite(runner, '0.0.0.0', 8888)
    await server_port.start()
    await my_dispatcher.start_polling(MY_BOT)

    try:
        await asyncio.Event().wait()
    finally:
        await runner.cleanup()

if __name__=='__main__':
    asyncio.run(main())
