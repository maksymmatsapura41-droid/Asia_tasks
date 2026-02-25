import asyncio

async def long_running_task():
    try:
        print("Starting to download a large file...")
        await asyncio.sleep(10)
        print("File downloaded!")
    except asyncio.CancelledError:
        print("Download was cancelled due to timeout!")
        raise

async def main():
    try:
        async with asyncio.timeout(2):
            await long_running_task()
    except TimeoutError:
        print("Main: Time is up, we didn't wait the full 10 seconds.")

asyncio.run(main())
