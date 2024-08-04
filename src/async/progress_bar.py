import time
from tqdm.asyncio import tqdm
import asyncio


def blocking_io(task_id: int, duration: int) -> int:
    print(f"Task {task_id} started. it will take {duration} seconds")
    time.sleep(duration)
    return task_id * 2


async def main():
    task_count = 3
    loop = asyncio.get_running_loop()
    result = await tqdm.gather(*[loop.run_in_executor(None, blocking_io, i, (task_count - i) * 2) for i in range(3)])

    print("All tasks completed: ", result)

asyncio.run(main())
