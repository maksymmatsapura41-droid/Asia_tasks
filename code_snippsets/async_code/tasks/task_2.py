import asyncio
import random


async def run_command(server):
    """
    Simulates a remote command execution.
    TODO: Add a random sleep to mimic network latency.
    """
    return f"Response from {server}"


async def main():
    servers = ["prod-db-01", "prod-web-01", "prod-cache-01"]

    # TODO: Prepare a list of coroutine objects (tasks)

    print("Executing commands... (Processing results as they finish)")

    # TODO: Use 'for task in asyncio.as_completed(tasks):'
    # TODO: Await each task and print the result immediately
    pass


if __name__ == "__main__":
    asyncio.run(main())