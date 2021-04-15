import asyncio
import time

# Event loop is a routine that can make two or more things at same time.
# The 'Await' means ..... safe point of async def go to another coroutine.
# This is a respose to solve very intensive I.O operations.
# All this stuff runs under the event loop.

contador1 = 0
contador2 = 0
contador3 = 0
star_time = time.timezone()


async def func1():
    global contador1

    while True:

        contador1 += 1
        print("This is function One", contador1)
        await asyncio.sleep(1)


async def func2():
    global contador2

    while True:

        contador2 += 1
        print("This is function Two", contador2)
        await asyncio.sleep(2)


async def func3():
    global contador3

    while True:

        contador3 += 1
        print("This is function Three", contador3)
        await asyncio.sleep(3)


asyncio.gather(func1(), func2(), func3())
# asyncio.get_event_loop().run_forever()
asyncio.get_event_loop().run_forever()
