import asyncio

async def fetch_data():
    print("API request started...")
    await asyncio.sleep(5)
    return {"data": 42}

async def main():
    try:
        result = await asyncio.wait_for(fetch_data(), timeout=2.0)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("Error: API did not respond in time, task was cancelled!")

asyncio.run(main())
