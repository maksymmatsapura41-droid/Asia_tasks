import asyncio
import time


async def stubborn_task():
    try:
        print("Task: Starting heavy computations...")
        start_time = time.time()

        while time.time() - start_time < 5:
            pass

        print("Task: Phew, I finally finished the computations!")
        await asyncio.sleep(0)

    except asyncio.CancelledError:
        print("Task: Oh... now I see I was cancelled. But it's already too late!")
        raise


async def main():
    task = asyncio.create_task(stubborn_task())

    await asyncio.sleep(1)
    print("Main: Trying to cancel the task RIGHT NOW...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main: The task has finally finished with Cancelled status.")


asyncio.run(main())
