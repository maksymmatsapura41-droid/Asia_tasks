import asyncio

shared_resource = 0
lock = asyncio.Lock()


async def update_resource(number):
    global shared_resource

    async with lock:
        print(f"Task {number} locked resource")

        current_value = shared_resource
        await asyncio.sleep(1)

        shared_resource = current_value + 1
        print(f"Task {number} updated resource to the {shared_resource}")


async def main():
    await asyncio.gather(update_resource(1), update_resource(2))


asyncio.run(main())