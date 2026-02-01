import asyncio
import time


async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")
    return f"Hi, {name}!"


async def main():
    print(f"Start: {time.strftime('%X')}")
    task1 = asyncio.create_task(say_hello("Alice", 5))
    task2 = asyncio.create_task(say_hello("Bob", 3))

    res2 = await task2
    print(res2)
    res1 = await task1


    print(f"Result: , {res1}")

    print(f"End: {time.strftime('%X')}")


asyncio.run(main())