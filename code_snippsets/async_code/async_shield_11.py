import asyncio

async def critical_write_operation():
    print("  [DB] Starting critical write operation...")
    await asyncio.sleep(5)
    print("  [DB] Write operation completed successfully! Data is safe.")
    return "Success"

async def main():
    task = asyncio.create_task(critical_write_operation())
    shielded_task = asyncio.shield(task)

    await asyncio.sleep(1)

    print("Main: Received a cancel command!")
    shielded_task.cancel()

    try:
        await shielded_task
    except asyncio.CancelledError:
        print("Main: The shield reported it was cancelled.")

    result = await task
    print(f"Main: Original task result: {result}")

asyncio.run(main())
