import asyncio

inventory = []
condition = asyncio.Condition()


async def consumer(name):
    async with condition:  # 1. Acquire the condition lock
        print(f"[{name}] Entered the warehouse, checking inventory...")

        while not inventory:  # 2. While the inventory is empty...
            print(f"[{name}] No items available. Waiting (releasing the lock)...")
            await condition.wait()  # 3. Wait for notify(). Lock is temporarily released!
            print(f"[{name}] Woke up! Lock reacquired, checking again...")

        # 4. If we are here, inventory is not empty and we hold the lock
        item = inventory.pop()
        print(f"[{name}] Took {item}. Leaving.")


async def producer():
    await asyncio.sleep(2)  # Simulate a long delivery process
    async with condition:
        inventory.append("Gold bar")
        print("[Supplier] Item added to inventory!")
        condition.notify(1)  # 5. Wake up one waiting consumer


async def main():
    # Run two consumers and one producer concurrently
    await asyncio.gather(
        consumer("Alex"),
        consumer("Ivan"),
        producer()
    )


asyncio.run(main())