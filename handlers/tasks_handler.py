import aiohttp

from bot_settings import config


async def my_tasks(tg_id: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(config.url + f'?telegram_user_id={tg_id}') as response:
            return await response.json()


async def make_task_done(task_id: str):
    async with aiohttp.ClientSession() as session:
        async with session.patch(config.url + f'{task_id}/', json={'status': 'done'}) as response:
            return await response.json()
