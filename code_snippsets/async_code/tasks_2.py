# import asyncio
#
# Task:
#
# Create an async def main() that starts two tasks:
# Task A: A background counter that prints "Loop is alive..." every 0.5 seconds (runs 10 times).
#
# Task B: A "heavy" synchronous function def heavy_computation() that uses time.sleep(5)
# (simulating a blocking database call).
#
# Experiment 1: Call heavy_computation() directly inside main using await (or just calling it).
# Notice how the "Loop is alive" messages stop.
#
# Experiment 2 (The Fix): Use asyncio.to_thread(heavy_computation) to run the blocking
# task in a separate thread within the async loop.
#
# Observe how the background counter now continues to print even while the heavy task is running.

import asyncio, time

async def task_A():
    for i in range(10):
        print("Loop is alive...")
        await asyncio.sleep(0.5)

def heavy_computation():
    time.sleep(5)

async def main():
    # await heavy_computation()
    # await task_A()
    await asyncio.gather(asyncio.to_thread(heavy_computation), task_A)

asyncio.run(main())
#-------------------------------------------------

# Task:
# You need to process 20 "legacy" data files. Processing each file is a synchronous, blocking operation.
#
# Define a sync function def process_file(file_id) that sleeps for 1 second and returns
# f"Result {file_id}".
#
# In your async def main():
#
# Use a loop or list comprehension to schedule all 20 files
# using asyncio.to_thread(process_file, i).
#
# Gather all results and print them.