import asyncio


async def long_task():
    try:
        print("Task: I'm starting to work...")
        await asyncio.sleep(10)
        print("Task: I'm done!")
    except asyncio.CancelledError:
        print("Task: Oh, I was cancelled! Starting resource cleanup...")
        raise


async def main():
    task = asyncio.create_task(long_task())

    await asyncio.sleep(2)
    print("Main: It's taking too long, cancelling...")
    task.cancel()  # Send cancellation signal

    try:
        await task
    except asyncio.CancelledError:
        print("Main: Confirmed, the task was successfully cancelled.")


asyncio.run(main())
