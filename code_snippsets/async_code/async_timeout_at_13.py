import asyncio


async def main():
    loop = asyncio.get_running_loop()
    # Deadline: current loop time + 3 seconds
    deadline = loop.time() + 3

    try:
        async with asyncio.timeout_at(deadline):
            await asyncio.sleep(5)  # Trying to sleep 5 seconds, but the deadline is in 3
    except TimeoutError:
        print("We have reached the hard deadline!")


asyncio.run(main())
