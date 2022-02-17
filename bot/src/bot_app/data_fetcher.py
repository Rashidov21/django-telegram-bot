import aiohttp
from . local_settings import WORDS_API_RANDOM_URL


async def get_random():
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_RANDOM_URL) as response:
            return await response.json()