#!/usr/bin/python3
"""Async generator"""

from random import uniform
import asyncio


async def async_generator():
    """Function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

if __name__ == "__main__":
    async def print_yielded_values():
        """this is the Function
        """
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
