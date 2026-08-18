import asyncio
import time


def read_huge_file(name):
    print(f"Starting to read file {name}...")
    time.sleep(3)  # Simulating long reading
    return f"Contents of {name}"


async def main():
    print("File read request started...")
    task = asyncio.to_thread(read_huge_file, "data.txt")

    print("While the file is being read, I can print this message.")

    input("Press enter to exit...")
    result = await task
    input("Press enter to exit...")
    print(f"Result: {result}")


asyncio.run(main())
