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
        print("Slow Work: I was cancelled, stopping.")


async def main():
    print("--- Starting with gather ---")
    try:
        # gather does NOT cancel other tasks when one of them fails
        await asyncio.gather(fast_error(), slow_work())
    except Exception as e:
        print(f"Main caught an exception: {e}")

    print("Main continues, but...")
    await asyncio.sleep(5)  # Wait to see if slow_work is still running
    print("--- End of program ---")


asyncio.run(main())
