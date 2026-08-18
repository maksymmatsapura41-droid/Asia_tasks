import asyncio
import random


async def fetch_url(url, semaphore):
    # Use semaphore as a guard to limit concurrency
    async with semaphore:
        print(f"[START] Downloading {url}...")

        await asyncio.sleep(random.uniform(1, 3))
        print(f"[DONE] {url} downloaded")


async def main():
    # Allow only 3 concurrent operations
    sem = asyncio.Semaphore(3)

    urls = [f"https://example.com/page/{i}" for i in range(10)]

    tasks = [fetch_url(url, sem) for url in urls]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())