import asyncio

preparing_count, max_preparing, working_count, max_working = 0, 0, 0, 0
lock = asyncio.Lock()

async def worker(worker_id, semaphore):
    global preparing_count, max_preparing, working_count, max_working, lock
    # Подготовка
    async with lock:
        preparing_count += 1
        max_preparing = max(max_preparing, preparing_count)
    await asyncio.sleep(0.1)
    async with semaphore:
        # Работа
        async with lock:
            working_count += 1
            max_working = max(max_working, working_count)
        await asyncio.sleep(0.1)

async def main():
    semaphore = asyncio.Semaphore(2)
    tasks = [worker(i, semaphore) for i in range(4)]
    await asyncio.gather(*tasks)
    print(max_preparing)
    print(max_working)


if __name__ == "__main__":
    asyncio.run(main())
