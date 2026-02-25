import asyncio
import random

async def fetch_url(name, delay):
    print(f"-> Request to {name} started (will take {delay} sec)")
    await asyncio.sleep(delay)
    return f"Result from {name}"

async def main():
    tasks = [
        fetch_url("Fast-Server", 1),
        fetch_url("Medium-Server", 3),
        fetch_url("Slow-Server", 5)
    ]

    print("--- Processing results as they complete ---")

    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"<- Received: {result}")

asyncio.run(main())
