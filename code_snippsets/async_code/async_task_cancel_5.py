import asyncio


async def heavy_work():
    try:
        print("Starting long-running work...")
        await asyncio.sleep(10)
        print("Work finished!")
    except asyncio.CancelledError:
        print("Work was interrupted!")
        raise


async def main():
    task = asyncio.create_task(heavy_work(), name="Worker-1")
    print(f"Task: {task.get_name()} was started.")

    await asyncio.sleep(1)
    print("Got tired of waiting, cancelling the task.")

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Task officially cancelled in main")


asyncio.run(main())
