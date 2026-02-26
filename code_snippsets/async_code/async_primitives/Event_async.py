import asyncio


async def system_check(name, event):
    print(f"[{name}] Waiting for the start signal...")
    await event.wait()  # Pause here until the event flag becomes True
    print(f"[{name}] Signal received! System started.")


async def control_tower(event):
    print("[Tower] Checking all systems in 3 seconds...")
    await asyncio.sleep(3)

    print("[Tower] Command issued: IGNITION!")
    event.set()  # Set the flag to True - all waiting tasks will resume


async def main():
    start_event = asyncio.Event()

    # Create multiple tasks that will wait for the signal
    tasks = [
        system_check("Navigation", start_event),
        system_check("Fuel", start_event),
        system_check("Communication", start_event)
    ]

    # Run tower and system checks concurrently
    await asyncio.gather(*tasks, control_tower(start_event))


asyncio.run(main())