import asyncio
import aiohttp

async def check_url(session, url):
    """
    TODO:
    1. Use a try/except block to catch connection errors.
    2. Use session.get(url, timeout=...) to fetch the status code.
    3. Return a tuple: (url, status)
    """
    pass


async def main():
    urls = ["https://google.com", "https://github.com", "https://python.org", "https://non-existing-url.example"]
    

    # async with aiohttp.ClientSession() as session:
    # TODO: Initialize a single ClientSession for all requests
    # TODO: Create a list of tasks using a list comprehension
    # TODO: Execute all tasks concurrently using asyncio.gather()
    pass


if __name__ == "__main__":
    asyncio.run(main())