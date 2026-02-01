import asyncio
import time


async def download_file_async(name):
    print("[Download] Downloading file...")
    await asyncio.sleep(1)
    print(f"[Download] Downloaded file {name}")


async def download_file_async_1(name):
    print("[Download] Downloading file...")
    await asyncio.sleep(1)
    print(f"[Download] Downloaded file {name}")

async def main():
    start = time.time()
    # await download_file_async("download_file_sync4")
    # await download_file_async("download_file_sync4")
    # await download_file_async("download_file_sync4")
    # task1 = asyncio.create_task(download_file_async("download_file_async"))
    # task2 = asyncio.create_task(download_file_async("download_file_async"))
    # task3 = asyncio.create_task(download_file_async("download_file_async"))
    # await task1
    # await task2
    # await task3
    await asyncio.gather(
        asyncio.Task(download_file_async("download_file_sync4")),
        download_file_async("download_file_sync4"),
        download_file_async("download_file_sync4"),
        download_file_async_1("download_file_sync4"),
    )
    end = time.time()
    print(str(end-start))


if __name__ == "__main__":
    asyncio.run(main()) # create event loop