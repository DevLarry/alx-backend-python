#!/usr/bin/env python3
"""Async generator"""

from random import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10

if __name__ == "__main__":
    async def print_yielded_values():
        """this is the Function
        """
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
