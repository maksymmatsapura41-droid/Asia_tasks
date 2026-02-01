import asyncio
import time


async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hi, {name}!")


async def main():
    print(f"Start: {time.strftime('%X')}")
    await say_hello("Alice", 5)
    await say_hello("Bob", 5)

    print(f"End: {time.strftime('%X')}")


asyncio.run(main())