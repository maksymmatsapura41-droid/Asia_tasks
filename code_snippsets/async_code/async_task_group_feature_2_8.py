import asyncio


async def fast_error():
    await asyncio.sleep(1)
    print("Fast Error: Oops, I crashed!")
    raise RuntimeError("Error!")


async def slow_work():
    try:
        for i in range(5):
            await asyncio.sleep(1)
            print(f"Slow Work: Still working... ({i + 1} sec)")
    except asyncio.CancelledError:
        print("Slow Work: I was AUTOMATICALLY cancelled!")
        raise  # Important to propagate the cancellation further


async def main():
    print("\n--- Starting with TaskGroup ---")
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fast_error())
            tg.create_task(slow_work())
    except* RuntimeError as e:  # Python 3.11+ uses ExceptionGroup
        print(f"Main caught: {e}")

    print("Main continues. All background tasks are GUARANTEED to be stopped.")
    await asyncio.sleep(2)
    print("--- End of program ---")


asyncio.run(main())
