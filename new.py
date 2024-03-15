import asyncio


async def custom_filter(some_list: list[int]) -> bool:
    total = 0
    for elem in some_list:
        if int(elem) % 7 == 0:
            total += int(elem)
    return total < 83

some_list = [7, 14, 28, 32, 32, 56]

# Для вызова асинхронной функции правильно,
# мы используем asyncio.run() вне асинхронного контекста
print(asyncio.run(custom_filter(some_list)))
