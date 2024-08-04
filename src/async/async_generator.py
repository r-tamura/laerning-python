import asyncio
import collections
import collections.abc
import time
import typing


def blocking_io(task_id: int, duration: int) -> int:
    time.sleep(duration)
    return task_id


class Task(typing.NamedTuple):
    id: int
    duration: int


async def run_tasks(tasks: list[Task], *, loop: asyncio.AbstractEventLoop | None = None) -> collections.abc.AsyncGenerator[int, None]:
    if loop is None:
        loop = asyncio.get_running_loop()
    futures = [loop.run_in_executor(
        None, blocking_io, task.id, task.duration) for task in tasks]

    for future in asyncio.as_completed(futures):
        result = await future
        yield result


async def main():
    start = time.time()

    task_count = 3
    tasks = [Task(i, task_count - i) for i in range(task_count)]

    start = time.time()

    async for task_id in run_tasks(tasks):
        print(f"Task {task_id} completed")

    end = time.time()
    elapsed = end - start
    print(f"Program finished in {elapsed} seconds")

asyncio.run(main())
