#!/usr/bin/env python3
"""Async generator"""

from random import uniform
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Function that does it all
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result

if __name__ == "__main__":
    async def main():
        """Function"""
        print(await async_comprehension())

    asyncio.run(main())
