#!/usr/bin/env python3
"""Async generator"""

from random import uniform
import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function that does it all
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    elapsed = time.perf_counter() - s
    return elapsed

if __name__ == "__main__":
    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )
