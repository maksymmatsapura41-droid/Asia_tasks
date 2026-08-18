# BAD asyncio.create_task(coro())
import asyncio


# Good task = asyncio.create_task(coro())


async def say_hello(name: str, age: int):
    return f"Hello, {name}! You are {age} years old."


async def say_goodbye(name: str):
    return f"Goodbye, {name}!"

# async def main():
#     result = await asyncio.gather(say_hello("Bob", 5), say_goodbye("Bob"))
#     print(result)

async def main():
    async with asyncio.TaskGroup() as tg:
        res1 = tg.create_task(say_hello("Bob", 5))
        res2 = tg.create_task(say_goodbye("Bob"))
    print(await res1)
    print(await res2)


if __name__ == "__main__":
    asyncio.run(main())