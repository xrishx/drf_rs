import asyncio
import time

def sync_task():
    time.sleep(2)
    print("Completed")

async def main():
    result = await asyncio.to_thread(sync_task)
    print(result)

asyncio.run(main())